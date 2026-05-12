#!/usr/bin/env python3
# -*- coding: utf-8 -*-

try:
    import sys
    import time

    from UI.ui   import (
        cls, print_banner,
        B, C, DIM, G, Y, RE, M, W, BLU, R,
        prompt, section, tag, ok, warn, pause,
    )
    from core.state     import flags, reset_flags, actual_cmd
    from utils.shortcuts import load as load_shortcuts, menu_shortcuts
    from core.runner    import send_command
    from UI.menus     import (
        menu_ping, menu_scan, menu_ports,
        menu_detection, ask_timing, menu_output,
        ask_evasion, menu_misc,
    )
except ImportError as e:
    print(f"Import error: {e}")
    print("Make sure you ran:  pip install -r requirements.txt")
    sys.exit(1)


SCAN_MENU = [
    ("Ping / Host Discovery",  menu_ping),
    ("Scan Techniques",        menu_scan),
    ("Port Specification",     menu_ports),
    ("Detection & Scripts",    menu_detection),
    ("Timing",                 ask_timing),
    ("Output",                 menu_output),
    ("Evasion / Bypass",       ask_evasion),
    ("Misc / Advanced",        menu_misc),
]

# Icons per option (purely decorative)
ICONS = ["◈", "◉", "◎", "◆", "◷", "◫", "⊘", "⊞"]


def print_main_menu():
    shortcuts = load_shortcuts()

    cls()

    # ── Top bar ──────────────────────────────────────────────────────────────
    print(f"\n{B}{C}{'═'*55}{R}")
    print(f"  {B}{M}H4shmap{R}  {DIM}·{R}  {B}{W}nmap framework{R}  {DIM}·{R}  {C}Main Menu{R}")
    print(f"{B}{C}{'═'*55}{R}")

    # ── Current command ───────────────────────────────────────────────────────
    print(f"\n  {DIM}Command :{R}  {actual_cmd()}")
    if flags:
        flag_str = "  ".join(f"{G}{f}{R}" for f in flags)
        print(f"  {DIM}Flags    : {flag_str}{R}")
    print()

    # ── Scan options ─────────────────────────────────────────────────────────
    print(f"  {B}{Y}┌─ Scan Options {'─'*37}┐{R}")
    for i, (label, _) in enumerate(SCAN_MENU):
        icon = ICONS[i] if i < len(ICONS) else "›"
        num  = tag(i + 1)
        print(f"  {B}{Y}│{R}  {num}  {C}{icon}{R}  {W}{label:<28}{R}  {B}{Y}│{R}")
    print(f"  {B}{Y}└{'─'*51}┘{R}")

    # ── Shortcuts ────────────────────────────────────────────────────────────
    print()
    print(f"  {B}{M}┌─ Shortcuts {'─'*40}┐{R}")
    if shortcuts:
        for slot, data in sorted(shortcuts.items(), key=lambda x: int(x[0])):
            name    = data.get("name", "?")
            cmd_str = "nmap " + " ".join(data.get("flags", []))
            s_tag   = f"{B}{M}s{slot}{R}"
            print(f"  {B}{M}│{R}  {tag(f's{slot}', M)}  {G}{name:<22}{R} {DIM}→ {cmd_str}{R}")
    else:
        print(f"  {B}{M}│{R}  {DIM}No shortcuts yet — manage them with [sc]{R}")
    print(f"  {B}{M}└{'─'*51}┘{R}")

    # ── Actions ──────────────────────────────────────────────────────────────
    print()
    print(f"  {DIM}{'─'*53}{R}")
    cols = [
        (tag("sc", C), "Manage shortcuts"),
        (tag("send", G), f"{G}Send command{R}"),
        (tag("r", RE), "Reset flags"),
        (tag("q", BLU), "Quit"),
    ]
    # Print in two columns
    for j in range(0, len(cols), 2):
        left_tag,  left_lbl  = cols[j]
        right_tag, right_lbl = cols[j+1] if j+1 < len(cols) else ("", "")
        left_part  = f"  {left_tag}  {W}{left_lbl:<22}{R}"
        right_part = f"  {right_tag}  {W}{right_lbl}{R}" if right_tag else ""
        print(left_part + right_part)
    print(f"  {DIM}{'─'*53}{R}\n")


def main():
    print_banner()

    while True:
        print_main_menu()
        raw = prompt()

        if raw.lower() in ("q", "quit", "exit"):
            print(f"\n  {DIM}Bye.{R}\n")
            sys.exit(0)

        elif raw.lower() == "send":
            send_command()

        elif raw.lower() == "r":
            reset_flags()
            warn("Flags cleared.")
            pause()

        elif raw.lower() == "sc":
            menu_shortcuts()

        # Load shortcut directly (s1 … s9)
        elif raw.lower().startswith("s") and raw[1:].isdigit():
            shortcuts = load_shortcuts()
            slot = raw[1:]
            if slot in shortcuts:
                loaded = shortcuts[slot]["flags"]
                flags.clear()
                flags.extend(loaded)
                name = shortcuts[slot]["name"]
                ok(f"Loaded [{slot}] '{name}': nmap {' '.join(flags)}")
                pause()
            else:
                print(f"  {RE}Shortcut [{slot}] not found.{R}")
                pause()

        else:
            try:
                idx = int(raw) - 1
                if 0 <= idx < len(SCAN_MENU):
                    _, fn = SCAN_MENU[idx]
                    fn()
            except ValueError:
                pass


if __name__ == "__main__":
    main()