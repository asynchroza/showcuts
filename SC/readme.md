## Tool for displaying shortcut notes

> If you want to achieve coloring such as the one on the picture beneath, use `markdown` files and put the shortcuts between backticks
> Other filetypes parse the whole output to the set color (`COLOR`)

---
## How to work with it
Run one of the installation scripts (`zsh/bash`)

Set `SHELL_PROFILE` in `sc.py` to be the same as your shell's rc file  

Set the path to the directory where you store your shortcut notes by typing `sc -p <YOUR_PATH_TO_DIR>` - e.g. `sc --path /Users/misho/Documents/Obsidian/Shortcuts`

Set `TERMINAL`, `PYCHARM` to the full filenames of the notes in which you store your shortcuts - e.g. `TERMINAL='terminal.md'`  

To display terminal shortcuts, run `sc -t` or `sc --terminal`
To display pycharm shortcuts, run `sc -c` or `sc --pycharm`

To display undeclared shortcuts which could be found in the default path, run `sc -r <filename.extension>` or `sc --read <filename.extension> (e.g. `sc -r `readme.md`) **** RECURSSIVE SEARCH TBA ****

To display undeclared shortcuts which are out of the scope of the default path: `TBA`

To see all possible arguments - `sc -h` or `sc --help`


<img src="https://i.ibb.co/zGsrqJh/Screenshot-2022-08-24-at-10-49-32.png"/>
