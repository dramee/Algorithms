import shlex
import subprocess
from pathlib import Path
import os

command = shlex.split(input().replace("\\", "/"))
print(command)
pth = Path(input())

start = "726cf794aba820f9a1941acde5142f6f8f59c70c"
end = "97149701edbc224d54def2f1fcbd377f0d693da3"


def git_bisect(cmd, start_hash, end_hash, path):
    os.chdir(path)
    info = subprocess.getstatusoutput("git log")
    assert info[0] == 0
    info = info[1].split()

    commits_hashes = []

    for i in range(1, len(info) - 1):
        if info[i - 1] == "commit" and info[i + 1] == "Author:":
            commits_hashes.append(info[i])
    commits_hashes.reverse()

    left = commits_hashes.index(start_hash)
    right = commits_hashes.index(end_hash)
    os.chdir("..")

    while left != right:
        ind_curr_commit = (left + right) // 2
        subprocess.run(f"git checkout {commits_hashes[ind_curr_commit]}", text=True)
        if subprocess.run(cmd).returncode != 0:
            right = ind_curr_commit - 1
        else:
            left = ind_curr_commit + 1

    subprocess.run(f"git checkout {commits_hashes[left]}")
    if subprocess.run(cmd).returncode != 0:
        return -1
    return commits_hashes[left]


print(git_bisect(command, start, end, pth))
