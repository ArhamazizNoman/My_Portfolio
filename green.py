import subprocess
import os
import random
from datetime import datetime, timedelta

# Fill contributions from here to today
START = datetime(2025, 5, 1)
END   = datetime(2026, 4, 27)

LOG = "activity.log"

def commit_on(date: datetime, msg: str):
    ds = date.strftime("%Y-%m-%dT%H:%M:%S")
    with open(LOG, "a") as f:
        f.write(f"{ds} — {msg}\n")
    subprocess.run(["git", "add", LOG], check=True)
    env = os.environ.copy()
    env["GIT_AUTHOR_DATE"]    = ds
    env["GIT_COMMITTER_DATE"] = ds
    subprocess.run(
        ["git", "commit", "-m", msg],
        env=env, check=True,
        capture_output=True
    )
    print(f"  committed {ds}")

messages = [
    "Update portfolio data",
    "Refine project descriptions",
    "Improve layout styles",
    "Add skill details",
    "Clean up code",
    "Update contact info",
    "Improve accessibility",
    "Tweak animations",
    "Update experience section",
    "Polish UI details",
    "Adjust responsive layout",
    "Update project links",
    "Fix typos",
    "Improve readability",
    "Optimize performance",
]

current = START
while current <= END:
    # ~65% chance of activity each day, skip weekends less often
    weekday = current.weekday()
    threshold = 0.45 if weekday >= 5 else 0.65

    if random.random() < threshold:
        n = random.randint(1, 4)
        for i in range(n):
            hour   = random.randint(9, 22)
            minute = random.randint(0, 59)
            dt = current.replace(hour=hour, minute=minute, second=random.randint(0, 59))
            commit_on(dt, random.choice(messages))

    current += timedelta(days=1)

print("\nDone. Now run:  git push")
