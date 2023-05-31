'''
Sản sinh ra một danh sách có 10 số nguyên giá trị từ 0-100
Xuất danh sách ra màn hình
Sắp xếp danh sách này tăng dần theo thuật toán sắp xếp nổi bọt
Xuất danh sách sau khi đã sắp xếp ra màn hình
'''
import random
def san_sinh_mang_ngau_nhien(n):
    mang =[]
    for i in range(n):
        so_ngau_nhien=random.randint(0,100)
        mang.append(so_ngau_nhien)
    return mang

def sap_xep_noi_bot(mang):
    n = len(mang)

    for i in range(n): #i =[0,n-1]
        tiep_tuc = False

        for j in range(n-2, i-1, -1): #j=[n-2, i]
            if mang[j] > mang[j+1] :
                mang[j], mang[j+1]  = mang[j+1],mang[j]
                tiep_tuc = True
        print(i +1,'-',mang)

        if tiep_tuc == False:
            break
    return mang

def main():
    mang = san_sinh_mang_ngau_nhien(10)
    print("Mang ban dau la:\n",mang)
    print("\nMang sau khi sap xep noi bot la:",sap_xep_noi_bot(mang))

if __name__ == '__main__':
    main()