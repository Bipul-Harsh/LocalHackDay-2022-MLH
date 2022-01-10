'''
# Project Setup Creator

Desctiption:
    - This program is designed to allow user to create a project setup file by giving it a name and add list of commands to create it.
    - They then can just pass the setup name as arguments to run the command list.

Things you can do:
    - Create a new setup file and add commands to it.
    - Update setup file name
    - Delete setup file
    - Run setup file
    - Update setup file
    - Show editor

'''

import os
import argparse
import shutil

def getSetupList():
    '''
    Get the dictionary of setups saved in setups directory created by user.
    The setup file is stored as:
        `<setup_name>.txt`
    
    Returns:
        setupList: list cotaines setup names
    '''
    setupList = []
    for file in os.listdir('setups'):
        if file.endswith('.txt'):
            setupList.append(file.split('.')[0])
    return setupList

def getEditor():
    '''
    - Get the editor to use for editing setup file.
    - Will read the content of '.editor' file in current directory.
    - If '.editor' file does not exist, will search from editors list. And create '.editor' file and append available editor path.
    '''
    editors = ['vi', 'nano', 'emacs', 'notepad', 'vim', 'neovim', 'gedit', 'sublime', 'code', 'atom']
    if not os.path.isfile('.editor'):
        with open('.editor', 'w') as f:
            pass
    with open('.editor', 'r+') as f:
        editor_info = f.readline()
        if '|' in editor_info:
            editor_name, editor_path = editor_info.split('|')
            return [editor_name, editor_path]
        else:
            for editor in editors:
                editor_name, editor_path = editor, shutil.which(editor)
                if editor_path:
                    with open('.editor', 'w') as f:
                        f.write(editor + '|' + editor_path)
                        return [editor, editor_path]
            else:
                print(f'Editor is not saved. Please install an editor and run:\n> python3 main.py -se <editor_name>')
                exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
    prog="Project Setup Creator",
    formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument('file', type=str, default='', help="to run setup. Give either project name or index.",nargs='*')
    parser.add_argument('-u', type=str, help="Update setup file name",nargs='*')
    parser.add_argument('-to', type=str, help="New file name to change with",nargs='*')
    parser.add_argument('-d', type=str, help="Delete setup file.",nargs='*')
    parser.add_argument('-c', type=str, help="Create new setup file. This will create and open the file in editor to add commands.",nargs='*')
    parser.add_argument('-e', type=str, help="Edit setup file.", nargs='*')
    parser.add_argument('-se', type=int, help="To set editor. Please provide editor name which can be executed on running in terminal/shell.")
    parser.add_argument('-l', action='store_const', const=True, default=False, dest='list_setups', help="List all setup files.")
    parser.add_argument('-editor', action='store_const', const=True, default=False, dest='show_editor', help="Show editor name with path.")

    args = parser.parse_args()
    editor = getEditor()

    if args.list_setups:
        if(len(getSetupList()) == 0):
            print("No setup is created yet.")
        else:
            print("List of setup files:\n--------------------")
            for setup in getSetupList():
                print(f'-> {setup}')
    if args.show_editor:
        print(f'Editor: {editor[0]}\nPath: {editor[1]}')
    if args.u:
        if args.to:
            source_file = f'setups/{" ".join(args.u)}.txt'
            dest_file = f'setups/{" ".join(args.to)}.txt'
            if os.path.exists(source_file):
                shutil.move(source_file, dest_file)
                print(f'Setup file {" ".join(args.u)} renamed to {" ".join(args.to)}')
            else:
                print(f'Setup file {" ".join(args.u)} does not exist!')
            exit()
        else:
            print("Please provide new setup file name.")
            exit()
    if args.d:
        file_path = f'setups/{" ".join(args.d)}.txt'
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f'Setup file {" ".join(args.d)} deleted.')
            exit()
        else:
            print(f'Setup file {" ".join(args.d)} does not exist.')
            exit()
    if args.se:
        editor_path = shutil.which(args.se)
        if editor_path:
            with open('.editor', 'w+') as f:
                f.write(f'{args.se} | {editor_path}')
                print(f'Editor set to {args.se}')
            exit()
        else:
            print(f'{args.se} is not a valid editor! Please check if it is installed and can be open with this name from shell.')
            exit()
    if args.c:
        file_name = "\ ".join(args.c)
        file_path = f'setups/{file_name}.txt'
        if ' '.join(args.c) in getSetupList():
            print(f'Setup file {" ".join(args.c)} already exists!')
            exit()
        else:
            os.system(f'{editor[1]} {file_path}')
            exit()
    if args.e:
        file_name = "\ ".join(args.e)
        file_path = f'setups/{file_name}.txt'
        if os.path.exists('setups/' + ' '.join(args.e) + '.txt'):
            os.system(f'{editor[1]} {file_path}')
            exit()
        else:
            print(f'Setup file {" ".join(args.e)} does not exist!')
            exit()
    if args.file:
        setup_name = " ".join(args.file)
        if setup_name in getSetupList():
            file_path = f'setups/{setup_name}.txt'
            with open(file_path, 'r') as f:
                for line in f.readlines():
                    os.system(line.strip())
                print(f'Setup {setup_name} executed!')
            exit()
        else:
            print(f'Setup {setup_name} does not exist!')
            exit()