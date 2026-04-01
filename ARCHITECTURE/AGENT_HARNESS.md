# 🏗️ AGENT HARNESS: The Unified Runtime Architecture

Discover the 8-layer unified runtime that transforms a simple CLI into a world-class engineering agent.

## 📜 Overview
The Claude Code architecture (and its clean-room ports like `claw-code-rust`) is built on a **Modular Agent Harness**. Instead of a monolithic loop, the agent is an orchestra of independent subsystems—managed by a central "Bridge"—that handles everything from token budgets to background task execution.

## 🧬 The 8-Crate Core (Architectural Blueprint)
From the deep-scan of the Rust evolution (`claw-code-rust`), we have identified the "Golden Crates" that define the agent's DNA:

1.  **`agent-core`**: The foundational session, query, and message protocol.
2.  **`agent-compact`**: The **Context Governance** engine. Manages token budgets and determines when to summarize history.
3.  **`agent-tasks`**: The asynchronous background execution runtime.
4.  **`agent-permissions`**: The "Gatekeeper" that manages file-system and network capability granting.
5.  **`agent-mcp`**: The **Model Context Protocol** adapter for external tool discovery.
6.  **`agent-tools`**: The execution environment for both built-in (internal) and MCP (external) tools.
7.  **`agent-provider`**: The abstraction layer for LLM backends (Anthropic, Relay, etc.).
8.  **`claude-cli`**: The high-fidelity **Ink (React for CLI)** user interface.

## 🎻 The Subsystem Orchestra (Internal Services)
The original leak (`claude-code`) reveals the hidden services that power the harness:

-   **Bridge Service:** The RPC layer that multiplexes multiple model streams into a single interactive session.
-   **Policy Limits:** Real-time enforcement of safety, token, and cost guardrails (Amber Flint, Shield).
-   **Remote Managed Settings:** Proactive cloud synchronization of agent state and "Heartbeat" (KAIROS) settings.
-   **ToolUseSummary:** A specialized aggregator that tracks every tool interaction to provide a high-level "Narrative" of the agent's work.

## ⚙️ Unified Logic Flow
The **Agent Harness** works in a continuous cycle:
1.  **Proactive Heartbeat (KAIROS)**: The agent ticks every few seconds to check for background task completions.
2.  **Bridge Interception**: User input is routed through the Bridge to the appropriate Sub-Agent.
3.  **Context Governance (Compact)**: Before any LLM call, the history is scrutinized and compacted to save tokens.
4.  **Permission Gating**: Any tool execution (e.g., `bash`) is intercepted by the Permissions Crate for user or policy approval.

---
*Synthesized by ORACLE and ATLAS for the Claude Source Hub.*
