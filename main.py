

# item 24: Use @classmethod Polymorphism to construct objects generically
# ------------------------------------------------------------------------------

# in python, both objects and classes support Polymorphism, which is essentially a way for multiple classes in a hierarchy to
# implement the same method in their own unique way. This allows several classes to fulfill the same interface or abstract base
# class while providing different functionality.

# for example, consider a MapReduce implementation that requires a common class to represent the input data

class InputData():
    def read(self):
        raise NotImplementedError

class PathInputData(InputData):

    def __init__(self, path):
        self.path = path

    def read(self):
        return open(self.path).read()


# Item 28: Inherit from collections.abc for Custom Container Types
# ------------------------------------------------------------------------------

# Every python class is a container of some form or another, and the collections.abc module contains a
# large number of readily accessible containers

# consider a custom object that adds some additional functionality to a list that counts
# the number of times that an item comes up

class FrequencyList(list):

    def __inti__(self, members):

        super().__init__(members)

    def frequency(self):

        counts = {}

        for item in self:

            #dict.setdefault() sets a key with some default value if the key does not
            #already exist

            counts.setdefault(item, 0)
            counts[item] += 1

        return counts

test = FrequencyList([1,2,3,4,5,5,5,'foo'])
print(test.frequency())

import time
import numpy as np
from multiprocessing import Process

class DataThread(Process):

    def __init__(self, func, args, kwargs):
        self._func = func
        self._args = args
        self._kwargs = kwargs

        super().__init__()

    def run(self):

        start =  time.time()

        self.func(*self._args, **self._kwargs)

        end = time.time()

        self.time = (end - start)
        print(self.time)




def timer(*args, **kwargs):
    _accepted_args = ['n']

    for arg in kwargs:
        if arg not in _accepted_args:
            raise AttributeError('Argument not in accepted list of arguments')

    def make_wrapper(func):
        def wrapper(*fargs, **fkwargs):

            times = []

            for n in range(kwargs['n']):

                    # start =  time.time()
                    #
                    # func(*fargs, **fkwargs)
                    #
                    # end = time.time()

                    # times.append(end - start)

                p = DataThread(func, fargs, fkwargs)
                times.append(p)

                if __name__ == '__main__':
                    p.start()
                p.join()

            print('Average run time for {} is {:.2f} seconds'.format(func.__name__, np.mean(times)))

            return func(*fargs, **fkwargs)

            return times
        return wrapper
    return make_wrapper

class Fibonacci():

    def __iter__(self):

        a, b = 0, 1

        while True:
            yield a

            a, b = b, a + b

    def getValueByLength(self, length):

        for num in self:
            if len(str(num)) >= length:
                return num


@timer(n=10)
def testFibonacci(length=100):
    seq = Fibonacci()
    a = seq.getValueByLength(length)

testFibonacci(100)
