
#! functions in python

#* ---------- Basics ----------
def greet(name):
    """Return a greeting string for name."""
    return f"Hello, {name}!"

print(greet("Anas"))  # Hello, Anas!

#^ ---------- Multiple returns ----------
def div_mod(a, b):
    """Return quotient and remainder as a tuple."""
    return a // b, a % b

q, r = div_mod(11, 3)
print("q,r:", q, r)

#& ---------- Default arguments ----------
def power(x, n=2):
    return x ** n

print(power(3), power(3, 3))       # 9 27

#todo Mutable default gotcha
def add_item_bad(item, lst=[]):
    lst.append(item)
    return lst

print(add_item_bad(1))             # [1]
print(add_item_bad(2))             # [1, 2]  <- unexpected shared list

#? Correct pattern
def add_item(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst

print(add_item(1), add_item(2))    # [1] [2]

#~ ---------- Positional-only, keyword-only (Python 3.8+) ----------
def pos_only(a, b, /, c, *, d=4):
    return a + b + c + d

print(pos_only(1, 2, 3, d=5))      # 11

#* ---------- *args and **kwargs ----------
def func_args(a, *args, **kwargs):
    print("a:", a)
    print("*args:", args)
    print("**kwargs:", kwargs)

func_args(1, 2, 3, x=10, y=20)

#? Example: forwarding arguments
def wrapper(func, *args, **kwargs):
    return func(*args, **kwargs)

print(wrapper(pow, 2, 5))          # 32

#^ ---------- Lambdas, map/filter/reduce ----------
double = lambda x: x * 2
print(double(5))                   # 10

nums = [1, 2, 3, 4, 5]
print(list(map(lambda x: x + 1, nums)))
print(list(filter(lambda x: x % 2 == 0, nums)))

from functools import reduce
print(reduce(lambda a, b: a + b, nums))  # sum: 15

#! ---------- Higher-order functions & closures ----------
def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

times3 = make_multiplier(3)
print(times3(5))                    # 15

# nonlocal usage
def counter():
    count = 0
    def inc():
        nonlocal count
        count += 1
        return count
    return inc

c = counter()
print(c(), c(), c())                # 1 2 3

#& ---------- Decorators ----------
from functools import wraps

def simple_decorator(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print(f"Calling {fn.__name__}")
        result = fn(*args, **kwargs)
        print(f"{fn.__name__} returned {result}")
        return result
    return wrapper

@simple_decorator
def add(a, b):
    return a + b

print(add(2, 3))

#todo Decorator with arguments
def repeat(n):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(n):
                result = fn(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def say(msg):
    print(msg)
    return "done"

print(say("Hi"))

#~ ---------- Recursion ----------
def factorial(n):
    """Simple recursive factorial."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))                 # 120

#? Recursion with memoization (cache)
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(30))                      # fast due to caching

#! ---------- Generators ----------
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for x in countdown(3):
    print("gen:", x)

#& Generator expression vs list comprehension
gen = (x * x for x in range(5))
print(next(gen), list(gen))         # 0 [1,4,9,16] (first consumed then rest)

#* ---------- Annotations & docstrings ----------
def annotated(a: int, b: int) -> int:
    """Add two integers (annotations are optional metadata)."""
    return a + b

print(annotated.__annotations__)    # {'a': <class 'int'>, 'b': <class 'int'>, 'return': <class 'int'>}

#^ ---------- Examples / small exercises ----------
# 1) Write a function that groups words by their first letter (use defaultdict)
from collections import defaultdict
def group_by_first(words):
    d = defaultdict(list)
    for w in words:
        d[w[0]].append(w)
    return dict(d)

print(group_by_first(["apple", "ant", "banana", "berry"]))

# 2) Function that accepts arbitrary keyword options and prints them nicely
def config(**options):
    for k, v in options.items():
        print(f"{k} = {v}")

config(debug=True, retries=3)
