import zipfile, os, glob

path = r'/home/dima/working/python/games/snake/'

def tree(path):
    p = []
    for i in os.listdir(path):
        new_path = os.path.join(path, i)
        if os.path.isdir(new_path):
            p.extend(tree(new_path))
        else:
            p.append(new_path)
    return p

def main():
    os.chdir(path)
    files = tree('.')
    print('List of files:')
    for i in files:
        print(i)
    with zipfile.ZipFile('archive.zip', mode='w',
                         compression=zipfile.ZIP_DEFLATED) as zf:
        for fil in files:
            zf.write(fil)


if __name__ == '__main__':
    main()

