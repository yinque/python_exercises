# 协程函数是否等待的区别
import asyncio


async def f():
    await asyncio.sleep(1)
    print("f执行")


async def main1():
    print("等待")
    print(".")
    await f()
    print(".")

async def main2():
    print("不等待")
    print(".")
    f()
    print(".")


# asyncio.run(main1())
asyncio.run(main2())

# 总结：协程在没有被等待的情况下不会实际执行。
# 不等待时出现了RuntimeWarning: coroutine 'f' was never awaited
#   f()
# RuntimeWarning: Enable tracemalloc to get the object allocation traceback
# 异常
