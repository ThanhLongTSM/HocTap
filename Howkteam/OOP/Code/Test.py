class sieunhan :
    def __init__(self,para_name,para_color):
        self.name = 'Sieu nhan ' + para_name
        self.color = para_color
    def xinchao(self) :
        return 'Xin chao toi ten la: '+ self.name
sieunhan_A = sieunhan('Thanh Long','Red')
print(sieunhan_A.xinchao())
print(sieunhan.xinchao(sieunhan_A))

# print('Ten sieu nhan la: ',sieunhan_A.name)
# print('Mau sac sieu nhan la: ',sieunhan_A.color)

