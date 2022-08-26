#!/usr/bin/env python
# cli tool for displaying shortcuts

import argparse

import os, sys, subprocess
import textwrap

parser = argparse.ArgumentParser()

class bcolors:
    YELLOW_IN = '\033[33m'
    YELLOW_OUT = '\033[43m' 
    RED_IN = '\033[31m'
    RED_OUT = '\033[41m'
    CYAN_IN = '\033[96m'
    CEND = '\033[0m'

SHELL_PROFILE='zshrc' # or bashrc, etc ($HOME parent directory is assumed)
TERMINAL='terminal.md' 
PYCHARM='pycharm.md'
COLOR=bcolors.YELLOW_IN




def cat_shortcuts_liner(filename): # color only `` strings

    path = subprocess.check_output(['echo $SHORTCUTS_DIR_PATH'], shell=True).decode('utf-8')
    

    file_dir = '{}/{}'.format(path[0: -1], filename) # .replace("\\n", '')

    lines = None
    with open(file_dir, 'r') as file:
        lines = file.readlines()

    MAX_CAPACITY_STRING = 25
    SPACE_BEFORE_HEADER = 18
    
    
    for line in lines:
        is_format_correct = True
        output_string = ""
        
        count_backticks = line.count('`')
        if count_backticks == 1 or count_backticks > 2:
            raise Exception("Error parsing backticks")

        index_of_first_md_char = line.find('`')
        index_of_second_md_char = line.rfind('`')

        if line[0] == '#':
            line = bcolors.CYAN_IN + SPACE_BEFORE_HEADER * ' ' + line + bcolors.CEND
            output = line.replace('#', '')
            print(output)
            continue
        
        if index_of_first_md_char != -1:
            
            shortcut = line[index_of_first_md_char:index_of_second_md_char+1]
            
            edited_shortcut = bcolors.YELLOW_IN + shortcut + bcolors.CEND
            
            edited_shortcut = edited_shortcut + " " * (MAX_CAPACITY_STRING - len(shortcut))

            output_string = line.replace(shortcut, edited_shortcut).replace('`', '')

        else:
            output_string = line

        print(output_string) # print each line


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

parser.add_argument(
        '-r', '--read',
        help='Read shortcut file from default directory'
        )

parser.add_argument(
        '-ro', '--read_not_default', 
        help='Pass full path to shortcut file'
        )

args = parser.parse_args()

directory_path = args.path


if args.path:
    if not os.path.isdir(args.path):
        print('The specified path does not exist')
        sys.exit()
    else:
        command = 'echo \"export SHORTCUTS_DIR_PATH=\'{}\'\n$(cat $HOME/.{})\" > $HOME/.{}'.format(args.path, SHELL_PROFILE, SHELL_PROFILE) # :))))))
        if os.system(command) != 0:
            sys.exit()

        print(" ... ")
        print("Executing shell in order to reload PATH as environment variable")

        os.system('exec $SHELL')

def sandboxed_liner_call(args):
    try:
        cat_shortcuts_liner(args)
    except Exception as e:
        print(e)
        sys.exit(1)
        

# TERMINAL SHORTCUTS
if args.terminal:
    sandboxed_liner_call(TERMINAL)


# PYCHARM SHORTCUTS
if args.pycharm:
    sandboxed_liner_call(PYCHARM)

def check_correct_file(filename):
    if '.' in filename:
        return filename
    else:
        command = 'cd $SHORTCUTS_DIR_PATH && ls'

        # BREAKS SECURITY POLICIES
        # command = 'find $SHORTCUTS_DIR_PATH -name \"{}\" | cat'.format(filename)

        result = subprocess.check_output([command], shell=True).decode('utf-8')

        lines = result.splitlines()
        
        file = None

        if not lines:
            raise Exception('Directory is empty')

        for line in lines:
            if filename in line:
                if file is not None:
                    raise Exception('Files with duplicated names. A file extension will be needed')
                file = line

        if file is None:
            raise Exception('No file has been found')
        
        return(file)

if args.read:
    try:
        if not '/' in args.read: # we may read files without extensions
            sandboxed_liner_call(check_correct_file(args.read))
        else:
            raise Exception('Argument should like like: readme.txt or readme')
    except Exception as e:
        print(e)
        sys.exit()


if args.read_not_default:
    print(os.path.abspath(args.read_not_default))


# TBA:
# Remove start at the beginning of the lines
# Pass full path to a file outside of default dir (-ro)


