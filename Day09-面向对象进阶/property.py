#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Project  : Python-100-Days
  @File     : property.py
  @Desc     : property装饰器
  @Time     : 2020/12/14 20:55
  @Author   : clownfish7 yuzhiyou999@outlook.com
  @Software : PyCharm
  @Version  : 1.0
"""


class Person(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    # 访问器 - getter方法
    @property
    def name(self):
        return self._name

    # 访问器 - getter方法
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s正在玩飞行棋.' % self._name)
        else:
            print('%s正在玩斗地主.' % self._name)


def main():
    person = Person('clownfish7', 15)
    person.play()
    person.age = 22
    person.play()


if __name__ == '__main__':
    main()
