import os
import shutil
from pathlib import Path

class SmartGenAssembler:
    def __init__(self, blueprints_dir="blueprints", output_dir="generated_skills"):
        self.blueprints_dir = Path(blueprints_dir)
        self.output_dir = Path(output_dir)

        # Create the output directory automatically if it does not already exist.
        if not self.output_dir.exists():
            self.output_dir.mkdir(parents=True)

    def assemble(self, parsed_data):
        """
        Assemble a new skill by merging the required blueprints
        based on the parsed input data.
        """
        if parsed_data.get("status") == "error":
            print(f"❌ Assembler Error: {parsed_data.get('message')}")
            return None

        intent = parsed_data.get("intent")
        blueprints_to_load = parsed_data.get("blueprints_to_load", [])

        # Generate a unique skill name (e.g., creation-hugo_deployment).
        skill_name = f"{intent}-" + "-".join(blueprints_to_load)
        target_path = self.output_dir / skill_name

        # Remove any existing generated skill directory to ensure a clean build.
        if target_path.exists():
            shutil.rmtree(target_path)

        target_path.mkdir(parents=True)

        print(f"⚙️ Assembling skill: {skill_name}...")

        # Copy and merge files from all selected blueprints.
        for bp_name in blueprints_to_load:
            bp_source = self.blueprints_dir / bp_name
            if bp_source.exists():
                # Merge blueprint contents into the target directory.
                # Requires Python 3.8+ for dirs_exist_ok=True support.
                shutil.copytree(bp_source, target_path, dirs_exist_ok=True)
                print(f"  ✅ Blueprint '{bp_name}' merged successfully.")
            else:
                print(
                    f"  ⚠️ Warning: Blueprint '{bp_name}' was not found in "
                    f"{self.blueprints_dir}"
                )

        return str(target_path)
