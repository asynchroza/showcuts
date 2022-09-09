#!/bin/bash
if [ "$(basename $SHELL)" == "zsh" ]; then
    RCFILE=.zshrc
else
    RCFILE=.bashrc
fi

ln -s $PWD/sc.py $PWD/sc
echo "export PATH="\$PATH:$PWD"" >> $HOME/$RCFILE

echo "Loading the shell so that SC is on PATH"
echo "Run the tool by typing sc in the terminal"
exec $SHELL
