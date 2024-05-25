import os

# 设置工作目录，即包含要重命名文件的目录
directory = r'素材位置'

# 遍历目录中的所有文件
for filename in os.listdir(directory):
    new_name = filename
    # 检查文件名中是否包含“副本”或括号
    if '副本' in new_name:
        new_name = new_name.replace('副本', '')  # 删除“副本”
    new_name = new_name.replace('(', '').replace(')', '')  # 删除括号
    # 重命名文件
    os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))

print("文件名修改完成。")
