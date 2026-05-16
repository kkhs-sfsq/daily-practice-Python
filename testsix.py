import time
from contextlib import contextmanager

@contextmanager
def timer():
    start = time.time()
    yield
    elapsed = time.time() - start
    print(f"耗时: {elapsed:.2f} 秒")
# 测试代码
with timer():
    time.sleep(0.5)
    print("工作中...")
