#  coding=utf-8
import os
import json


def make_dirs(var_1, var_2):
    """var_1: список папок; var_2: корневая директория"""
    for folder in var_1:
        goal_dir = os.path.join(var_2, folder)
        if os.path.exists(goal_dir):
            print(f'Директория {goal_dir} существует')
        else:
            os.makedirs(goal_dir)
            print(f'Директория {goal_dir} создана')
    return 0


with open('structure.json', encoding='utf-8') as f:
    structure = json.loads(f.read())
for root, folders in structure.items():
    if os.path.exists(root):
        print(f'Корневая директория {root} уже существует!')
        if input('Продолжить создание вложенных директорий? (yes/no): ').lower() == 'yes':
            make_dirs(folders, root)
        else:
            print('Процесс создания стартера прерван')
            exit(1)
    else:
        make_dirs(folders, root)
