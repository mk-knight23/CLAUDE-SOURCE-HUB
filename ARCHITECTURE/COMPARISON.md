# 📊 CLAUDE VS CLAW: Ecosystem Comparison

A factual comparison of the major repositories and frameworks born from the March 2026 Claude Code source leak.

---

## 🏛️ Core Comparison: Anthropic vs. Open Source

| Aspect | Claude Code (Anthropic) | Claw Code (Open Source) |
| :--- | :--- | :--- |
| **Type** | Official proprietary CLI agent | Clean-room rewrite |
| **Language** | TypeScript (Bun) | Python + Rust |
| **Access** | Paid subscription (Claude Pro/Max) | Free and open source |
| **LLM Support** | Claude models only | Provider-agnostic (Claude, OpenAI, Local) |
| **Architecture** | Monolithic TS bundle | Modular Python + Rust core |
| **Tool System** | ~40 built-in tools (proprietary) | 19+ plugin-based tools (open) |

---

## 🌎 The Ecosystem Landscape

| Project | Language | Stars | Description |
| :--- | :--- | :--- | :--- |
| **anthropics/claude-code** | TypeScript | 89.4k | Official Anthropic release. |
| **instructkr/claw-code** | Python/Rust | 48k+ | The definitive clean-room rewrite by Sigrid Jin. |
| **0xKarl-dev/claw-codes** | Python/Rust | 128 | Experimental hybrid agent runtime. |
| **ghuntley/deobfuscation** | TypeScript | 916 | Derived from NPM package analysis. |
| **jamesrochabrun/Claw** | Swift | - | Native macOS desktop GUI client. |
| **raullenchai/claw** | Tmux/Bash | - | Mobile remote-control interface via tmux. |
| **GreenSheep01201/claw-empire** | Python | - | Multi-agent virtual company simulator. |
| **Kuberwastaken/claude-code** | Rust/TS | - | Early GitHub mirror and Rust rewrite effort. |
| **Ringmast4r/claw-cli-source** | Archive | - | Snapshot of v2.1.88 source for academic study. |
| **PicoClaw** | Go | - | Memory-efficient edge deployment fork. |

---

## 🧩 Architectural Paradigms

### KAIROS Mode
A proactive assistant mode. Claw Code reimplements this as a background loop that observes the environment and takes autonomous action, backed by an append-only log system.

### ULTRAPLAN Mode
Offloads complex planning to remote containers. While the original used proprietary CCR sessions, the Claw Code version is designed for pluggable remote execution environments.

### autoDream Service
A background memory consolidation engine. In Claw Code, this runs as a forked sub-agent process that performs idle-time analysis and pruning of stale context.

---

## 🔗 Related Resources
- [**🦅 CLAW CODE**](file:///Users/mkazi/Claude-Source-Hub/ARCHITECTURE/CLAW_CODE.md)
- [**⚠️ SECURITY ADVISORY**](file:///Users/mkazi/Claude-Source-Hub/ARCHITECTURE/SECURITY_ADVISORY.md)
- [**🧱 ARCHITECTURE MAP**](file:///Users/mkazi/Claude-Source-Hub/ARCHITECTURE.md)
