import random

def san_sinh_mang_ngau_nhien(n):
    mang =[]
    for i in range(n):
        so_ngau_nhien = random.randint(0,100)
        mang.append(so_ngau_nhien)
    return mang

def sap_xep_chon(mang):
    n= len(mang)
    for i in range(n-1):
        tiep_tuc = False
        vi_tri_min = i
        for j in range(i+1,n):
            if mang[vi_tri_min]>mang[j]:
                vi_tri_min = j
                tiep_tuc = True
        mang[i],mang[vi_tri_min] = mang[vi_tri_min],mang[i]
        print(i+1,'-',mang)

        if tiep_tuc == False:
            break

def main():
    mang= san_sinh_mang_ngau_nhien(10)
    print('Mang ban dau la:\n')
    sap_xep_chon(mang)
    print('\nMang sau khi sap xep la:' ,mang)
if __name__ == '__main__':
    main()