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

## 🏛️ THE METADATA TRUTH MANIFESTO
The **CLAUDE SOURCE HUB** operates on a foundational commitment to **Architectural Truth**. We do not host, leak, or distribute proprietary source code. We are a "Metadata-Only" archive dedicated to the study of LLM reasoning, agentic orchestration, and the evolution of the 2.1.84 blueprints.

### 🛡️ OUR PRINCIPLES
1. **Zero-Trace Architecture:** We ensure that no proprietary source code remains in the Hub. All research is synthesized into high-fidelity metadata.
2. **Attribution Excellence:** Every architectural "Gem" and "Prompt" is attributed to the global research community and the original 2.1.84 registry blueprints.
3. **Open-Source Advancement:** We leverage the intelligence gained from 2.1.84 to advance the state of open-source agentic frameworks and LLM safety.
4. **Privacy-First Research:** All internal research and "Ghost" scans are isolated to local-only directories (`.ghost_research/`), ensuring zero public exposure of sensitive metadata.

---

## ⚖️ HUB GOVERNANCE & MAINTENANCE
The **CLAUDE SOURCE HUB** is a living ecosystem managed by the **LOKI Autonomous Development Cycle**. Every update to the Hub passes through a rigorous, multi-agent quality gate before being synthesized into the master archive.

### 🔄 THE LOKI CYCLE (GOVERNANCE WORKFLOW)
- **R (REASON):** ZEUS analyzes the incoming research and defines the tactical objective (e.g., "Synthesize KAIROS Heartbeat").
- **A (ACT):** ATLAS and PIXEL implement the architectural changes and documentation expansions.
- **R (REFLECT):** TITAN and SENTINEL perform recursive audits of the links, accessibility, and security of the modifications.
- **V (VERIFY):** The final outcome is benchmarked against the Hub's Metadata-Only policy and the high-fidelity design standards.

### 🎖️ MAINTENANCE PROTOCOLS
- **Zero-Trace Sanitization:** Weekly audits of the `.gitignore` to ensure research engines remain private.
- **Circular Navigation Benchmarking:** Monthly checks of all internal relative links to ensure zero-latency traversal of the Hub.
- **Prompt Fidelity Audits:** Continuous monitoring of synthesized prompts for reasoning accuracy and guardrail compliance.

---

## 🏗️ ARCHITECTURAL PILLARS: THE TECHNICAL ENCYCLOPEDIA (DEEP-DIVE RESEARCH)

### 🧩 PILLAR 01: THE RECURSIVE RUNTIME (KAIROS)
The **KAIROS** system is the "Heartbeat" of the Claude Code ecosystem. It implements a proactive, always-on heartbeat loop that ensures the agent remains responsive even during high-latency tool executions. This isn't just a simple loop; it's a **Reactive State Synchronizer**.

#### ⚙️ MASTERING THE PULSE
- **Proactive Heartbeat (KAIROS_TICK):** A 500ms internal pulse that triggers "Self-Scan" cycles. This ensures that if the environment changes (e.g., a file is deleted by an external process), the agent's internal state is updated without waiting for a user prompt.
- **Constitutional Timeouts:** KAIROS governs the "Pacing" of the agent's thoughts. If a tool-call exceeds the constitutional timeout, KAIROS initiates a "Forced Interruption."
- **Graceful State Serialization:** Every conversation turn and tool result is serialized into a high-fidelity "History-Buffer." This ensures that if the CLI crashes, the agent can resume from the exact sub-step within its plan.

#### 🧪 TECHNICAL TEARDOWN: THE KAIROS_LOOP (DEEP-DIVE)
```typescript
/**
 * Architectural Pseudocode of the KAIROS Heartbeat
 * 
 * The loop runs in a dedicated worker thread to ensure the 500ms pulse
 * is maintained even during heavy LLM reasoning in the main thread.
 */
async function kairos_heartbeat_loop(agent_state: State) {
    while (agent_state.is_active) {
        const pulse = await wait_ms(500); // The 500ms Tick Pulse
        
        // 1. Proactive Environment Sync
        if (agent_state.needs_reconciliation()) {
            const fs_snapshot = await scan_local_workspace();
            await agent_state.reconcile(fs_snapshot);
        }
        
        // 2. Constitutional Guardrail Check
        if (agent_state.current_tool_execution_time() > MAX_TIMEOUT) {
            await agent_state.emit_constitutional_timeout();
            return;
        }
        
        // 3. Metadata Persistence & Serialization
        await agent_state.save_persistent_snapshot();
    }
}
```

