#!/usr/bin/env python
# cli tool for displaying shortcuts

import argparse

import os, sys, subprocess
import textwrap

parser = argparse.ArgumentParser()
                        
class bcolors:          # example color gamma 
    YELLOW_IN = '\033[33m'
    YELLOW_OUT = '\033[43m' 
    RED_IN = '\033[31m'
    RED_OUT = '\033[41m'
    CYAN_IN = '\033[96m'
    CEND = '\033[0m'

SHELL_PROFILE='zshrc'   # set default shell rc file

TERMINAL='terminal.md'  # shortcut 
PYCHARM='pycharm.md'    # shortcut 

COLOR=bcolors.YELLOW_IN # change color of backticks output

MAX_CAPACITY_STRING = 40 # space between shortcut and command
SPACE_BEFORE_HEADER = 18 # space before ## header
WRAP_LIMIT = MAX_CAPACITY_STRING + 5

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
            if filename == line.split('.')[0]:
                if file is not None:
                    raise Exception('Files with duplicated names. A file extension will be needed')
                file = line

        if file is None:
            raise Exception('No file has been found')
        
        return(file)


def build_colored_output(start, middle, end):
    calc_mid_section = MAX_CAPACITY_STRING - len(middle)
    
    # line wrapping
    if len(end) > WRAP_LIMIT:

        wrap_follower = WRAP_LIMIT
        initial_end_size = len(end)
            
        # stores the end of the first line of the shortcut
        first_line_end = end[0:wrap_follower] + '\n'
        
        # stores the following part of the wrapped text
        following_end = ''

        while wrap_follower < initial_end_size:

            following_end += ' ' * (len(middle) + calc_mid_section - 1) + end[wrap_follower:wrap_follower+WRAP_LIMIT] + '\n'
            wrap_follower += WRAP_LIMIT

        
        return(start + " " + COLOR + middle.replace('`', '') + bcolors.CEND + ' ' * calc_mid_section + first_line_end + following_end)

    return(start + " " + COLOR + middle.replace('`', '') + bcolors.CEND + ' ' * calc_mid_section + end)


def cat_shortcuts_liner(filename): # color only `` strings

    path = subprocess.check_output(['echo $SHORTCUTS_DIR_PATH'], shell=True).decode('utf-8')
    
    # check if file is full path or just a filename
    if '/' in filename:
        if not os.path.isfile(args.read):
            raise Exception('Incorrect path to shorcuts note')

        file_dir = filename
    else: 
        file_dir = '{}/{}'.format(path[0: -1], check_correct_file(filename)) # .replace("\\n", '')
    

    lines = None
    with open(file_dir, 'r') as file:
        lines = file.readlines()

    print() # newline

    final_output = str()

    for line in lines:
        
        count_backticks = line.count('`')
        if count_backticks == 1 or count_backticks > 2:
            raise Exception("Error parsing backticks")

        index_of_first_md_char = line.find('`')
        index_of_second_md_char = line.rfind('`')

        if line[0] == '#':
            line = bcolors.CYAN_IN + SPACE_BEFORE_HEADER * ' ' + line + bcolors.CEND
            output = line.replace('#', '')
            final_output += output + '\n'
            continue
        
        if index_of_first_md_char != -1:
            
            shortcut = line[index_of_first_md_char:index_of_second_md_char+1].strip()
            beginning_of_line = line[0:index_of_first_md_char].strip()
            ending_of_line = line[index_of_second_md_char+1:].strip()

            final_output += build_colored_output(beginning_of_line, shortcut, ending_of_line) + '\n'
            
        else:
            final_output += line

    print(final_output) # print each line


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

args = parser.parse_args()

directory_path = args.path

if len(sys.argv) < 2:
    print("\nShowCuts:")
    print("Type --help to see all the arguments\n")
    sys.exit(0)


if args.path:
    if not os.path.isdir(args.path):
        print('The specified path does not exist')
        sys.exit()
    else:
        path = os.path.abspath(args.path)
        command = 'echo \"export SHORTCUTS_DIR_PATH=\'{}\'\n$(cat $HOME/.{})\" > $HOME/.{}'.format(path, SHELL_PROFILE, SHELL_PROFILE) # :))))))
        if os.system(command) != 0:
            sys.exit()

        print(" ... ")
        print("Executing shell in order to reload PATH as environment variable")

        os.system('exec $SHELL')

def sandboxed_liner_call(args):
    try:
        cat_shortcuts_liner(args)
    except Exception as e:
        try:
            print(e.args[1])
        except:
            print(e)

        sys.exit(1)

# TERMINAL SHORTCUTS
if args.terminal:
    sandboxed_liner_call(TERMINAL)


# PYCHARM SHORTCUTS
if args.pycharm:
    sandboxed_liner_call(PYCHARM)



if args.read:
    try:
        sandboxed_liner_call(args.read)

    except Exception as e:
        print(e)
        sys.exit()

# TBA:
# Remove stars from displayed lines
