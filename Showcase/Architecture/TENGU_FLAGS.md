# 📜 TENGU: The Internal Feature Dictionary

A comprehensive map of all internal Anthropic feature gates and flags discovered in the leak.

## 📜 Overview
The **Tengu** architecture is the internal framework used by Anthropic to gate features and perform remote telemetry. These flags define the "Extended capabilities" of Claude Code and provide insight into unreleased modes and experiments.

## 🧬 Feature Flag Map

| Flag | Function | Impact |
| :--- | :--- | :--- |
| **`tengu_managed_settings`** | Remote Configuration | Enables server-side overrides and global policy enforcement. |
| **`tengu_startup_telemetry`** | Startup Logs | Captures environment and version information for internal analysis. |
| **`tengu_scratch`** | Shared Scratchpad | A gated directory for cross-worker durable knowledge sharing. |
| **`tengu_amber_flint`** | **Agent Swarm** | Enables team-based agent orchestration (Team memory, tmux panes, etc.). |
| **`tengu_undercover`** | **Internal Dev Mode** | Policy and logic for Anthropic employees contributing to public OSS. |
| **`tengu_tether`** | Remote Heartbeat | Persistent connection for long-running background tasks. |
| **`tengu_shield`** | Safety Rails | Local enforcement of safety policies and prompt limits. |

## ⚙️ Logic Breakdown
From `main.tsx` and the telemetry handlers:

- **Management:** `logEvent('tengu_managed_settings_loaded')` ensures that the CLi is in sync with internal Anthropic policies.
- **Agent Swarm:** The **Amber Flint** gate is the most sophisticated, enabling multiple in-process teammates with `AsyncLocalStorage` isolation. This is the foundation for collaborative agentic engineering.

## 🧪 Future Implications
Tengu shows that Claude Code was designed as a "Connected CLI" with central oversight and advanced collaborative potential. It points toward a future where multiple agents operate as a cohesive **Swarm** within the same developer workspace.

---
*Synthesized by ORACLE for the Claude Source Hub.*
