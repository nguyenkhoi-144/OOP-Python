'''class SieuNhan:
    suc_manh = 50
    def __init__(self, ten, vu_khi, mau_sac):
        self.ten = ten
        self.vu_khi = vu_khi
        self.mau_sac = mau_sac
    @classmethod
    def from_string(cls, s):
        lst = s.split("-")
        new_lst = [st.strip() for st in lst]
        ten, vu_khi, mau_sac =  new_lst
        return cls(ten, vu_khi, mau_sac)
infor_str = "Sieu nhan do - Kiem - do"
sieu_nhan_A = SieuNhan.from_string(infor_str)
print(sieu_nhan_A.__dict__)'''

#class method thi sua nguyen ca 1 ham
#trong ham classmethod co argv = cls giong nhu self trong __init__
#ham def trong class method viet giong trong __init thay self thanh cls
class SieuNhan:
    suc_manh = 50
    def __init__(self, para_ten, para_vu_khi, para_mau_sac):
        self.ten = para_ten
        self.vu_khi = para_vu_khi
        self.mau_sac = para_mau_sac
    @classmethod
    def cap_nhat_suc_manh(cls, smanh):
        cls.suc_manh = smanh
sieu_nhan_A = SieuNhan("Sieu nhan do", "Kiem", "Do")

print(SieuNhan.suc_manh)
print(sieu_nhan_A.suc_manh)

sieu_nhan_A.cap_nhat_suc_manh(40)

print(SieuNhan.suc_manh)
print(sieu_nhan_A.suc_manh)
# sua nguyen 1 ham dung class method