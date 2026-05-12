# -*- coding: utf-8 -*-
import json
import os

from UI.ui import (
    B, C, DIM, G, Y, RE, M, W, BLU, R,
    prompt, header, section, tag, ok, err, warn, pause,
)
from core.state import flags

SHORTCUTS_FILE = "nmap_shortcuts.json"
MAX_SHORTCUTS  = 9

# ─── KEYWORD MAP for auto-naming ─────────────────────────────────────────────
_KEYWORDS = {
    "-sS": "SYN Stealth Scan",
    "-sT": "TCP Connect Scan",
    "-sU": "UDP Scan",
    "-sA": "ACK Scan",
    "-sV": "Version Detection",
    "-O":  "OS Detection",
    "-A":  "Aggressive Scan",
    "-PE": "ICMP Ping",
    "-Pn": "No Ping",
    "--script vuln":    "Vuln Script",
    "--script all":     "All Scripts",
    "--script exploit": "Exploit Script",
    "--script brute":   "Brute Force",
    "-p-": "Full Port Scan",
    "-F":  "Fast Scan",
    "-sC": "Default Scripts",
    "--traceroute": "Traceroute",
}


def auto_name(flag_list: list[str]) -> str:
    if not flag_list:
        return "Empty scan"
    for flag, name in _KEYWORDS.items():
        if flag in flag_list:
            return name
    return " + ".join(flag_list[:2])


# ─── PERSISTENCE ─────────────────────────────────────────────────────────────
def load() -> dict:
    if os.path.exists(SHORTCUTS_FILE):
        try:
            with open(SHORTCUTS_FILE, "r") as f:
                return json.load(f)
        except Exception:
            pass
    return {}


def save(shortcuts: dict):
    with open(SHORTCUTS_FILE, "w") as f:
        json.dump(shortcuts, f, indent=2)


# ─── DISPLAY ─────────────────────────────────────────────────────────────────
def _print_shortcuts(shortcuts: dict):
    if shortcuts:
        section("Saved shortcuts")
        for slot, data in sorted(shortcuts.items(), key=lambda x: int(x[0])):
            name = data.get("name", "?")
            cmd  = "nmap " + " ".join(data.get("flags", []))
            slot_tag = f"{B}{Y}[{slot}]{R}"
            print(f"  {slot_tag}  {G}{name:<22}{R}  {DIM}→ {cmd}{R}")
    else:
        print(f"\n  {DIM}No shortcuts saved yet.{R}")


# ─── MENU ────────────────────────────────────────────────────────────────────
def menu_shortcuts():
    shortcuts = load()

    while True:
        header("Shortcuts")
        _print_shortcuts(shortcuts)

        section("Actions")
        print(f"  {tag('a')}  {W}Add current flags as shortcut{R}  {DIM}(max {MAX_SHORTCUTS}){R}")
        print(f"  {tag('l')}  {W}Load a shortcut into flags{R}")
        print(f"  {tag('d')}  {W}Delete a shortcut{R}")
        print(f"  {tag('r')}  {W}Rename a shortcut{R}")
        print(f"\n  {tag('0', BLU)}  {DIM}Back{R}")

        raw = prompt()

        # ── ADD ──────────────────────────────────────────────────────────
        if raw.lower() == "a":
            if not flags:
                err("No flags set — nothing to save.")
                pause()
                continue

            if len(shortcuts) >= MAX_SHORTCUTS:
                err(f"Max {MAX_SHORTCUTS} shortcuts reached. Delete one first.")
                pause()
                continue

            used      = {int(k) for k in shortcuts}
            available = [i for i in range(1, MAX_SHORTCUTS + 1) if i not in used]
            print(f"\n  {DIM}Available slots: {', '.join(str(s) for s in available)}{R}")

            slot_raw = prompt("Choose a slot number : ")
            try:
                slot = int(slot_raw)
                if slot not in available:
                    err(f"Slot {slot} not available.")
                    pause()
                    continue
            except ValueError:
                err("Invalid slot.")
                pause()
                continue

            auto = auto_name(flags)
            name = prompt(f"Shortcut name [{auto}] : ")
            if not name:
                name = auto

            shortcuts[str(slot)] = {"name": name, "flags": list(flags)}
            save(shortcuts)
            ok(f"Shortcut [{slot}] '{name}' saved!")
            pause()

        # ── LOAD ─────────────────────────────────────────────────────────
        elif raw.lower() == "l":
            if not shortcuts:
                err("No shortcuts to load.")
                pause()
                continue
            slot_raw = prompt("Slot to load : ")
            if slot_raw in shortcuts:
                loaded = shortcuts[slot_raw]["flags"]
                flags.clear()
                flags.extend(loaded)
                ok(f"Loaded: nmap {' '.join(flags)}")
            else:
                err("Slot not found.")
            pause()

        # ── DELETE ───────────────────────────────────────────────────────
        elif raw.lower() == "d":
            if not shortcuts:
                err("No shortcuts to delete.")
                pause()
                continue
            slot_raw = prompt("Slot to delete : ")
            if slot_raw in shortcuts:
                name = shortcuts[slot_raw]["name"]
                del shortcuts[slot_raw]
                save(shortcuts)
                print(f"\n  {Y}Deleted [{slot_raw}] '{name}'.{R}")
            else:
                err("Slot not found.")
            pause()

        # ── RENAME ───────────────────────────────────────────────────────
        elif raw.lower() == "r":
            if not shortcuts:
                err("No shortcuts to rename.")
                pause()
                continue
            slot_raw = prompt("Slot to rename : ")
            if slot_raw in shortcuts:
                old = shortcuts[slot_raw]["name"]
                new = prompt(f"New name [{old}] : ")
                if not new:
                    new = old
                shortcuts[slot_raw]["name"] = new
                save(shortcuts)
                ok(f"Renamed to '{new}'.")
            else:
                err("Slot not found.")
            pause()

        elif raw == "0":
            return