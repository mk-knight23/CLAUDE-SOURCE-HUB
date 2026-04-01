# ⌛ KAIROS: The "Always-On" Mode

Discover the unreleased, high-frequency agentic ticker logic found in the Claude Code leak.

## 📜 Overview
**KAIROS** is an internal Anthropic feature designed for proactive, autonomous task management. While the standard Claude Code operates in a request-response cycle, KAIROS enables a persistent "Heartbeat" that allows the agent to check for updates, manage background tasks, and proactively prompt the user.

## 🧬 Ticking Logic
From `main.tsx` and `bootstrap/state.js`:

- **Interval:** The core logic indicates a heartbeat cycle, intended to tick at a frequent interval (e.g., every 15 seconds).
- **Proactivity:** When `setKairosActive(true)` is triggered, the agent gains access to persistent `AsyncLocalStorage` context.
- **Tooling:** KAIROS is closely tied to the `ScheduleCronTool` and `ScheduleOnceTool`, which allow it to register future actions and "wake up" to execute them.

## ⚙️ Capabilities
| Feature | Flag | Description |
| :--- | :--- | :--- |
| **Active Mode** | `KAIROS` | The base "Always-On" capability. |
| **Channels** | `KAIROS_CHANNELS` | Multi-transport support for persistent sessions. |
| **Brief Mode** | `KAIROS_BRIEF` | High-density status updates for background processes. |

## 🧪 Architectural Impact
KAIROS represents a fundamental shift from a "Tool" to a "Worker". It enables the agent to maintain state across power-cycles and terminal sessions, essentially turning Claude Code into a permanent background daemon for development.

---
*Synthesized by ORACLE for the Claude Source Hub.*
