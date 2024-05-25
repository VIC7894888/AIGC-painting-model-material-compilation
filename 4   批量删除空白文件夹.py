import os

# 设置要处理的根目录的路径
root_dir = r'E:\建筑\补充素材\图片助手(ImageAssistant)_批量图片下载器\www.behance.net'

# 确保目标目录存在
if not os.path.exists(root_dir):
    print(f"指定的目录不存在: {root_dir}")
    exit(1)

# 倒序遍历目录树
for folder_name, subfolders, filenames in os.walk(root_dir, topdown=False):
    # 检查当前文件夹是否为空
    if not os.listdir(folder_name):
        print(f"删除空文件夹: {folder_name}")
        os.rmdir(folder_name)

print("空白文件夹删除完成。")
