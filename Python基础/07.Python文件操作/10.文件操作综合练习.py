
# open文件
fr = open("Python基础/07.Python文件操作/操作文件/bill.txt", "r", encoding="utf-8")
fw = open("Python基础/07.Python文件操作/操作文件/bill.txt.bak", "w", encoding="utf-8")

# 操作文件
for line in fr.readlines():
    line = line.strip() # 清除行尾的换行符
    print(line.split(",")[4])
    if "测试" == line.split(",")[4]:
        continue
    else:
        fw.write(line + "\n")


    
# close文件
fr.close()
fw.close()