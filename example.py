import time
import asyncio
from toasync import async_

@async_
def func(i):
    print('Start {}'.format(i))
    time.sleep(i)
    print('Done {}'.format(i))

c = asyncio.gather(
    func()(1),
    func()(2),
    func()(3)
)
loop = asyncio.get_event_loop()
loop.run_until_complete(c)
