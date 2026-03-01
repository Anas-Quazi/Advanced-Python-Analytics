#! python basics

#* ---------- printing ----------
print("Hello, world")              
print('Single quotes too')
print(123, 4.56, True)            #~ multiple arguments
print("line1\nline2")             #^ escape sequence
name = "Anas"
print(f"Hi {name}")               #* f‑string (formatted)

#* ---------- data types ----------
i = 10                            
f = 3.14                          
s = "Razvi"                       
b1 = True                         
b2 = False
none_val = None                   #! NoneType

lst = [1, 2, 3]                   # list
tup = (4, 5, 6)                   # tuple
st = {"a", "b"}                   # set
dct = {"x": 1, "y": 2}            # dict

print(type(i), type(f), type(s), type(b1), type(none_val))

#* ---------- operators ----------
#^ arithmetic
print("add", 5 + 2)
print("sub", 5 - 2)
print("mul", 5 * 2)
print("div", 5 / 2)              #& float result
print("floordiv", 5 // 2)        #& integer division
print("mod", 5 % 2)
print("pow", 5 ** 2)

#^ comparison / relational
print(5 > 2, 5 < 2, 5 == 2, 5 != 2, 5 >= 2, 5 <= 2)

#^ logical
print(True and False, True or False, not True)

#? bitwise
print(5 & 3, 5 | 3, 5 ^ 3, ~5, 5 << 1, 5 >> 1)

#? membership
print(3 in [1,2,3], 'z' not in "xyz")

#? identity
a = [1,2,3]
b = a
c = [1,2,3]
print(a is b, a is c)            #~ same object vs equal value


#* ---------- conditional statements ----------
x = 7
if x < 0:
    print("negative")
elif x == 0:
    print("zero")
else:
    print("positive")

#& inline if
message = "even" if x % 2 == 0 else "odd"
print(message)

#* ---------- loops ----------

#^ for‑loop over a sequence
for item in ["apple", "banana", "cherry"]:
    print(item)

#^ for with range
for n in range(5):               # 0..4
    print(n, end=" ")
print()

#^ while‑loop
count = 0
while count < 3:
    print("count is", count)
    count += 1

#? break / continue
for n in range(10):
    if n == 5:
        break                    #~ exit loop
    if n % 2 == 0:
        continue                 #~ skip to next iteration
    print("odd before break:", n)

#* ---------- type casting ----------
num_str = "123"
num_int = int(num_str)
num_float = float(num_str)
print(num_int, num_float)

print(str(456), bool(0), bool(""), list((1,2)), tuple([3,4]))

#* ---------- input (commented out) ----------
name = input("Enter your name: ")
age = int(input("your age: "))
print("Hello", name, "age", age)

#* ---------- simple functions ----------
def add(a, b):
    return a + b

print("add func:", add(3, 4))

#* ---------- comments ----------
# a single‑line comment starts with #
"""
a multi-line (doc)string uses triple quotes
and can span multiple lines.
"""


#* ----------- data structures -------

#^ list
lst = [1, 2, 3]
lst.append(4)           #~ [1, 2, 3, 4]
lst.insert(0, 0)        #? [0, 1, 2, 3, 4]
lst.extend([5, 6])      #& [0,1,2,3,4,5,6]
lst.remove(3)           #todo remove first occurrence
lst.pop()               #! pop last item, returns 6
lst.pop(0)              #^ pop at index 0, returns 0
lst.index(2)            #~ 1 (first index of value)
lst.count(2)            #? how many 2’s
lst.sort()              #& in‑place sort
lst.reverse()           #todo in‑place reverse
lst.clear()             #! becomes []

#^ tuple
t = (1, 2, 3)
t[0]                    # 1
len(t)                  # 3
(4, 5) + t              #? concatenation → (4,5,1,2,3)

#^ set
s = {1, 2, 3}
s.add(4)                #~ {1,2,3,4}
s.update([5,6])         #? union with iterable
s.remove(2)             #& KeyError if missing
s.discard(10)           #todo no error if missing
s.pop()                 #! remove arbitrary element
s.clear()               #~ empty set
s.union({3,7})          #? new set {1,3,4,5,6,7}
s.intersection({3,7})   #& {3}
s.difference({1,5})     #todo {2,3,4,6}
s.symmetric_difference({3,7})  #* {1,2,4,5,6,7}

#^ dictionary
d = {"x": 1, "y": 2}
d["z"] = 3              #~ add or update
val = d.get("x")        #? get val (1)
d.get("missing", 0)     #& default if not present
d.keys()                #todo dict_keys(['x','y','z'])
d.values()              #! dict_values([1,2,3])
d.items()               #* dict_items([('x',1),...])
d.pop("y")              #! remove key, return value
d.popitem()             #todo remove last inserted 
d.update({"a": 10})     #& merge another dict
"d" in d                #? membership test on keys
for k,v in d.items():   #~ iteration
    print(k, v)

#^ string
s = "Hello World"
s.lower()               #~ "hello world"
s.upper()               #? "HELLO WORLD"
s.capitalize()          #& "Hello world"
s.title()               #! "Hello World"
s.strip()               #todo remove whitespace
s.split()               #* ["Hello","World"]
" ".join(["a","b"])     #^ "a b"
s.replace("World","You")
s.startswith("He"), s.endswith("ld")
s.find("o")             #& 4 (index) or -1
len(s)                  #todo 11


