import asyncio

@asyncio.coroutine
def hello():
    print("Hello world!")
    # 异步调用asyncio.sleep(1):
    r = yield from asyncio.sleep(1)
    print("Hello again!")

# 获取EventLoop:
loop = asyncio.get_event_loop()
# 执行coroutine
loop.run_until_complete(hello())
loop.close()

def hello1():
    # 异步调用asyncio.sleep(1):
    # print('hello1')
    for i in range(0,10):
        yield i;
    return 'hello1'
def hello3():
    # 异步调用asyncio.sleep(1):
    yield 'asd1'
    yield 'asd2'
    yield 'asd3'
    return 'hello3';
def hello2():
    #yield 返回的是一个生成器generator 需要自己去next执行才可以拿到值
    # yield from会把生成器 generator 里面执行完然后 如果要把yield from的值返回的话 需要在yield from对应的方法里面写return
    r1 =yield from hello1();
    print(r1)
    r2 =yield from hello1();
    print(r2)
    r3 =yield from hello3();
    print(r3)
    r4 =yield from hello3();
    print(r4)
print(list(hello2()))
