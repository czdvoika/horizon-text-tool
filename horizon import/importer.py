s = open("save.txt", "r")
f = open("save.core", "r+b")


line = s.readline()
print(line)
print("start",f.tell())
size = len(line)
print("size",size)
nsize = (size-1)
print("nsize",nsize)
usize = hex(nsize)
print("hexsize",usize)
enusize = nsize.to_bytes(2, 'little')
print("hexsize",enusize)
f.write(enusize)
encodeline = line.encode("utf-8")
f.write(encodeline)
print("end",f.tell())



