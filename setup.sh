#!/bin/bash

echo "🚀 Initializing smartgen-Ai Project Structure..."

# Create Directories
mkdir -p smartgen-Ai/.github/workflows
mkdir -p smartgen-Ai/blueprints
mkdir -p smartgen-Ai/config
mkdir -p smartgen-Ai/core
mkdir -p smartgen-Ai/tools
mkdir -p smartgen-Ai/references

cd smartgen-Ai

# ==========================================
# 1. README.md
# ==========================================
cat << 'EOF' > README.md
# 🚀 SmartGen AI Engine

> A zero-dependency, rule-based procedural generation engine.

## 📌 Overview
**smartgen-Ai** is an advanced, self-contained automation engine designed to parse user intent via strict keyword matching and assemble ready-to-deploy execution packages (Blueprints).

## 🧠 The Brain: `config/rules.json`
The entire intelligence of the SmartGen engine lives inside `config/rules.json`.

## 🛠️ Usage & CLI Commands
1. Run Engine: `python main.py "build a python scraper"`
2. Scaffold Blueprint: `python tools/init_blueprint.py your-new-automation`
3. Validate Blueprint: `python tools/validate_blueprint.py your-new-automation`
EOF

# ==========================================
# 2. GitHub Actions Workflow
# ==========================================
cat << 'EOF' > .github/workflows/engine_trigger.yml
name: Run SmartGen AI Engine

on:
  workflow_dispatch:
    inputs:
      prompt:
        description: "Specify the automation blueprint to assemble (e.g., build python scraper)"
        required: true
        type: string

jobs:
  generate-skill:
    name: Generate SmartGen Skill Package
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4

      - name: Set Up Python Environment
        uses: actions/setup-python@v4
        with:
          python-version: "3.10"

      - name: Initialize SmartGen AI Ecosystem
        run: |
          echo "🚀 Starting SmartGen Generation Pipeline..."
          python main.py "${{ github.event.inputs.prompt }}"

      - name: Upload Generated Skill Artifact
        uses: actions/upload-artifact@v4
        with:
          name: generated-skill-package
          path: dist/*.skill
          retention-days: 14
EOF

# ==========================================
# 3. Config (rules.json)
# ==========================================
cat << 'EOF' > config/rules.json
{
  "blueprints_mapping": {
    "python_scraper": {
      "keywords": ["python", "scraper", "scrape", "data extraction"],
      "required_variables": ["target_url"]
    },
    "social_media_poster": {
      "keywords": ["social media", "post", "automation", "publish"],
      "required_variables": []
    }
  }
}
EOF

# ==========================================
# 4. Tools (init_blueprint.py)
# ==========================================
cat << 'EOF' > tools/init_blueprint.py
#!/usr/bin/env python3
import sys, os
from pathlib import Path

SKILL_TEMPLATE = """---
name: {skill_name}
description: [TODO: Complete explanation of what this blueprint does.]
---

# {skill_title}

## Sequential Workflow
1. Step 1...
2. Step 2...
"""

BASE_DIR = Path(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SKILLS_BASE_PATH = BASE_DIR / "blueprints"

def init_skill(skill_name):
    skill_dir = SKILLS_BASE_PATH / skill_name
    if skill_dir.exists():
        print(f"❌ Error: Blueprint exists: {skill_dir}")
        return False
    skill_dir.mkdir(parents=True)
    (skill_dir / 'SKILL.md').write_text(SKILL_TEMPLATE.format(skill_name=skill_name, skill_title=skill_name.title()))
    (skill_dir / 'scripts').mkdir()
    (skill_dir / 'scripts' / 'execute.py').write_text('print("Running...")')
    (skill_dir / 'references').mkdir()
    (skill_dir / 'templates').mkdir()
    print(f"✅ Blueprint '{skill_name}' initialized!")
    return True

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python tools/init_blueprint.py <name>")
        sys.exit(1)
    init_skill(sys.argv[1])
EOF
chmod +x tools/init_blueprint.py

# ==========================================
# 5. Tools (validate_blueprint.py)
# ==========================================
cat << 'EOF' > tools/validate_blueprint.py
#!/usr/bin/env python3
import sys, os, re, yaml
from pathlib import Path

BASE_DIR = Path(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BLUEPRINTS_BASE_PATH = BASE_DIR / "blueprints"

def validate_blueprint(name):
    path = BLUEPRINTS_BASE_PATH / name
    skill_md = path / 'SKILL.md'
    if not skill_md.exists(): return False, "❌ SKILL.md not found"
    
    content = skill_md.read_text(encoding='utf-8')
    if not content.startswith('---'): return False, "❌ No YAML frontmatter"
    
    print(f"✅ Blueprint {name} is valid!")
    return True, "Success"

if __name__ == "__main__":
    if len(sys.argv) != 2: sys.exit(1)
    valid, msg = validate_blueprint(sys.argv[1])
    print(msg)
    sys.exit(0 if valid else 1)
EOF
chmod +x tools/validate_blueprint.py

# ==========================================
# 6. References
# ==========================================
cat << 'EOF' > references/output-patterns.md
# SmartGen Output Patterns
Use exact template structures for strict requirements or flexible guidance for manual adaptation.
EOF

cat << 'EOF' > references/progressive-disclosure-patterns.md
# SmartGen Progressive Disclosure Patterns
Keep SKILL.md under 500 lines. Link to advanced files in `references/` instead of bloating context.
EOF

cat << 'EOF' > references/workflow-patterns.md
# SmartGen Workflow Patterns
Use **Sequential Workflows** for step-by-step logic. Use **Conditional Workflows** for branching decisions.
EOF

# ==========================================
# 7. Core Stubs & Main
# ==========================================
cat << 'EOF' > main.py
import sys
print(f"🚀 smartgen-Ai Engine Triggered with prompt: {sys.argv[1:]}")
EOF

echo "✨ Project scaffolding complete! Your smartgen-Ai engine is ready."
