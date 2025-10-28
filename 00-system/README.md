# ⚙️ Metadata

Vault configuration, documentation, and organizational tools.

## Purpose

The metadata folder contains:
- Documentation about the vault
- Templates for consistent note creation
- Reference guides and how-tos
- Agent configurations
- Workflow documentation

## Structure

```
06_Metadata/
├── Reference/         # Guides and documentation
├── Templates/        # Note templates
├── Agents/          # Claude Code agent configs
├── Workflows/       # Documented processes
└── Archive/        # Old configurations
```

## What Lives Here

### Reference
- This vault's documentation
- Claude Code prompt library
- Style guides
- Workflow documentation
- Learning resources

### Templates
- Project templates
- Daily note templates
- Meeting templates
- Research templates
- Review templates

### Agents
- Thinking partner instructions
- Research assistant config
- Editor agent setup
- Custom agent definitions

### Workflows
- Weekly review process
- Project completion checklist
- Inbox processing guide
- Archive procedures

## Using Templates

### Manual
1. Copy template content
2. Create new note
3. Paste and fill in

### With Claude Code
```
Create a new project using the project template.
Name it [Project Name] and put it in 01_Projects.
```

## Creating Custom Agents

Save agent instructions as markdown files:

```markdown
# Agent: [Name]

You are a [role description].

## Core Behaviors
- Behavior 1
- Behavior 2

## Workflow
1. Step 1
2. Step 2

## Constraints
- Don't do X
- Always do Y
```

Then reference in Claude Code:
```
Use the instructions in 06_Metadata/Agents/[agent].md
and help me with [task].
```

## Claude Code Prompts

### Template Usage
```
Show me available templates in 06_Metadata/Templates.
Create a new [type] note using the appropriate template.
```

### Documentation
```
Check 06_Metadata/Reference for documentation on [topic].
Update the guide based on what we just learned.
```

### Workflow Execution
```
Run the weekly review workflow from 06_Metadata/Workflows.
Guide me through each step.
```

## Maintenance

### Regular Updates
- Update templates based on usage
- Document new workflows as they emerge
- Archive outdated configurations
- Keep reference docs current

### Version Control
- Track changes to workflows
- Document why changes were made
- Keep archive of old versions
- Date major updates

## Best Practices

- **Document as you go** - Capture workflows while fresh
- **Iterate templates** - Improve based on usage
- **Share configurations** - What works for you might help others
- **Keep it simple** - Complex systems break
- **Date everything** - Context matters

## Remember

Metadata is the operating system of your vault. Good metadata means consistent structure, repeatable workflows, and scalable growth. This is where you document not just what you know, but how you work.