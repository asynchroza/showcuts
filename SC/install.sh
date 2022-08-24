#!/bin/bash

cp $PWD/sc.py $PWD/sc
echo "export PATH="\$PATH:$PWD"" >> $HOME/.bashrc
exec $SHELL


