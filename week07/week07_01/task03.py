from time import time, sleep


class Measure_performance(object):

    def __init__(self):
        self.benchmark_num = 0
        pass

    def __enter__(self):
        self.start = time()
        self.start_all = time()
        return self

    def __exit__(self, type, value, traceback):
        self.end = time()
        total = self.end - self.start_all
        print("Ending at {0} ".format(total))

    def benchmark(self, txt=None, restart=False):
        self.benchmark_num += 1
        if txt is not None:
            print("{0}:{1}".format(txt, time() - self.start))
        else:
            print("benchmark num {0}:{1}".format(self.benchmark_num, time() - self.start))
        if restart is True:
            self.start = time()


with Measure_performance() as mp:
    sleep(1)
    mp.benchmark("1st step")

    sleep(2)
    mp.benchmark('2nd step', restart=True)

    sleep(3)
    mp.benchmark()
