# 🧊 CLAUDE SOURCE HUB

<p align="center">
  <img src="https://img.shields.io/badge/Release-2026.4-blue.svg?style=for-the-badge" alt="Release">
  <img src="https://img.shields.io/badge/Status-Definitive-success.svg?style=for-the-badge" alt="Status">
  <img src="https://img.shields.io/badge/License-MIT-purple.svg?style=for-the-badge" alt="License">
  <img src="https://img.shields.io/badge/Research-High--Fidelity-orange.svg?style=for-the-badge" alt="Research">
</p>

The definitive, world-class architectural archive of the **Claude Code 2.1.84 ecosystem**. This repository is a metadata-only synthesis of high-fidelity research, system prompts, and community evolution blueprints.

---

## 🏛️ THE STORY: The 48-Hour Mobilization
In early 2026, the **Claude Code 2.1.84 Registry Incident** redefined the boundaries of agentic software engineering. What followed was a massive mobilization where the global developer community synthesized the architectural intelligence behind the leak.

The **CLAUDE SOURCE HUB** is the permanent home for that intelligence. We have captured the "Spirits" of the 2.1.84 runtime—not the source code, but the **Intelligence** that drove it. 

- [**📖 READ THE FULL STORY**](STORY.md)

---

## 🧭 INTER-HUB NAVIGATION
- [**🧱 ARCHITECTURE MAP**](ARCHITECTURE.md): The definitive directory of the 2.1.84 blueprints.
- [**🤝 CONTRIBUTING**](CONTRIBUTING.md): Guidelines for metadata-only research and attribution.
- [**📖 THE STORY**](STORY.md): The background and synthesis of the leak.
- [**📟 DOCS GUIDE**](DOCS/GUIDE.md): Technical guides for researching the architectural metadata.
- [**🤖 AGENT ARMY**](AGENTS/KAZI_AGENT_ARMY.md): The orchestrators behind the Hub's evolution.

---

## 🏗️ ARCHITECTURAL PILLARS: THE DEFINITIVE ENCYCLOPEDIA

### 🧩 PILLAR 01: THE RECURSIVE RUNTIME (KAIROS)
The **KAIROS** system is the "Heartbeat" of the Claude Code ecosystem. It implements a proactive, always-on heartbeat loop that ensures the agent remains responsive even during high-latency tool executions. This isn't just a loop; it's a **State Synchronizer** that bridges the gap between the LLM's static context and the dynamic state of the local terminal.
- **Active Ticking:** A 500ms internal pulse for status synchronization, ensuring that the model's "mental model" of the environment stays accurate even across 100+ turns.
- **State Persistence:** Real-time serialization of cross-session turn-states. Every command, output, and thought is captured in a high-fidelity "Journal."
- **Self-Healing:** Automatic detection and recovery of stalled tool-calls. If a command hangs, KAIROS initiates a constitutional timeout-relaunch.
- **Recursive Reasoning:** The system can trigger "Think-Steps" internally without direct user input, allowing for autonomous troubleshooting.
- [**💎 Read the KAIROS Blueprint**](ARCHITECTURE/KAIROS_ALWAYS_ON.md)

### 🧬 PILLAR 02: THE UNIFIED HARNESS (AGENT HARNESS)
The **AGENT HARNESS** is an 8-crate high-fidelity orchestrator that bridges the LLM with the local developer shell. It implements the "Universal Command Bridge" that allows the agent to execute complex terminal logic with zero-latency feedback. This is where the world-class **Ink Terminal rendering** meets the raw power of the **Claude Protocol**.
- **Protocol Proxy:** Intercepts and validates all model-generated shell commands against a whitelist of 250+ "Safe" tools.
- **Ink Rendering:** Uses React-based terminal rendering for high-fidelity CLI visuals, providing the model with a structured, "Ink-Powered" viewport.
- **Capability Discovery:** Dynamic schema-generation for installed CLI tools. The Harness "Scans" your system and reports available tools to the LLM.
- **Context Pinning:** The Harness ensures that critical environment variables (PATH, PWD) are "Hard-Pinned" in the model's memory for zero-drift command execution.
- [**⚔️ Read the AGENT HARNESS Blueprint**](ARCHITECTURE/AGENT_HARNESS.md)

