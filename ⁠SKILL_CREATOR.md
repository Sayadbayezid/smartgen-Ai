---
name: smartgen-skill-creator
description: Guide for creating, updating, and managing blueprints that extend the smartgen-Ai ecosystem via rule-based parsing, modular workflows, and zero-dependency tool integrations.
license: Complete terms in LICENSE.txt
---

# SmartGen Skill Creator

This guide provides the architectural standards and workflow for creating effective automation skills within the **smartgen-Ai** ecosystem.

## About SmartGen Skills & Blueprints

In the smartgen-Ai engine, "Skills" start as **Blueprints**. A blueprint is a modular, self-contained template that provides specialized knowledge, workflows, and executable Python scripts. 

When a user submits a prompt, the `parser.py` engine matches keywords from `config/rules.json`, and the `assembler.py` merges the required blueprints into a standalone, deployable `.skill` package. 

### What Blueprints Provide

1. **Specialized workflows** - Step-by-step sequential or conditional procedures for specific tasks.
2. **Tool integrations** - Ready-to-run Python scripts for GitHub, API integrations, or file manipulations.
3. **Domain expertise** - Hardcoded templates, base configs, and predefined architectures.
4. **Bundled resources** - Assets that the user needs for complex and repetitive tasks.

## Core Principles

### Rule-Based Logic is Key
Unlike LLMs, smartgen-Ai relies on strict rule-based keyword parsing (`rules.json`). The system does not "guess"—it executes exactly what is mapped.
* Ensure your keywords in `rules.json` are distinct to avoid cross-triggering.
* Keep `SKILL.md` instructions clear and sequential, as they serve as the ultimate execution manual for the end-user or the automated pipeline.

### Set Appropriate Degrees of Freedom
Match the level of specificity to the task's fragility:
* **High freedom (text-based instructions):** Use when multiple approaches are valid (e.g., writing a blog post).
* **Medium freedom (parameterized scripts):** Use when configuration affects behavior (e.g., deploying with different themes).
* **Low freedom (strict scripts):** Use when operations are fragile (e.g., API authentication, directory scaffolding).

## Anatomy of a Blueprint

Every blueprint resides in the `blueprints/` directory and consists of a required `SKILL.md` file and optional bundled resources. When assembled, this structure becomes the final `.skill` package.

```text
blueprints/skill-name/
├── SKILL.md (required)
│   ├── YAML frontmatter metadata (name, description)
│   └── Markdown instructions (Sequential/Conditional workflow)
└── Bundled Resources (optional)
    ├── scripts/          - Executable Python/Bash code (e.g., setup_hugo.py)
    ├── references/       - Variant-specific docs (e.g., aws_patterns.md)
    └── templates/        - Output assets (config files, boilerplate code)
