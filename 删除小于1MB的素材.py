import os

def delete_small_files(directory, size_limit):
    for foldername, subfolders, filenames in os.walk(directory):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            if os.path.getsize(file_path) < size_limit * 1024:  # 转换为KB
                os.remove(file_path)
                print(f"已删除: {file_path}")

# 设置要搜索的目录和大小限制
directory_to_search = directory_to_search = r'素材'
  # 替换为你的目录路径
size_limit_kb = 1024

# 调用函数
delete_small_files(directory_to_search, size_limit_kb)
