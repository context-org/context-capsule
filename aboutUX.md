Context Capsule Ecosystem – User Experience Manifesto
Version 1.0
“Expertise, injected.”

This manifesto defines how users interact with the Context Capsule ecosystem: from discovering a capsule to loading it into their agent and using it seamlessly. It sets expectations, explains the domain hierarchy, and addresses comparisons to other tools (including “Claude Skills”). The goal is to make the experience intuitive, transparent, and trustworthy – whether you are a first‑time user or a seasoned professional.

1. Core Principles
Principle	Meaning for Users
Expertise on demand	You don’t train or fine‑tune; you load a capsule and your agent instantly becomes competent in a domain.
Open by default	All capsules are open source, auditable, and free (initially). You can inspect every rule and source.
Simple injection	One command or one function call – no complex configuration.
Transparent trust	Every capsule declares its sources and passes automated tests. Community ratings and professional audits (future) provide confidence.
Hierarchical organisation	Capsules are organised by domain → sub‑domain → bounded context, so you always know what you’re getting.
2. Domain Hierarchy: How Capsules Are Organised
Capsules are not a flat list of thousands of micro‑skills. They follow a clear, predictable hierarchy:

text
Domain (e.g., “accounting”)
  └─ Sub‑domain (e.g., “fixed-assets”)
        └─ Bounded context (e.g., “depreciation”)
Domain capsule – the whole field (rare; mostly a container).

Sub‑domain capsule – a complete branch of expertise (e.g., “fixed‑assets”).

Bounded context capsule – a very specific task, but intended to be part of a larger capsule.

What you will typically download: a sub‑domain capsule, because it provides enough breadth to be useful without being overwhelming.

Example:
accounting/fixed-assets gives you everything about fixed assets: depreciation methods, disposal accounting, revaluation rules, and related tools.

Visual aid (text diagram):

text
┌─────────────────────────────────────────────────┐
│  Capsule Registry (index)                       │
│  ┌───────────────────────────────────────────┐  │
│  │ accounting/                               │  │
│  │   ├─ fixed-assets/  ← you are here       │  │
│  │   ├─ accounts-receivable/                │  │
│  │   └─ tax/                                │  │
│  └───────────────────────────────────────────┘  │
└─────────────────────────────────────────────────┘
3. Finding Capsules: The Registry
Capsules are listed in a public registry – a simple JSON index that maps capsule IDs to Git repositories.

How to search:

Use the capsule search command (if the SDK provides it) to list capsules by domain.

Or browse the registry repository on GitHub – each entry includes a description, author, version, and source integrity level.

Example search output:

text
$ capsule search accounting
accounting/fixed-assets         Fixed Assets (GAAP)               v1.0.0   community-verified
accounting/accounts-receivable  AR Management                     v0.9.0   self-certified
accounting/tax                  US Corporate Tax                  v2.1.0   community-verified
What you see for each capsule:

ID (e.g., accounting/fixed-assets)

Human‑readable name

Version

Trust level (self‑certified, community‑verified, professionally‑audited)

Author

Short description

No web store required – the registry is a Git repository. You can also install directly from a Git URL if the author shares it privately.

4. Installing (Procuring) a Capsule
Installation is a single command using the capsule CLI (included in the SDK).

bash
capsule install accounting/fixed-assets
What happens behind the scenes:

The CLI looks up the capsule ID in the registry index.

It clones the capsule’s Git repository (or downloads a tagged release).

It verifies the capsule’s integrity (checksum, optional signature).

It stores the capsule in a local cache (~/.capsules/).

No account, no login, no payment required for open capsules.

Alternative installation (for power users or when a capsule is not in the registry):

bash
capsule install git+https://github.com/author/my-capsule
First‑time setup:

Install the SDK: pip install capsule-sdk

Run capsule init to create a local configuration (optional, only if you plan to author capsules).

Regular use: You only need to install a capsule once. After that, you inject it into your agent.

5. Loading (Injecting) a Capsule into Your Agent
Once installed, loading a capsule into your agent is one line of code (or one CLI command for testing).

For Python agents (using the SDK):
python
from capsule_sdk import CapsuleLoader, Injector

# Load the capsule
capsule = CapsuleLoader.load("accounting/fixed-assets")

# Create an injector
injector = Injector(capsule)

# Generate the system prompt and tools for your agent
system_prompt = injector.generate_system_prompt()
tools = injector.get_tools()

# Now pass these to your agent (e.g., LangChain, CrewAI, or raw OpenAI)
agent = create_agent(system_prompt, tools)
For CLI testing (to see what the capsule does):
bash
capsule run accounting/fixed-assets --input "What is the straight‑line depreciation for an asset costing $10,000 with a salvage value of $1,000 and a 5‑year life?"
Visual aid: Injection flow
text
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│ User Agent  │────▶│   Injector  │────▶│   Capsule   │
│ (your code) │     │ (SDK)       │     │ (local copy)│
└─────────────┘     └─────────────┘     └─────────────┘
                            │
                            ▼
                    ┌─────────────┐
                    │   Agent     │
                    │ now has     │
                    │ domain      │
                    │ expertise   │
                    └─────────────┘
