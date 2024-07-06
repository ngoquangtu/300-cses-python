# Kiểu dữ liệu số
a = 5
b = 3.14
c = 1 + 2j

print(abs(-5))       # 5
print(round(3.1415, 2))  # 3.14
print(pow(2, 3))     # 8

# Kiểu dữ liệu chuỗi
s = "Hello, World!"
print(len(s))        # 13
print(s.upper())     # "HELLO, WORLD!"
print(s.lower())     # "hello, world!"
print(s.split(", ")) # ['Hello', 'World!']
print(" ".join(['Hello', 'World!']))  # "Hello World!"

# Kiểu dữ liệu danh sách
lst = [1, 2, 3]
lst.append(4)
print(lst)           # [1, 2, 3, 4]
lst.remove(2)
print(lst)           # [1, 3, 4]
print(lst.pop(1))    # 3
print(lst)           # [1, 4]

# Kiểu dữ liệu bộ
tup = (1, 2, 3)
print(len(tup))      # 3
print(tup.index(2))  # 1

# Kiểu dữ liệu tập hợp
st = {1, 2, 3}
st.add(4)
print(st)            # {1, 2, 3, 4}
st.remove(2)
print(st)            # {1, 3, 4}

# Kiểu dữ liệu từ điển
d = {"key1": "value1", "key2": "value2"}
print(d.keys())      # dict_keys(['key1', 'key2'])
print(d.values())    # dict_values(['value1', 'value2'])
print(d.items())     # dict_items([('key1', 'value1'), ('key2', 'value2')])
