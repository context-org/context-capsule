# Context Capsule Template

This repository is a **template** for creating a new Context Capsule. A Context Capsule is a portable unit of domain expertise—including knowledge, skills, and experience—that can be injected into an AI agent at runtime.

## What's Inside

- **`manifest.yaml`** – capsule identity and metadata.
- **`process_graph.json`** – the “map” of states and transitions.
- **`knowledge/`** – domain knowledge (rules, definitions, experience) as JSONL.
- **`src/`** – executable tools (Python functions, etc.).
- **`tests/`** – unit tests and graph validation.
- **`sources.csv`** – provenance for every knowledge entry.
- **`CHANGELOG.md`** – version history.
- **`LICENSE`** – open source license (MIT by default).
- **`.github/workflows/ci.yml`** – automated validation on push.

## How to Use This Template

1. **Clone or fork** this repository.
2. **Replace placeholders** in all files with your own domain content.
3. **Follow the sourcing guidelines** (see below) to fill `knowledge/knowledge.jsonl` and `sources.csv`.
4. **Write tools** in `src/tools.py` (or separate modules) and **add tests** in `tests/`.
5. **Run validation**:
   ```bash
   pytest tests/
   Optionally, install the capsule CLI for more checks.)
6. Package your capsule with the CLI or manually zip the required files.
7. Submit to the Capsule Registry (or share directly via Git).

Sourcing Guidelines (Maintain Integrity)
Every piece of knowledge in your capsule must trace back to a public, verifiable source. Use the following trusted categories:

Category	Examples
Government & Standards	IRS, SEC, FASB, CMS, GAAP, IFRS
Open Educational Resources	OpenStax, MIT OCW, Saylor Academy
Public Peer Forums	Reddit (r/accounting, etc.), Stack Exchange, industry forums
Regulatory Enforcement	Tax court opinions, SEC enforcement actions
Practitioner Content	Blogs, newsletters, conference slides
Public Datasets	FinTabNet, InvoiceNet (under open licenses)
Prohibited: scraped commercial content, copyrighted textbooks used verbatim, private communications.

For each entry in knowledge.jsonl, add a corresponding row in sources.csv with the URL, license, and rationale.

Structure Overview
my-capsule/
├── README.md
├── manifest.yaml
├── process_graph.json
├── knowledge/
│   └── knowledge.jsonl
├── src/
│   └── tools.py
├── tests/
│   ├── test_tools.py
│   └── test_graph.py
├── sources.csv
├── CHANGELOG.md
├── LICENSE
└── .github/workflows/ci.yml

Next Steps
Edit manifest.yaml with your capsule's name, domain, version, etc.

Define your process graph in process_graph.json (replace the placeholder).

Add your knowledge to knowledge/knowledge.jsonl (one JSON object per line).

Implement your tools in src/tools.py (or add more modules).

Write tests to ensure correctness.

Run tests and verify everything works.

Package and share!

For more detailed instructions, see the Capsule Specification and the Authoring Guide.

License
This template is provided under the MIT License. You may choose a different license for your capsule.
