# Conformance Checklist

This document defines the criteria for determining whether an artifact
conforms to the Governance Boundary specification.

Identifiers referenced in this document are the sole normative reference.
Section ordering, formatting, and presentation are non-normative.

An artifact may be a specification, schema, implementation, repository,
or other deliverable claiming conformance.

## Conformance Overview

An artifact CONFORMS if and only if:

- all mandatory requirements are satisfied
- no prohibited assertions are present
- conformance with Structural Explainability (SE) is preserved

Failure of any single check constitutes non-conformance.

GB.CONFORMANCE.SE.REQUIRED

- [ ] The artifact explicitly claims conformance with Structural Explainability.
- [ ] No requirement weakens or contradicts SE neutrality constraints.
- Fail if: conformance is asserted without explicit SE conformance.

GB.DEFINITION.CORE

- [ ] The artifact defines governance artifacts and governance actions as structural constructs.
- [ ] The artifact limits scope to governance structure only.
- Fail if: epistemic, causal, or normative semantics are introduced.

GB.ADAPTER.MANIFEST

- [ ] Adapter identity, scope, and compatibility claims are structurally declared.
- [ ] Adapter manifests record claims only, not endorsements.
- Fail if: adapter correctness, trust, or approval is asserted.

GB.CANONICAL.ENCODING

- [ ] Canonical encoding rules for governance artifacts are explicitly defined.
- [ ] Encoding rules are structural and interpretation-neutral.
- Fail if: encoding implies semantic preference or authority.

GB.DEPENDENCY.GRAPH

- [ ] Dependencies among governance artifacts are represented structurally.
- [ ] Dependency relationships do not assert semantic or operational behavior.
- Fail if: dependency semantics imply execution, enforcement, or causality.

GB.GOVERNANCE.ACTION

- [ ] Governance actions are recorded as structural events.
- [ ] Action kinds are explicit and interpretation-neutral.
- Fail if: actions imply legitimacy, authority, or enforcement.

GB.FINGERPRINT

- [ ] Governance artifacts MAY include structural fingerprints.
- [ ] Fingerprints are used only for identification and traceability.
- Fail if: fingerprints are treated as endorsements or trust signals.

GB.PROVENANCE

- [ ] Structural provenance for governance actions is recorded.
- [ ] Provenance records describe governance lifecycle events only.
- Fail if: provenance asserts interpretive or evaluative meaning.

GB.VERSIONING

- [ ] Governance artifacts include explicit version identifiers.
- [ ] Versioning rules are structural and deterministic.
- Fail if: versioning is implicit, informal, or interpretation-dependent.

GB.SCOPE.EXCLUSIONS

Verify that the artifact does not define:

- [ ] domain vocabularies
- [ ] application-specific semantics
- [ ] behavioral models
- [ ] causal explanations
- [ ] epistemic evaluation
- [ ] normative judgment or enforcement
- [ ] exchange or interaction mechanisms
- [ ] identity-and-persistence regime specifications
- [ ] graph evolution semantics
- [ ] interpretive/explanatory overlays (context, evidence, explanation, attestation)

Presence of any of the above constitutes non-conformance.

## Final Determination

An artifact CONFORMS if:

- all checks above pass, and
- no prohibited assertions are present.

Otherwise, the artifact is NON-CONFORMANT.

## Conformance Declaration

Artifacts claiming conformance SHOULD include a declaration of the form:

```text
Conforms to: GB Specification vx.y
Conforms to: SE Specification vx.y
```
