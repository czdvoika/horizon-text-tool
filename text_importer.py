core = open("more.core", "r+b")
txt =  open("save.txt", "rb")


bin = core.read()
pozice1 = bin.find(b"\xE2\xB2\x0B\x42\x6B\x59\x9A\xB8")
print(pozice1)
text = core.seek(pozice1+28)
print(text)
size = core.read(1)
usize = ord(size)
print(usize)
nic = core.read(1)
radek = txt.readline()


a = len(radek)
print(a)

print(radek)
core.write(radek)
