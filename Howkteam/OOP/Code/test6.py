# class Kter:
#     def __init__(self,ho,ten):
#         self.ho= ho
#         self.ten = ten
#         self.email = ho + '-' + ten + '@gmail.com'
#     @property
#     def ho_va_ten(self):
#         return 'Ho va ten: {} {}'.format(self.ho,self.ten)
#     @property
#     def emails(self ):
#         return self.ho + '-' + self.ten + '@gmail.com'
# Kter_A = Kter("Le",'Long')
#
# Kter_A.ho = 'nguyen'
# Kter_A.ten = 'Hoang'
#
# print(Kter_A.ho_va_ten)
# print(Kter_A.emails)



#Setter and Deleter
class Kter:
    def __init__(self,ho,ten):
        self.ho= ho
        self.ten = ten
    @property
    def ho_va_ten(self):
        return 'Ho va ten: {} {}'.format(self.ho,self.ten)
    @property
    def email(self ):
        return self.ho + '-' + self.ten + '@gmail.com'
    @ho_va_ten.setter
    def ho_va_ten(self,ten_moi):
        ho_moi,ten_moi = ten_moi.split(' ')
        self.ho = ho_moi
        self.ten = ten_moi
    @ho_va_ten.deleter
    def ho_va_ten(self):
        self.ho = None
        self.ten = None
        print('Da xoa')
Kter_A = Kter("Le",'Long')

Kter_A.ho = 'nguyen'
Kter_A.ten = 'Hoang'

print(Kter_A.ho_va_ten)
print(Kter_A.email)

del Kter_A.ho_va_ten
print(Kter_A.ho_va_ten)