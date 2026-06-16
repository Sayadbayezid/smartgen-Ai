# SmartGen Workflow Patterns

## Sequential Workflows

For complex tasks within your blueprint, break operations into clear, sequential steps. It is strictly required to provide an overview of the process towards the beginning of your `SKILL.md` so the user knows exactly which scripts to run and in what order:

Filling a PDF form involves these steps:

1. Analyze the form (run `python scripts/analyze_form.py`)
2. Create field mapping (edit `templates/fields.json`)
3. Validate mapping (run `python scripts/validate_fields.py`)
4. Fill the form (run `python scripts/fill_form.py`)
5. Verify output (check the generated output folder)

## Conditional Workflows

For tasks with branching logic, guide the user through clear decision points so they know which specific workflow or variant they need to execute:

1. Determine the operation type:
   **Fresh Setup?** → Follow the "Creation workflow" below
   **Updating Existing Setup?** → Follow the "Editing workflow" below

2. Creation workflow:
   - Step 1: Run `python scripts/init_project.py`
   - Step 2: [Additional creation steps]

3. Editing workflow:
   - Step 1: Edit `templates/config.json`
   - Step 2: Run `python scripts/update_project.py`
   - Step 3: [Additional editing steps]
