#!/bin/bash

if [ "$(basename $SHELL)" == "zsh" ]; then
    RCFILE=.zshrc
else
    RCFILE=.bashrc
fi


FILE_PATH=$HOME/$RCFILE
EXPORT_LINE="export PATH="\$PATH:$PWD""

if grep -Fxq "$EXPORT_LINE" "$FILE_PATH"; then
    echo "Path to ShowCuts is already exported!"
    exit 0
else
     # Create a symbolic link to sc.py if it doesn't exist
    if [ ! -L "$PWD/sc" ]; then
        ln -s "$PWD/sc.py" "$PWD/sc"
    else
        echo "ShowCuts is already installed in /usr/bin"
    fi

    echo $EXPORT_LINE >> $HOME/$RCFILE

    echo "Run the tool by typing sc in the terminal"
fi

exec $SHELL

