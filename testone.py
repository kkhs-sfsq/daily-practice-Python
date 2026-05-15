import time

def timer(func):
    def wrapper():
        start = time.time()
        result = func()
        print(time.time() - start)
        return result
    return wrapper
@timer
def slow_function():
    time.sleep(1.5)
    print("done")

if __name__ == "__main__":
    slow_function()
