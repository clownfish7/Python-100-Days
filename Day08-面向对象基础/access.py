#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Project  : Python-100-Days
  @File     : access.py
  @Desc     : 访问可见性
  @Time     : 2020/12/14 20:46
  @Author   : clownfish7 yuzhiyou999@outlook.com
  @Software : PyCharm
  @Version  : 1.0
"""


class Test:

    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')


def main():
    test = Test('hello')
    test._Test__bar()
    print(test._Test__foo)


if __name__ == "__main__":
    main()
