# 🎨 INK TERMINAL UX: React for the CLI

Discover the "Delight Engineering" behind the high-fidelity terminal interface using **Ink (React for CLI)**.

## 📜 Overview
The Claude Code interface is a masterclass in modern CLI design. Instead of standard text output, the agent uses **Ink**, a React-based rendering engine that treats the terminal as a dynamic viewport. This allows for complex layouts, stateful components, and "Smooth Transitions" usually reserved for web applications.

## 🧬 The Ink Rendering Engine
From the analysis of `ink/render.tsx` and `termio/`, we have identified the "Virtual Terminal" logic:

-   **Reconciliation:** Like React on the web, Ink maintains a virtual tree of the CLI output and only "Re-draws" the parts that change.
-   **Hooked State:** The agent uses standard React hooks (`useState`, `useEffect`) to manage real-time updates for tool progress, spinners, and typing animations.
-   **Flexbox Layout:** Ink provides a Flexbox-like layout system (`<Box>`, `<Text>`) to handle responsive resizing within different terminal widths.

## 🧱 High-Fidelity Components (UI Breakdown)
The `src/components/` directory reveals the "Lego blocks" of the agent's identity:

### 1. `StructuredDiff`
A side-by-side file comparison unit that renders `git diff` outputs with syntax highlighting and inline "Change Indicators." This is the core of the agent's "Trust" system.

### 2. `Spinner` (Multi-Stage)
The agentic loading state is not just a circle. It is a multi-stage component that tracks:
- **Thinking:** The LLM's internal deliberation.
- **Executing:** Active tool-use.
- **Finalizing:** Translation and summary.

### 3. `PromptInput`
A rich text editor embedded in the CLI that supports multi-line input, history recall, and command auto-completion—all rendered via Ink.

## 🧪 The "Colleague" UI Principles
In `src/components/agents/`, we found the logic for "Agent Personas." When a sub-agent is spawned, the UI changes its **Design System**:

-   **Color Mappings:** Different agents (e.g., Buddy vs. Researcher) have distinct color palettes (Amethyst, Cinnabar, Emerald).
-   **LogoV2:** The "Face" of the agent is a dynamic Ink component that reacts to the agent's status (Active, Idle, Thinking).

---
*Synthesized by ORACLE and ATLAS for the Claude Source Hub.*
