# ⚠️ SECURITY ADVISORY: Supply-Chain Attack (March 31, 2026)

**During the window of 00:21–03:29 UTC on March 31, 2026**, users who installed or updated Claude Code via npm may have received a malicious version of the `axios` package.

---

## 🛑 Critical Warning
Affected installations included an unauthorized dependency on `plain-crypto-js`, which contained a **Remote Access Trojan (RAT)**. 

### If your lockfile contains:
- `axios` version **1.14.1**
- `axios` version **0.30.4**
- Any reference to `plain-crypto-js`

**Treat the host as fully compromised:**
1.  **Rotate all credentials** (API keys, SSH keys, passwords).
2.  **Audit access logs** for unusual activity.
3.  **Perform a clean system reinstall.**

---

## 🛡️ Anthropic's Response
Anthropic has since migrated the recommended installation method to a native installer to bypass the vulnerable npm distribution channel.

**Current Installation Command:**
```bash
curl -fsSL https://claude.ai/install.sh | bash
```

---

## 📜 Historical Context
The supply-chain attack occurred simultaneously with the Claude Code source leak event. While the leak itself was an accidental exposure of proprietary code, the malicious npm packages were an intentional attempt to capitalize on the community's sudden focus on the tool.

---

## 🔗 Related Resources
- [**🦅 CLAW CODE**](file:///Users/mkazi/Claude-Source-Hub/ARCHITECTURE/CLAW_CODE.md)
- [**📊 COMPARISON MATRIX**](file:///Users/mkazi/Claude-Source-Hub/ARCHITECTURE/COMPARISON.md)
- [**🧱 ARCHITECTURE MAP**](file:///Users/mkazi/Claude-Source-Hub/ARCHITECTURE.md)
