import sys
from core.parser import SmartGenParser
from core.assembler import SmartGenAssembler
from core.packager import SmartGenPackager

def main():
    # Receive the input prompt from GitHub Actions, CLI, or terminal execution.
    if len(sys.argv) < 2:
        print("Usage: python main.py '<your_prompt_here>'")
        sys.exit(1)

    user_prompt = sys.argv[1]
    print(
        f"🚀 SmartGen AI Triggered!\n"
        f"📝 Input Prompt: '{user_prompt}'\n"
        + "-" * 40
    )

    # Step 1: Parser (The Brain)
    # Analyze the user prompt and determine the required blueprint strategy.
    parser = SmartGenParser()
    parsed_data = parser.parse(user_prompt)

    if parsed_data.get("status") == "error":
        print(f"❌ Failed: {parsed_data.get('message')}")
        sys.exit(1)

    # Step 2: Assembler (The Builder)
    # Merge the selected blueprints into a complete skill package structure.
    assembler = SmartGenAssembler()
    generated_folder = assembler.assemble(parsed_data)

    # Step 3: Packager (The Packager)
    # Convert the generated skill directory into a deployable .skill artifact.
    if generated_folder:
        packager = SmartGenPackager()
        success = packager.package(generated_folder)

        if success:
            print("-" * 40)
            print("✨ Process Complete! Artifacts are ready for deployment.")
        else:
            print("❌ Packaging failed.")
            sys.exit(1)

if __name__ == "__main__":
    main()
