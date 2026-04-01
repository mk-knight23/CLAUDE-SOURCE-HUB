# ⚡ PROTOCOL PROXY: The "Model Hijacker"

Discover the community-developed orchestration layer used to bypass API restrictions and enable multiple LLM backends.

## 📜 Overview
The **Upstream Proxy** (found in `claw-code` and `NanoClaw`) is a sophisticated interception layer in Python/Rust that acts as a "Gateway" between the Claude Code client and its AI backend. This proxy was the cornerstone of the community's effort to make the agent a truly agnostic platform.

## 🧬 Interception Logic
The **Model Hijacking** process involves three key steps:

### 1. SDK Hooking
The community intercepted calls to the Anthropic SDK by setting custom `API_BASE_URL` environment variables. This redirected all traffic from `anthropic.com` to the local proxy.

### 2. Request Mapping
The proxy translates the structured Claude Code request (with its complex Tool definitions) into a generic format compatible with standard agentic endpoints and alternative model backends.

### 3. Response Translation
The local proxy translates the model's response (including `tool_use`) back into the specific format expected by the Claude Code runtime, maintaining session stability and tool-calling integrity.

## 🧱 The Subsystem Architecture
From the `upstreamproxy/` and `relay.ts` logic:

- **Relay System:** Manages the multiplexing of multiple streams into a single CLI response.
- **Protocol Bridge:** Translates between MCP (Model Context Protocol) and standard agentic tool-calling endpoints.

## ⚙️ Why it Matters
The Proxy architecture proved that any LLM with sufficient tool-calling capability (e.g., DeepSeek V3, GPT-4o) could drive the Claude Code runtime. It turned a proprietary tool into a **Universal Agent Shell**.

---
*Synthesized by ORACLE for the Claude Source Hub based on the Project Claw logic.*
