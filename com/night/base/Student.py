#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Administrator'
__date__ = '2017/10/16'


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'


            # bart = Student('Bart Simpson', 50)
            # lisa = Student('Lisa Simpson', 87)
            #
            # print('bart.name: ',bart.name)
            # print('lisa.name: ',lisa.name)
            # bart.print_score()
            # print bart.get_grade()
            #
            # lisa.print_score()
            # print lisa.get_grade()
