import json
from pathlib import Path

class SmartGenParser:
    """
    The Brain of SmartGen. Parses user prompts and matches them
    to blueprints using keywords defined in config/rules.json.
    """
    def __init__(self, base_dir=None):
        self.base_dir = Path(base_dir) if base_dir else Path.cwd()
        self.rules_path = self.base_dir / "config" / "rules.json"

    def parse(self, prompt):
        if not self.rules_path.exists():
            print(f"❌ Error: rules.json not found at {self.rules_path}")
            return None

        # Load the rule mappings
        with open(self.rules_path, 'r', encoding='utf-8') as f:
            rules_data = json.load(f)
            
        blueprints = rules_data.get("blueprints_mapping", {})
        prompt_lower = prompt.lower()

        # Search for keyword matches in the prompt
        for blueprint_name, mapping in blueprints.items():
            keywords = mapping.get("keywords", [])
            for keyword in keywords:
                if keyword.lower() in prompt_lower:
                    print(f"🧠 Parser Match! Keyword '{keyword}' triggered blueprint '{blueprint_name}'")
                    return blueprint_name
                    
        print("⚠️ No keywords matched. Engine cannot determine which blueprint to build.")
        return None