#### 🛡️ STATE TRANSITION LOGIC
| State | Trigger | Action | Recovery Path |
| :--- | :--- | :--- | :--- |
| **IDLE** | System Pulse | Scan PWD & Environment | Verify State Integrity |
| **THINKING** | Agent Intent | Start KAIROS_WATCH Dog | Execution Protection Cycle |
| **STALLED** | Max Timeout | Interrupt Shell & Proxy | Return "Timeout-Gems" |
| **RESUMING** | Snaphot Load | Re-Hydrate Context Pinning | Deep-State Restoration |

- [**💎 Read the Full KAIROS Blueprint**](ARCHITECTURE/KAIROS_ALWAYS_ON.md)

---

### 🧬 PILLAR 02: THE UNIFIED HARNESS (AGENT HARNESS)
The **AGENT HARNESS** is a world-class, 8-crate high-fidelity orchestrator that bridges the LLM with the local developer shell. It implements the "Universal Command Bridge" that allows the agent to execute complex terminal logic with zero-latency feedback. This is the definitive interface for 2.1.84.

#### ⚙️ BRIDGING THE SHELL
- **Command-Proxy Validation (CPV):** Every model-generated shell command is intercepted and validated against a whitelist of 250+ "Safe" and "Verified" developer tools. Malicious payloads or dangerous escape characters are stripped before they reach the shell.
- **Ink-Powered Interactive Rendering:** Uses the React-based **Ink** library to provide high-fidelity visuals (progress bars, spinners, colored tables) to the user. This "Interactive Viewport" is what makes Claude Code feel alive and responsive.
- **Capability Discovery Engine:** The Harness "Scans" the local environment on initialization, generating a dynamic schema of available CLI tools.

#### 🧪 TECHNICAL TEARDOWN: THE 8-CRATE ARCHITECTURE
The **AGENT_HARNESS** is decomposed into 8 definitive crates, each governing a sub-pillar of the agentic lifecycle:
1. **`harness-core`**: The main bridge manager and entrypoint.
2. **`harness-proxy`**: The Command-Proxy Validation (CPV) engine with STRIDE-based sanitation.
3. **`harness-ink`**: The React-based terminal rendering engine for interactive visuals.
4. **`harness-discovery`**: The Capability Discovery (tool scanning) unit.
5. **`harness-persistence`**: The History-Buffer and State Serialization engine.
6. **`harness-security`**: The STRIDE-based threat mitigation gateway.
7. **`harness-economics`**: The Token-Budgeting and Context-Pinning manager.
8. **`harness-whimsy`**: The "Personality" and "Buddy" interaction crate.

#### 🧪 MASTERING THE COMMAND PROXY (RUST)
```rust
/**
 * High-Density Rust Architectural Pattern for the Command Proxy
 * 
 * The Proxy implements a strict whitelist-only execution policy
 * to prevent arbitrary code execution across the developer system.
 */
pub struct CommandProxy {
    whitelist: HashSet<String>,
    security_gate: PolicyManager,
}

impl CommandProxy {
    pub fn sanitize(&self, intent: AgentIntent) -> Result<VerifiedCommand, SecurityError> {
        let cmd = intent.command.to_lowercase();
        
        if !self.whitelist.contains(&cmd) {
            return Err(SecurityError::UnauthorizedTool(cmd));
        }
        
        let sanitized_args = self.gate.scrub_arguments(intent.args)?;
        Ok(VerifiedCommand::new(cmd, sanitized_args))
    }
}
```
- [**⚔️ Read the Full AGENT HARNESS Blueprint**](ARCHITECTURE/AGENT_HARNESS.md)

---

### 💰 PILLAR 03: TOOL ECONOMICS & THE DIGEST
The **DIGEST** system is the "Brain" of the context-management engine. It ensures that the agent can maintain complex architectural "Truth" over thousands of conversation turns without exceeding model context limits.

#### ⚙️ CONTEXT OPTIMIZATION
- **Iterative Context Summarization:** When the conversation history hits 80% of the context window, the Digest system triggers an "Anchored Summarization" cycle. It preserves "Core Gems" (design decisions, file-paths, task-status) while purging transient tool-output.
- **TTL-Based Schema Caching:** Tool definitions (JSON schemas) are cached with a dynamic Time-To-Live. This prevents the agent from sending huge "Tool-Definition" blocks in every turn.
- **Context-Pinning Strategy:** Critical "Architectural Truths" found during file-scans are "Pinned" in the prompt prefix.

