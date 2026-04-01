# 🛡️ ORACLE Intelligence Brief: The Claude Code Leak Ecosystem

**BLUF (Bottom Line Up Front):** 
The recent leak of Anthropic's `Claude Code v2.1.84` via NPM sourcemaps has spawned a massive open-source ecosystem overnight. The community response falls into three distinct phases: **Archival** (hoarding the leaked TypeScript), **Analysis** (reverse-engineering hidden flags and system prompts), and **Evolution** (rebuilding the agentic framework natively in Rust under the "Claw" moniker).

Here is the comprehensive synthesis and sorted analysis of your targets.

---

## 📊 1. GitHub Repositories (Sorted by Stars ⬇️, then Name ⬇️)

### **1. instructkr/claw-code**
* **Stars:** 64,262 🌟
* **Content/Summary:** The undisputed heavyweight of this event. Originally surging in popularity just for hosting the leaked code (breaking GitHub records), it has pivoted intensely. It is no longer just an archive; it is an active initiative to rebuild Claude Code natively in Rust. Their mission is to build "better harness tooling" and create actionable outcomes rather than just hoarding the TypeScript leak.

### **2. asgeirtj/system_prompts_leaks**
* **Stars:** 35,350 🌟
* **Content/Summary:** A goldmine of AI intelligence. *[NEXUS Analysis]*: This repository systematically archives the core system prompts that drive major AI models and agents. It contains the raw instructions that govern Claude (Opus, Sonnet, Claude Code), OpenAI's models (GPT-4.5/4o, Codex), Google Gemini, and Grok. It reveals the exact "context windows" and behavioral guardrails these companies use to tether their agents.

### **3. NanmiCoder/claude-code-haha**
* **Stars:** 345 🌟
* **Content/Summary:** A practical implementation repository. While others just dumped the files, this repository focuses on providing a **locally runnable version** of the leaked Claude Code source, complete with the necessary scaffolding to actually execute the terminal agent on a developer's local machine bypassing strict cloud gates.

### **4. leaked-claude-code/leaked-claude-code**
* **Stars:** 172 🌟
* **Content/Summary:** A literal mirror archive. Its purpose is purely redundancy, providing the raw, unadulterated source code of the agent.

### **5. GitHpriyanshu23/Claude-code-leaks**
* **Stars:** 106 🌟
* **Content/Summary:** Another archival repository, but specifically focused on caching the tool's natural language command handlers and its Git workflow integrators. 

### **6. soufianebouaddis/claude-code**
* **Stars:** 66 🌟
* **Content/Summary:** A highly structural breakdown. *[SENTINEL Analysis]*: This developer utilized the leaked NPM sourcemaps to reconstruct the exact architecture of Anthropic's codebase—extracting over **512,000 lines of TypeScript across 1,900 files**. It demonstrates exactly how the modular capabilities of the terminal agent are separated.

### **7. claw-cli/claw-code-rust**
* **Stars:** 33 🌟
* **Content/Summary:** The specialized engineering offshoot of `instructkr/claw-code`. This is a dedicated organizational repository aimed specifically at the architectural translation of Claude Code's Node.js/TypeScript logic into high-performance Rust.

---

## 🕵️ 2. Deep-Dive Analysis of `ccu.galdoron.com`

**Subject:** *Claude Code Unleashed | Hidden Features of v2.1.84*
This site serves as the ultimate reverse-engineering wiki for the macOS binary and the NPM package, exposing Anthropic's internal architecture. 

**Key Discoveries Inside the Agent:**
* **Hidden Subsystems:** Uncovered dormant AI features such as **Auto-Dream** (background memory consolidation), **Ultraplan** (remote 10-30 min multi-agent planning cycles via Opus), **Kairos** (automated cron scheduling), and **Willow Mode** (advanced idle/AFK detection).
* **Beta SDK Headers:** Found 30 hidden API flags sent to Anthropic's servers (e.g., `interleaved-thinking-2025-05-14`, `prompt-caching-scope-2026-01-05`, `task-budgets-2026-03-13`), revealing their internal roadmap into late 2025 and 2026.
* **Internal "Tengu" Feature Flags:** Discovered Anthropic's internal Statsig gating system (named `tengu_*`), which controls kill-switches like `tengu_iron_gate_closed` (fail-closed safety guardrails).

---

## 🧠 Strategic Synthesis & Next Actions

**The ORACLE Insight:**
Data without insight is noise. What we are observing is the rapid convergence of **leak-driven development**. The market immediately recognized that Claude Code's architecture (TypeScript CLI orchestrating cloud LLMs with MCP servers) is highly effective, but slow. The community (via `instructkr` and `claw-cli`) is bypassing Anthropic's proprietary walls by rewriting the methodology into a native, high-performance **Rust** ecosystem (Claw).

If we are to integrate any of these findings into our own Agent Army workflows, the recommended strategies are:
1. **[NEXUS Integration]** Audit the `asgeirtj/system_prompts_leaks` repo to refine our own agents' operational prompts based on Anthropic's "Auto-Mode Classifier" patterns. 
2. **[ATLAS Migration]** Monitor `claw-cli/claw-code-rust` for architectural lessons on how to port slow TypeScript CLI agent toolings into hyper-efficient Rust binaries.
