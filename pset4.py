#  kế thùa gồm kế thùa thuột tính , kế thùa contructor, kết thừa phương thưc

'''class SieuNhan:
    suc_manh = 50

class SieuNhanKhoi(SieuNhan):
    pass

sieu_nhan_A = SieuNhanKhoi()
print(sieu_nhan_A.suc_manh)'''
# kế thừa constructor
'''class SieuNhan:
    suc_manh = 50
    def __init__(self, ten, vu_khi, mau_sac):
        self.ten = ten
        self.vu_khi = vu_khi
        self.mau_sac = mau_sac
class SieuNhanKhoi(SieuNhan):
    suc_manh = 40

    def __init__(self, ten, vu_khi, mau_sac, robot):
        # dung super() de ke thua toan bo ham __init tren
        super().__init__(ten, vu_khi, mau_sac)
        self.robot = robot

sieu_Nhan_A = SieuNhanKhoi("khoi", "sung","do", "su tu" )
print(sieu_Nhan_A.__dict__)
print(sieu_Nhan_A.suc_manh)'''

#tuple thì không thể thay đoi
# list thi có thể thay đổi, và có thể trung lặp
#dict là 1 cạp key và giá trị

class SieuNhan:
    suc_manh = 50
    def __init__(self, ten, vu_khi, mau_sac):
        self.ten = ten
        self.vu_khi = vu_khi
        self.mau_sac = mau_sac
    def xin_chao(self):
        print("Xin chao ta la: ",self.ten)
    def show_suc_manh(self):
        print("suc manh cua ta la; ", self.suc_manh)
class SieuNhanKhoi(SieuNhan):
    suc_manh = 40
    def __init__(self, ten , vu_khi, mau_sac, robot):
        super().__init__(ten, vu_khi, mau_sac)
        self.robot = robot
    def show_suc_manh(self):
        print("suc manh cua ta la: ", self.suc_manh)
        print("su dung robot: ", self.robot)
sieu_nhan_A = SieuNhan("khoi", "sung", "do")
sieu_nhan_B = SieuNhanKhoi("B", "cung", "vang", "su tu")
sieu_nhan_A.xin_chao()
sieu_nhan_B.xin_chao()
sieu_nhan_A.show_suc_manh()
sieu_nhan_B.show_suc_manh()