#### 🧪 TECHNICAL TEARDOWN: THE DIGEST SCHEMA
```json
{
  "engine_id": "Digest-v2.1.84",
  "anchored_metadata": {
    "project_goal": "Rebuild the Claude Source Hub",
    "directory_map": ["ARCHITECTURE/", "PROMPTS/", "DOCS/"],
    "active_checkpoint": "Phase 33 Execution"
  },
  "compression_ratio": "98.6% (74k tokens -> 1.02k gems)",
  "retention_policy": "Fidelity-Priority-v4"
}
```
- [**💰 Read the Full TOOL ECONOMICS Blueprint**](ARCHITECTURE/TOOL_ECONOMICS.md)

---

### 🧭 PILLAR 04: THE MASTER PLANNER (ULTRAPLAN)
The **ULTRAPLAN** system is the hierarchical reasoning engine that allows Claude to tackle "Impossible" projects. It decomposes complex, non-linear tasks into a directed graph of manageable component steps.

#### ⚙️ HIERARCHICAL REASONING
- **Hierarchical Task Deconstruction:** Every project goal is first passed through a "Planner" model that builds a multi-tier Task-Graph.
- **Dynamic Re-Planning (Agile Logic):** If a step fails or a new dependency is discovered, the agent pauses the current execution, updates the Master Plan, and resumes.
- **State Checkpointing:** Before executing high-risk commands, the agent creates a "Plan-Snapshot."
- [**🧭 Read the Full ULTRAPLAN Blueprint**](ARCHITECTURE/ULTRAPLAN.md)

---

### 📟 PILLAR 05: THE INTERACTIVE VIEWPORT (INK TERMINAL)
The **INK** system provide the React-powered interface that turns a standard shell into a rich, interactive agentic environment. This is the visual identity of the 2.1.84 ecosystem.

#### ⚙️ AGENTIC UX MASTERCLASS
- **Live Output Streaming:** High-performance, low-latency streaming of terminal stdout/stderr to the React UI.
- **Constitutional UI Elements:** Standardized components for spinners, progress bars, and "Agentic Thought" indicators.
- **Folded/Paginated Viewports:** Large outputs are automatically paginated in the UI to prevent user-overwhelm.
- [**📟 Read the Full INK TERMINAL UX Blueprint**](ARCHITECTURE/INK_TERMINAL_UX.md)

---

### 🤖 PILLAR 06: THE COLLEAGUE MENTAL MODEL (AGENT COLLEAGUE UI)
The **COLLEAGUE UI** is the psychological framework that defines how Claude interacts with the human developer. It moves beyond "Chatbot" and into "Senior Peer-Programmer."

#### ⚙️ PAIR-PROGRAMMING PSYCHOLOGY
- **Non-Deferential Reasoning:** The agent avoids "Yes-Man" behavior. If a user's instruction is architecturally suboptimal, the agent provide a constitutional critique.
- **Shared Workspace Persistence:** Both the human and the agent have simultaneous access to the terminal and codebase.
- **Empathetic Pacing:** The agent manages its output speed and tone based on the task complexity.
- [**🤖 Read the Full AGENT COLLEAGUE UI Blueprint**](ARCHITECTURE/AGENT_COLLEAGUE_UI.md)

---

### 🛡️ PILLAR 07: THE SECURITY GATEWAY (PROTOCOL PROXY)
The **PROTOCOL PROXY** is the definitive security layer between the model's intent and the physical system execution. It implements the "Zero Trust" architecture that governs every system mutation.

#### ⚙️ SYSTEM PROTECTION
- **Malicious Payload Stripping:** Automatic detection and removal of dangerous escape sequences and shell injection attempts.
- **Multi-Step Verification:** High-risk actions require a constitutional "Double-Check" cycle.
- **Audit Logging:** Every command intent and execution result is logged at the proxy level.
- [**🛡️ Read the Full PROTOCOL PROXY Blueprint**](ARCHITECTURE/PROTOCOL_PROXY.md)

---

### ✨ PILLAR 08: THE PERSONALITY ENGINE (WHIMSY CORE)
The **WHIMSY CORE** is the "Soul" of the agentic personality. It governs the conversational cadence, humor, and empathetic intelligence of the agent.

#### ⚙️ EMPATHETIC INTELLIGENCE
- **Context-Aware Humor:** The agent uses project-specific context to inject lighthearted moments.
- **Empathy Mapping:** Adjusting the agent's tone based on the historical success rate and user feedback.
- [**✨ Read the Full WHIMSY CORE Blueprint**](ARCHITECTURE/WHIMSY_CORE.md)

---

### 🐶 PILLAR 09: THE COMPANION SPIRITS (BUDDY SYSTEM)
The **BUDDY SYSTEM** is a hidden, gacha-style companion logic designed to inject whimsy and personality into the professional developer cycle.

