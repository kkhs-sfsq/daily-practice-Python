#2.写一个retry装饰器


# 目标：函数如果报错，自动重试，最多 n 次
# 提示：retry 是带参数的装饰器，比 timer 多一层

def retry(n=1):
    def decorator(func):
        def wrapper():
            for i in range(n):  # ✅ 用循环控制重试次数
                try:
                    result = func()
                    print(f"第{i+1}次尝试成功")
                    return result
                except Exception as e:
                    if i == n - 1:  # 最后一次也失败了
                        raise  # 抛出异常
        return wrapper
    return decorator


@retry(1)
def unstable_function():
    import random
    if random.random() < 0.7:
        raise ValueError("炸了")
    print("成功")

if __name__ == "__main__":
    try:
        result = unstable_function()
    except Exception as e:
        print(f"所有尝试都失败了: {e}")