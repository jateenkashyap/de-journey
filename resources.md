🚀 Git & GitHub — Complete Notes
    Learned through hands-on practice | Data Engineering Journey | Month 1 Every concept explained with real examples and step-by-step commands

📌 What is Git & Why Does It Matter?
Git is a version control system — it takes snapshots of your work over time so you can:
    • Go back to any previous version if something breaks
    • Work on new features without touching working code
    • Collaborate with teammates without overwriting each other's work
Real world analogy:
    Imagine writing a 50-page report in Word with no Ctrl+Z and no version history. One wrong delete and it's gone forever. Git is the ultimate Ctrl+Z for your entire project — forever.

🗂️ The Three States of Git
Every file in Git lives in one of three states:
Working Directory → Staging Area → Repository
   (you edit)         (git add)     (git commit)

State	What it means	Real world analogy
Working Directory	Files you are actively editing	Writing on paper
Staging Area	Files selected for the next snapshot	Putting papers in an envelope
Repository	Permanent snapshots saved in Git	Sealing and posting the envelope

⚙️ Initial Setup (One Time Only)
# Set your identity — required before first commit
git config --global user.name "Your Name"
git config --global user.email "you@email.com"

# Set VS Code as your default Git editor
git config --global core.editor "code --wait"
# Verify everything is set
git config --list

📋 SECTION 1 — The Core Daily Workflow
This is the loop you will repeat every single day.
Step 1 — Check what's happening
git status          # shows modified, staged, untracked files
git log --oneline   # shows commit history (short version)
git diff            # shows exactly what changed line by line
Example output of git status:
On branch master
Changes not staged for commit:
  modified:   hello.py        ← file changed but not staged (red)

Untracked files:
  README.md                   ← new file Git has never seen (red)

Example output of git log --oneline:
b5a7368 add week 1 complete message   ← most recent commit
f4451cc add README file
cd2714e update hello.py with DE message
55fcbd2 Initial commit: add hello.py  ← first ever commit

Step 2 — The Save Loop
git add filename.py     # stage a specific file
git add .               # stage ALL changed files
git commit -m "message" # save a snapshot with a description
Real example — full workflow:
# You edited hello.py and created README.md
git status                          # see what changed
git add hello.py                    # stage just hello.py
git commit -m "update greeting"     # save snapshot
git add README.md                   # stage README
git commit -m "add README file"     # save another snapshot
Why two separate commits?
    Each commit should do ONE thing. Small, focused commits are easier to understand, review, and undo if something goes wrong.
Step 3 — View history visually
git log --oneline --all --graph
Example output:
* 6c4bc1f (HEAD -> master) latest commit
* 55698fc previous commit
*   3e3ef3c merge commit
|\
| * 38f117d branch commit
* | 354b9c1 another branch commit
|/
* f19af71 older commit
    This is your best friend in real teams — run it constantly to see where everything is.

📝 SECTION 2 — Writing Good Commit Messages
Bad commit messages make history unreadable. Good ones tell a story.
❌ Bad	✅ Good
"fix"	"fix null pointer error in read_data function"
"changes"	"add count_rows function to pipeline"
"asdf"	"update README with setup instructions"
"stuff"	"resolve merge conflict in hello.py"
Format to follow:
<what you did> <where you did it>
"add read_data function to pipeline.py"
"fix login bug in auth module"
"update README with venv setup steps"

↩️ SECTION 3 — Undoing Things
Mistakes are normal. Git makes them recoverable.
Scenario 1 — You edited a file but don't want the changes
# You accidentally deleted a function in pipeline.py
git restore pipeline.py    # restores file to last committed version
    ⚠️ This permanently discards your edits — use carefully.
Scenario 2 — You staged a file but want to unstage it
# You ran git add by mistake
git restore --staged pipeline.py   # removes from staging, keeps your changes
# File goes back to "modified but not staged"
Scenario 3 — You committed with the wrong message
# You just committed with message "asdf" by mistake
git commit --amend -m "add read_data function to pipeline"
# Replaces the last commit message
    ⚠️ Only use this on commits NOT yet pushed to GitHub.
Scenario 4 — You want to undo entire commits
git log --oneline
# f19af71 bad commit 2
# e0b67ce bad commit 1
# b5a7368 last good commit   ← you want to go back here

