import zipfile, os, glob


def tree(path):
    p = []
    for i in os.listdir(path):
        new_path = os.path.join(path, i)
        if os.path.isdir(new_path):
            p.extend(tree(new_path))
        else:
            p.append(new_path)
    return p

def pack(list_files, name='archive'):
    with zipfile.ZipFile(name+'.zip', mode='w',
                         compression=zipfile.ZIP_DEFLATED) as zf:
        for fil in list_files:
            zf.write(fil, arcname=new_name(fil))
    return 0

def new_name(name):
    return name + '_'

def old_name(name):
    return name[0:-1]


def main():
    path = r'/home/dima/working/python/games/snake/'
    path = os.path.abspath(path)
    name_archive = os.path.split(path)[-1]
    os.chdir(path)
    files = tree('.')
    print('List of files:')
    for i in files:
        print(i)
    print('Имя архива', name_archive)

    pack(files, name=name_archive)




if __name__ == '__main__':
    main()

