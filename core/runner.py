# -*- coding: utf-8 -*-
import subprocess

from UI.ui import B, G, RE, DIM, R, header, prompt, err, pause
from core.state import flags


def send_command():
    header("Execute")

    if not flags:
        err("No flags set.")
        pause()
        return

    target = prompt("Target IP / hostname / range : ")
    if not target:
        err("No target provided.")
        pause()
        return

    full = ["nmap"] + flags + [target]
    print(f"\n  {B}{G}Running:{R} {' '.join(full)}\n")
    print(f"  {DIM}{'─'*50}{R}")

    try:
        proc = subprocess.Popen(
            full,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
        )
        for line in proc.stdout:
            print(f"  {line}", end="")
        proc.wait()
        print(f"\n  {DIM}{'─'*50}{R}")
        print(f"  {B}Exit code:{R} {proc.returncode}")
    except FileNotFoundError:
        err("nmap not found.  →  brew install nmap  /  apt install nmap")

    pause()
