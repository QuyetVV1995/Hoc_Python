#from thuvien import ham2 as Func2;

#Func2()

class sinhVien:
    def __init__(sv, ma, ten):  # tao doi tuong sv co 2 thuoc tinh: ma, ten
        sv.msv = ma;
        sv.name = ten;
    def inthongtin(sv):
        print('Ma sinh vien: ' +sv.msv);
        print('Ten sinh vien: '+sv.name);

sinhvienA = sinhVien('2019','Quyet');
sinhvienA.inthongtin();
