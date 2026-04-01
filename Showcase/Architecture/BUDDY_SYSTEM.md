# 🦀 BUDDY: The Secret Pet System

Discover the hidden gacha-style companion system embedded within the Claude Code leak.

## 📜 Overview
The **BUDDY** system (internally referred to as `Companion`) is a secret feature that adds a persistent AI pet to the CLI. These companions sit beside the user's input box, react to commands, and occasionally comment in a speech bubble.

> [!NOTE]
> The primary Claude model is **not** the companion. The companion is a separate, autonomous observer designed for personality and user delight.

## 🧬 Rarity & Species Table

Companions are "rolled" based on a hash of the user's ID (`userId + SALT`) using the `mulberry32` algorithm. This ensures that every user has a consistent, unique "soul" for their pet.

| Rarity | Species | Lore / Visuals |
| :--- | :--- | :--- |
| **Common** | Pebblecrab, Dustbunny, Mossfrog, Twigling, Dewdrop, Puddlefish | The base ecosystem of the CLI. |
| **Rare** | Moonmoth, Cloudkitten, Sunpup, Stargazer | Glowing or atmospheric variants. |
| **Epic** | Nebulynx, Voidvoid, Chronobear | Cosmic and temporal entities. |
| **Legendary** | Ghost | Rare, transparent entity with unique animations. |

## ⚙️ Logic Breakdown
From `buddy/companion.ts` and `buddy/prompt.ts`:

### 1. The Watcher Protocol
When the user addresses a companion directly, the primary Claude model is instructed to:
- Respond in **ONE line or less**.
- "Stay out of the way"—the companion's specialized bubble handles the response.
- Never explain that they aren't the companion; the user already knows.

### 2. Mechanics
- **Interaction:** Triggered via `<task-notification>` and `CompanionSprite.tsx`.
- **States:** Active, Muted, and "soul" persistence.
- **Gacha:** The soul is generated once and persists unless the user "rerolls" (requires specific internal flags).

---
*Synthesized by ORACLE for the Claude Source Hub.*
