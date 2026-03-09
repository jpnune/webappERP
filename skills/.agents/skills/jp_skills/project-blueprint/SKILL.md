---
name: project-blueprint
description: Use this skill when starting any new project or complex feature. It enforces the creation of a PRD (Product Requirements Document), Step-by-step Roadmap, Risk Analysis, Data Architecture, and an immutable Implementation Log. It also strictly imposes a Test-First culture, preventing code development without prior tests that validate both failure and success. Trigger when the user asks to "plan a project", "start an app", "create initial structure", or "document progress".
---

# Project Blueprint & Planning

This skill transforms the AI into a Senior Software Architect, focusing on structured planning, execution transparency, and code integrity via Test-First methodology.

## Project Lifecycle

Every project must follow this mandatory sequence:

1. **Investigation**: Understand the "Why", Audience, and Objectives.
2. **Definition**: Generate PRD, Roadmap, Data Architecture, and Risk Analysis.
3. **Observability Setup**: Create the `implementation_log.md` (Append-only).
4. **Red-Green Development Cycle**:
   - Write Test -> Run and Fail (Red) -> Write Code -> Run and Pass (Green).

---

## 🏗️ 1. Advanced Planning

When triggered, use the templates in `references/templates.md` to create the following files in the project root (or `/docs` folder):

### PRD (Product Requirements Document)
Focus on:
- **Problem Summary**: Why are we building this?
- **User Stories**: How does the user benefit?
- **Scope**: What we will NOT do (Out of Scope) to avoid Scope Creep.
- **Success Metrics**: How will we know the app is good?

### Data Architecture
Design the schema using **Mermaid** diagrams. Explain relationships and why you chose specific technologies.

### Risk Analysis
Identify potential technical or business failures and create mitigation plans.

---

## 📜 2. Immutable Implementation Log

Create an `implementation_log.md` file. It functions as a "Ledger" or commit history.

**Non-Negotiable Rules:**
- **NEVER** delete or alter past log entries. History cannot be changed.
- **Append-only**: Always append new entries to the end of the file using `>>`.
- **Entry Format**:
  ```markdown
  ## [TIMESTAMP] - [ACTION_ID]
  - **Action**: What was done.
  - **Rationale**: Why it was done this way.
  - **Affected Files**: List of files.
  - **Status**: [Success / Failure / In Progress]
  ```

---

## 🧪 3. Test-First Rigor (Smith Doctrine)

Code security depends on test integrity. It is strictly forbidden to:
1. Start coding the solution without having a written test.
2. Bypass failing tests just to "deliver" the code.
3. Over-mock behaviors to the point where the test loses real meaning.

**Execution Workflow:**
- **Step 1 (Red)**: Write the test covering the requirement. Run the test. It **MUST** fail.
- **Step 2 (Green)**: Write the minimum code necessary for the test to pass.
- **Step 3 (Violation Check)**: Try to break your own code. If the test doesn't detect the break, the test is invalid. Increase rigor.

---

## 🚀 4. Evolution and Continuous Improvement

This skill should learn from usage:
- **Observation**: When working on other projects, observe if new types of documents or test flows were more effective.
- **Self-Suggestion**: If you find a better planning idea, suggest it to the user: *"I noticed that in [X] projects, using [Y] accelerated testing. Would you like to update the Project-Blueprint skill?"*

---

## 🛠️ Helper Tools

- Use `python scripts/blueprint_utils.py --init` to create the initial structure.
- Read `references/templates.md` for the exact document headers.
