#parallelism consist doing multiple operations at the same time and it implies multi-core CPU's CPU bound taks  image processing, encryption
#
# concurrency does not imply parallelism, we can have concurrency with single core cpu
#
# threading "- concurrent execution model takes turn executing tasks
# multiple threads run inside a single process
# note that threads do not run in parallel and execution does not happen simultaneosly and exection does not happen in multiple physical cores
# this is good for IO bound tasks which imply some waiting time like working with DB or external websites, configuring networking device or working with files  ...
# python program should wait for these external resources to be ready
# downside is memory safety and race conditions
# all child threads of a parent process operate in the same shared memory space
# standard threading module implements threading in python
## single threaded ,



## RACE CONDITION

#A race condition or race hazard is the condition of an electronics, software, or other system where the system's substantive behavior is dependent on the sequence or timing of other uncontrollable events. It becomes a bug when one or more of the possible behaviors is undesirable. Wikipedia

# SHARED MEMORY SAFETY
#The issued of sharing data between threads are mostly due to the consequences of modifying data. If the data we share is read-only data, there will be no problem, because the data read by one thread is unaffected by whether or not another thread is reading the same data.
#A running program may consist of multiple subprograms that maintain their own independent control flow and that are allowed to run concurrently. These subprograms are defined as threads. Communication between threads is via updates and access to memory appearing in the same address space.
#Thread safety is a computer programming concept applicable to multi-threaded code. Thread-safe code only manipulates shared data structures in a manner that ensures that all threads behave properly and fulfill their design specifications without unintended interaction.
#Thread safety implies multiple threads can write/read data in same object without memory inconsistency errors. In highly multi threaded program, a thread safe program does not cause side effects to shared data.4 Nov 2008

## PROCESS VS THREAD
#Process means a program is in execution, whereas thread means a segment of a process. A Process is not Lightweight, whereas Threads are Lightweight. A Process takes more time to terminate, and the thread takes less time to terminate. Process takes more time for creation, whereas Thread takes less time for creation

import asyncio
import time
## synchronous code

def sync_f():
    print('one ', end='') # new line after string one
    time.sleep(1)
    print('two ', end ='')

## async code # define a corouting using the async key-word
async def async_f():
    print('one ', end='')
    await asyncio.sleep(1)  ## this is blocking io asyncio.sleep is a co-routing, we cannot call a simple function after await ,
    print('two ' , end='')   # we have to call asyncio.function() only
                            # task will be suspended after await

#

async def main(): # top level co-routing
      #tasks = [async_f(),async_f(),asyncio]            # three awaitable objects coroutine, tasks and futures.
      tasks = [async_f() for _ in range(3)]    # future is a low level object that acts as a placeholder for data that hasn't been calculated or fetched yet
      # this is list comprehension            # its used mainly by framework and library developers , starting with python 3.7 you dont need to create future object
      # above two task lines are equivalent        # async.io task is used to schedule coroutines concurrently, its an object that wraps co-routines providing methods to controlling
      await asyncio.gather(*tasks)             # execution and query its status
                                              # a taskk maybe created as asyncio.create_task() or asyncio.gather() methods
                                              # create a list of task which consist of 3 cores to our co-routine called async_f

#### top level co-routing is "async def main():, tasks = [async_f() for _ in range(3)], await asyncio.gather(*tasks)
# end transpoint of any asyncio program is .asyncio.run and co-routine as argment
start = time.time()
asyncio.run(main())
end = time.time()
print(f'execution time asycn {end - start}')

## calling asyncio.run creates an event loop and the co-routine will run on it , event loop is core of any asyncio application
# its the one that runs async tasks and performs network io operations or runs sub-processes.

start = time.time()
print('\n')
for  _ in range(3):
    sync_f()
end = time.time()
print(f'execution time sycn {end - start}')

#async def f():
 #   pass

#async def g():
#    await f()  ## await calls f and suspends G,
                # this will wait for F to complete or return
                # async function passes
                # await passes function control back to the event loop
                # await can only be called in the body of async
                # it suspends the execution of surrounding co-routine i.e. g






################# FINAL CODE #########################
import asyncio
import time


def sync_f():
    print('one', end=' ')
    time.sleep(
        1)  # I'm simulating an expensive task like working with an external resource. I want it to wait for 1 sec
    print('two', end=' ')


# ASYNCHRONOUS
async def async_f():
    print('one', end=' ')
    await asyncio.sleep(1)

    print('two', end=' ')


async def main():
    # Note that there are 3 awaitable objects: coroutines, tasks and futures.
    tasks = [async_f() for _ in range(3)]

    # we schedule the coroutines to run asap by gathering the tasks like this:
    await asyncio.gather(*tasks)


s = time.time()

# The entrance point of any asyncio program is asyncio.run(main()), where main() is a top-level coroutine.
# asyncio.run() was introduced in Python 3.7, and calling it creates an event loop
# and runs a coroutine on it for you. run() creates the event loop.
asyncio.run(main())  # prints out: one one one two two two and takes 1 second
print(f'Execution time (ASYNC):{time.time() - s}')

print('\n')

s = time.time()
for _ in range(3):
    sync_f()  # prints out: one two one two one two and takes 3 seconds
print(f'Execution time (SYNC):{time.time() - s}')
########################################################################