git reset --soft b5a7368    # removes commits, keeps changes STAGED
git reset --hard b5a7368    # removes commits AND deletes all changes
When to use which:
Command	Use when
git reset --soft	"I committed too early, need to add more before committing"
git reset --hard	"Those commits were completely wrong, delete everything"
What happens to deleted commits?
    They don't immediately disappear — Git keeps them internally as "dangling commits" for 30 days. You can recover them using git reflog within that window. After 30 days, Git's garbage collector permanently deletes them.
    ⚠️ Never use git reset on commits already pushed to GitHub.
The difference between restore and reset
    git restore	git reset
What it undoes	File changes	Commits
Touches history?	❌ No	✅ Yes
Danger level	🟢 Safe	🔴 Dangerous
Use when	Editing mistake	Wrong commits
Simple rule:
    Made a typing/editing mistake → git restore Made a wrong commit → git reset

👀 SECTION 4 — Seeing What Changed
git diff            # changes not yet staged
git diff --staged   # changes that are staged
Example output:
- print("Hello, Data Engineering!")    ← removed line (red)
+ print("Hello, Data Engineering!")    ← same line with newline added
+ print("Week 1 complete!")            ← new line added (green)

    - = removed, + = added. Always review diff before committing.

💾 SECTION 5 — Stashing
Real world situation: You're editing pipeline.py on master — half done, not ready to commit. Your boss messages: "Fix the README typo RIGHT NOW!" You can't commit half-done code. You can't delete your work. Solution → stash it.
# Step 1 — hide your half-done work
git stash

# Step 2 — your working directory is now clean
# Fix the urgent thing and commit it
git add README.md
git commit -m "fix README typo urgent"

# Step 3 — bring your half-done work back
git stash pop
# Your pipeline.py edits are back exactly as you left them!

When NOT to use stash:
    If you're already on a feature branch, just switch to master — your branch work is already isolated. Stash is mainly for when you forgot to create a branch and started working directly on master.
    Command	Brings work back	Keeps in stash list
    git stash pop	✅	❌
    git stash apply	✅	✅
git stash list      # see all stashed work

🌿 SECTION 6 — Branching
A branch is a parallel universe copy of your project. Changes on a branch don't affect master until you merge.
Real world situation: You need to build a new data pipeline feature. Instead of editing master directly (risky!), you create a branch, build the feature safely, then merge when done.
# Create and switch to a new branch
git branch feature-data-pipeline
git switch feature-data-pipeline
# Verify you're on the right branch (* = current)
git branch
# * feature-data-pipeline
#   master
# Do your work — add, commit as normal
git add pipeline.py
git commit -m "add read_data function"

# Switch back to master (your feature branch work stays on its branch)
git switch master
# master doesn't have your feature yet — safe and clean!

Key commands:
git branch                    # list all branches
git branch feature-name       # create a new branch
git switch feature-name       # switch to that branch
git branch -d feature-name    # delete branch after merging
git branch -D feature-name    # force delete (even if not merged)

🔀 SECTION 7 — Merging
# Always merge INTO master
git switch master
git merge feature-name        # brings feature branch changes into master
The professional workflow:
get task
  → git branch feature-task-name
  → git switch feature-task-name
  → make small commits
  → git switch master
  → git merge feature-task-name
  → git branch -d feature-task-name


⚡ SECTION 8 — Merge Conflicts
When does it happen? Two branches edit the same line of the same file. Git doesn't know which version to keep — so it asks YOU.
Real world simulation:
# master version of hello.py line 1:
print("Hello, Data Engineering - Master version!")
# feature branch version of hello.py line 1:
print("Hello, Data Engineering - Branch version!")
# When you merge → CONFLICT!

Git marks the conflict in the file:
<<<<<<< HEAD
print("Hello, Data Engineering - Master version!")    ← your branch (master)
=======
print("Hello, Data Engineering - Branch version!")    ← incoming branch
>>>>>>> feature-branch

How to resolve — step by step:
# Step 1 — open the file in VS Code
# Step 2 — delete ALL conflict markers (<<<, ===, >>>)
# Step 3 — keep what you want:
print("Hello, Data Engineering - Final version!")

# Step 4 — save the file
# Step 5 — stage and commit
git add hello.py
git commit -m "resolve merge conflict in hello.py"

git merge --abort    # emergency exit — cancels merge, goes back to before


🔄 SECTION 9 — Rebase vs Merge
The Problem
You branch off master on Monday. By Wednesday, teammates added 5 commits to master. Your branch is now behind master — it's missing critical updates.
master:  A → B → C → D → E   (D and E added by teammates)
                 \
feature:          X → Y       (your work, branched from C)

Why this matters:
    If teammate fixed a critical bug in D — your branch doesn't have that fix. When you eventually merge, things could break.

