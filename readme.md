## Shortcuts or ShowCuts 😁: CLI tool for displaying shortcuts

<img src="https://i.ibb.co/S6XVWXh/Screenshot-2022-09-02-at-1-19-12.png"/>

---

Installation:
```
./install.sh  # pass --zsh argument if you are running zsh and not bash
```
Installs the tool globally but you won't be able to run it with sudo.
If you want to delete the directory and keep the tool, either change `PATH` to point to the location of the tool or move it to `/usr/bin`

---
Setup in `sc.py`:
```
SHELL_PROFILE=`zshrc` # or `bashrc` if you are using bash
COLOR=bcolors.YELLOW_IN  # choose a color from the bcolors class or set a custom one
MAX_CAPACITY_STRING = 40  # space between shortcut and command
SPACE_BEFORE_HEADER = 18  # space before # tags
```
---
```
sc -t && sc -c # terminal and pycharm shortcuts
```
`TERMINAL` and `PYCHARM` variables should be set in `sc.py`

<img src="https://i.ibb.co/ZGyrKv0/image.png"/>

---
```
sc -r filename # search shortcuts in --path directory
```
If there are files with the same name, you may run the same command but this time passing the extension of the file

<img src="https://i.ibb.co/8mD0ygY/Screenshot-2022-08-26-at-14-17-58.png"/>

---

Example formatting:

```
# KEYBOARD SHORTCUTS
* `ctrl + c`  copy
```
The space between the shortcut and the command does not matter. The tool takes care of the formatting. You are able to experiment and make the notes look good both in your text editor and your terminal.

[A more detailed example](https://github.com/mbozhilov-qb/showcuts/blob/main/example_shortcut_file.md)

```
* `0`  go to start of line
*   `q + letter` start recording macro
*       `@ + letter`    play recorded macro

Parsed as: 
```
<img src="https://i.ibb.co/56ZqwWT/Screenshot-2022-08-26-at-14-09-32.png"/>



