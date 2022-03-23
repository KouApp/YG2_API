import time

start_time = time.time()
metin1 = []
with open("metin1.txt","r") as f1:
    metin1 = f1.read().split()

metin2 = []
with open("metin2.txt","r") as f2:
    metin2 = f2.read().split()

print("metin1 : ",metin1)
print("metin2 : ",metin2)

benzer_kelime_sayisi = 0

for mt1 in metin1:
    for mt2 in metin2:
        if mt1 == mt2 and len(mt1) > 2 and len(mt2) > 2 :
            benzer_kelime_sayisi += 1

stp=time.time()
res = stp-start_time
print("gecen süre : ",round(res,4))
print("Benzer kelime sayisi : ",benzer_kelime_sayisi)
print("Toplam kelime sayisi : ",str(len(metin1)+len(metin2)))