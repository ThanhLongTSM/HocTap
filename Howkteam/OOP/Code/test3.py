class sieunhan():
    suc_manh = 50
    def __init__(self,para_name,para_vk,para_color):
        self.name = para_name
        self.vk = para_vk
        self.color = para_color
    @classmethod
    def from_string(cls,s):
        lst = s.split('-')
        new_lst = [st.strip() for st in lst]
        name,vk,color = new_lst
        return cls(name,vk,color)

infor_str = 'Thanh Long-Sung-Black'
sieunhan_a = sieunhan.from_string(infor_str)
print(sieunhan_a.__dict__)