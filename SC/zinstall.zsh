#!/bin/zsh

ln -s $PWD/sc.py $PWD/sc
echo "export PATH="\$PATH:$PWD"" >> $HOME/.zshrc
exec $SHELL


