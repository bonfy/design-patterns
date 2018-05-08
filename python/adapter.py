# -*- coding:utf-8 -*-
""" Adapter
适配器模式 将一个类的接口，转换成客户期望的另一个接口。

作用是 让原本接口不相容的两个类可以合作无间。

分 对象适配器 和 类适配器

类适配器 Adapter 继承（Target 和 Adaptee)
对象适配器 Adapter 依赖Adaptee 实现 Target接口，
"""
import abc


class Target(metaclass=abc.ABCMeta):
    """
    Define the domain-specific interface that Client uses.
    """

    @abc.abstractmethod
    def request(self):
        pass


class Adapter(Target):
    """
    Adapt the interface of Adaptee to the Target interface.
    """

    def __init__(self):
        self._adaptee = Adaptee()

    def request(self):
        print('Adapt to a request method.')
        self._adaptee.specific_request()


class Adaptee:
    """
    Define an existing interface that needs adapting.
    """

    def specific_request(self):
        print('Not a request method.')


def main():
    adapter = Adapter()
    adapter.request()


if __name__ == "__main__":
    main()