Option 1 — git merge (brings master INTO your feature branch)
git switch feature-branch
git merge master
What happens:
master:  A → B → C → D → E
                                   \         \
feature:                      X → Y → → M   (M = merge commit created automatically)

History looks like:
M   Merge branch 'master' into feature    ← extra merge commit
Y   your second commit
X   your first commit
E   teammate commit
D   teammate commit

    History gets messy with many branches — lots of merge commits everywhere.

Option 2 — git rebase (cleaner, professional)
git switch feature-branch
git rebase master
What happens: Git picks up YOUR commits (X, Y) and replays them on TOP of the latest master (E):
BEFORE rebase:
master:  A → B → C → D → E
                                 \
feature:                   X → Y

AFTER rebase:
master:  A → B → C → D → E
                                                  \
feature:                                    X' → Y'   (your commits replayed on top of E)

History looks like:
Y'  your second commit
X'  your first commit
E   teammate commit        ← clean, linear, no merge commit!
D   teammate commit
C   original commit


After rebasing — merge into master
# Rebase just repositions your branch — master still needs to move forward
git switch master
git merge feature-branch    # fast-forward merge — clean, no conflicts
git branch -d feature-branch

Why is it called fast-forward?
    After rebase, your commits are directly on top of master. Master just moves its pointer forward — no merge commit needed.

When to use which
Situation	Use
Merging finished feature INTO master	git merge
Updating your feature branch WITH latest master	git rebase
Working in a team, want clean history	git rebase
Working alone on simple projects	Either is fine

Checking if master has moved ahead of your branch
git log --oneline --all --graph         # visual tree of all branches
git log master..feature-branch          # commits in master your branch doesn't have
    ⚠️ Golden rule: Never rebase a branch teammates are also working on. It rewrites history and breaks their work.

🌐 SECTION 10 — GitHub Setup
GitHub is the cloud layer for your local Git repos.
    • Local Git = save points on your laptop
    • GitHub = save points on the internet (shareable, collaborative, backed up)
Setting up HTTPS connection (Windows recommended)
Step 1 — Create a Personal Access Token (PAT) on GitHub:
    1. GitHub → Profile picture → Settings
    2. Left sidebar → Developer Settings → Personal Access Tokens → Tokens (classic)
    3. Generate new token (classic)
    4. Note: "de-journey access" | Expiration: 90 days | Check ✅ repo
    5. Click Generate token → COPY IMMEDIATELY (shown only once!)
    PAT = same concept as an API token. It's a secret string that proves your identity. You pass it instead of a password when pushing code.
Step 2 — Create a repo on GitHub:
    1. github.com → green "New" button
    2. Name: de-journey | Public | Don't add README (you have one locally)
    3. Create repository
    4. Copy the HTTPS URL: https://github.com/yourusername/de-journey.git
Step 3 — Connect local repo to GitHub:
# "origin" is just a nickname for your GitHub URL
git remote add origin https://github.com/yourusername/de-journey.git
# Verify connection
git remote -v
# origin  https://github.com/yourusername/de-journey.git (fetch)
# origin  https://github.com/yourusername/de-journey.git (push)
What is origin?
    Just a nickname for your GitHub URL. Convention — everyone uses origin. Like saving a contact name in your phone instead of typing the number every time.
Step 4 — Push your code for the first time:
git push -u origin master
# -u flag sets "origin master" as default for future pushes
# Enter GitHub username and PAT token when prompted

