#getter
'''class Thongtin:
    def __init__(self, ho, ten):
        self.ho = ho
        self.ten = ten
    @property
    def ho_va_ten(self):
        return "{} {}". format(self.ho, self.ten)
    @property
    def emails(self):
        return self.ho + "-" + self.ten +"@gmail.com"

nguoi_1 = Thongtin("nguyen", "khoi")
nguoi_1.ho = "tran"
nguoi_1.ten = "an"

print(nguoi_1.ho)
print(nguoi_1.ten)
print(nguoi_1.emails)
print(nguoi_1.ho_va_ten)'''

#setter


class Thongtin:
    def __init__(self, ho, ten):
        self.ho = ho
        self.ten = ten
    @property
    def ho_va_ten(self):
        return "{} {}". format(self.ho, self.ten)
    @property
    def emails(self):
        return self.ho + "-" + self.ten +"@gmail.com"
    @ho_va_ten.setter
    def ho_va_ten(self, ten_moi):
        ho_moi, ten_moi = ten_moi.split(" ")
        self.ho = ho_moi
        self.ten = ten_moi
    @ho_va_ten.deleter
    def ho_va_ten(self):
        self.ten = None
        self.ho = None
        print("da xoa")

nguoi_1 = Thongtin("nguyen", "khoi")
nguoi_1.ho_va_ten = "tran an"
print(nguoi_1.ho_va_ten)
del nguoi_1.ho_va_ten