# Conformance Checklist

This document defines the criteria for determining whether an artifact
conforms to the Governance Boundary (GB) specification.

Identifiers referenced in this document are the sole normative reference mechanism.
Section ordering, formatting, and presentation are non-normative.

An artifact may be a specification, schema, implementation, repository,
or other deliverable claiming conformance.

## Conformance Overview

An artifact CONFORMS if and only if:

- all mandatory requirements are satisfied
- no prohibited assertions are present
- conformance with Structural Explainability (SE) is preserved

Failure of any single check constitutes non-conformance.

## GB.ADAPTER.MANIFEST

- Adapter identity, scope, and compatibility claims are structurally declared.
- Adapter manifests record claims only, not endorsements.
- Fail if: adapter correctness, trust, approval, safety, compliance, or endorsement is asserted.

## GB.CANONICAL.ENCODING

- Canonical encoding rules for governance artifacts and identifiers are explicitly defined.
- Encoding rules are structural and interpretation-neutral.
- Fail if: encoding implies semantic preference, authority, legitimacy, obligation, or epistemic priority.

## GB.CONFORMANCE.SE.REQUIRED

- The artifact explicitly claims conformance with Structural Explainability.
- No requirement weakens, overrides, or contradicts SE neutrality constraints.
- Fail if: GB conformance is asserted without explicit SE conformance.

## GB.DEFINITION.CORE

- The artifact defines governance artifacts and governance actions as structural constructs.
- The artifact limits scope to governance structure only.
- Fail if: epistemic, causal, interpretive, authoritative, legitimacy-bearing, obligation-bearing,
  or enforcement semantics are introduced.

## GB.DEPENDENCY.GRAPH

- Dependencies among governance artifacts are represented structurally.
- Dependency relationships do not assert semantic, causal, operational, authoritative,
  or normative behavior.
- Fail if: dependency semantics imply execution order, enforcement, authority, obligation, causality,
  or legitimacy.

## GB.FINGERPRINT

- The artifact defines or uses fingerprints only as structural identifiers for
  traceability and change detection.
- Fingerprints are not treated as endorsements, guarantees, trust signals, or authority signals.
- Fail if: fingerprints are treated as endorsements, guarantees, trust signals, authority signals,
  correctness claims, or compliance claims.

## GB.GOVERNANCE.ACTION

- Governance actions are recorded as structural events.
- Action kinds are explicit and interpretation-neutral.
- Fail if: actions imply legitimacy, authority, obligation, correctness, endorsement, or enforcement.

## GB.PROVENANCE

- Structural provenance for governance actions and artifact lifecycle events is recorded.
- Provenance records describe lineage, process, or lifecycle events only.
- Fail if: provenance asserts interpretive, evaluative, epistemic, causal, legitimacy-bearing,
   authority-bearing, obligation-bearing, or enforcement meaning.

## GB.SCOPE.EXCLUSIONS

Verify that the artifact does not define:

- domain vocabularies
- application-specific semantics
- behavioral models
- causal explanations
- epistemic evaluation
- authority
- legitimacy
- obligation
- normative judgment or enforcement
- exchange or interaction mechanisms
- identity-and-persistence regime specifications
- graph evolution semantics
- interpretive or explanatory overlays, including context, evidence, explanation, and attestation

Presence of any excluded concern as a GB-defined construct constitutes non-conformance.

## GB.VERSIONING

- Governance artifacts include explicit version identifiers.
- Versioning rules are structural and deterministic.
- Fail if: versioning is implicit, informal, interpretation-dependent, authority-dependent,
  or allows silent change.

## Final Determination

An artifact CONFORMS if:

- all checks above pass
- no prohibited assertions are present
- conformance with Structural Explainability is preserved

Otherwise, the artifact is NON-CONFORMANT.

## Conformance Declaration

Artifacts claiming conformance SHOULD include a declaration of the form:

```text
Conforms to: GB Specification vX.Y
Conforms to: SE Specification vX.Y
```