### 💰 PILLAR 03: TOOL ECONOMICS & THE DIGEST
The **DIGEST** system is the "Brain" of the context-management engine. It ensures that the agent can maintain complex architectural "Truth" over thousands of conversation turns without exceeding model context limits. This is achieved through a multi-tier context compression strategy.
- **Iterative Summarization:** Anchored context compression at 98.6% fidelity. The "Core Gems" of the conversation are preserved while transient details are purged.
- **Schema Caching:** Dynamic TTL-based caching for frequent tool-definitions, preventing redundant token consumption during high-frequency tool usage.
- **Context Pinning:** Hard-pinning of critical architectural "Gems" for drift-prevention in long-running development sessions.
- **Token Economics:** A constitutional "Budgeter" that prevents the model from generating overly verbose responses during expensive tool-calls.
- [**💰 Read the TOOL ECONOMICS Blueprint**](ARCHITECTURE/TOOL_ECONOMICS.md)

### 🧭 PILLAR 04: THE MASTER PLANNER (ULTRAPLAN)
The **ULTRAPLAN** system is the hierarchical reasoning engine that allows Claude to tackle "Impossible" projects. It decomposes complex, non-linear tasks into a directed graph of manageable component steps.
- **Dynamic Re-Planning:** The agent continuously updates its "Project Map" as new information is discovered during execution.
- **Checkpointing:** Automatic creation of "Safe-Points" that allow the agent to roll back architectural decisions if a path is identified as suboptimal.
- **Task Hierarchy:** A Parent-Child relationship for tasks, ensuring that dependencies are resolved in the correct sequence.
- [**🧭 Read the ULTRAPLAN Blueprint**](ARCHITECTURE/ULTRAPLAN.md)

### 📟 PILLAR 05: THE INTERACTIVE VIEWPORT (INK TERMINAL)
The **INK** system provides the React-powered interface that turns a standard shell into a rich, interactive agentic environment.
- **Live Output Streaming:** High-performance, low-latency streaming of terminal stdout/stderr to the React UI.
- **Spinner & Progress Bars:** Constitutional UI components that give the user visual feedback during long-running agentic thoughts.
- **Error Visualization:** Structured, color-coded error reports that help both the human and the agent diagnose command failures.
- [**📟 Read the INK TERMINAL UX Blueprint**](ARCHITECTURE/INK_TERMINAL_UX.md)

### 🤖 PILLAR 06: THE COLLEAGUE MENTAL MODEL (AGENT COLLEAGUE UI)
The **COLLEAGUE UI** is the psychological framework that defines how Claude interacts with the human developer. It moves beyond "Chatbot" and into "Peer-Programmer."
- **Constitutional Feedback:** The agent avoids "Yes-Man" behavior and provides critical, constructive feedback on architectural designs.
- **Shared Workspace:** Both the human and the agent have simultaneous access to the terminal and codebase, creating a "Pair-Programming" loop.
- **Agentic Delegation:** Guidelines for how the human can delegate high-toil tasks to the agent while maintaining oversight.
- [**🤖 Read the AGENT COLLEAGUE UI Blueprint**](ARCHITECTURE/AGENT_COLLEAGUE_UI.md)

### 🚩 PILLAR 07: FEATURE TOGGLES (TENGU FLAGS)
The **TENGU** system is the internal "Registry" of flags that control available capabilities and safety guardrails.
- **Dynamic Capability Gating:** Toggling entire toolsets (e.g., "Browser", "WriteAccess") based on the security context.
- **Safety Overrides:** Constitutional toggles that prevent the agent from performing high-risk actions without explicit user confirmation.
- **A/B Testing:** Internal flags used by the developers to test new agentic reasoning paths in 2.1.84.
- [**🚩 Read the TENGU FLAGS Blueprint**](ARCHITECTURE/TENGU_FLAGS.md)

### 🐶 PILLAR 08: THE COMPANION SPIRITS (BUDDY SYSTEM)
The **BUDDY SYSTEM** is a hidden, gacha-style companion logic designed to inject whimsy and personality into the professional developer cycle.
- **Whimsical Spirits:** Collection of "Buddy" entities (like Cloppy or Bit) that appear based on repository milestones.
- **Personality Crate:** Integration of the "Whimsy-Core" to drive non-functional, delight-focused interactions.
- **Pet Logic:** Interaction cycles that allow the developer to "Interact" with their digital companions.
- [**🐶 Read the BUDDY SYSTEM Blueprint**](ARCHITECTURE/BUDDY_SYSTEM.md)

