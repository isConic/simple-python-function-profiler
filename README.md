# Simple Function Profiler

With a limited amount of time to do performance profiling and instead of researching and
 using a ready made tool, this utility was written to meet a few very basic needs. 

- passive profiling, rather than designing experiments, collect data as functions are being used.  
- Decorator style tags to mark a function as worth profiling
- Keeping a history or record of the time it takes to run a function
- options for simple reductions along runtime history like `mean`, `std`, `sum`, `max`, `min`
- options to `load` and `save` history. 


# Usage

The history of a function is captured in an instance of the `PerformanceProfiler` class.  

```py
import profiler

fun_profiler = profiler.PerformanceProfiler()
```

To profile a function, use the `time_function` wrapper that belongs to the profiler, 

```py

@fun_profiler.time_function
def count_to_ten_thousand():
    for x in range(10000):
        pass

@fun_profiler.time_function
def count_to_on_million():
    for x in range(1000000):
        pass
```

Run the function a few times. Below we run each function 10 times. Every time a function is run
the profiler keeps record of the time it took to run each function

```
for x in range(10):
    count_to_ten_thousand()
    count_to_on_million()
```

# History

To print a datastructure containing the execution time of each function, you can access the `history` attribute of the fun profiler. 
```python

fun_profiler.history

>> {    'count_to_on_million': [0.026912450790405273,
                                0.026929140090942383,
                                0.025929927825927734,
                                0.028921127319335938,
                                0.027927398681640625,
                                0.02695941925048828,
                                0.02589893341064453,
                                0.02596569061279297,
                                0.028912067413330078,
                                0.028897762298583984],
        'count_to_ten_thousand': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]}


```

# Aggregate Stats

A few aggregate stats options are provided to glimpse brief summaries of the dataset. 


**mean**  
```python
fun_profiler.mean()
>>  {'count_to_on_million': 0.026030373573303223,
     'count_to_ten_thousand': 0.0001995086669921875}
```

**standard deviation**
```python
fun_profiler.std()
>> {'count_to_on_million': 0.0013784160946390387,
    'count_to_ten_thousand': 0.0003990173482302267}
```

**min**
```python
fun_profiler.min()
>> {'count_to_on_million': 0.02489495277404785,
    'count_to_ten_thousand': 0.0}
```

**max**
```python
fun_profiler.max()
>> {'count_to_on_million': 0.026927709579467773,
 'count_to_ten_thousand': 0.000997781753540039}
```

# IO

**pandas**
```python
fun_profiler.to_dataframe()

>>   durrations function
0    0.000000   pass_n
1    0.000997   pass_n
2    0.000000   pass_n
3    0.001081   pass_n
4    0.000000   pass_n

```

**json save**

```python

fun_profiler.to_json("function_stats.json") 

```

**json load**
```python

new_profiler = PerformanceProfiler()
new_profiler.from_json("function_stats.json") 

```
