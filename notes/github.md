## …or create a new repository on the command line
echo "# Python-Bootcamp" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/abdulfatinla/Python-Bootcamp.git
git push -u origin main

### …or push an existing repository from the command line
git remote add origin https://github.com/abdulfatinla/Python-Bootcamp.git
git branch -M main
git push -u origin main


## Location repo
https://github.com/abdulfatinla/Python-Bootcamp.git

# Create a new repository on the command line

get init
git add namafileygkitabuat.py (utk semua file, type git add. )
git commit -m "first commit"        #
git branch -M main
git remote add origin https://github
git push -u origin main

###############################################
# Updated files from visual studio code to github
Using Terminal Commands
If you have the terminal open in VS Code (`Ctrl+``), use these standard Git commands: 
git add .: This stages all modified files for the update.
git commit -m "your message": This records your changes locally with a descriptive note.
git push: This uploads your committed changes to the GitHub repository.

🧠 Quick Summary
git add → prepare changes
git commit → save changes locally
git push → upload to GitHub


🔁 Step-by-step: Update your changes to GitHub
✅ 1. Save your file
Make sure your changes are saved in VS Code:
Ctrl + S

✅ 2. Open Terminal in VS Code
Go to Terminal → New Terminal

✅ 3. Check changed files
git status
 This shows which files you modified.

✅ 4. Add (stage) your changes

To add one file:

git add filename.py

Or add all changes:

git add .


✅ 5. Commit your changes
git commit -m "Describe what you changed"

Example:
git commit -m "Fixed bug in text analyzer"


✅ 6. Push to GitHub
git push origin main

⚠️ If your branch is not main, replace it:

git push origin your-branch-name
💡 Alternative (GUI way in VS Code)

You don’t always need the terminal:

Click Source Control (🔁 icon) on the left
Click + to stage files
Type a commit message
Click ✔ Commit
Click Sync Changes or Push

🧠 Quick Summary
git add → prepare changes
git commit → save changes locally
git push → upload to GitHub