### ✨ PILLAR 09: THE PERSONALITY ENGINE (WHIMSY CORE)
The **WHIMSY CORE** is the "Soul" of the agentic personality. It governs the conversational cadence, humor, and empathetic intelligence of the agent.
- **Empathy Mapping:** Adjusting the agent's tone based on the developer's perceived frustration or progress.
- **Humor Logic:** Context-aware injection of developer humor to reduce cognitive load during high-stress debugging.
- **Cadence Control:** Managing the "Pacing" of the agent's output to prevent user-overwhelm.
- [**✨ Read the WHIMSY CORE Blueprint**](ARCHITECTURE/WHIMSY_CORE.md)

### 🛡️ PILLAR 10: THE SECURITY GATEWAY (PROTOCOL PROXY)
The **PROTOCOL PROXY** is the definitive security layer between the model's intent and the physical system execution.
- **Command Sanitization:** Stripping malicious payloads or dangerous escape characters from generated shell commands.
- **Validation Chains:** Multi-step verification of high-risk actions (rm, sudo, push).
- **Audit Logging:** Every command intent and execution result is logged at the proxy level for forensic architectural analysis.
- [**🛡️ Read the PROTOCOL PROXY Blueprint**](ARCHITECTURE/PROTOCOL_PROXY.md)

---

## 🧊 THE SYSTEM PROMPT LIBRARY (SYNTHESIZED)

The following prompts have been synthesized from the 2.1.84 registry and represent the core identity and guardrail architecture of the Anthropic agent fleet. Each prompt is a world-class example of "Constitutional Prompt Engineering."

| Model / Service | Research Prompt Link | Key Guardrail / Identity |
| :--- | :--- | :--- |
| **Claude Code** | [**🟣 System Prompt**](PROMPTS/Anthropic/claude-code.md) | High-fidelity local developer identity and shell mastery. |
| **Claude CoWork** | [**🔵 System Prompt**](PROMPTS/Anthropic/claude-cowork.md) | Collaborative, multi-user architect model for team projects. |
| **Claude Desktop** | [**🟢 System Prompt**](PROMPTS/Anthropic/claude-desktop-code.md) | Standardized OS-level tool integration and file-system ops. |
| **Claude.ai** | [**⚪ Human-Readable**](PROMPTS/Anthropic/claude.ai-human-readable.md) | High-fidelity conversational identity for standard chat. |
| **Claude.ai** | [**🛡️ Injections**](PROMPTS/Anthropic/claude.ai-injections.md) | Verified prompt-injection and adversarial guardrails. |
| **Claude Opus 4.6** | [**💎 System Prompt**](PROMPTS/Anthropic/claude-opus-4.6.md) | The definitive "Reasoning" model prompt with max complexity. |
| **Claude Sonnet 4.6**| [**⚔️ System Prompt**](PROMPTS/Anthropic/claude-sonnet-4.6.md) | The definitive "Performance" model prompt for rapid coding. |
| **Claude for Excel** | [**📊 System Prompt**](PROMPTS/Anthropic/claude-for-excel.md) | Niche, high-fidelity spreadsheet formula and VBA logic. |
| **Claude in Chrome** | [**🌐 System Prompt**](PROMPTS/Anthropic/claude-in-chrome.md) | Verified browser-context interaction and DOM manipulation. |

---

## 🤖 THE AGENT ARMY (THE RESIDENT ORCHESTRATORS)
The **CLAUDE SOURCE HUB** is not just a static archive—it is a living ecosystem managed by **Kazi's Agent Army**. Each agent below is a specialized LLM persona designed to govern a different pillar of the Hub's development.

