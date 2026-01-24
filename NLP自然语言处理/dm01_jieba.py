# conding:utf-8
import jieba


# todo: 1. jieba实现精确模式的分词

def dm1_jieba():
    # 1.给出需要待切分的文本
    content = "传智教育是一家上市公司，旗下有黑马程序员品牌。我是在黑马这里学习人工智能"
    # 2.调用jieba.cut方法进行分词:返回的是生成器，取出元素的方法：for循环，next，强转list等
    # result1 = jieba.cut(content, cut_all=False)
    # print("精确模式分词结果：", result1)
    # 3.基于jieba。lcut()实现文本的切分，直接返回列表
    result2 = jieba.lcut(content, cut_all=False)
    print("精确模式分词结果是：", result2)


def dm2_jieba():
    # 1.给出需要待切分的文本
    content = "传智教育是一家上市公司，旗下有黑马程序员品牌。我是在黑马这里学习人工智能"
    # 2.调用jieba.cut方法进行分词:返回的是生成器，取出元素的方法：for循环，next，强转list等
    # result1 = jieba.cut(content, cut_all=False)
    # print("精确模式分词结果：", result1)
    # 3.基于jieba。lcut()实现文本的切分，直接返回列表
    result2 = jieba.lcut(content, cut_all=True)
    print("精确模式分词结果是：", result2)


def dm3_jieba():
    # 1.给出需要待切分的文本
    content = "传智教育是一家上市公司，旗下有黑马程序员品牌。我是在黑马这里学习人工智能"
    # 2.调用jieba.cut方法进行分词:返回的是生成器，取出元素的方法：for循环，next，强转list等
    result1 = jieba.lcut_for_search(content)
    print("搜索引擎模式分词结果是：", result1)


if __name__ == '__main__':
    dm1_jieba()
    dm2_jieba()
    dm3_jieba()
