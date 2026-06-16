import os
import shutil
from pathlib import Path

class SmartGenPackager:
    def __init__(self, output_dir="dist"):
        self.output_dir = Path(output_dir)

        # Automatically create the distribution directory if it does not exist.
        if not self.output_dir.exists():
            self.output_dir.mkdir(parents=True)

    def package(self, skill_folder_path):
        """
        Package the generated skill directory into a .skill archive file.
        """
        if not skill_folder_path:
            return False

        skill_path = Path(skill_folder_path)
        skill_name = skill_path.name
        archive_name = self.output_dir / skill_name

        print(f"📦 Packaging {skill_name} into .skill file...")

        # Create a ZIP archive from the skill directory.
        # shutil.make_archive automatically appends the .zip extension.
        shutil.make_archive(str(archive_name), 'zip', str(skill_path))

        # Rename the generated .zip archive to the custom .skill extension.
        zip_file = self.output_dir / f"{skill_name}.zip"
        skill_file = self.output_dir / f"{skill_name}.skill"

        if skill_file.exists():
            skill_file.unlink()  # Remove any existing package before replacement.

        os.rename(zip_file, skill_file)

        print(f"🎯 Successfully created: {skill_file}")
        return True