📤 SECTION 11 — Push & Pull
git push = local → GitHub   (you sending your work to the cloud)
git pull = GitHub → local   (you receiving teammates' work)

Daily push workflow
# Make changes, add, commit as normal
git add pipeline.py
git commit -m "add new transformation function"
# Push to GitHub
git push origin master
Pull teammates' changes
# Always pull before starting work — get the latest code first!
git pull origin master

After pulling — your log shows:
0cab09e (HEAD -> master, origin/master) teammate's commit   ← pulled from GitHub
5b66471 your last commit

    origin/master = GitHub's copy master = your local copy When they point to same commit = you are in sync ✅
Checking if you're behind GitHub
git log --oneline --all --graph
# If origin/master is ahead of master → you need to pull


🔀 SECTION 12 — Pull Requests (PRs)
The professional way to merge code in teams. Instead of merging directly — you open a PR so teammates can review your code first.
Real world situation: You built a new feature. Before it goes into master, your team lead wants to:
    • Review what changed
    • Leave comments or suggestions
    • Approve it
Step by step PR workflow:
# Step 1 — create and switch to feature branch
git branch feature-new-transform
git switch feature-new-transform

# Step 2 — do your work
git add pipeline.py
git commit -m "add new transformation function"

# Step 3 — push the BRANCH to GitHub (not master!)
git push origin feature-new-transform

On GitHub:
    1. You'll see a yellow banner: "feature-new-transform had recent pushes — Compare & pull request"
    2. Click "Compare & pull request"
    3. Fill in title and description
    4. Click "Create pull request"
    5. Teammates review → leave comments → approve
    6. Click "Merge pull request" → "Confirm merge"
    7. Click "Delete branch" on GitHub
Back in your terminal:
# Sync your local machine with the merged changes
git switch master
git pull origin master
# Clean up local branch
git branch -d feature-new-transform
What you see in git log after merging a PR:
16098d5 (HEAD -> master, origin/master) Merge pull request #1   ← GitHub merge commit
c684530 your feature commit
0cab09e previous commit

    GitHub automatically creates a merge commit when a PR is merged. This records that a PR was merged — normal and expected.

🔁 SECTION 13 — The Complete Professional Workflow
This is how real teams work every single day:
# 1. Start of day — get latest code
git pull origin master

# 2. Create a branch for your task
git branch feature-task-name
git switch feature-task-name
# 3. Work in small, meaningful commits
git add filename
git commit -m "descriptive message"
# repeat...
# 4. Keep your branch updated with master (if working for multiple days)
git rebase master
# 5. Push your branch to GitHub
git push origin feature-task-name
# 6. Open a Pull Request on GitHub
# → team reviews → approves → merges

# 7. Sync locally and clean up
git switch master
git pull origin master
git branch -d feature-task-name

📊 SECTION 14 — Quick Command Reference
Local Git
Command	What it does
git init	Initialize a new Git repo
git status	See what's changed
git add filename	Stage a specific file
git add .	Stage all changed files
git commit -m "msg"	Save a snapshot
git log --oneline	View commit history
git log --oneline --all --graph	Visual tree of all branches
git diff	See line-by-line changes
git restore filename	Undo changes in a file
git restore --staged filename	Unstage a file
git commit --amend -m "msg"	Fix last commit message
git reset --soft <hash>	Undo commit, keep changes staged
git reset --hard <hash>	Undo commit, delete changes
git stash	Hide work temporarily
git stash pop	Bring hidden work back
git stash list	See all stashed work
git reflog	See every action ever taken (recovery tool)
Branching & Merging
Command	What it does
git branch	List all branches
git branch name	Create a new branch
git switch name	Switch to a branch
git merge branch	Merge branch into current
git rebase master	Replay commits on top of master
git merge --abort	Cancel a merge in progress
git branch -d name	Delete a merged branch
git branch -D name	Force delete a branch
GitHub (Remote)
Command	What it does
git remote add origin <url>	Connect local repo to GitHub
git remote -v	Verify remote connection
git push origin master	Push local commits to GitHub
git push -u origin master	Push and set default remote
git push origin branch-name	Push a branch to GitHub
git pull origin master	Pull latest changes from GitHub

⚠️ SECTION 15 — The Golden Rules
    1. Never git reset on pushed commits — rewrites history, breaks teammates
    2. Never git rebase shared branches — same reason
    3. Never git commit --amend pushed commits — same reason
    4. Always create a branch for new work — never work directly on master
    5. Always git pull before starting work — get the latest code first
    6. Commit small and often — easier to track, review, and undo
    7. Write meaningful commit messages — your future self will thank you
    8. Always delete branches after merging — keep things clean

🔐 SECTION 16 — Multiple GitHub Accounts (Future Reference)
If you ever need to connect both personal and work GitHub from the same laptop:
Create a config file at ~/.ssh/config:
# Personal GitHub
Host github.com
  HostName github.com
  User git
  IdentityFile ~/.ssh/id_ed25519
# Work GitHub
Host github-work
  HostName github.com
  User git
  IdentityFile ~/.ssh/id_ed25519_work
Each repo points to the right account via the Host alias.
    Set this up when you need it — 15 minute setup.

🔥 The Habit That Makes This Stick
Commit something to GitHub every single day — even one line changed in your README. The GitHub contribution graph starts building your story.
After 14 days:
    • ✅ Two-week streak on GitHub
    • ✅ Working dev environment
    • ✅ Real Git fluency
    • ✅ Public repo that proves it
    That is more than most people have after months of watching tutorials.

Next up: Python fundamentals for Data Engineering — Month 1, Week 3 & 4

From <https://claude.ai/chat/8b8c1bb2-2d27-4859-ac53-ad9ee4b44f12> 
