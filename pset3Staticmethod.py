# static method thi k can argv trong ham dep
# muon bỏ chữ saticmethod thì thêm argv
class SieuNhan:
    def __init__(self, ten, vu_khi, mau_sac):
        self.ten = ten
        self.vu_khi = vu_khi
        self.mau_sac = mau_sac
    @staticmethod
    def sieu_nhan_bien_hinh():
        print("1,2,3 sieu nhan bien hinh")
sieu_nhan_A = SieuNhan("khoi", "sung", "do")
sieu_nhan_A.sieu_nhan_bien_hinh()