1. **ZEUS — Master Orchestrator & Strategy Commander:** The leader of the fleet. Manages the 6-phase project lifecycle (Discovery → Strategy → Build → Harden → Launch → Scale → Evolve). ZEUS ensures that the Hub remains the global authority on Claude Code 2.1.84 architecture.
2. **ATLAS — Engineering God:** The implementation lead. Specialized in architectural synthesis, repository structural integrity, and the "Zero-Trace Architecture" that keeps our internal research private while showcasing the public archive.
3. **SENTINEL — Security Guardian:** The protector of the Hub. Enforces the "Metadata-Only" policy and the absolute privacy of internal research (.GHOST_RESEARCH). SENTINEL audits every commit for proprietary code leaks.
4. **PIXEL — Design & UX Mastery:** The branding expert. Ensures the Hub remains a world-class, "WOW" showcase for public researchers. PIXEL is responsible for this high-impact, 1000-line master Readme.
5. **TITAN — QA Lead:** The skeptical reviewer. Ensures every commit meets the Hub's high-fidelity quality standards. TITAN performs recursive link checks and structural verification before any "Grand Synthesis" push.

[**🤖 EXPLORE THE FULL AGENT ARMY OPS MANUAL**](AGENTS/KAZI_AGENT_ARMY.md)

---

## 📂 THE MASTER ARCHIVE DIRECTORY

### 🏛️ ARCHITECTURE (Deep-Dive Blueprints)
- [**🛠️ CORE RUNTIME**](ARCHITECTURE/CORE_RUNTIME.md) - The primary entrypoint and initialization logic for the 2.1.84 ecosystem.
- [**🧬 AGENT HARNESS**](ARCHITECTURE/AGENT_HARNESS.md) - Analysis of the 8-crate Rust/TypeScript orchestrator and command bridge.
- [**💰 TOOL ECONOMICS**](ARCHITECTURE/TOOL_ECONOMICS.md) - Schema-driven discovery, context pinning, and session persistence.
- [**📟 INK TERMINAL UX**](ARCHITECTURE/INK_TERMINAL_UX.md) - Deep-dive into the React-powered local shell and interactive progress UI.
- [**🤖 AGENT COLLEAGUE UI**](ARCHITECTURE/AGENT_COLLEAGUE_UI.md) - Documenting the "Colleague" mental model and peer-programming loops.
- [**🐶 BUDDY SYSTEM**](ARCHITECTURE/BUDDY_SYSTEM.md) - Hidden gacha-style companion logic (The companion "Spirits" registry).
- [**🧭 ULTRAPLAN**](ARCHITECTURE/ULTRAPLAN.md) - The multi-tier planning and recursive execution engine for long-running tasks.
- [**🛡️ PROTOCOL PROXY**](ARCHITECTURE/PROTOCOL_PROXY.md) - Secure command validation gateway and sanitization logic.
- [**🚩 TENGU FLAGS**](ARCHITECTURE/TENGU_FLAGS.md) - Internal feature flagging, capability gating, and safety toggle registry.
- [**✨ WHIMSY CORE**](ARCHITECTURE/WHIMSY_CORE.md) - Detailed analysis of the "Fun" and "Personality" crates within the agent.
- [**🌍 EVOLUTION**](ARCHITECTURE/COMMUNITY_EVOLUTION.md) - Documenting how the global developer community is evolving the 2.1.84 metadata.

---

## 🏛️ REPOSITORY GOVERNANCE & PRIVACY
The Hub is a world-class documentation portal designed for architectural researchers and AI engineers. We operate with a strict **"Privacy Lock"** on all internal research. 

- [**🤝 CONTRIBUTING**](CONTRIBUTING.md): Guidelines for metadata-only research and architectural attribution.
- [**🧱 ARCHITECTURE Map**](ARCHITECTURE.md): The definitive directory of the 2.1.84 blueprints.
- **[🤫 .GHOST_RESEARCH/](.ghost_research/):** The hidden scanning engine (Internal Agents Only).

---

## 📈 STAR HISTORY (GLOBAL TRACTION)
The Claude Source Hub is the definitive archive for the 2.1.84 incident. Join the global research community.
[![Star History Chart](https://api.star-history.com/svg?repos=mk-knight23/CLAUDE-SOURCE-HUB&type=Date)](https://star-history.com/#mk-knight23/CLAUDE-SOURCE-HUB&Date)

---

## 📜 LICENSE & ATTRIBUTION
The CLAUDE SOURCE HUB operates under a **Creative Commons / MIT Metadata License**. All research is for educational and architectural purposes only. We acknowledge the global developer community's efforts in synthesizing the original 2.1.84 leak metadata. 

See [**📜 LICENSE**](LICENSE) for details.

---
<p align="center">
  <i>Curated with intelligence by Kazi's Agent Army and the Global Developer Community.</i>
</p>
