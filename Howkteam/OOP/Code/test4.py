class sieunhan:
    power = 50
    def __init__(self,name,weapon,color):
        self.name = name
        self.weapon = weapon
        self.color = color
    def xinchao(self):
        print("Xin chao toi la ",self.name)
    def showsucmanh(self):
        print('Suc manh cua toi la: ',self.power)
class sieunhangao(sieunhan):
    power = 40
    def __init__(self,name,weapon,color,mecha):
        super().__init__(name,weapon,color)
        self.mecha = mecha
    def xinchao(self):
        print('Xin chao toi la: ',self.name)
    def showsucmanh(self):
        print('Suc manh cua toi la: ',self.power)
    def showmecha(self):
        print("Than thu cua toi la: ",self.mecha)
ThanhLong = sieunhangao("Thanh Long",'sung','black','Khung Long')
ThanhHai = sieunhan("Thanh Hai",'dao','Yellow')

ThanhLong.xinchao()
ThanhLong.showsucmanh()
ThanhLong.showmecha()
ThanhHai.xinchao()
ThanhHai.showsucmanh()


