import os

def make_folder(day: int, files=False):
    """
    Creates directory named dayX if does not exist
    and create 3 files: [dayX.py, input.txt, puzzle.txt] if files is True, ignoring any that already exist
    where X is the day number given
    """
    current = os.getcwd()
    final = os.path.join(current, f'day{day}')
    name = final.split('\\')[-1]
    if not os.path.exists(final):
        os.mkdir(final)
        print(f'Created folder: {name}')
    else:
        print(f'Folder {name} already exists!')

    if files:
        files_to_create = [f'day{day}.py', 'input.txt', 'puzzle.txt']
        for file in files_to_create:
            path = os.path.join(final, file)
            if os.path.exists(path):
                print(f'File {file} already exists!')
                continue
            open(os.path.join(final, file), 'w')
            print(f'Created: {file}')

if __name__ == '__main__':
    for i in range(1, 26):
        make_folder(i, files=True)
