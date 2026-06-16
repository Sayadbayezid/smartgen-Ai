import sys
import os
import shutil
from core.parser import SmartGenParser
from core.assembler import Assembler

def main():
    if len(sys.argv) < 2:
        print("❌ Please provide a prompt.")
        sys.exit(1)
        
    prompt = " ".join(sys.argv[1:])
    print("🚀 SmartGen AI Triggered!")
    print(f"📝 Input Prompt: '{prompt}'")
    print("-" * 40)
    
    # 1. Parse the prompt
    parser = SmartGenParser()
    parsed_data = parser.parse(prompt)
    
    # 2. Safely handle the case where no keywords match
    if parsed_data is None:
        print("❌ Exiting Workflow: The prompt did not match any keywords in config/rules.json.")
        sys.exit(1)

    # Handle dictionary output if your parser uses it
    if isinstance(parsed_data, dict):
        if parsed_data.get("status") == "error":
            print("❌ Exiting Workflow: Parser returned an error status.")
            sys.exit(1)
        blueprint_name = parsed_data.get("blueprint", parsed_data.get("name"))
    else:
        # Handle string output
        blueprint_name = parsed_data
        
    if not blueprint_name:
        print("❌ Exiting Workflow: Blueprint name could not be resolved.")
        sys.exit(1)
        
    # 3. Assemble the blueprint
    assembler = Assembler()
    try:
        workspace_path = assembler.assemble(blueprint_name)
        print(f"🎯 Assembly complete at: {workspace_path}")
        
        # 4. Package the output into a .skill (ZIP) file
        print("📦 Packaging into .skill file...")
        
        # Make a zip archive of the workspace directory
        archive_path = shutil.make_archive(workspace_path, 'zip', workspace_path)
        
        # Rename the .zip extension to .skill
        skill_file_path = f"{workspace_path}.skill"
        if os.path.exists(skill_file_path):
            os.remove(skill_file_path) # Remove if already exists from a previous run
            
        shutil.move(archive_path, skill_file_path)
        print(f"✅ Successfully created artifact: {skill_file_path}")
        
    except Exception as e:
        print(f"❌ Assembly/Packaging failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()