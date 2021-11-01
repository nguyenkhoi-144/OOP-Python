class SieuNhan:
    def __init__(self, ten, vu_khi, mau_sac):
        self.ten = ten
        self.vu_khi = vu_khi
        self.mau_sac = mau_sac
    def Xin_chao(self):
        return "Xin chao , toi la: " + self.ten

sieu_nhan_A = SieuNhan("khoi", "sung", "do") # truyen doi so cho ham
print("ten la sieu nhan :", sieu_nhan_A.ten)
print("su dung vu khi: ", sieu_nhan_A.vu_khi)
print("mau sieu nhan la:", sieu_nhan_A.mau_sac)

print(sieu_nhan_A.Xin_chao())
print(SieuNhan.Xin_chao(sieu_nhan_A))