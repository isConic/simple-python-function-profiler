from time import time
import numpy as np
import json
import pandas
import matplotlib.pyplot as plt


class PerformanceProfiler:
    def __init__(self):
        self.history = {}

    def time_function(self, function):
        def _wrapper(*args, **kwargs):

            t1 = time()
            ans = function(*args, **kwargs)
            t2 = time()

            fn_name = function.__name__

            if fn_name not in self.history.keys():
                self.history[fn_name] = []

            self.history[fn_name].append(t2 - t1)
            return ans

        return _wrapper

    def __how_to_merge_array(self, a, b):
        return a + b

    def __merge_array_dict(self, a, b, merge_fun = __how_to_merge_array):
        shared_keys      = set(a.keys()).intersection(b.keys())
        a_exclusive_keys = set(a.keys()) - shared_keys
        b_exclusive_keys = set(b.keys()) - shared_keys

        a_side = {key:a[key] for key in a_exclusive_keys}
        b_side = {key:b[key] for key in b_exclusive_keys}
        shared_side = {key: merge_fun(a[key], b[key]) for key in shared_keys}

        return {**a_side, **b_side, **shared_side}

    def apply(self, function):
        return {k: function(self.history[k]) for k in self.history.keys()}

    def mean(self):
        return self.apply(np.mean)

    def std(self):
        return self.apply(np.std)

    def max(self):
        return  self.apply(np.max)

    def min(self):
        return self.apply(np.min)

    def to_dataframe(self):
        log = self.history

        durrations = []
        function_names = []
        
        for function_name in log.keys():
            for value in log[function_name]:
                durrations.append(value)
                function_names.append(function_name)

        return pandas.DataFrame(dict(durrations = durrations,
                                     function = function_name))
    def to_json(self, file_name):
        with open(file_name, 'w') as fp:
            json.dump(self.history, fp)

    def from_json(self, file_name):
        with open(file_name, 'r') as fp:
            self.history = self.merge_array_dict(json.load(fp), self.history)

    def plot(self):
        for key in self.history.keys():
            values = self.history[key]
            plt.figure(figsize = (10,2))
            plt.hist(values, bins = int(values)//4)
            plt.title(key)
        plt.show()


