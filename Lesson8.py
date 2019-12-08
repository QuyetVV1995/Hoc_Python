'''
# Dictionary
user = {'name' : 'Vu Quyet', 'age': 24, 'gt': 'nam'}
for i in user:
    print(user[i])
    
if  'agel' not in user.keys():
    print('khong co tu khoa')
else:
    print('co tu khoa')

# input trong python
age = int(input('ban bao nhieu tuoi?'))
if age < 18:
    print('chua den tuoi di tu')
else:
    print('Da den tuoi di tu')
'''
# Ham trong python
def tenHam(thamso1, thamso2):
    print(thamso1 )
    print(thamso2)
    return thamso1+ ' ' + thamso2;

#tenHam('Vu', 'Quyet')
#print(tenHam('Vu', 'Quyet'))

def tiemBanh(tenTiemBanh, *danhsachbanh):
    print("TiemBanh " + tenTiemBanh)
    for banh in danhsachbanh:
        print('-Banh' + banh+'\n')

#tiemBanh("QuyetVV",'chung', 'ran','goi')
