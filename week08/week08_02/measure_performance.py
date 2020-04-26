import os
import time


class MeasurePerformance:
    def __init__(self):
        self._benchmarks = []

    def __enter__(self):
        self.original_start = time.time()
        self.start = self.original_start

        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        benchmark = '\n'.join(self._benchmarks)
        end = f'\nFinished for: {int(time.time() - self.original_start)}s'
        return benchmark + end

    def get_exceeded_time(self):
        return int(time.time() - self.start)

    def benchmark(self, msg=None, restart=False):
        exceeded_time = self.get_exceeded_time()

        if restart:
            self.start = time.time()

        if msg is None:
            msg = f'Benchmark No.{len(self._benchmarks) + 1}'

        benchmark = f'{msg}: {exceeded_time}s'
        self._benchmarks.append(benchmark)
