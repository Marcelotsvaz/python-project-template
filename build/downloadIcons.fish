#! /usr/bin/env fish

cd docs/overrides/.icons/ || exit
mkdir -p vscode-icons/{,folder,opened-folder}/
cd vscode-icons



set icons		\
	git			\
	gitlab		\
	markdown	\
	toml		\
	unlicense

set folderIcons	\
	dist		\
	docs		\
	gitlab		\
	python		\
	test		\
	vscode

set openedFolderIcons	\
	python

set -a allIcons default_file.svg
set -a allIconsPath default.svg

set -a allIcons default_folder.svg
set -a allIconsPath folder/default.svg

set -a allIcons default_folder_opened.svg
set -a allIconsPath opened-folder/default.svg



for icon in $icons
	set -a allIcons file_type_$icon.svg
	set -a allIconsPath $icon.svg
end

for icon in $folderIcons
	set -a allIcons folder_type_$icon.svg
	set -a allIconsPath folder/$icon.svg
end

for icon in $openedFolderIcons
	set -a allIcons folder_type_$icon\_opened.svg
	set -a allIconsPath opened-folder/$icon.svg
end



for index in $(seq $(count $allIcons))
	echo Downloading $allIcons[$index]
	wget https://raw.githubusercontent.com/vscode-icons/vscode-icons/master/icons/$allIcons[$index] -O $allIconsPath[$index] --quiet
	or echo Error downloading $allIcons[$index]
end