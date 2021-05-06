#!/bin/bash

cd ~/Github/dotfiles
list="$(ls ~/Github/dotfiles)"
rm -rf ~/Github/dotfiles/*
cp -r ~/.config/$list .
git add .
git commit -m "Update as of $(date +%d/%m/%y)"
git push
