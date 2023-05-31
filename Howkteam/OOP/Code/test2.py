class sieunhan():
    suc_manh = 50
    so_thu_tu=1
    stt = 1
    def __init__(self,para_name,para_color):
        self.name =para_name
        self.color = para_color
        self.stt = sieunhan.so_thu_tu
        sieunhan.so_thu_tu +=1

sieunhan_A=sieunhan("Thanh Long",'Red')
sieunhan_b=sieunhan("Hoang Thanh Thang Long",'Blue')

print(sieunhan_A.stt)
print(sieunhan_b.stt)
print(sieunhan.so_thu_tu)

