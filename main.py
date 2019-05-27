
import time
import numpy as np



def timer(*args, **kwargs):
    _accepted_args = ['n']

    for arg in kwargs:
        if arg not in _accepted_args:
            raise AttributeError('Argument not in accepted list of arguments')

    def make_wrapper(func):
        def wrapper(*fargs, **fkwargs):

            times = []

            for n in range(kwargs['n']):

                start =  time.time()
                    
                func(*fargs, **fkwargs)
                    
                end = time.time()

                times.append(end - start)

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
