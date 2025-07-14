import time

def time_tracker(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        duration = (end-start) * 1000 #millisecond
        print(f"Execution Time: {duration} ms")
        return result
    return wrapper

def parameterized_time_tracker(second_value=True):
    def parent_wrapper(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            duration_sec = (end - start)
            if second_value:
                print(f"Execution Time: {duration_sec} sec")
            else:
                duration_ms = duration_sec * 1000
                print(f"Execution Time: {duration_ms} ms")
            return result
        return wrapper
    return parent_wrapper

@time_tracker
def long_time_taking_function():
    print("doing something")
    time.sleep(0.2)

# change params to get value is second or ms
@parameterized_time_tracker(second_value=False)
def add(a, b):
    time.sleep(1)
    return a + b

if __name__ == '__main__':
    long_time_taking_function()
    result = add(1, 2)
    print(result)
