## Tool for displaying shortcut notes


> When used with MARKDOWN files, it colors only the commands put between backticks  
> When used with other filetypes, it colors the whole output

---
## How to work with it
Run one of the installation scripts which specific for your shell (`zsh/bash`)  

Set `SHELL_PROFILE` in `sc.py` to be the same as your shell's rc file  

Set the path to the directory where you store your shortcut notes by typing `sc -p <YOUR_PATH_TO_DIR>` - e.g. `sc --path /Users/misho/Documents/Obsidian/Shortcuts`  

Set `TERMINAL`, `PYCHARM` to the full filenames of the notes in which you store your shortcuts - e.g. `TERMINAL='terminal.md'`  

To display terminal shortcuts, run `sc -t` or `sc --terminal`

To see all possible arguments - `sc -h` or `sc --help`


<img src="https://i.ibb.co/yQw36QK/Screenshot-2022-08-24-at-10-26-18.png"/>
