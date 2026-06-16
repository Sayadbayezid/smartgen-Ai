import os
import shutil
from pathlib import Path

class Assembler:
    def __init__(self, blueprints_dir="blueprints", output_dir="dist"):
        self.blueprints_dir = Path(blueprints_dir)
        self.output_dir = Path(output_dir)

        # Create the output directory automatically if it does not already exist.
        if not self.output_dir.exists():
            self.output_dir.mkdir(parents=True)

    def assemble(self, blueprint_name):
        """
        Assemble a new skill by copying the required blueprint
        based on the parsed blueprint name.
        """
        # Ensure we are working with a valid string
        if not isinstance(blueprint_name, str):
            raise ValueError(f"❌ Assembler Error: Expected a string for blueprint_name, got {type(blueprint_name)}")

        target_path = self.output_dir / blueprint_name

        # Remove any existing generated skill directory to ensure a clean build.
        if target_path.exists():
            shutil.rmtree(target_path)

        target_path.mkdir(parents=True)

        print(f"⚙️ Assembling skill: {blueprint_name}...")

        # Copy files from the selected blueprint.
        bp_source = self.blueprints_dir / blueprint_name
        
        if bp_source.exists():
            # Merge blueprint contents into the target directory.
            # Requires Python 3.8+ for dirs_exist_ok=True support.
            shutil.copytree(bp_source, target_path, dirs_exist_ok=True)
            print(f"  ✅ Blueprint '{blueprint_name}' merged successfully.")
        else:
            print(f"  ⚠️ Warning: Blueprint '{blueprint_name}' was not found in {self.blueprints_dir}")
            raise FileNotFoundError(f"Blueprint '{blueprint_name}' is missing.")

        return str(target_path)