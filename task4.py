import shlex
import subprocess
from pathlib import Path
import os

# command = shlex.split(input().replace("\\", "/"))
# print(command)
pth = Path(input())

start = "726cf794aba820f9a1941acde5142f6f8f59c70c"
end = "97149701edbc224d54def2f1fcbd377f0d693da3"


def get_commits(path):
    os.chdir(path)
    info = subprocess.getstatusoutput("git log")
    assert info[0] == 0
    info = info[1].split()
    print(info)
    commits_hashes = []

    for i in range(1, len(info) - 1):
        if info[i - 1] == "commit" and info[i + 1] == "Author:":
            commits_hashes.append(info[i])
    commits_hashes.reverse()

    return commits_hashes


def git_bisect(cmd, start_hash, end_hash, path):
    os.chdir("..")
    commits_hashes = get_commits(path)
    left = start_hash
    right = end_hash
    while left != right:
        ind_curr_commit = (left + right) // 2
        subprocess.run(f"git checkout {commits_hashes[ind_curr_commit]}")
        if subprocess.run(cmd).returncode != 0:
            right = ind_curr_commit - 1
        else:
            left = ind_curr_commit + 1

    subprocess.run(f"git checkout {commits_hashes[left]}")
    if subprocess.run(cmd).returncode != 0:
        return -1
    return commits_hashes[left]


print(get_commits(pth))
