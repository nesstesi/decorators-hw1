import time


def time_func(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__ + ' ' + 'took' + ' ' + str((end - start)*1000) + 'ms')
        return result
    return wrapper

@time_func
def print_hello():
    print('hello\n'*5)


time_func(print_hello())