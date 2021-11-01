class SieuNhan:
    suc_manh = 50
    def __init__(self, ten, vu_khi, mau_sac):
        self.ten = ten
        self.vu_khi = vu_khi
        self.mau_sac = mau_sac

    def Xin_chao(self):
        print("xin chao ta la: ", self.ten)
        print("suc manh cua ta: ", self.suc_manh)

sieu_nhan_A = SieuNhan("khoi", "sung", "do")
sieu_nhan_B = SieuNhan("B", "cung", "vang")

sieu_nhan_A.Xin_chao()