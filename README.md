# Governance Boundary Specification (GB)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/license/MIT)
![Build Status](https://github.com/structural-explainability/spec-gb/actions/workflows/ci-hygiene.yml/badge.svg?branch=main)
[![Check Links](https://github.com/structural-explainability/spec-gb/actions/workflows/links.yml/badge.svg)](https://github.com/structural-explainability/spec-gb/actions/workflows/links.yml)

> Authoritative specification of Governance Boundary (GB).

## Overview

The Governance Boundary (GB) specification defines the structural requirements
for representing governance artifacts and actions whose identity, scope,
and traceability must remain explicit and stable under reinterpretation.

GB is a downstream specification that conforms to Structural Explainability (SE).
All SE neutrality constraints apply.

GB introduces no epistemic, causal, or normative commitments.
GB records governance structure only.

## Purpose

The purpose of GB is to specify what governance-level structures
may be represented so that coordination, traceability, and accountability
are possible without altering the neutral substrate.

GB defines constraints on:

- governance artifacts (e.g., specifications, adapters, profiles, appendices)
- governance actions over artifacts (e.g., publication, approval, deprecation)
- versioning, dependency, and provenance structures

GB does not define meaning, enforcement, or correctness of governance actions.

## Versioning and Stability

GB v1 defines a closed set of governance structures for the purpose of conformance.

For GB v1:

- governance artifacts are structurally constrained as specified by GB identifiers

Closure applies to structural shape only and does not assert institutional finality.

## Extension Policy

Extension is explicitly permitted only under a new
version of the specification.

Any extension MUST:

- preserve conformance with Structural Explainability
- introduce explicit structural definitions and constraints via new identifiers
- demonstrate non-overlap with existing structures
- remain neutral with respect to epistemic, causal, and normative interpretation

Extensions are expected to be rare and explicitly justified.

## Scope

This specification defines:

- structural governance artifacts
- adapter identity, scope, and compatibility claims
- canonical encoding requirements
- structural dependency graphs among governance artifacts
- governance actions over artifacts
- structural provenance for governance lifecycle events
- versioning rules for governance artifacts and specifications

This specification does NOT define:

- domain vocabularies
- behavioral models
- causal explanations
- epistemic evaluation
- normative judgment or enforcement
- exchange or interaction mechanisms
- interpretive explanation overlays (e.g., explanation or attestation systems)
- neutral substrate identity or persistence rules
- graph evolution semantics

These concerns are explicitly out of scope.

## Relationship to Other Work

- GB **conforms to** the Structural Explainability Specification.
- GB operates downstream of neutral substrate specifications but does not depend on their internal semantics.
- GB provides structural governance context for downstream interpretive systems.
- Interpretation, evaluation, and enforcement remain external.

## Repository Contents

- [SPEC.md](./SPEC.md) - Normative specification
- [IDENTIFIERS.md](./IDENTIFIERS.md) - Stable requirement identifiers
- [CONFORMANCE.md](./CONFORMANCE.md) - Conformance checklist
- [ANNOTATIONS.md](./ANNOTATIONS.md) - Annotation standards
- [LICENSE](./LICENSE) - licensing terms
- [CITATION.cff](./CITATION.cff) - Citation metadata
- [CHANGELOG.md](./CHANGELOG.md) - Version history

## Clarifying Statement

Governance Boundary defines structural governance, not governance outcomes.

A governance artifact or action recorded under GB specifies
how governance information is structured, not whether
it is valid, correct, legitimate, or enforced in any context.

GB exists so that governance structure can remain stable
across reinterpretation, disagreement, and changing institutional frameworks.

## Developer (running pre-commit)

Steps to run pre-commit locally. Install `uv`.

Initialize once:

```shell
uv self update
uvx pre-commit install
uvx pre-commit run --all-files
```

Save progress as needed:

```shell
git add -A
# If pre-commit makes changes, re-run `git add -A` before committing.
git commit -m "update"
git push -u origin main
```
