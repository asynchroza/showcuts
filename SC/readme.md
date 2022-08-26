## Shortcuts or ShowCuts 😁: CLI tool for displaying shortcuts
---
Installation:
```
./install.sh  # --zsh if you are running zsh and not bash
```
Installs the tool globally but you won't be able to run it with sudo (and you don't need to 🏥)

---
Setup in `sc.py`:
```
SHELL_PROFILE=`zshrc` # or `bashrc` if you are using bash
COLOR=bcolors.YELLOW_IN  # choose a color from the bcolors class or set a custom one
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

<img src="https://i.ibb.co/LQSBXKS/image.png"/>
---
(Example formatting)[https://github.com/mbozhilov-qb/utils/blob/main/SC/example_shortcut_file.md]:

```
# KEYBOARD SHORTCUTS
* `ctrl + c`  copy
```
The space between the shortcut and the command does not matter. The tool takes care of the formatting. You are able to experiment and make the notes look good both in your text editor and your terminal.

<img src="https://i.ibb.co/RzXP4kD/image.png"/>
