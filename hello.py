# Hello world
print('Hello world')

# Khai bao bien
var = 1
var2 = "Quyet";
var3 = 2.3

print(var)

# Danh sach trong python
li = ['111', 2, 'Vu', 2.34]
print(li)
# Lay phan tu trong danh sach
print(li[2])
# Them phan tu vao cuoi danh sach
li.append('li.append')
# Chen phan tu vao vi tri
li.insert(1,'li.insert')
# Xoa phan tu trong danh sach
del li[3]
print(li)

#vong lap
for i in range(4):
    print(li[i])

array = [1,2,3,4,5,6,7,8,9,10]
array2 = array[3:6]
for i in array[3:6]:
    print(i)
    print(array2)

# cau truc if else
for i in array:
    if i % 2 == 0:
        print(i)
