# Steps to follow to run the application
- run this on git bash
- bash setup.sh
- else on linux = ./setup.sh


# for cloud deployement:
- nohup ./setup.sh > output.log 2>&1 &

# Git
- git init
- git add .
- git commit -m "msg"
- git branch -M main
- git remote add origin https://
- git push -u origin main

# Activate virtual environment
- environment - pdfvenv
- .\pdfvenv\Scripts\activate
- pip freeze > requirements.txt
# Run the app
- streamlit run main.py


# Git
- git branch
## If you're not on test-branch, switch to it:
- git checkout test-branch
## Pull Latest Changes from test-branch 
- git pull origin test-branch
## Switch to main
- git checkout main
## Merge Changes from test-branch into main
- git merge test-branch

## if conflict
- git add .
- git commit -m "Resolved issue"

## Push main tp Remote repo
- git push origin main

