# -*- coding: utf-8 -*-
from colorama import Fore, Back, Style, init
import os

init(autoreset=True)

# ─── STYLES ──────────────────────────────────────────────────────────────────
R   = Style.RESET_ALL
B   = Style.BRIGHT
DIM = Style.DIM
C   = Fore.CYAN
G   = Fore.GREEN
Y   = Fore.YELLOW
RE  = Fore.RED
M   = Fore.MAGENTA
W   = Fore.WHITE
BLU = Fore.BLUE

# ─── BANNER ──────────────────────────────────────────────────────────────────
BANNER = r"""
                    ___.-------.___
                _.-' ___.--;--.___ `-._
             .-' _.-'  /  .+.  \  `-._ `-.
           .' .-'      |-|-o-|-|      `-. `.
          (_ <O__      \  `+'  /      __O> _)
            `--._``-..__`._|_.'__..-''_.--'
                  ``--._________.--''
   ____  _____  ____    ____       _       _______
  |_   \|_   _||_   \  /   _|     / \     |_   __ \
    |   \ | |    |   \/   |      / _ \      | |__) |
    | |\ \| |    | |\  /| |     / ___ \     |  ___/
   _| |_\   |_  _| |_\/_| |_  _/ /   \ \_  _| |_
  |_____|\____||_____||_____||____| |____||_____|
"""

WELCOME = "                   NMAP FRAMEWORK\n\n       Please contribute to this project by forking"

BANNER_COLORS = [C, C, C, C, C, C, C, C, M, M, M, M, M, M]


def cls():
    os.system("cls" if os.name == "nt" else "clear")


def print_banner():
    cls()
    lines = BANNER.split("\n")
    for i, line in enumerate(lines):
        color = BANNER_COLORS[i] if i < len(BANNER_COLORS) else C
        print(f"{B}{color}{line}{R}")
    print(f"{B}{Y}{WELCOME}{R}")
    print(f"\n{DIM}{C}{'─'*55}{R}\n")
    input(f"  {G}Press Enter to start...{R}")


def prompt(label=""):
    return input(f"  {G}>{R} {label}").strip()


def header(title):
    cls()
    print(f"\n{B}{C}{'─'*55}{R}")
    print(f"  {B}{M}H4shmap{R}  {DIM}>{R}  {B}{W}{title}{R}")
    print(f"{B}{C}{'─'*55}{R}")


def section(label, width=50):
    pad = width - len(label) - 2
    print(f"\n  {DIM}{Y}── {label} {'─' * max(pad, 2)}{R}")


def tag(text, color=Y):
    return f"{B}{color}[{text}]{R}"


def ok(msg):
    print(f"\n  {G}✓ {msg}{R}")


def err(msg):
    print(f"\n  {RE}✗ {msg}{R}")


def warn(msg):
    print(f"\n  {Y}! {msg}{R}")


def pause(msg="Press Enter to continue..."):
    prompt(msg)