#!/usr/bin/env python3
"""
Blueprint Initializer for smartgen-Ai
Creates a new blueprint template directory.

Usage:
    python tools/init_blueprint.py <blueprint-name>

Examples:
    python tools/init_blueprint.py my-new-automation
    python tools/init_blueprint.py github-repo-setup

Blueprints are created at ./blueprints/<blueprint-name>/
"""

import sys
import os
from pathlib import Path

SKILL_TEMPLATE = """---
name: {skill_name}
description: [TODO: Complete explanation of what this blueprint does. Add trigger keywords to rules.json to activate this.]
---

# {skill_title}

## Overview
[TODO: 1-2 sentences explaining what this blueprint automates]

## Sequential Workflow
[TODO: List the exact steps smartgen-Ai or the user needs to follow]
1. Step 1...
2. Step 2...

## Resources
This blueprint includes:
- `scripts/`: Executable Python/Bash files.
- `references/`: Optional documentation for progressive disclosure.
- `templates/`: Config files and boilerplates.
"""

EXAMPLE_SCRIPT = '''#!/usr/bin/env python3
"""
Execution script for {skill_name} blueprint.
"""

def main():
    print("🚀 Running automation for {skill_name}...")
    # TODO: Add your smartgen-Ai automation logic here

if __name__ == "__main__":
    main()
'''

EXAMPLE_REFERENCE = """# Reference Documentation for {skill_title}

This is a placeholder for detailed reference documentation.
Use this when your blueprint has multiple variants (e.g., AWS vs GCP deployment).
smartgen-Ai assembler will package this along with the main skill.
"""

EXAMPLE_TEMPLATE = """# Example Template File
{
  "project_name": "{{ PROJECT_NAME }}",
  "status": "ready"
}
"""

def title_case_skill_name(skill_name):
    return ' '.join(word.capitalize() for word in skill_name.split('-'))

# Modified to point directly to your blueprints folder
SKILLS_BASE_PATH = Path(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "blueprints"))

def init_skill(skill_name):
    skill_dir = SKILLS_BASE_PATH / skill_name

    if skill_dir.exists():
        print(f"❌ Error: Blueprint directory already exists: {skill_dir}")
        return None

    try:
        skill_dir.mkdir(parents=True, exist_ok=False)
        print(f"✅ Created blueprint directory: {skill_dir}")
    except Exception as e:
        print(f"❌ Error creating directory: {e}")
        return None

    skill_title = title_case_skill_name(skill_name)
    skill_content = SKILL_TEMPLATE.format(skill_name=skill_name, skill_title=skill_title)

    skill_md_path = skill_dir / 'SKILL.md'
    try:
        skill_md_path.write_text(skill_content)
        print("✅ Created SKILL.md")
    except Exception as e:
        print(f"❌ Error creating SKILL.md: {e}")
        return None

    try:
        scripts_dir = skill_dir / 'scripts'
        scripts_dir.mkdir(exist_ok=True)
        example_script = scripts_dir / 'execute.py'
        example_script.write_text(EXAMPLE_SCRIPT.format(skill_name=skill_name))
        example_script.chmod(0o755)
        print("✅ Created scripts/execute.py")

        references_dir = skill_dir / 'references'
        references_dir.mkdir(exist_ok=True)
        example_reference = references_dir / 'advanced_guide.md'
        example_reference.write_text(EXAMPLE_REFERENCE.format(skill_title=skill_title))
        print("✅ Created references/advanced_guide.md")

        templates_dir = skill_dir / 'templates'
        templates_dir.mkdir(exist_ok=True)
        example_template = templates_dir / 'config.json'
        example_template.write_text(EXAMPLE_TEMPLATE)
        print("✅ Created templates/config.json")
    except Exception as e:
        print(f"❌ Error creating resource directories: {e}")
        return None

    print(f"\n✨ Blueprint '{skill_name}' initialized successfully!")
    print("\nNext steps:")
    print("1. Add trigger keywords to config/rules.json")
    print("2. Edit SKILL.md and add your workflow")
    print("3. Write your automation logic in scripts/execute.py")

    return skill_dir

def main():
    if len(sys.argv) != 2:
        print("Usage: python tools/init_blueprint.py <blueprint-name>")
        sys.exit(1)

    skill_name = sys.argv[1]
    print(f"🚀 Initializing new blueprint: {skill_name}")
    
    if init_skill(skill_name):
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()
