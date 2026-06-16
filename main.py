import sys
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
    
    # 2. Safely handle the case where no keywords match (Returns None)
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
        print(f"🎯 Assembly complete. Ready for packaging at: {workspace_path}")
    except Exception as e:
        print(f"❌ Assembly failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()