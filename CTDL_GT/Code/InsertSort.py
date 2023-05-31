import random
def san_sinh_so_ngau_nhien(n):
    mang =[]
    for i in range (n)  :
        so_ngau_nhien = random.randint(0,100)
        mang.append(so_ngau_nhien)
    return mang

def sap_xep_chen(mang):
    n = len(mang)

    for i in range(1,n):
        temp = mang[i]
        j = i
        while j > 0 and mang[j-1]> temp:
            mang[j] = mang[j-1]
            j = j-1

        mang[j] =temp
        print(i,'-',mang)
def main():
    mang = san_sinh_so_ngau_nhien(10)
    print('Mang ban dau la:\n',   mang)
    sap_xep_chen(mang)
    print('Mang sau khi da sap xep lai:',mang)
if __name__ == '__main__':
    main()