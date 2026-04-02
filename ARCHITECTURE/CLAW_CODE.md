# 🦅 CLAW CODE: The Clean-Room Evolution

> **"No proprietary code. No model weights. Just architecture, reimagined."**

**Claw Code** is an open-source AI coding agent framework — a clean-room rewrite of the Claude Code agent harness architecture, built from scratch in Python and Rust. It represents the community's response to the March 2026 source leak, transforming a proprietary incident into an open-source movement.

---

## 📊 Project Statistics
- **48k+** GitHub Stars
- **56k+** Forks
- **335** Active Watchers
- **512k** Lines Analyzed (Original Leak)
- **72.9%** Rust / **27.1%** Python

---

## 🏛️ Architecture Overview
Claw Code reimplements the core architectural patterns observed in the Claude Code agent harness but focuses on a high-performance, memory-safe runtime.

### Key Components:
1.  **Tool System**: A plugin-based architecture with 19 built-in, permission-gated tools (Bash, File I/O, Web Fetch, etc.).
2.  **Query Engine**: Provider-agnostic intelligence managing LLM calls, streaming, and multi-step orchestration.
3.  **Multi-Agent Orchestration**: Support for "swarms" — spawning sub-agents to parallelize complex engineering tasks.
4.  **MCP Integration**: Full Model Context Protocol support with 6 transport types (Stdio, SSE, HTTP, WebSocket, SDK, ClaudeAiProxy).

---

## 🧬 Core Capabilities

### 🧠 Autonomous Agent Loop
A terminal-native agent that reads files, executes commands, runs tests, and handles Git operations autonomously until the task is complete.

### 💾 Session & Memory
Multi-layer memory system with session persistence, transcript compaction, and context discovery via the `CLAUDE.md` instruction file system.

### 🔒 Permission System
Three permission modes with a per-tool policy engine, deny lists, and interactive prompting to ensure safe execution.

---

## ⚡ Rust Runtime Core
The performance-critical paths are implemented in a 6-crate Rust workspace, providing:
- Zero-dependency JSON parsing.
- OAuth PKCE flows.
- Syntax-highlighted terminal rendering.
- High-concurrency tool execution.

---

## 📅 The History: How Claw Code Began
On **March 31, 2026**, the Claude Code source code was accidentally published to npm. Within hours, developer **Sigrid Jin (@sigridjineth)** began a clean-room rewrite.

The project became one of the fastest-growing in GitHub history, reaching 30,000 stars within hours of publication. It catalyzed an entire ecosystem of related projects aimed at democratizing agentic engineering.

---

## 🔗 Related Resources
- [**📊 COMPARISON MATRIX**](file:///Users/mkazi/Claude-Source-Hub/ARCHITECTURE/COMPARISON.md)
- [**⚠️ SECURITY ADVISORY**](file:///Users/mkazi/Claude-Source-Hub/ARCHITECTURE/SECURITY_ADVISORY.md)
- [**🧱 ARCHITECTURE MAP**](file:///Users/mkazi/Claude-Source-Hub/ARCHITECTURE.md)
