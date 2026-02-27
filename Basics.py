#! full‑python‑basics.py

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
a multi‑line (doc)string uses triple quotes
and can span multiple lines.
"""
