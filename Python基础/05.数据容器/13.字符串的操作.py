
# 字符串的下标操作
s = "itheima哈哈666"

print(s[7])
print(s[-6])

# 字符串的修改,不可修改
try:
    s[-6] = "b"
except TypeError as e:
    print("修改字符串元素时出错:", e)


s = "abc" # 字符串不可修改，但是可以重新赋值变量
print(s)

# index 方法可以查找子字符串在字符串中的位置
print(s.index("a"))
print(s.index("b"))
print(s.index("c"))

# replace 方法可以替换字符串中的子字符串
str1 = s.replace("a", "A")
print(str1)
print(s)  # 原字符串不变   

# split 方法可以将字符串拆分成列表,字符串本身不会发生变化
str2 = "a,b,c,d,e"
lst2 = str2.split(",")
print(lst2, type(lst2))

# strip 方法可以去除字符串首尾的空格和换行符
str3 = "   \na,b,c,d,e\n   "
print(str3)
print(str3.strip())

# strip(字符串) 可以去除字符串首尾的指定字符
str4 = "###a,b,c,d,e###"
print(str4)
print(str4.strip("#"))

# count(字符)统计字符串中某个字符出现的次数
# count("字符串")统计字符串中某个子串出现的次数
str5 = "itheima a a a a a a a a"
num_a = str5.count("a")
print(num_a)

# len()统计字符串的长度
str6 = "itheima"
print(len(str6))


