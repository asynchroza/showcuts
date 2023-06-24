## Shortcuts or ShowCuts 😁: CLI tool for displaying shortcuts

![Example](https://github.com/asynchroza/showcuts/assets/104720011/d8c12413-5bf6-4b75-8dfe-e99a5ba5ac82)

---
Installation:
```bash
./install.sh
```
---
Setup in `sc.py`:
```python
SHELL_PROFILE=`zshrc` # or `bashrc` if you are using bash
COLOR=bcolors.YELLOW_IN  # choose a color from the bcolors class or set a custom one
MAX_CAPACITY_STRING = 40  # space between shortcut and command
SPACE_BEFORE_HEADER = 18  # space before # tags
```
---
### Configuring path to your notes directory
![Configuring path](https://github.com/asynchroza/showcuts/assets/104720011/cfa9329c-0f8d-44b0-b948-3524f61f7da4)

---
### Files with the same name
![Files with the same name](https://github.com/asynchroza/showcuts/assets/104720011/afd376c8-2430-4a35-bc5c-7cb7275c6d1c)

---

Example shortcuts file:

```text
`⇧⌘F` Open/Show search
`⌘\` Split editor pane
`⌃⇧E` Focus explorer pane
`⌃TAB` Cycle through open tabs
`⌘W` Close tab
```


