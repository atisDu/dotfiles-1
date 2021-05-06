#!/bin/bash

echo "Changing directory to ~/Github/dotfiles..."
cd ~/Github/dotfiles/
i=0
while read line
do
    list[$i]="$line"        
    (( i++ ))
done < <(ls ~/Github/dotfiles)
#list=("awesome" "kitty" "polybar.old" "ranger" "sway" "waybar" "README.md"  "awesome-back" "leftwm" "qtile" "rofi" "terminator" "alacritty" "fish" "polybar" "qtile-back" "scripts" "termite" "hi")

echo "List of Directories being synced..."
for ((i=0 ; i < ${#list[@]} ; i++)); do
	echo "Removing ${list[i]}"
	rm -r ~/Github/dotfiles/"${list[i]}"
	echo "Copying ${list[i]}"
	cp -r ~/.config/"${list[i]}" ~/Github/dotfiles
	echo "Adding ${list[i]} to git"
	git add "${list[i]}"
done
echo "Sync complete..."
echo "Committing changes..."
git commit -m "Update as of $(date +%d/%m/%y-%T)"
echo "Pushing to remote Github repository (if any)..."
git push
echo "Success"
