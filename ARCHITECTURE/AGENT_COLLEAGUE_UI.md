# 🎭 AGENT COLLEAGUE UI: The Persona Design System

Discover how Claude Code uses a sophisticated color-coded "Persona System" to distinguish between different sub-agents in the terminal.

## 📜 Overview
The Claude ecosystem is not just a single agent—it's a team. To manage the complexity of multi-agent collaboration, the UI uses a **Visual Persona System** anchored in the `src/components/agents/` logic. This ensures that users always know which "Specialist" is currently driving the session.

## 🧬 Tactical Personas (Color Mappings)
From the analysis of the `new-agent-creation` wizard and the `LogoV2` component, we have identified the "Golden Personas":

-   **🟣 Amethyst (The Researcher):** Focused on deep-context gathering and documentation synthesis.
-   **🔴 Cinnabar (The Debugger):** Focused on error-tracking, stack-trace analysis, and surgical fixes.
-   **🟢 Emerald (The Companion):** The "Buddy" system. Focused on whimsy, delightful interaction, and user-motivation.
-   **🔵 Sapphire (The Orchestrator):** The default persona for task planning and tool-calling.

## 🧱 The "LogoV2" Animation States
The agent's visual identity is a dynamic **Ink** component that changes its "State" based on the underlying logic:

1.  **Thinking (Pulse):** A soft, rhythmic glow indicating LLM inference.
2.  **Working (Busy):** A high-frequency rotation or "Flicker" indicating active tool-use.
3.  **Error (Crit):** A shift to high-contrast red/orange to draw immediate attention.
4.  **Idle (Static):** A minimal, solid mark signifying the agent is waiting for input.

## ⚙️ The "Wizard-Steps" Agent Creation
The `new-agent-creation/wizard-steps/` logic reveals how the agent "Spawns" its colleagues. The process involves:
1.  **Role Injection:** Defining the specific governing prompt for the persona.
2.  **Visual Binding:** Linking the persona to its assigned HEX color and icon.
3.  **Harness Binding:** Connecting the new sub-agent to the main **Bridge Service** for RPC communication.

---
*Synthesized by ORACLE and ATLAS for the Claude Source Hub.*
