# SmartGen Progressive Disclosure Patterns

Keep SKILL.md body to the essentials and under 500 lines. Split content into separate files when approaching this limit. When splitting out content into other files, it is very important to reference them from SKILL.md and describe clearly when to read them, to ensure the reader of the blueprint knows they exist and when to use them.

**Key principle:** When a blueprint supports multiple variations, frameworks, or options, keep only the core workflow and selection guidance in SKILL.md. Move variant-specific details (patterns, examples, configuration) into separate reference files.

## Pattern 1: High-level guide with references

# PDF Processing Blueprint

## Quick start
Extract text with the default script:
`python scripts/extract_text.py`

## Advanced features
- **Form filling**: See `references/FORMS.md` for complete guide
- **API reference**: See `references/REFERENCE.md` for all methods
- **Examples**: See `references/EXAMPLES.md` for common patterns

smartgen-Ai users will access FORMS.md, REFERENCE.md, or EXAMPLES.md only when needed.

## Pattern 2: Domain-specific organization

For blueprints with multiple domains, organize content by domain to avoid clutter:

blueprints/bigquery_automation/
├── SKILL.md (overview and navigation)
└── references/
    ├── finance.md (revenue, billing metrics)
    ├── sales.md (opportunities, pipeline)
    ├── product.md (API usage, features)
    └── marketing.md (campaigns, attribution)

Similarly, for blueprints supporting multiple frameworks or variants, organize by variant:

blueprints/cloud_deploy/
├── SKILL.md (workflow + provider selection)
└── references/
    ├── aws.md (AWS deployment patterns)
    ├── gcp.md (GCP deployment patterns)
    └── azure.md (Azure deployment patterns)

When the user chooses AWS, they only need to read aws.md.

## Pattern 3: Conditional details

Show basic content, link to advanced content:

# DOCX Processing

## Creating documents
Use the base script for new documents. See `references/DOCX-JS.md`.

## Editing documents
For simple edits, run the basic editor script.

**For tracked changes**: See `references/REDLINING.md`
**For OOXML details**: See `references/OOXML.md`

Users will read REDLINING.md or OOXML.md only when they need those specific features.

## Important guidelines:

- **Avoid deeply nested references** - Keep references one level deep inside the `references/` directory. All reference files should link directly from SKILL.md.
- **Structure longer reference files** - For files longer than 100 lines, include a table of contents at the top so users can see the full scope when previewing.
