#!/bin/zsh

cp $PWD/sc.py $PWD/sc
echo "export PATH="\$PATH:$PWD"" >> $HOME/.zshrc
exec $SHELL

