# 🚀 SmartGen AI Engine

> A zero-dependency, rule-based procedural generation engine. It powers the SmartGen ecosystem by parsing intents and assembling custom Python workflows without external APIs.

## 📌 Overview

**smartgen-Ai** is an advanced, self-contained automation engine designed to parse user intent via strict keyword matching and assemble ready-to-deploy execution packages (Blueprints). Instead of relying on unpredictable LLMs or external APIs, SmartGen uses a deterministic, rule-based architecture to guarantee consistent, high-quality, and secure output every single time.

## ✨ Core Features

* **Zero-Dependency Architecture:** Pure Python. No external libraries, API keys, or internet requirements for the core engine.
* **Rule-Based Parsing (`The Brain`):** Deterministic intent recognition driven by `config/rules.json`.
* **Dynamic Assembler (`The Builder`):** Automatically merges core instructions (`SKILL.md`), executable scripts, and templates into a unified workspace.
* **Artifact Packager:** Compiles assembled workflows into highly portable `.skill` (ZIP) packages.
* **GitHub Actions Native:** Fully integrated CI/CD pipeline for generating blueprints directly from the GitHub UI.

## 📁 Repository Structure

```text
smartgen-Ai/
├── .github/workflows/       # GitHub Actions pipelines
├── blueprints/              # Your custom automation templates
├── config/                  # Engine configurations (rules.json)
├── core/                    # Core engine modules
│   ├── parser.py            # Intent extraction logic
│   ├── assembler.py         # Blueprint merging logic
│   └── packager.py          # .skill artifact generation
├── tools/                   # Developer utilities
│   ├── init_blueprint.py    # CLI tool to scaffold new blueprints
│   └── validate_blueprint.py# CLI tool to test blueprint integrity
├── main.py                  # Engine entry point
└── README.md                # Project documentation