#!/usr/bin/python3
import zipfile, os
import sys
import time

def tree(path):
    """Рекурсивный обход директорий и создание списка со всеми файлами"""
    p = []
    for i in os.listdir(path):
        new_path = os.path.join(path, i)
        if os.path.isdir(new_path):
            p.extend(tree(new_path))
        else:
            p.append(new_path)
    return p

def pack(list_files, name='archive'):
    """Запаковка"""
    with zipfile.ZipFile(name+'.zip', mode='w',
                         compression=zipfile.ZIP_DEFLATED) as zf:
        for fil in list_files:
            zf.write(fil, arcname=new_name(fil))
    return 0

def unpack(archive):
    """Распаковка"""
    # выделяем имя зипфайла без расширения
    name_dir = os.path.splitext(os.path.split(archive)[-1])[0]
    with zipfile.ZipFile(archive) as zf:
        for fil in zf.infolist():
            file_name = fil.filename
            file_time = fil.date_time
            full_path = os.path.join(name_dir, file_name)
            full_path_old = os.path.join(name_dir, old_name(file_name))
            if os.path.exists(full_path_old):
                os.remove(full_path_old)
            zf.extract(fil, name_dir)
            os.rename(full_path, full_path_old)
            # преобразуем время файла из архива в числовой вид
            file_time = time.mktime(file_time + (0, 0, -1))
            # переписываем время создания на то, что было в зипе
            os.utime(os.path.join(name_dir, old_name(file_name)),
                    (file_time, file_time))


def new_name(name):
    return name + '_'

def old_name(name):
    return name[0:-1]


def main():
    if len(sys.argv) == 1:
        path = '.'
        flag = 'pack'
    elif os.path.isdir(sys.argv[1]):
        path = sys.argv[1]
        flag = 'pack'
    elif os.path.isfile(sys.argv[1]):
        path, name_archive = os.path.split(sys.argv[1])
        flag = 'unpack'

    path = os.path.abspath(path)
    os.chdir(path)

    if flag == 'pack':
        files = tree('.')
        name_archive = os.path.split(path)[-1]
        print('List of files:')
        for i in files:
            print(i)
        print('Create archive:', os.path.join(os.getcwd(), name_archive+'.zip'))
        pack(files, name=name_archive)
    elif flag == 'unpack':
        unpack(name_archive)
        print('Unpack archive to:\n', os.path.join(os.getcwd(), name_archive[:-4]))


if __name__ == '__main__':
    main()

