## Async IO in Python

Async IO is a concurrent programming design that has received dedicated support in Python, evolving rapidly from Python 3.4 through 3.7, and probably beyond. You may be thinking with dread, `“Concurrency, parallelism, threading, multiprocessing`. That’s a lot to grasp already. Where does async IO fit in?”

- `Asynchronous IO (async IO)`: a language-agnostic paradigm (model) that has implementations across a host of programming languages.
- `async/await`: two new Python keywords that are used to define coroutines.
- `asyncio`: the Python package that provides a foundation and API for running and managing coroutines.

Coroutines (specialized generator functions) are the heart of async IO in Python. `async IO` to denote the language-agnostic design of asynchronous IO, while `asyncio` refers to the Python package.

### Packages to install
- aiodns: aiodns provides a simple way for doing asynchronous DNS resolutions using pycares.
- aiofiles: aiofiles is an Apache2 licensed library, written in Python, for handling local disk files in asyncio applications.
- aiohttp :
    - Supports both client and server side of HTTP protocol.
    - Supports both client and server Web-Sockets out-of-the-box and avoids Callback Hell.
    - Provides Web-server with middlewares and plugable routing.

### Parallelism
Parallelism consists of performing multiple operations at the same time. Multiprocessing is a means to effect parallelism, and it entails spreading tasks over a computer’s central processing units (CPUs, or cores). Multiprocessing is well-suited for CPU-bound tasks: tightly bound for loops and mathematical computations usually fall into this category.

### Concurrency
Concurrency is a slightly broader term than parallelism. It suggests that multiple tasks have the ability to run in an overlapping manner. (There’s a saying that concurrency does not imply parallelism.)

### Threading
Threading is a concurrent execution model whereby multiple threads take turns executing tasks. One process can contain multiple threads. Python has a complicated relationship with threading thanks to its GIL(Global Interpreter Lock)

Concurrency encompasses both multiprocessing (ideal for CPU-bound tasks) and threading (suited for IO-bound tasks). Multiprocessing is a form of parallelism, with parallelism being a specific type (subset) of concurrency. The Python standard library has offered longstanding support for both of these through its `multiprocessing`, `threading`, and `concurrent.futures` packages. 

The `asyncio` package is billed by the Python documentation as a library to `write concurrent code`. However, `async IO` is not threading, nor is it multiprocessing. It is not built on top of either of these. It has been said in other words that async IO gives a feeling of concurrency despite using a single thread in a single process. Coroutines (a central feature of async IO) can be scheduled concurrently, but they are not inherently concurrent. 

To reiterate, async IO is a style of concurrent programming, but it is not parallelism. It’s more closely aligned with threading than with multiprocessing but is very much distinct from both of these and is a standalone member in concurrency’s bag of tricks.

What does it mean for something to be `asynchronous?` This isn’t a rigorous definition, but for our purposes here, I can think of two properties:
- `Asynchronous routines` are able to “pause” while waiting on their ultimate result and let other routines run in the meantime.
- `Asynchronous code`, through the mechanism above, facilitates concurrent execution. To put it differently, asynchronous code gives the look and feel of concurrency.


### Async IO Explained
Async IO may at first seem `counterintuitive` and `paradoxical`. How does something that facilitates concurrent code use a single thread and a single CPU core? 

### The asyncio Package and async/await
Python’s asyncio package (introduced in Python 3.4) and its two keywords, async and await, serve different purposes but come together to help you declare, build, execute, and manage asynchronous code. 

- The async/await Syntax and Native Coroutines
At the heart of async IO are coroutines. A coroutine is a specialized version of a Python generator function. Let’s start with a baseline definition and then build off of it as you progress here: a coroutine is a function that can suspend its execution before reaching return, and it can indirectly pass control to another coroutine for some time. 

### The Rules of Async IO

A more formal definition of `async, await`, and the coroutine functions that they create are in order. This section is a little dense, but getting a hold of `async/await` is instrumental, so come back to this if you need to:

- The syntax `async def` introduces either a native `coroutine` or an `asynchronous` generator. The expressions 
    - `async with` and 
    - `async for` are also valid 

- The keyword `await` passes function control back to the event loop. (It suspends the execution of the surrounding coroutine.) If Python encounters an 
    - `await f()` expression in the scope of 
    - `g()`, this is how `await` tells the event loop, “Suspend execution of 
    - `g()` until whatever I’m waiting on—the result of 
    - `f()`—is returned. In the meantime, go let something else run.”

```
async def g():
    # Pause here and come back to g() when f() is ready
    r = await f()
    return r
```

