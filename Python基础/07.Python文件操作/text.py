import os

def diagnose_file_problem():
    """
    用于诊断文件无法打开的问题
    """
    target_filename = "hi.txt"

    # 1. 获取脚本所在的目录
    script_dir = os.path.dirname(os.path.abspath(__file__))
    print(f"1. 脚本所在的目录: {script_dir}")

    # 2. 获取当前工作目录
    current_working_dir = os.getcwd()
    print(f"2. 当前工作目录 (os.getcwd()): {current_working_dir}")

    # 3. 检查脚本目录和当前工作目录是否一致
    if script_dir == current_working_dir:
        print("   -> 脚本目录与当前工作目录一致。")
    else:
        print("   -> ⚠️ 警告：脚本目录与当前工作目录不一致！")

    # 4. 列出当前工作目录下的所有文件和子目录
    try:
        files_in_current_dir = os.listdir(current_working_dir)
        print(f"3. 当前工作目录下的文件和文件夹: {files_in_current_dir}")
        
        # 检查目标文件是否存在
        if target_filename in files_in_current_dir:
            print(f"   ✓ 在当前目录找到了 '{target_filename}'")
            
            # 获取文件的详细信息
            file_path = os.path.join(current_working_dir, target_filename)
            file_stats = os.stat(file_path)
            print(f"   -> 文件大小: {file_stats.st_size} 字节")
            print(f"   -> 文件路径: {file_path}")
            
        else:
            print(f"   ✗ 在当前目录没有找到 '{target_filename}'")
            
            # 检查是否有相似名称的文件
            similar_files = [f for f in files_in_current_dir if target_filename.split('.')[0].lower() in f.lower()]
            if similar_files:
                print(f"   -> 提示：发现了可能相关的文件: {similar_files}")

    except PermissionError:
        print("   ✗ 无法访问当前目录，可能存在权限问题。")

    # 5. 尝试使用绝对路径打开文件
    absolute_file_path = os.path.join(script_dir, target_filename)
    print(f"\n4. 尝试使用脚本目录下的绝对路径: {absolute_file_path}")
    
    try:
        with open(absolute_file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            print(f"   ✓ 成功打开文件！内容如下:\n--- 文件内容开始 ---\n{content}\n--- 文件内容结束 ---")
    except FileNotFoundError:
        print(f"   ✗ 使用绝对路径也失败了，'{absolute_file_path}' 不存在。")
    except Exception as e:
        print(f"   ✗ 使用绝对路径时发生其他错误: {e}")

    # 6. 再次尝试使用相对路径（这是你原来的代码逻辑）
    print(f"\n5. 尝试使用相对路径: {target_filename}")
    try:
        with open(target_filename, 'r', encoding='utf-8') as f:
            content = f.read()
            print(f"   ✓ 成功打开文件！内容如下:\n--- 文件内容开始 ---\n{content}\n--- 文件内容结束 ---")
    except FileNotFoundError:
        print(f"   ✗ 相对路径失败，'{target_filename}' 未找到。")
    except Exception as e:
        print(f"   ✗ 相对路径时发生其他错误: {e}")

if __name__ == "__main__":
    diagnose_file_problem()