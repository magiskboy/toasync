# toasync


[![GithubCI](https://github.com/magiskboy/toasync/workflows/ci/badge.svg)](https://github.com/magiskboy/toasync/actions?query=workflow%3ACI)
[![PyPI version](https://badge.fury.io/py/toasync.svg)](https://badge.fury.io/py/toasync)


Convert sync function to async function and start at same time


```python
from time import sleep, time
import asyncio
from toasync import async_


@async_
def func(name, i=1):
    print('Start function {}'.format(name))
    sleep(1)
    print('Done function {}'.format(name))


if __name__ == '__main__':
    coroutine = asyncio.gather(
        func()('1'),
        func()('2'),
        func()('3'),
    )
    start_time = time()
    asyncio.get_event_loop().run_until_complete(coroutine)
    print('Process take {} sencond'.format(time-start_time))
```

then

```bash
Start function 1
Start function 2
Start function 3
Done function 2
Done function 1
Done function 3
Process take 1.007418155670166 sencond
```


If run function as synchronous, you can call `delay` method

```python
from time import sleep
from toasync import async_


@async_
def func(name, i=1):
    print('Start function {}'.format(name))
    sleep(1)
    print('Done function {}'.format(name))


if __name__ == '__main__':
    func().delay('1')
    func().delay('2')
    func().delay('3')
```

then

```bash
Start function 1
Done function 1
Start function 2
Done function 2
Start function 3
Done function 3
```
