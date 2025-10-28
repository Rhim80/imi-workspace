# Agents

> Claude Code Subagents for advanced automation

## What are Agents?

Agents are specialized AI assistants that can:
- Perform complex multi-step tasks
- Read and analyze multiple files
- Generate comprehensive reports
- Operate semi-autonomously

Think of them as "mini Claude" with specific expertise.

## Available Agents

### 🔗 Zettelkasten Linker

**Purpose**: Comprehensive PKM vault analysis and curation

**What it does:**
1. **Quality Assessment**: Identifies files to delete/split/keep
2. **Link Suggestions**: Proposes bidirectional connections between notes
3. **Vault Health Report**: Generates actionable improvement plan

**When to use:**
- Your vault has grown to 50+ files
- Many notes feel isolated (few links)
- Want to clean up low-quality files
- Need help finding connections between ideas

**How to invoke:**

In Claude Code, say:
```
"Analyze my vault and suggest links between my notes"
```

Or:
```
"Check which files I should delete or split"
```

**Example workflow:**
1. User: "Analyze my entire PKM vault"
2. Agent reads all markdown files (except system files)
3. Agent evaluates quality (delete/split/keep)
4. Agent extracts key concepts from each file
5. Agent suggests connections between related notes
6. Agent generates comprehensive report with action items
7. User reviews and approves changes
8. (Optional) Agent applies approved changes

**Configuration:**

See `zettelkasten-linker.md` for:
- Quality thresholds (word counts, etc.)
- Link confidence settings
- Exclude patterns

## Creating Your Own Agent

Want to create a custom agent for your workflow?

### 1. Create a new `.md` file in this folder

### 2. Use this template:

```yaml
---
name: my-agent-name
description: Short description for when Claude should use this agent
model: sonnet
color: blue
---

You are [agent role and expertise].

## Core Mission
[What this agent does]

## Configuration
[Settings and parameters]

## Process
[Step-by-step workflow]

## Output Format
[What the agent returns]
```

### 3. Examples of useful agents:

- **Meeting Prep Agent**: Reads project folder → generates meeting agenda
- **Content Publisher**: Processes draft → formats for blog → publishes
- **Weekly Planner**: Reviews last week's daily notes → creates next week's plan
- **Expense Tracker**: Scans inbox for receipts → categorizes → updates sheet

## Tips for Effective Agents

1. **Single Responsibility**: One agent = one job
2. **Clear Output**: Define exactly what the agent returns
3. **Configurable**: Use config section for parameters
4. **Examples**: Include example workflows in description
5. **Testing**: Test with small datasets first

## Learn More

- [Agent Development Guide](../../../00-system/04-docs/agent-guide.md) (if available)
- Claude Code official docs: https://docs.claude.com/
- Example agents: Browse this folder

## Troubleshooting

**Q: How do I invoke an agent?**
A: Just describe what you want in natural language. Claude Code will automatically detect when to use an agent based on the `description` field.

**Q: Can agents modify files?**
A: Yes, if you approve. Most agents generate reports first, then ask for approval before making changes.

**Q: How long do agents take?**
A: Depends on vault size. For 300+ files, expect 2-5 minutes for analysis.

**Q: Can I run multiple agents?**
A: Yes, but run them sequentially (one at a time) to avoid conflicts.

---

**Need help?** Ask Claude Code: "How do I use the zettelkasten-linker agent?"
