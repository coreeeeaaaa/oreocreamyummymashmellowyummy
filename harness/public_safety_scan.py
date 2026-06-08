#!/usr/bin/env python3
"""Public release safety scan for generic harness documents."""

from __future__ import annotations

import re
import sys
from pathlib import Path


SKIP_DIRS = {".git", "__pycache__"}
TEXT_SUFFIXES = {
    ".md",
    ".txt",
    ".json",
    ".yaml",
    ".yml",
    ".py",
    ".toml",
    ".ini",
    ".cfg",
}

RISK_PATTERNS = [
    ("absolute_local_path", re.compile(r"/Users/[^\\s:`'\"<>]+")),
    ("home_directory_path", re.compile(r"~/[A-Za-z0-9._/-]+")),
    ("env_file_reference", re.compile(r"(^|/)\.env(\.|$)", re.IGNORECASE)),
    ("private_key_block", re.compile(r"BEGIN (RSA |DSA |EC |OPENSSH |PGP )?PRIVATE KEY")),
    ("generic_secret_assignment", re.compile(r"(?i)(api[_-]?key|access[_-]?token|refresh[_-]?token|client[_-]?secret|password)\\s*[:=]\\s*['\\\"]?[^\\s'\\\"]{8,}")),
    ("credential_file_marker", re.compile(r"(?i)(service[_-]?account|credential[_-]?file|secret[_-]?file)")),
]


def iter_files(root: Path):
    for path in root.rglob("*"):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.name == "public_safety_scan.py":
            continue
        if path.is_file() and path.suffix.lower() in TEXT_SUFFIXES:
            yield path


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    findings = []
    for path in iter_files(root):
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for name, pattern in RISK_PATTERNS:
            for match in pattern.finditer(text):
                line = text.count("\n", 0, match.start()) + 1
                findings.append((path, line, name))

    if findings:
        print("PUBLIC_SAFETY_SCAN_FAIL")
        for path, line, name in findings:
            print(f"{path}:{line}: {name}")
        return 1

    print("PUBLIC_SAFETY_SCAN_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
