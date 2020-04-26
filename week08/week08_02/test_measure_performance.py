import os
import unittest
import time
from unittest.mock import patch, Mock
from measure_performance import MeasurePerformance


class MeasurePerformanceTests(unittest.TestCase):
    @patch('measure_performance.time', autospec=True)
    def test_benchmark_measures_correct_time_from_init_to_first_call(self, time_mock):
        time_mock.sleep.return_value = time.time() + 1
        with MeasurePerformance() as meter:
            time.sleep()

            self.assertEqual(meter.get_exceeded_time(), 1)

    @patch('measure_performance.time', autospec=True)
    def test_benchmark_appends_benchmark_using_passed_message(self, time_mock):
        time_mock.sleep.return_value = time.time() + 1
        with MeasurePerformance() as meter:
            time.sleep()

            meter.benchmark('test')

            expected = ['test: 1s']

            self.assertEqual(meter._benchmarks, expected)

    @patch('measure_performance.time', autospec=True)
    def test_benchmark_appends_benchmark_with_no_message_using_benchmarks_count(self, time_mock):
        time_mock.sleep.return_value = time.time() + 1
        with MeasurePerformance() as meter:
            time.sleep()

            meter.benchmark('test')

            time.sleep()
            meter.benchmark()

            expected = ['test: 1s', 'Benchmark No.2: 2s']

            self.assertEqual(meter._benchmarks, expected)

    @patch('measure_performance.time', autospec=True)
    def test_benchmark_does_not_restart_the_start_of_measure_performance_if_not_passed(self, time_mock):
        time_mock.sleep.return_value = time.time() + 1
        with MeasurePerformance() as meter:
            original_start = meter.original_start

            time.sleep()
            meter.benchmark('test')

            self.assertEqual(meter.original_start, original_start)

    @patch('measure_performance.time', autospec=True)
    def test_benchmark_restarts_the_start_of_the_measure_performance_if_passed(self, time_mock):
        time_mock.sleep.return_value = time.time() + 1
        with MeasurePerformance() as meter:
            original_start = meter.original_start

            time.sleep()
            meter.benchmark('test', restart=True)

            self.assertEqual(meter.original_start, original_start)

    @patch('measure_performance.time', autospec=True)
    def test_benchmark_preserves_correct_execution_times_if_not_restarted(self, time_mock):
        msg = 'test'
        time_mock.sleep.return_value = time.time() + 1
        with MeasurePerformance() as meter:
            time.sleep()

            meter.benchmark(msg)

            time.sleep()
            meter.benchmark(msg, restart=False)

            expected = ['test: 1s', 'test: 2s']

            self.assertEqual(meter._benchmarks, expected)

    @patch('measure_performance.time', autospec=True)
    def test_benchmark_preserves_correct_execution_times_if_restarted(self, time_mock):
        msg = 'test'
        time_mock.sleep.return_value = time.time() + 1
        with MeasurePerformance() as meter:
            time.sleep()

            meter.benchmark(msg, restart=True)

            time.sleep()
            meter.benchmark(msg)

            expected = ['test: 1s', 'test: 1s']

            self.assertEqual(meter._benchmarks, expected)


if __name__ == '__main__':
    unittest.main()