No environment variables, no API keys, no model retraining. The capsule is just data + lightweight logic.

6. First Use vs. Regular Use
Step	First‑time user	Regular user
Setup	Install SDK (pip install capsule-sdk).	Already installed.
Finding a capsule	Use capsule search or browse registry.	Already knows which capsules are needed; may search for new ones.
Installation	capsule install <id> – downloads and caches.	Same command (cached, so fast).
Injection	Write a few lines of code (or use CLI).	Reuse the same injection pattern; may automate in agent startup.
Updates	capsule update <id> to get latest version.	Same command.
Expected learning curve: 5 minutes to first injection. The CLI and SDK are designed to be minimalist and self‑documenting.

7. Comparison to “Claude Skills” and Similar Tools
You may have heard of Claude Skills (Anthropic) or other “skill” systems. The Context Capsule ecosystem differs in several deliberate ways:

Feature	Claude Skills	Context Capsules
Granularity	Typically micro‑skills (single task).	Sub‑domain (complete area of expertise).
Knowledge representation	Implicit in prompts.	Explicit, auditable rules + process graphs.
Source provenance	Not required.	Mandatory sources.csv – every rule traces to a public source.
Injection method	Built into Claude’s API.	Framework‑agnostic SDK (LangChain, CrewAI, raw Python).
Trust model	Relies on Anthropic’s curation.	Community verification + optional professional audits.
Openness	Closed, proprietary.	Fully open source (capsules and SDK).
Our validated approach: We prioritise order, transparency, and user control over convenience of a single vendor. The ecosystem is designed to be a public commons of domain expertise, not a product tied to one model.

We welcome comparisons – they highlight that we have solved the fragmentation problem (too many micro‑skills) and the trust problem (black‑box skills) that plague other “skill” systems.

8. Expectations and Limitations (Be Honest)
What capsules can do:

Provide deterministic, auditable domain knowledge to any agent.

Dramatically improve an SLM’s performance on domain‑specific tasks.

Reduce hallucinations by giving the agent a map and rules to follow.

Enable collaboration – authors improve capsules over time; users get updates.

What capsules cannot do (yet):

Guarantee 100% accuracy – always verify critical outputs.

Replace general intelligence – they augment, not replace, the base model.

Automatically update when regulations change – you must install new versions.

Provide real‑time data (e.g., live stock prices) – they are static knowledge packs.

User responsibility: You are responsible for validating capsule outputs in high‑stakes scenarios (e.g., tax filings). Capsules are tools, not authorities.

9. Future Roadmap (User‑Facing)
Professional audits – third‑party firms will certify capsules (paid, optional).

Automatic update notifications – the SDK will check for newer versions.

Graphical capsule explorer – a web UI to browse and compare capsules.

Private capsules – for organisations that want to share internal expertise without public disclosure (using private Git repos + access tokens).

All these will be backward compatible – your existing injection code will continue to work.

10. Get Started Today
Install the SDK

bash
pip install capsule-sdk
Search for a capsule

bash
capsule search accounting
Install it

bash
capsule install accounting/fixed-assets
Inject into your agent (see code example above).

Explore the source – every installed capsule is just a folder. Open it, read the rules, check the sources.

You are now part of the ecosystem. Whether you use capsules or contribute your own, you help build a commons of verified, portable expertise.

Appendix: Visual Reference Cards
A. Domain Hierarchy Card
text
┌─────────────────────────────────────────────┐
│  DOMAIN (e.g., healthcare)                  │
│  ┌────────────────────────────────────────┐ │
│  │ SUB‑DOMAIN (e.g., medical billing)     │ │
│  │ ┌────────────────────────────────────┐ │ │
│  │ │ BOUNDED CONTEXT (e.g., claim form) │ │ │
│  │ └────────────────────────────────────┘ │ │
│  └────────────────────────────────────────┘ │
└─────────────────────────────────────────────┘
B. Installation & Injection Flow
text
User Command                SDK Actions
─────────────               ────────────
capsule install id    →     Look up in registry
                            Clone repo
                            Verify hash
                            Store locally

In agent code:        →     Load from cache
CapsuleLoader.load()        Generate prompt & tools
                            Inject into agent
C. Trust Badges
Badge	Meaning
🟢 Self‑certified	Passes automated tests; author claims integrity.
🟡 Community‑verified	Positive ratings and usage by others.
🔵 Professionally‑audited	Audited by an accredited third party (future).
End of Manifesto

“Expertise should be a resource, not a secret.” – The Context Capsule Project


