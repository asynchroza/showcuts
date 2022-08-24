
# cli tool for displaying shortcuts

import argparse

import os, sys

parser = argparse.ArgumentParser()


SHELL_PROFILE='zshrc' # or bashrc, etc ($HOME parent directory is assumed)
TERMINAL='terminal.md' 
PYCHARM='pycharm.md'
COLOR=3 # currently yellow
# 1 = red, 2 = green, 3 = yellow, 4 = blue, 5 = pink, ...


def cat_shortcuts(filename):
    file_dir = '$SHORTCUTS_DIR_PATH/{}'.format(filename)

    color_filter = 'tput setaf {}; cat; tput sgr0;'.format(COLOR)
    pipe = "clrfilter() { " + color_filter + " }"

    os.system('{} && cat {} | clrfilter && echo \"\\n\"'.format(pipe, file_dir))
    sys.exit()

# set path to shortcuts
parser.add_argument(
        '-p', '--path',
        type=str,
        help='Path to the directory where you store the documents populated with shortcuts')

# terminal shortcuts
parser.add_argument(
        '-t', '--terminal',
        action='store_true',
        help='Display terminal shortcuts'
        )

parser.add_argument(
        '-c', '--pycharm',
        action='store_true', 
        help='Display pycharm shortcuts'
        )

# pycharm shortcuts

args = parser.parse_args()

directory_path = args.path


if args.path:
    if not os.path.isdir(args.path):
        print('The specified path does not exist')
        sys.exit()
    else:
        command = 'echo \"export SHORTCUTS_DIR_PATH=\'{}\'\n$(cat $HOME/.{})\" > $HOME/.{}'.format(args.path, SHELL_PROFILE, SHELL_PROFILE) # :))))))
        # command = 'echo \"export SHORCUTS_DIR_PATH=\'{}\'\" >> $HOME/.{}'.format(args.path, SHELL_PROFILE)
        if os.system(command) != 0:
            sys.exit()

        print(" ... ")

        if os.system("source $HOME/.{} > /dev/null 2>&1".format(SHELL_PROFILE)) == 0:
            print("Path set successfully")
        else: 
            print("Something went wrong executing the shell")

        sys.exit()

if args.terminal:
    cat_shortcuts(TERMINAL)

if args.pycharm:
    cat_shortcuts(PYCHARM)


