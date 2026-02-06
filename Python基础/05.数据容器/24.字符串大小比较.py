
"""
字符串大小比较
字符串的大小比较是根据ASCII码值进行的，比较时会逐个字符进行比较，直到找到不同的字符为止。
有内容大于无内容
"""
# 示例代码
str1 = "apple"
str2 = "banana"
print(str1 > str2) # False
print(str1 < str2) # True
print(str1 == str2) # False

# 中文也能比较大小，依靠编码表（一般是UTF-8或GBK）
str3 = "苹果"
str4 = "香蕉"
print(str3 > str4) # False
print(str3 < str4) # True

"""
英文比较规则
- 小写字母大于大写字母
- 大写字母大于数字
其余查询ASCII码表
"""