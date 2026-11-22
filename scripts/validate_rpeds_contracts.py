#!/usr/bin/env python3
"""Validate RPEDS JSON Schemas, positive/negative fixtures, and cross-record graph invariants."""
from __future__ import annotations

import json
from collections import deque
from pathlib import Path
import sys

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_DIR = ROOT / "plugin" / "references" / "schemas" / "rpeds"
FIXTURE_PATH = ROOT / "plugin" / "tests" / "rpeds-schema-fixtures.json"

EXPECTED_SCHEMAS = {
    "roadmap.schema.json",
    "milestone.schema.json",
    "iteration.schema.json",
    "progress-measurement.schema.json",
    "adaptation-decision.schema.json",
    "risk.schema.json",
    "work-item.schema.json",
}
errors: list[str] = []


def fail(message: str) -> None:
    errors.append(message)


def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        fail(f"invalid JSON {path.relative_to(ROOT)}: {exc}")
        return None


def validate_semantic_graph(scenario: dict) -> tuple[bool, list[str]]:
    """Check unique IDs, resolvable references, valid edges, and acyclic dependencies."""
    issues: list[str] = []
    records = scenario.get("records", [])
    edges = scenario.get("edges", [])
    identifiers = [record.get("id") for record in records]

    if any(not isinstance(identifier, str) or not identifier for identifier in identifiers):
        issues.append("every semantic record must have a non-empty string id")
    if len(identifiers) != len(set(identifiers)):
        issues.append("duplicate record identifiers")

    known = {identifier for identifier in identifiers if isinstance(identifier, str)}
    for record in records:
        for reference in record.get("refs", []):
            if reference not in known:
                issues.append(f"dangling reference {reference!r} from {record.get('id')!r}")

    adjacency = {identifier: set() for identifier in known}
    indegree = {identifier: 0 for identifier in known}
    for edge in edges:
        if not isinstance(edge, list) or len(edge) != 2:
            issues.append(f"invalid dependency edge {edge!r}")
            continue
        source, target = edge
        if source not in known or target not in known:
            issues.append(f"dependency edge references unknown node: {edge!r}")
            continue
        if source == target:
            issues.append(f"self dependency at {source!r}")
            continue
        if target not in adjacency[source]:
            adjacency[source].add(target)
            indegree[target] += 1

    queue = deque(node for node, degree in indegree.items() if degree == 0)
    visited = 0
    while queue:
        node = queue.popleft()
        visited += 1
        for dependency in adjacency[node]:
            indegree[dependency] -= 1
            if indegree[dependency] == 0:
                queue.append(dependency)
    if visited != len(known):
        issues.append("dependency graph contains a cycle")

    return not issues, issues


def main() -> int:
    schema_paths = sorted(SCHEMA_DIR.glob("*.schema.json"))
    found = {path.name for path in schema_paths}
    if found != EXPECTED_SCHEMAS:
        fail(
            "RPEDS schema inventory mismatch: "
            f"missing={sorted(EXPECTED_SCHEMAS-found)}, unexpected={sorted(found-EXPECTED_SCHEMAS)}"
        )

    validators = {}
    for path in schema_paths:
        schema = load_json(path)
        if not isinstance(schema, dict):
            continue
        try:
            Draft202012Validator.check_schema(schema)
            validators[path.name] = Draft202012Validator(schema, format_checker=FormatChecker())
        except Exception as exc:
            fail(f"invalid Draft 2020-12 schema {path.name}: {exc}")

    fixtures = load_json(FIXTURE_PATH)
    fixture_count = 0
    if isinstance(fixtures, dict):
        if fixtures.get("schema_version") != "1.0.0":
            fail("RPEDS schema-fixture document must use schema_version 1.0.0")
        fixture_rows = fixtures.get("fixtures", [])
        fixture_count = len(fixture_rows)
        if fixtures.get("fixture_count") != fixture_count:
            fail("RPEDS schema-fixture fixture_count does not match fixtures length")
        seen_fixture_ids = set()
        for fixture in fixture_rows:
            fixture_id = fixture.get("fixture_id")
            schema_file = fixture.get("schema_file")
            if not fixture_id or fixture_id in seen_fixture_ids:
                fail(f"missing or duplicate RPEDS fixture_id: {fixture_id!r}")
                continue
            seen_fixture_ids.add(fixture_id)
            validator = validators.get(schema_file)
            if validator is None:
                fail(f"{fixture_id}: unknown or invalid schema file {schema_file!r}")
                continue
            actual_valid = not list(validator.iter_errors(fixture.get("instance")))
            expected_valid = fixture.get("expected_valid")
            if actual_valid != expected_valid:
                fail(
                    f"{fixture_id}: expected_valid={expected_valid}, "
                    f"actual_valid={actual_valid}"
                )

        semantic_rows = fixtures.get("semantic_scenarios", [])
        if fixtures.get("semantic_scenario_count") != len(semantic_rows):
            fail("RPEDS semantic_scenario_count does not match semantic_scenarios length")
        seen_semantic_ids = set()
        for scenario in semantic_rows:
            scenario_id = scenario.get("scenario_id")
            if not scenario_id or scenario_id in seen_semantic_ids:
                fail(f"missing or duplicate semantic scenario id: {scenario_id!r}")
                continue
            seen_semantic_ids.add(scenario_id)
            actual_valid, issues = validate_semantic_graph(scenario)
            expected_valid = scenario.get("expected_valid")
            if actual_valid != expected_valid:
                fail(
                    f"{scenario_id}: expected_valid={expected_valid}, "
                    f"actual_valid={actual_valid}; issues={issues}"
                )
    else:
        fail("RPEDS schema-fixture document is not a JSON object")
        semantic_rows = []

    if errors:
        print("RPEDS CONTRACT VALIDATION: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        "RPEDS CONTRACT VALIDATION: PASS "
        f"({len(validators)} Draft 2020-12 schemas, {fixture_count} schema fixtures, "
        f"{len(semantic_rows)} semantic graph scenarios)"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
