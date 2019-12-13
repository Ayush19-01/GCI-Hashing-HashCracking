#Made for the sole purpose of GCI-2019
import pickle
import hashlib
def adding_data(type1):
    mn=input("Enter the data to be hashed:")
    mn1=mn.encode()
    mb=xz(mn1) 
    mb=mb.hexdigest()
    print(mn,"=",mb)
    a=open(type1,"rb")
    x=pickle.load(a)
    a.close()
    a=open(type1,"wb")
    x[mb]=mn
    pickle.dump(x,a)
    a.close()
def retrieve(type1):
    try:
        a=open(type1,"rb")
        xo=pickle.load(a)
        lp=input("Enter the hash to crack:")
        cr=xo[lp]
        print("Found=",cr)
        a.close()
    except:
        print("Data not found!")
    
while True:
    print('Choose from the following options:\n 1.Hashing \n 2.Cracking \n 3.Exit')
    bv=int(input("Enter your choice:"))
    if bv==1:
        print("What kind of Hashing: \n 1.md5 \n 2.sha1 \n 3.sha224 \n 4.sha256 \n 5.sha384 \n 6.sha512")
        bx=int(input("Enter your choice:"))
        if bx==1:
            xz=hashlib.md5
            adding_data("md5.dat")
        if bx==2:
            xz=hashlib.sha1
            adding_data("sha1.dat")
        if bx==3:
            xz=hashlib.sha224
            adding_data("sha224.dat")
        if bx==4:
            xz=hashlib.sha256
            adding_data("sha256.dat")
        if bx==5:
            xz=hashlib.sha384
            adding_data("sha384.dat")
        if bx==6:
            xz=hashlib.sha512
            adding_data("sha512.dat")
    if bv==2:
        print("What kind of Cracking: \n 1.md5 \n 2.sha1 \n 3.sha224 \n 4.sha256 \n 5.sha384 \n 6.sha512")
        bx=int(input("Enter your choice:"))
        if bx==1:
            retrieve("md5.dat")
        if bx==2:
            retrieve("sha1.dat")
        if bx==3:
            retrieve("sha224.dat")
        if bx==4:
            retrieve("sha256.dat")
        if bx==5:
            retrieve("sha384.dat")
        if bx==6:
            retrieve("sha512.dat")
    if bv>=3:
        break