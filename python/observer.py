# -*- coding:utf-8 -*-
""" Observer

出版者 + 订阅者 = 观察者模式

出版者（Subject） 订阅者（Observer）

观察者模式 定义了对象之间的一对多依赖
这样一来，当一个对象改变状态时，它的所有依赖者都会收到通知并自动更新

优点: 松耦合

当两个对象之间松耦合，它们依然可以交互，但是不太清楚彼此的细节。
观察者模式提供了一种对象设计，让 主题 和 观察者 之间松耦合
"""

import abc


class Subject:

    def __init__(self):
        self._observers = set()

    def attach(self, observer):
        self._observers.add(observer)

    def detach(self, observer):
        self._observers.discard(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)


class Observer(metaclass=abc.ABCMeta):

    @abc.abstractclassmethod
    def update(self, subject):
        pass


# Example usage
class Data(Subject):

    def __init__(self, name=''):
        super().__init__()
        self.name = name
        self._data = 0

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
        self.notify()


class HexViewer(Observer):

    def update(self, subject):
        print(
            u'HexViewer: Subject %s has data 0x%x' %
            (subject.name, subject.data)
        )


class DecimalViewer(Observer):

    def update(self, subject):
        print(
            u'DecimalViewer: Subject %s has data %d' %
            (subject.name, subject.data)
        )


# Example usage...
def main():
    # Attach
    data1 = Data('Data 1')
    data2 = Data('Data 2')
    view1 = DecimalViewer()
    view2 = HexViewer()
    data1.attach(view1)
    data1.attach(view2)
    data2.attach(view1)
    data2.attach(view2)
    print(u"Setting Data 1 = 10")
    data1.data = 10
    print(u"Setting Data 2 = 15")
    data2.data = 15
    print(u"Setting Data 1 = 3")
    data1.data = 3
    print(u"Setting Data 2 = 5")
    data2.data = 5
    # Detach
    print(u"Detach HexViewer from data1 and data2.")
    data1.detach(view2)
    data2.detach(view2)
    print(u"Setting Data 1 = 10")
    data1.data = 10
    print(u"Setting Data 2 = 15")
    data2.data = 15


if __name__ == '__main__':
    main()
### OUTPUT ###
# Setting Data 1 = 10
# DecimalViewer: Subject Data 1 has data 10
# HexViewer: Subject Data 1 has data 0xa
# Setting Data 2 = 15
# HexViewer: Subject Data 2 has data 0xf
# DecimalViewer: Subject Data 2 has data 15
# Setting Data 1 = 3
# DecimalViewer: Subject Data 1 has data 3
# HexViewer: Subject Data 1 has data 0x3
# Setting Data 2 = 5
# HexViewer: Subject Data 2 has data 0x5
# DecimalViewer: Subject Data 2 has data 5
# Detach HexViewer from data1 and data2.
# Setting Data 1 = 10
# DecimalViewer: Subject Data 1 has data 10
# Setting Data 2 = 15
# DecimalViewer: Subject Data 2 has data 15
