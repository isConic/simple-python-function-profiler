import unittest
import profiler
class TestFunctionality(unittest.TestCase):


    def test_one_for_loop(self):
        fun_profiler = profiler.PerformanceProfiler()

        @fun_profiler.time_function
        def pass_n(n = 100):
            for _ in range(n):
                pass

        pass_n(n = 10000)
        pass_n(n = 10000)
        pass_n(n = 20000)
        pass_n(n = 30000)
        pass_n(n = 10000)

        return fun_profiler

    def test_std(self):
        prof = self.test_one_for_loop()
        _ = prof.std()

    def test_mean(self):
        prof = self.test_one_for_loop()
        _ = prof.mean()

    def test_max(self):
        prof = self.test_one_for_loop()
        _ = prof.max()

    def test_min(self):
        prof = self.test_one_for_loop()
        _ = prof.min()
