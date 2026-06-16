#!/usr/bin/env python3
"""
Blueprint Validation Script for smartgen-Ai

Usage:
    python tools/validate_blueprint.py <blueprint-name>
    python tools/validate_blueprint.py <absolute-path-to-blueprint>

Examples:
    python tools/validate_blueprint.py hugo_deployment
"""

import sys
import os
import re
import yaml
from pathlib import Path

# ডায়নামিক পাথ: স্ক্রিপ্টের লোকেশন থেকে blueprints ফোল্ডারটি চিনে নেবে
BASE_DIR = Path(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BLUEPRINTS_BASE_PATH = BASE_DIR / "blueprints"

def resolve_blueprint_path(path_or_name):
    """Resolve blueprint path to absolute path."""
    path = Path(path_or_name)
    if path.is_absolute():
        return path
    return BLUEPRINTS_BASE_PATH / path_or_name

def validate_blueprint(path_or_name):
    """Basic validation of a blueprint's SKILL.md"""
    blueprint_path = resolve_blueprint_path(path_or_name)

    # চেক: SKILL.md আছে কি না
    skill_md = blueprint_path / 'SKILL.md'
    if not skill_md.exists():
        return False, f"❌ SKILL.md not found in {blueprint_path}"

    # চেক: Frontmatter আছে কি না
    content = skill_md.read_text(encoding='utf-8')
    if not content.startswith('---'):
        return False, "❌ No YAML frontmatter found at the top of SKILL.md"

    match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return False, "❌ Invalid frontmatter format"

    frontmatter_text = match.group(1)

    # চেক: YAML পার্সিং
    try:
        frontmatter = yaml.safe_load(frontmatter_text)
        if not isinstance(frontmatter, dict):
            return False, "❌ Frontmatter must be a YAML dictionary"
    except yaml.YAMLError as e:
        return False, f"❌ Invalid YAML in frontmatter: {e}"

    # অ্যালাউড প্রপার্টিজ
    ALLOWED_PROPERTIES = {'name', 'description', 'license', 'allowed-tools', 'metadata'}
    unexpected_keys = set(frontmatter.keys()) - ALLOWED_PROPERTIES
    if unexpected_keys:
        return False, (
            f"❌ Unexpected key(s) in SKILL.md frontmatter: {', '.join(sorted(unexpected_keys))}. "
            f"Allowed properties are: {', '.join(sorted(ALLOWED_PROPERTIES))}"
        )

    # রিকোয়ার্ড ফিল্ড চেক
    if 'name' not in frontmatter:
        return False, "❌ Missing 'name' in frontmatter"
    if 'description' not in frontmatter:
        return False, "❌ Missing 'description' in frontmatter"

    # নাম ভ্যালিডেশন
    name = frontmatter.get('name', '')
    if not isinstance(name, str):
        return False, f"❌ Name must be a string, got {type(name).__name__}"
    name = name.strip()
    if name:
        if not re.match(r'^[a-z0-9-]+$', name):
            return False, f"❌ Name '{name}' should be hyphen-case (lowercase letters, digits, and hyphens only)"
        if name.startswith('-') or name.endswith('-') or '--' in name:
            return False, f"❌ Name '{name}' cannot start/end with hyphen or contain consecutive hyphens"
        if len(name) > 64:
            return False, f"❌ Name is too long ({len(name)} chars). Max 64 allowed."

    # ডেসক্রিপশন ভ্যালিডেশন
    description = frontmatter.get('description', '')
    if not isinstance(description, str):
        return False, f"❌ Description must be a string, got {type(description).__name__}"
    description = description.strip()
    if description:
        if '<' in description or '>' in description:
            return False, "❌ Description cannot contain angle brackets (< or >)"
        if len(description) > 1024:
            return False, f"❌ Description is too long ({len(description)} chars). Max 1024 allowed."

    return True, "✅ Blueprint is valid and ready for assembly!"

def main():
    if len(sys.argv) != 2:
        print("Usage: python tools/validate_blueprint.py <blueprint-name>")
        sys.exit(1)
    
    blueprint_input = sys.argv[1]
    resolved_path = resolve_blueprint_path(blueprint_input)
    
    print(f"🔍 Validating blueprint at: {resolved_path}")
    
    valid, message = validate_blueprint(blueprint_input)
    print(message)
    sys.exit(0 if valid else 1)

if __name__ == "__main__":
    main()
