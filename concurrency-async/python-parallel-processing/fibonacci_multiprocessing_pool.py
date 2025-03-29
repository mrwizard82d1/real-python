"""
Create a pool of processes to exercise data parallelism.

This particular implementation, including a Timer, does not work as
I intend. This issue results from, for example, the result of `fib(10)`
being calculated by each and every process in the `multiprocessing.Pool`.

I think the solution, as suggested by generative AI, is to have each
process query a shared result cache before beginning the recursive
calculation of `fib(n)`.  Here is the text from Generative AI:

    Memoization, as implemented with decorators like
    functools.lru_cache, does not inherently work across multiple
    processes in Python. Each process has its own memory space,
    including its own cache. Therefore, if multiple processes call
    the same memoized function, each process will compute the result
    independently and store it in its own separate cache. To share
    the results of a memoized function across multiple processes, you
    can use shared memory or inter-process communication mechanisms.
    Here's how:

    • Shared Memory:
        • Utilize multiprocessing.Manager or
          multiprocessing.shared_memory to create a shared memory
          space accessible by all processes.
        • Store the cache (e.g., a dictionary) in this shared memory
          space.
        • Wrap the memoized function to access and update the shared
          cache.
        • Synchronization mechanisms (e.g., locks) might be necessary
          to prevent race conditions when multiple processes access
          the cache simultaneously.

    • Inter-Process Communication (IPC):
        • Use multiprocessing.Queue or other IPC mechanisms to
          communicate between processes.
        • Designate one process as the "cache manager."
        • When a process needs the result of a memoized function, it
          sends a request to the cache manager.
        • The cache manager checks its cache and either returns the
          result or computes it and updates the cache.

    It's important to consider the overhead of communication and
    synchronization when implementing shared memoization. For simple
    cases, the overhead might outweigh the benefits of caching.
    However, for computationally expensive functions with repeated
    calls across multiple processes, shared memoization can
    significantly improve performance.

    Generative AI is experimental.
"""

import multiprocessing

from codetiming import Timer


def fib(n):
    with Timer(name='fib', text=f'fib({n}) elapsed time: {{:.3f}}'):
        return n if n < 2 else fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(fib, range(40))
        for i, result in enumerate(results):
            print(f'fib({i})={result}')
