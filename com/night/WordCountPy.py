#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import string


# Walden.txt 下载链接：https://pan.baidu.com/s/1o75GKZ4

def word_count_first(path='C:\Users\zhang\Desktop\Walden.txt'):
    path = 'C:\Users\zhang\Desktop\Walden.txt'
    with open(path, 'r') as text:
        words = text.read().split()
        print(words)
        for word in words:
            print('{}-{} times'.format(word, words.count(word)))
    pass


def word_count_second(path):
    # 打开文件
    with open(path, 'r') as text:
        # strip(string.punctuation)剔除首位连在一起的标点符号 lower()字母小写  text.read().split()单词分割
        words = [raw_word.strip(string.punctuation).lower() for raw_word in text.read().split()]
        # print(words)
        # 用set函数转换成集合,自动剔除所有重复的元素
        words_index = set(words)
        # 创建一个以单词为键[Key] 出现频率为值[value]的字典
        count_dirc = {index: words.count(index) for index in words_index}
        # 移除""空字符串的key
        count_dirc.pop("")
        # print(count_dirc)
        # 对字典进行排序，以数值大小进行排序
        for word in sorted(count_dirc, key=lambda x: count_dirc[x], reverse=True):
            print('{}  --  {} times'.format(word, count_dirc[word]))
        # words = text.read().split()
        # print(words)
        # for word in words:
        #     print('{}-{} times'.format(word, words.count(word)))

    pass


if __name__ == '__main__':
    # word_count_first()
    word_count_second('C:\Users\zhang\Desktop\Walden.txt')
