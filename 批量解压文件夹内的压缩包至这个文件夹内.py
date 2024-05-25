import os
import zipfile

def unzip_all_in_folder(folder_path):
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isfile(item_path) and item.endswith('.zip'):
            with zipfile.ZipFile(item_path, 'r') as zip_ref:
                zip_ref.extractall(folder_path)
                print(f"解压 '{item}' 完成.")
        elif os.path.isdir(item_path):
            unzip_all_in_folder(item_path)

# 使用时指定要解压的文件夹路径
folder_to_unzip = '素材'
unzip_all_in_folder(folder_to_unzip)
