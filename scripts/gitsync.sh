#!/bin/bash

cd ~/Github/dotfiles
cp -r ~/.config/$(/bin/ls ~/Github/dotfiles/) .
git add .
git commit -m "Update as of $(date +%x)"
git push
