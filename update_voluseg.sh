#!/bin/bash
## upgrade voluseg package
python37pip install --upgrade --force-reinstall git+https://github.com/mikarubi/voluseg.git

## commit uncommit changes, probably in janelia_setup branch
cd ~/janelia_voluseg
git fetch upstream
git checkout janelia_setup
git status
git diff

echo "Enter your commit message below:"
read commitmsg
echo "Your commit message is:"
echo $commitmsg
echo "Would you like to commit? [y/n]"
read -n 1 -s input

if [ $input = "y" ];
 then
  git commit -am "$commitmsg"
elif [ $input = "n" ];
 then
  echo "process abort exit code 0"
  exit 0
else
  echo "process abort exit code 1 - your input $input is not y or n"
  exit 1
fi

## update master and janelia_setup branch
git checkout master
git merge upstream/master
git checkout janelia_setup
git merge master
