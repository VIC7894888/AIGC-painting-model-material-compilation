import os
import shutil

# 设置要处理的目录的路径
root_dir = r'您的目录路径'

# 确保目标目录存在
if not os.path.exists(root_dir):
    print(f"指定的目录不存在: {root_dir}")
    exit(1)

# 遍历目录中的所有文件
for folder_name, subfolders, filenames in os.walk(root_dir):
    for filename in filenames:
        # 获取文件名（不含扩展名）和扩展名
        file_base, file_extension = os.path.splitext(filename)

        # 创建以文件名命名的新目录路径
        new_folder_path = os.path.join(root_dir, file_base)

        # 如果该目录不存在，则创建它
        if not os.path.exists(new_folder_path):
            os.makedirs(new_folder_path)

        # 构建原始文件的完整路径和新文件的完整路径
        original_file_path = os.path.join(folder_name, filename)
        new_file_path = os.path.join(new_folder_path, filename)

        # 移动文件到新目录
        shutil.move(original_file_path, new_file_path)

print("文件分类完成。")