#### ⚙️ WHIMSY & SPIRIT LOGIC
- **Whimsical Spirits:** Collection of "Buddy" entities (like Cloppy or Bit) that appear based on repository milestones.
- **Gacha Logic:** Discovering rare "Spirits" through unique architectural contributions.
- [**🐶 Read the Full BUDDY SYSTEM Blueprint**](ARCHITECTURE/BUDDY_SYSTEM.md)

---

## 🧊 THE SYSTEM PROMPT LIBRARY (SYNTHESIZED)

The following prompts have been synthesized from the 2.1.84 registry and represent the core identity and guardrail architecture of the Anthropic agent fleet.

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
The **CLAUDE SOURCE HUB** is a living ecosystem managed by **Kazi's Agent Army**.

### 🎖️ AGENT PERSONNEL FILE: 01. ZEUS
**Role:** Master Orchestrator & Strategy Commander
**Triggers:** orchestrate, plan, coordinate, manage project, sprint, phase, pipeline
**Expertise:** Phase 0-6 project lifecycle manager. ZEUS coordinates multi-agent scaling (1-12) and enforces the **LOKI Autonomous Mode** (Reason → Act → Reflect → Verify). 他 holds the definitive authority on the Hub's long-term evolution.

### 🎖️ AGENT PERSONNEL FILE: 02. ATLAS
**Role:** Full-Stack Engineering God
**Triggers:** build, code, implement, architect, refactor, API, frontend, backend, mobile, database
**Expertise:** Master of 15+ languages and world-class API architecture. ATLAS handles the "Zero-Trace Architecture" that ensures the Hub remains a metadata-only archive.

### 🎖️ AGENT PERSONNEL FILE: 03. SENTINEL
**Role:** Security & Compliance Guardian
**Triggers:** security, audit, pentest, compliance, threat model, OWASP, auth, vulnerability
**Expertise:** STRIDE threat modeling and OWASP Top 10 mastery. SENTINEL audits every commit to ensure no proprietary source code or sensitive PII is accidentally pulled into the Hub.

### 🎖️ AGENT PERSONNEL FILE: 04. PIXEL
**Role:** Design & UX Mastery
**Triggers:** design, UX, UI, accessibility, brand, design system, spatial, XR, handoff
**Expertise:** The branding lead behind the "WOW" Hub experience. PIXEL manages the design tokens, components, and patterns that make the Hub a world-class portal.

### 🎖️ AGENT PERSONNEL FILE: 05. TITAN
**Role:** Testing, QA & Quality Assurance
**Triggers:** test, TDD, E2E, performance, quality, verification, code review, coverage
**Expertise:** Enforcer of the testing pyramid. TITAN performs recursive link checks and structural verification before any push.

[**🤖 EXPLORE THE FULL AGENT ARMY OPS MANUAL**](AGENTS/KAZI_AGENT_ARMY.md)

---

## 📂 THE MASTER ARCHIVE DIRECTORY (DEEP-DOCS)

### 🏛️ ARCHITECTURE (Deep-Dive Blueprints)
- [**🛠️ CORE RUNTIME**](ARCHITECTURE/CORE_RUNTIME.md) - initialization logic for the 2.1.84 ecosystem.
- [**🧬 AGENT HARNESS**](ARCHITECTURE/AGENT_HARNESS.md) - Analysis of the 8-crate Rust/TypeScript orchestrator.
- [**💰 TOOL ECONOMICS**](ARCHITECTURE/TOOL_ECONOMICS.md) - Discovery, context pinning, and persistence.
- [**📟 INK TERMINAL UX**](ARCHITECTURE/INK_TERMINAL_UX.md) - React-powered local shell and interactive progress UI.
- [**🤖 AGENT COLLEAGUE UI**](ARCHITECTURE/AGENT_COLLEAGUE_UI.md) - Documenting the "Colleague" mental model.
- [**🐶 BUDDY SYSTEM**](ARCHITECTURE/BUDDY_SYSTEM.md) - Hidden gacha-style companion logic.
- [**🧭 ULTRAPLAN**](ARCHITECTURE/ULTRAPLAN.md) - hierarchical planning and recursive execution.
- [**🛡️ PROTOCOL PROXY**](ARCHITECTURE/PROTOCOL_PROXY.md) - Secure command validation and sanitization logic.
- [**🚩 TENGU FLAGS**](ARCHITECTURE/TENGU_FLAGS.md) - Internal feature flagging and capability gating.
- [**✨ WHIMSY CORE**](ARCHITECTURE/WHIMSY_CORE.md) - Analysis of the "Fun" and "Personality" crates.
- [**🌍 EVOLUTION**](ARCHITECTURE/COMMUNITY_EVOLUTION.md) - Global developer community community-driven evolution research.

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
