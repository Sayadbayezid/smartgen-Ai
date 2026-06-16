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
```
🛠️ Usage & CLI Commands
1. Run the Engine (Generate a Skill)
Trigger the engine by passing a prompt. The parser will map it to a blueprint and generate a ⁠.skill⁠ package in the ⁠dist/⁠ folder.
text```
python main.py "build a python scraper"
```
2. Scaffold a New Blueprint
Use the built-in tool to instantly generate the folder structure and boilerplate files for a new automation blueprint
text```
python tools/init_blueprint.py your-new-automation
```
Validate a Blueprint
Before pushing to production, ensure your blueprint meets all architectural standards (Frontmatter, syntax, required files).
text```
python tools/validate_blueprint.py your-new-automation```
Blueprint Architecture
Every skill inside the ⁠blueprints/⁠ directory follows a strict structural standard to ensure progressive disclosure and modularity:
 ⁠SKILL.md⁠: The required entry point containing YAML frontmatter (name, description) and the core sequential workflow.
 ⁠scripts/⁠: Executable Python/Bash files containing the actual automation logic.
 ⁠references/⁠: Additional documentation loaded via Progressive Disclosure patterns for complex workflows.
 ⁠templates/⁠: Boilerplate files and configuration standards injected by the assembler.
☁️ GitHub Actions Integration
You can trigger the generation pipeline directly from GitHub without cloning the repo:
1 Navigate to the Actions tab in your repository.
2 Select Run SmartGen AI Engine from the left sidebar.
3 Click Run workflow, enter your prompt, and execute.
4 Download your compiled ⁠.skill⁠ artifact from the workflow summary page.
