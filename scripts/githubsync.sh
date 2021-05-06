#!/bin/bash

echo "Changing directory to ~/Github/dotfiles..."
cd ~/Github/dotfiles/

# Here we are parsing the names of the folders in the current directory into an array: list[]
i=0
while read line
do
    list[$i]="$line"        
    (( i++ ))
done < <(ls ~/Github/dotfiles)

# Now to update the contents of directories in the Github repo, we remove, copy a new one from ~/.config and then add it to git
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

# Then we commit these changes with a message carrying the current date and time. And finally, we push these new directories to the remote Github repo
echo "Committing changes..."
git commit -m "Update as of $(date +%d/%m/%y-%T)"
echo "Pushing to remote Github repository (if any)..."
git push
echo "Success"
