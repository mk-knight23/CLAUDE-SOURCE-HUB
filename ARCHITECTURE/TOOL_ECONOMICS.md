# ⚙️ TOOL ECONOMICS: The Schema-Driven Engine

Discover how Claude Code manages complex tool-definitions and the "Modular Context Protocol" (MCP) for external discovery.

## 📜 Overview
The **Tool Economics** of the Claude ecosystem is based on a high-fidelity **Tool Registry**. Tools are not just functions—they are schema-driven "Economic Units" that the agent can discover, scaffold, and execute with precision.

## 🧬 The Tool Lifecycle
From the patterns in `src/tools/` and `agent-tools`, we have identified the "Golden Flow" of tool interaction:

1.  **Discovery (The Registry):** The agent scans its `builtin` directory and any connected **MCP (Model Context Protocol)** servers.
2.  **Scaffolding (The Schema):** Each tool provides a strictly-defined JSON Schema (Parameters + Types).
3.  **Permission Gating:** The **Permissions Crate** intercepts the call to ensure the user (or the policy) has granted the necessary capability.
4.  **Execution (The Runtime):** The tool is executed in a controlled environment (e.g., the `bash` tool uses a persistent sub-shell).
5.  **Result Translation (The Digest):** The output is formatted and, if necessary, "Compacted" (using the **Context Governance** engine) to preserve token space.

## 🧱 The Tool Registry (Subsystem Deep-Dive)
The architecture separates tools into two distinct categories:

### 1. Built-in (System) Tools
Native tools that provide "Hard" capabilities to the agent:
- **`bash` & `ls` & `find`**: High-performance file-system exploration.
- **`cat` & `grep`**: High-fidelity content extraction.
- **`dispatch`**: The internal RPC tool for inter-agent communication.

### 2. External (MCP) Tools
Dynamic tools discovered via the **Model Context Protocol**:
- **Search Servers**: Google, Brave, etc.
- **Data Servers**: Postgres, GitHub, Slack.
- **Custom Skills**: User-defined capabilities.

## 🧪 Token Efficiency: The "Digest" Strategy
When a tool returns a large output (e.g., a 1,000-line log), the **Context Governance** engine (from `agent-compact`) determines whether to:
- **Truncate:** Preserve only the head and tail.
- **Summarize:** Create a semantic digest of the result.
- **Pass-through:** Forward the full output if it's within the budget.

---
*Synthesized by ORACLE and ATLAS for the Claude Source Hub.*
