#!/usr/bin/env python3
"""
Self-Service Onboarding Script for Claude Code.
Configures:
1. ~/.claude/skills          -> Creates a Directory Junction (Windows) or symlink (POSIX) pointing to AI-OS/Skills.
2. ~/.claude/CLAUDE.md       -> Writes the Global Planning Rule + Strict Home.md Step-0 Funnel (zero duplicated vault rules).
3. <Vault-Root>/CLAUDE.md    -> Uses Claude Code's native @Home.md import directive (0-call auto-expansion, atomic-save safe, zero bypass routes).
"""

from __future__ import annotations

import os
import subprocess
from pathlib import Path

VAULT_ROOT = Path(__file__).resolve().parents[3]
SKILLS_DIR = VAULT_ROOT / "AI-OS" / "Skills"
VAULT_POSIX = VAULT_ROOT.as_posix()

CLAUDE_CONFIG_DIR = Path.home() / ".claude"
CLAUDE_SKILLS_LINK = CLAUDE_CONFIG_DIR / "skills"
GLOBAL_CLAUDE_MD = CLAUDE_CONFIG_DIR / "CLAUDE.md"
VAULT_CLAUDE_POINTER = VAULT_ROOT / "CLAUDE.md"

GLOBAL_CLAUDE_CONTENT = f"@{VAULT_POSIX}/Home.md\n"

WORKSPACE_CLAUDE_CONTENT = "@Home.md\n"


def setup_claude_skills_link() -> None:
    CLAUDE_CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    if os.path.lexists(str(CLAUDE_SKILLS_LINK)):
        try:
            if os.name == "nt":
                subprocess.run(["cmd", "/c", "rmdir", str(CLAUDE_SKILLS_LINK)], check=True, capture_output=True)
            else:
                if CLAUDE_SKILLS_LINK.is_symlink() or not CLAUDE_SKILLS_LINK.is_dir():
                    CLAUDE_SKILLS_LINK.unlink()
                else:
                    os.rmdir(CLAUDE_SKILLS_LINK)
        except Exception as e:
            print(f"[WARN] Could not remove existing {CLAUDE_SKILLS_LINK}: {e}")

    if os.name == "nt":
        subprocess.run(
            ["cmd", "/c", "mklink", "/J", str(CLAUDE_SKILLS_LINK), str(SKILLS_DIR)],
            check=True,
            capture_output=True,
            text=True,
        )
        print(f"[OK] Created Windows Directory Junction: {CLAUDE_SKILLS_LINK} -> {SKILLS_DIR}")
    else:
        os.symlink(SKILLS_DIR, CLAUDE_SKILLS_LINK, target_is_directory=True)
        print(f"[OK] Created symlink: {CLAUDE_SKILLS_LINK} -> {SKILLS_DIR}")


def setup_global_claude_md() -> None:
    CLAUDE_CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    GLOBAL_CLAUDE_MD.write_text(GLOBAL_CLAUDE_CONTENT, encoding="utf-8")
    print(f"[OK] Updated global Claude Code rules in: {GLOBAL_CLAUDE_MD}")


def setup_vault_root_include() -> None:
    if VAULT_CLAUDE_POINTER.exists() or VAULT_CLAUDE_POINTER.is_symlink():
        VAULT_CLAUDE_POINTER.unlink()
    VAULT_CLAUDE_POINTER.write_text(WORKSPACE_CLAUDE_CONTENT, encoding="utf-8")
    print(f"[OK] Wrote native @Home.md root include: {VAULT_CLAUDE_POINTER}")


def main() -> None:
    print(f"Setting up Second Brain harness for Claude Code (Vault: {VAULT_ROOT})...")
    setup_claude_skills_link()
    setup_global_claude_md()
    setup_vault_root_include()
    print("\nClaude Code setup complete!")


if __name__ == "__main__":
    main()
