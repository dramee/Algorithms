import shlex
import subprocess
from pathlib import Path
import os

command = shlex.split(input().replace("\\", "/"))
# print(command)
pth = Path(input())

start = "726cf794aba820f9a1941acde5142f6f8f59c70c"
end = "e25138d871abf115e32aebca0ef164f52511f470"


def get_commits(path):
    os.chdir(path)
    info = subprocess.getstatusoutput("git log -a")
    assert info[0] == 0
    info = info[1].split()
    commits_hashes = []

    for i in range(1, len(info) - 1):
        if info[i - 1] == "commit" and info[i + 1] == "Author:":
            commits_hashes.append(info[i])
    commits_hashes.reverse()

    return commits_hashes


def git_bisect(cmd, start_hash, end_hash, path):
    # base_commit
    commits_hashes = get_commits(path)
    left = commits_hashes.index(start_hash)
    right = commits_hashes.index(end_hash)
    os.chdir("..")
    while left <= right:
        ind_curr_commit = (left + right) // 2
        subprocess.run(f"git checkout {commits_hashes[ind_curr_commit]}")
        curr_process = subprocess.run(cmd)
        prev_process = None
        if ind_curr_commit > 0:
            subprocess.run(f"git checkout {commits_hashes[ind_curr_commit - 1]}")
            prev_process = subprocess.run(cmd)
        if prev_process is not None and prev_process.returncode == 0 and curr_process.returncode != 0:
            subprocess.run(f"git checkout {commits_hashes[-1]}")
            return commits_hashes[ind_curr_commit]
        elif curr_process != 0:
            right = ind_curr_commit - 1
        else:
            left = ind_curr_commit + 1
    subprocess.run(f"git checkout {commits_hashes[-1]}")
    return -1


# print(get_commits(pth))

print(git_bisect(command, start, end, pth))

# print(subprocess.getstatusoutput("git status")[1])

