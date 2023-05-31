#Special Method
## Magic Method & Dunder Method

class sn:
    def __init__(self,name,weapon,color):
        self.name = name
        self.weapon=weapon
        self.color = color
    def __str__(self):
        return "Day la {}, su dung vk {}, co mau {}".format(self.name,self.weapon,self.color)
    def __repr__(self):
        return 'Day la:  {}\nvk la: {}\nMau:{}\n'.format(self.name,self.weapon,self.color)

ThanhLong = sn('Long','Sung',"Blur")
print('%r'%ThanhLong)