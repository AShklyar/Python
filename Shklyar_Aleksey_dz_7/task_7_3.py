# coding='utf-8'
import os
import shutil
import sys

try:
    start_dir, goal_dir, file_extension = sys.argv[1:]
except ValueError:
    print(f'Ошибка выполнения скрипта. Не задан один или несколько обязательных параметров')
    print(f'<путь до скрипта> <исходная директория> <целевая директория> <расширение файла>')
    exit(1)
except Exception as e:
    print(f'Непредвиденная ошибка выполнения скрипта: {e}')

if not os.path.exists(start_dir):  # проверяем существует ли директория для анализа
    print(f'Директория для анализа {start_dir} не найдена')
    exit(1)

files_list = []  # создаем список целевых файлов для копирования
if '.' not in file_extension:
    file_extension = '.'+file_extension
    file_extension = file_extension.lower()
for root, _, files in os.walk(start_dir):  # прогуливаемся по папкам и собираем в лист все файлы с расширением
    for file in files:
        if file_extension in file:
            files_list.append(os.path.join(root, file))
# если ищем формат файла, которого нет в исходной директории, то выводим соответствующее сообщение и выходим
if len(files_list) == 0:
    print(f'Искомых файлов с расширением "{file_extension}" в заданной директории не обнаружено')
    exit(1)
# только если хоть что-то нашли проверяем и создаем целевую директорию
if not os.path.exists(goal_dir):    # если целевая директория отсутствует, создаем ее
    os.mkdir(goal_dir)

for path_from in files_list:
    # формируем структуру директорий в целевой директории
    folder = os.path.join(goal_dir, os.path.basename(os.path.dirname(path_from)))
    if not os.path.exists(folder):
        os.mkdir(folder)
    path_to = os.path.join(folder, os.path.basename(path_from))  # получаем путь к директории куда надо скопировать
    try:
        shutil.copyfile(path_from, path_to)
    except shutil.SameFileError:
        print(f'Файл {os.path.basename(path_from)} в директории {folder} уже существует. Проверьте целевую директорию')
