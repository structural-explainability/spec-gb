# Governance Boundary Specification (GB)

[![Repo](https://img.shields.io/badge/repo-GitHub-black?logo=github)](https://github.com/structural-explainability/spec-gb)
[![Tooling](https://img.shields.io/badge/python-3.15%2B-blue?logo=python)](./pyproject.toml)
[![License](https://img.shields.io/badge/license-MIT-yellow.svg)](./LICENSE)

[![CI](https://github.com/structural-explainability/spec-gb/actions/workflows/ci-python.yml/badge.svg?branch=main)](https://github.com/structural-explainability/spec-gb/actions/workflows/ci-python.yml)
[![Links](https://github.com/structural-explainability/spec-gb/actions/workflows/links.yml/badge.svg?branch=main)](https://github.com/structural-explainability/spec-gb/actions/workflows/links.yml)
[![Dependabot](https://img.shields.io/badge/Dependabot-enabled-brightgreen.svg)](https://github.com/structural-explainability/spec-gb/security)

> Authoritative specification of Governance Boundary (GB).

GB and IB are normative boundary specifications that protect the stack
and govern how downstream layers may use it.

## Overview

The Governance Boundary (GB) specification defines what
structural artifacts and actions are
allowed, required, constrained, or disallowed
within the SE ecosystem.

GB is a downstream specification that conforms to Structural Explainability (SE).
All SE neutrality constraints apply.

GB answers questions like:

- What counts as a valid structural artifact?
- What changes are permitted?
- What conformance obligations exist?
- What must be validated before downstream use?

GB introduces no epistemic, causal, or normative commitments.
GB records governance structure only.

## Purpose

The purpose of GB is to specify what governance-level structures
may be represented so that coordination, traceability, and accountability
are possible without altering the neutral substrate.

GB defines constraints on:

- governance artifacts (e.g., specifications, adapters, profiles, appendices)
- governance actions over artifacts (e.g., recorded publication, recorded approval,
  recorded deprecation, or recorded supersession)
- versioning, dependency, and provenance structures

GB does not define meaning, enforcement, or correctness of governance actions.

GB protects the neutral substrate and downstream structural artifacts from a specific failure mode:

- Unvalidated or unauthorized structural artifacts/actions entering the system.

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

## Command Reference

<details>
<summary>Show command reference</summary>

### In a machine terminal

Open a machine terminal where you want the project:

```shell
git clone https://github.com/structural-explainability/spec-gb

cd spec-gb
code .
```

### In a VS Code terminal

```shell
uv self update
uv python pin 3.15
uv sync --extra dev --extra docs --upgrade

# install git hooks once per clone
uvx pre-commit install

# generate/check registry artifacts
uv run se-validate
uv run se-ref-export
uv run se-ref-export --check
uv run se-ref-validate
uv run se-validate --strict

# autofix and manual fix issues
git add -A
uvx pre-commit run --all-files
# repeat if changes were made
git add -A
uvx pre-commit run --all-files

# do chores
uv run python -m pyright
uv run python -m pytest
uv run python -m zensical build

# save progress
git add -A
git commit -m "update"
git push -u origin main
```

</details>

## Citation

[CITATION.cff](./CITATION.cff)

## License

[MIT](./LICENSE)

## Manifest

[SE_MANIFEST.toml](./SE_MANIFEST.toml)
