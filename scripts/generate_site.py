#!/usr/bin/env python3
"""Render categorized project cards from the metadata block in README.md."""

from __future__ import annotations

import argparse
import html
import json
import re
import textwrap
from pathlib import Path
from urllib.parse import urlparse

BEGIN = "<!-- GENERATED PROJECT INDEX START -->"
END = "<!-- GENERATED PROJECT INDEX END -->"
SOURCE_BEGIN = "<!-- portfolio-projects:begin -->"
SOURCE_END = "<!-- portfolio-projects:end -->"
CATEGORIES = {
    "University": ("university", "01 / Academic work", "University projects"),
    "Personal": ("personal", "02 / Personal work", "Personal projects"),
    "Engineering & systems": ("engineering", "03 / Infrastructure and tooling", "Engineering, DevOps &amp; systems"),
}


def load_projects(readme: str) -> list[dict]:
    try:
        block = readme.split(SOURCE_BEGIN, 1)[1].split(SOURCE_END, 1)[0]
        raw = re.search(r"```json\s*(.*?)\s*```", block, re.DOTALL).group(1)
        projects = json.loads(raw)
    except (IndexError, AttributeError, json.JSONDecodeError) as exc:
        raise ValueError("README.md must contain a valid portfolio-projects JSON block") from exc
    if not isinstance(projects, list) or not projects:
        raise ValueError("project metadata must be a non-empty JSON array")
    seen = set()
    for project in projects:
        if not isinstance(project, dict):
            raise ValueError("each project entry must be an object")
        required = {"title", "category", "description", "tags", "source"}
        if not required <= project.keys():
            raise ValueError(f"project is missing fields: {', '.join(sorted(required - project.keys()))}")
        if not isinstance(project["category"], str) or project["category"] not in CATEGORIES:
            raise ValueError(f"unsupported category: {project['category']}")
        for field in ("title", "description"):
            if not isinstance(project[field], str) or not project[field].strip():
                raise ValueError(f"{field} must be a non-empty string")
        if not isinstance(project["tags"], list) or not project["tags"] or not all(isinstance(tag, str) and tag.strip() for tag in project["tags"]):
            raise ValueError("tags must be a non-empty list of strings")
        for field in ("source", "brief"):
            if field in project and (
                not isinstance(project[field], str) or urlparse(project[field]).scheme != "https"
            ):
                raise ValueError(f"{field} must be an HTTPS URL")
        if project["source"] in seen:
            raise ValueError(f"duplicate project source: {project['source']}")
        seen.add(project["source"])
    return projects


def render(projects: list[dict]) -> str:
    sections = []
    for category, (section_id, eyebrow, heading) in CATEGORIES.items():
        items = [project for project in projects if project["category"] == category]
        if not items:
            continue
        cards = []
        for project in items:
            title = html.escape(project["title"])
            tags = " · ".join(html.escape(tag) for tag in project["tags"])
            tag = html.escape(project["tags"][0])
            brief = project.get("brief")
            brief_link = f'<a href="{html.escape(brief, quote=True)}">Project brief ↗</a>' if brief else ""
            source = html.escape(project["source"], quote=True)
            cards.append(
                '<article class="project-card"><div class="project-top">'
                f'<span class="project-number">{html.escape(category.upper())}</span>'
                f'<span class="tag">{tag}</span></div><h3>{title}</h3>'
                f'<p>{html.escape(project["description"])}</p>'
                f'<div class="project-meta"><span>{tags}</span>{brief_link}'
                f'<a href="{source}">Source ↗</a></div></article>'
            )
        sections.append(
            f'<section id="{section_id}" class="portfolio-category" aria-labelledby="{section_id}-title">\n'
            f'    <div class="section-heading"><div><p class="eyebrow">{eyebrow}</p>'
            f'<h2 id="{section_id}-title">{heading}</h2></div></div>\n'
            f'    <div class="project-grid">\n        ' + "\n        ".join(cards) +
            "\n    </div>\n</section>"
        )
    return "\n\n".join(sections)


def update_site(readme_path: Path, site_path: Path) -> None:
    projects = load_projects(readme_path.read_text(encoding="utf-8"))
    page = site_path.read_text(encoding="utf-8")
    if page.count(BEGIN) != 1 or page.count(END) != 1:
        raise ValueError("site page must contain exactly one generated-index marker pair")
    start = page.index(BEGIN) + len(BEGIN)
    finish = page.index(END)
    if start > finish:
        raise ValueError("generated-index markers are out of order")
    rendered = textwrap.indent(render(projects), "        ")
    updated = page[:start] + "\n" + rendered + "\n        " + page[finish:]
    site_path.write_text(updated, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--readme", type=Path, default=Path("README.md"))
    parser.add_argument("--site", type=Path, required=True, help="website portfolio/index.html to update")
    args = parser.parse_args()
    update_site(args.readme, args.site)


if __name__ == "__main__":
    main()
