#Напишите функцию группового переименования файлов. Она должна:
#✔ принимать параметр желаемое конечное имя файлов.
#При переименовании в конце имени добавляется порядковый номер.
#✔ принимать параметр количество цифр в порядковом номере.
#✔ принимать параметр расширение исходного файла.
#Переименование должно работать только для этих файлов внутри каталога.
#✔ принимать параметр расширение конечного файла.
#✔ принимать диапазон сохраняемого оригинального имени. Например для диапазона
#[3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется
#желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.


import os

def group_rename_files(directory, desired_name, num_digits, source_extension, target_extension, name_range=None):
    files = [f for f in os.listdir(directory) if f.endswith(source_extension)]
    counter = 1
    for file in files:
        old_file_path = os.path.join(directory, file)
        if name_range:
            start = max(0, name_range[0] - 1)
            end = min(len(file), name_range[1])
            base_name = file[start:end]
        else:
            base_name = ""
        new_name = f"{desired_name}{base_name}{counter:0{num_digits}d}.{target_extension}"
        new_file_path = os.path.join(directory, new_name)
        os.rename(old_file_path, new_file_path)
        counter += 1

if __name__ == "1.py":
    directory = "C:\\Users\\chena\\PycharmProjects\\pythonProject\\homework7\\"
    desired_name = 'new_file'
    num_digits = 3  # Количество цифр в порядковом номере
    source_extension = ".jpg"  # Расширение исходных файлов
    target_extension = "png"  # Расширение конечных файлов
    name_range = [3, 6]  # Диапазон сохраняемых символов из оригинального имени

    group_rename_files(directory, desired_name, num_digits, source_extension, target_extension, name_range)