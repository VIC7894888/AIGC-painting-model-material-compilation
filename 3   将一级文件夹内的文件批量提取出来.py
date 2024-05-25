import os
import shutil

# 设置一级目录的路径
root_dir = r"E:\建筑\补充素材\图片助手(ImageAssistant)_批量图片下载器\www.behance.net"

for folder in os.listdir(root_dir):
    folder_path = os.path.join(root_dir, folder)

    # 确保它是一个目录
    if os.path.isdir(folder_path):
        for file in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file)

            # 检查是否为文件
            if os.path.isfile(file_path):
                # 构建文件在一级目录中的新路径
                new_file_path = os.path.join(root_dir, file)

                # 移动文件
                shutil.move(file_path, new_file_path)
