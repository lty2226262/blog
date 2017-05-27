# Version Control System

* Enforce disciplane
* Archive versions
* Maintain historical information
* Enable collaboration
* recover from accidental deletions or edits
* conserve disk space

## "DON'Ts" in VCS

* don't commit executable files
* don't save another snapshot, no local copies

## examples

    git // print out the information for git
    git help init //print out git manual page for git init
    git init //create a git repository
    git status // show the changes within a git repository
    touch README

    git add README //add README into this git repository
    git commit // commit this repository
    echo '123' > README
    git status // found that there was a different version in the code

    git diff README //show the difference between two files
    git commit -a //commit all of the files that git knows about
    git commit -n "Added README content" //add a comment content

    git clone gpbud@bear.cc.gatech.edu:~/git/myproject.git myproject2 //fetch a git repository online and rename it as myproject2

    git remote -v //see the details of the server
    git push //to push this repository to the remote repository

    git branch //see what branch are you in
    git branch newBranch //create a new branch
    git checkout newBranch //choose the specified branch

    git checkout -b testing //create a new branch and switch to it

    git branch -d testing //deleting a branch
    
