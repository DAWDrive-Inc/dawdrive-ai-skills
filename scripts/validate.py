#!/usr/bin/env python3
"""Validate every skill in skills/ and check internal markdown links.

Skills live at skills/<domain>/[<subdomain>/]<name>.md with YAML front matter.

Run locally:  python3 scripts/validate.py
Exits non-zero on any error. Warnings do not fail the build.
"""

from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SKILLS_DIR = REPO / "skills"

REQUIRED = ("name", "description", "version")

errors: list[str] = []
warnings: list[str] = []


def parse_frontmatter(text: str) -> dict[str, str] | None:
    """Minimal front-matter reader: top-level `key: value` pairs only."""
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    if end == -1:
        return None
    fields: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if not line.strip() or line.startswith(("#", " ")) or ":" not in line:
            continue
        key, _, value = line.partition(":")
        fields[key.strip()] = value.strip().strip('"')
    return fields


def validate_skill(path: Path, seen: dict[str, list[str]]) -> None:
    rel = path.relative_to(REPO)
    text = path.read_text(encoding="utf-8")
    fm = parse_frontmatter(text)

    if fm is None:
        errors.append(f"{rel}: missing or malformed YAML front matter")
        return

    for key in REQUIRED:
        if not fm.get(key):
            errors.append(f"{rel}: front matter missing required `{key}`")

    name = fm.get("name")
    if name:
        seen[name].append(str(rel))
        if name != path.stem:
            errors.append(
                f"{rel}: front-matter name {name!r} does not match "
                f"filename {path.stem!r}"
            )
        elif not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name):
            errors.append(f"{rel}: name {name!r} must be lowercase-kebab-case")

    version = fm.get("version")
    if version and not re.fullmatch(r"\d+\.\d+\.\d+", version):
        errors.append(f"{rel}: version {version!r} must be semver (e.g. 1.0.0)")

    description = fm.get("description")
    if description:
        if len(description) < 40:
            warnings.append(
                f"{rel}: description is short ({len(description)} chars) — it is the "
                "trigger, so say when to use the skill, not just what it does"
            )
        if len(description) > 1024:
            errors.append(f"{rel}: description is {len(description)} chars (max 1024)")

    body = text[text.find("\n---", 4) + 4 :]
    if not body.strip():
        errors.append(f"{rel}: body is empty")

    depth = len(path.relative_to(SKILLS_DIR).parts) - 1
    if depth == 0:
        warnings.append(f"{rel}: skill is not in a category directory")


LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")


def validate_links(md: Path) -> None:
    rel = md.relative_to(REPO)
    for target in LINK_RE.findall(md.read_text(encoding="utf-8")):
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        path = (md.parent / target.split("#", 1)[0]).resolve()
        if not path.exists():
            errors.append(f"{rel}: broken link → {target}")


def main() -> int:
    if not SKILLS_DIR.is_dir():
        print("error: no skills/ directory", file=sys.stderr)
        return 1

    skill_files = sorted(SKILLS_DIR.rglob("*.md"))
    if not skill_files:
        errors.append("skills/: no skills found")

    seen: dict[str, list[str]] = defaultdict(list)
    for f in skill_files:
        validate_skill(f, seen)

    # Two skills with the same name collide on install — both map to
    # ~/.claude/skills/<name>/SKILL.md.
    for name, paths in seen.items():
        if len(paths) > 1:
            errors.append(f"duplicate skill name {name!r} in: {', '.join(paths)}")

    for md in sorted(REPO.rglob("*.md")):
        if ".git" in md.parts or "promo" in md.parts:
            continue
        validate_links(md)

    for w in warnings:
        print(f"warning: {w}")
    for e in errors:
        print(f"error: {e}", file=sys.stderr)

    if errors:
        print(f"\n✗ {len(errors)} error(s)", file=sys.stderr)
        return 1

    print(f"\n✓ {len(skill_files)} skill(s) valid, all internal links resolve")
    return 0


if __name__ == "__main__":
    sys.exit(main())
