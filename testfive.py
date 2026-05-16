import time
class Timer:
    def __init__(self):
      self.elapsed = 0

    def __enter__(self):
      self.start = time.time()
      return self

    # ✅ 补全后面的三个参数，这是固定写法
    def __exit__(self, exc_type, exc_val, exc_tb):
      elapsed = time.time() - self.start
      print(f"耗时: {elapsed:.2f} 秒")
      return False

with Timer() as t:
    time.sleep(0.5)
    print("工作中...")