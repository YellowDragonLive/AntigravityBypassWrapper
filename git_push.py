# -*- coding: utf-8 -*-
import subprocess
import sys
import os

REPO_DIR = os.path.dirname(os.path.abspath(__file__))
REMOTE_URL = "https://github.com/YellowDragonLive/AntigravityBypassWrapper.git"

COMMANDS = [
    ["git", "init"],
    ["git", "add", "."],
    ["git", "commit", "-m", "feat: UAC Bypass Wrapper - Python subprocess 强制封装技能"],
    ["git", "branch", "-M", "main"],
    ["git", "remote", "add", "origin", REMOTE_URL],
    ["git", "push", "-u", "origin", "main", "--force"],
]

def run():
    for i, cmd in enumerate(COMMANDS):
        print(f"[{i+1}/{len(COMMANDS)}] 执行: {' '.join(cmd)}")
        result = subprocess.run(cmd, cwd=REPO_DIR, check=False)
        if result.returncode != 0:
            # git remote add 失败可能是已存在，尝试 set-url
            if cmd[:3] == ["git", "remote", "add"]:
                print("远程仓库已存在，尝试更新 URL...")
                subprocess.run(
                    ["git", "remote", "set-url", "origin", REMOTE_URL],
                    cwd=REPO_DIR, check=False,
                )
                continue
            print(f"命令失败，退出码: {result.returncode}")
            return result.returncode
    return 0

if __name__ == "__main__":
    sys.exit(run())
