# -*- coding:utf-8 -*-
import abc


#################
# Stratygy Class
#################
class Context:
    """
    Define the interface of interest to clients.
    Maintain a reference to a Strategy object.
    """

    def __init__(self, strategy):
        self._strategy = strategy

    def context_interface(self):
        self._strategy.algorithm_interface()


class Strategy(metaclass=abc.ABCMeta):
    """
    Declare an interface common to all supported algorithms. Context
    uses this interface to call the algorithm defined by a
    ConcreteStrategy.
    """

    @abc.abstractmethod
    def algorithm_interface(self):
        pass


class ConcreteStrategyA(Strategy):
    """
    Implement the algorithm using the Strategy interface.
    """

    def algorithm_interface(self):
        print('Strategy A')


class ConcreteStrategyB(Strategy):
    """
    Implement the algorithm using the Strategy interface.
    """

    def algorithm_interface(self):
        print('Strategy B')


#################
# Strategy Method
#################
class ContextMethod:

    def __init__(self, strategy):
        self._strategy = strategy

    def context_interface(self):
        self._strategy()


def main():
    # Stategy Class
    concrete_strategy_a = ConcreteStrategyA()
    context = Context(concrete_strategy_a)
    context.context_interface()
    concrete_strategy_b = ConcreteStrategyB()
    context = Context(concrete_strategy_b)
    context.context_interface()
    # Stategy Method
    funcA = lambda: print('strategy method A')
    funcB = lambda: print('strategy method B')
    context = ContextMethod(funcA)
    context.context_interface()
    context = ContextMethod(funcB)
    context.context_interface()


if __name__ == "__main__":
    main()
