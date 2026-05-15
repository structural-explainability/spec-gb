"""Reference artifact commands."""

import argparse
from pathlib import Path

from spec_gb.load import load_fallback_version
from spec_gb.orchestrate import run_ref_export, run_ref_validate
from spec_gb.ref_utils import find_repo_root


def ref_export_main(argv: list[str] | None = None) -> int:
    """Generate or check GB reference artifacts."""
    parser = argparse.ArgumentParser(description="Export spec-gb data/spec artifacts.")
    parser.add_argument("--repo-root", type=Path, default=None)
    parser.add_argument("--version", default=None)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args(argv)

    root = find_repo_root(args.repo_root)

    if args.version is None:
        args.version = load_fallback_version(root)

    paths = run_ref_export(
        version=args.version,
        root=root,
        check=args.check,
    )

    action = "Checked" if args.check else "Wrote"
    for path in paths:
        print(f"{action} {path}")

    return 0


def ref_validate_main(argv: list[str] | None = None) -> int:
    """Validate generated GB reference artifacts."""
    parser = argparse.ArgumentParser(
        description="Validate spec-gb data/spec artifacts."
    )
    parser.add_argument("--repo-root", type=Path, default=None)
    parser.add_argument("--version", default=None)
    args = parser.parse_args(argv)

    root = find_repo_root(args.repo_root)

    if args.version is None:
        args.version = load_fallback_version(root)

    run_ref_validate(version=args.version, root=root)

    print("spec-gb reference validation passed.")
    return 0
