# conding:utf-8
import jieba

#todo: 1. jieba实现精确模式的分词

def dm1_jieba():
    # 1.给出需要待切分的文本
    content = "传智教育是一家上市公司，旗下有黑马程序员品牌。我是在黑马这里学习人工智能"
    # 2.调用jieba.cut方法进行分词
    result1 = jieba.cut(content, cut_all=False)
    print("精确模式分词结果：", result1)
    print("精确模式分词结果：", list(result1))
    for value in result1:
        print(value)
    print("精确模式分词结果：", next(result1))

if __name__ == '__main__':
    dm1_jieba()
