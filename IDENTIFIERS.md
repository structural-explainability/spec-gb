# Governance Boundary Identifiers (GB)

This document defines the stable requirement identifiers used by the
Governance Boundary (GB) specification.

Identifiers are the sole normative reference mechanism.
Section ordering, formatting, and presentation are non-normative.

## Overview

Defines the stable set of identifiers.

## Identifier Semantics and Ordering

Identifiers are the sole normative reference mechanism.
Section ordering, formatting, and presentation are non-normative.

Identifiers are listed in strict alphabetical order to remove
editorial discretion and ensure deterministic placement.

## Identifier Naming Rules

All identifiers follow this pattern:

GB.<CATEGORY>.<SUBCATEGORY>.<QUALIFIER>

Identifiers are:

- semantic, not positional
- stable across versions
- reusable across prose, code, and formal proofs
- language-agnostic
- suitable for direct mapping to Lean theorem names

Identifiers MUST NOT be renamed or repurposed.
New identifiers MAY be added only in a new major version of this document.

## Identifier Notes

Each identifier MUST be followed by exactly one note.

- The note MUST be expressed as a single bullet.
- The bullet text MAY wrap across lines.
- No additional bullets, sublists, or structural markers are permitted.
- Notes are explanatory only and do not introduce additional requirements.

## Canonical Identifier List (Alphabetical, with Notes)

GB.ADAPTER.MANIFEST

- Defines the structural form for declaring adapter identity, scope, and claimed compatibility.

GB.CANONICAL.ENCODING

- Defines requirements for canonical encoding of governance artifacts and identifiers.

GB.CONFORMANCE.SE.REQUIRED

- States that Governance Boundary conforms to the Structural Explainability specification.

GB.DEFINITION.CORE

- Defines Governance Boundary as a structural specification for governance-layer artifacts and rules.

GB.DEPENDENCY.GRAPH

- Defines structural dependency graphs among governance artifacts.

GB.FINGERPRINT

- Defines structural fingerprints used to identify governance artifacts or states.

GB.GOVERNANCE.ACTION

- Defines structural records of governance actions applied to artifacts.

GB.PROVENANCE

- Defines structural provenance for governance actions and artifact lifecycle events.

GB.SCOPE.EXCLUSIONS

- Defines what Governance Boundary explicitly does not specify.

GB.VERSIONING

- Defines versioning rules for governance artifacts and specifications.

## Cross-Artifact Consistency Rule

Each identifier in this list MUST appear:

- exactly once in SPEC.md
- exactly once in CONFORMANCE.md
- exactly once as a field in the Lean `ConformanceEvidence` structure
- exactly once in the Lean requirements list

Alphabetical order SHOULD be preserved across all artifacts.
