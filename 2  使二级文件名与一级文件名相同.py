import os

# 设置一级目录的路径
root_dir = r'E:\建筑\补充素材\地标'

def get_unique_filename(file_path, new_name):
    base, extension = os.path.splitext(new_name)
    counter = 1
    while os.path.exists(file_path):
        new_name = f"{base}_{counter}{extension}"
        file_path = os.path.join(os.path.dirname(file_path), new_name)
        counter += 1
    return file_path

for folder in os.listdir(root_dir):
    folder_path = os.path.join(root_dir, folder)

    if os.path.isdir(folder_path):
        for file in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file)

            if os.path.isfile(file_path):
                file_extension = os.path.splitext(file)[1]
                new_file_name = folder + file_extension
                new_file_path = os.path.join(folder_path, new_file_name)
                new_file_path = get_unique_filename(new_file_path, new_file_name)

                os.rename(file_path, new_file_path)
