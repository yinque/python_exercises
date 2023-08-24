# 使用事件循环将两个函数并发执行
import asyncio

async def f1():
    while True:
        print("f1执行")
        await asyncio.sleep(2)

async def f2():
    await asyncio.sleep(1)
    while True:
        print("f2执行")
        await asyncio.sleep(2)
async def main():
    task1 = asyncio.create_task(f1())
    task2 = asyncio.create_task(f2())
    await task1
    await task2
    print("done")   # 必须等待两个函数都返回后才回执行，所以永远不会执行

asyncio.run(main())

# 总结
# 可以使用 await asyncio.create_task() 来并发执行异步函数