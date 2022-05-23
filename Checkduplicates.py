mdict={}#倉頡碼Dict
qrdict={}#倉頡碼Dict,value對應qwerty
dupli=[]#collecting duplicates
qkeytom={}#qwerty to tshuocii
with open('tshuocii qwerty.txt',encoding='utf-8') as qwertyCT: #Define a dictionary that maps qwerty keys to tshuocii mo.
    for line in qwertyCT:
        line=line.strip('')
        (qkey, tshcm)=line.split()
        qkeytom[qkey]=tshcm
with open('Cangjie5_TC copy.txt',encoding='utf-8') as cangjieCT:
    for line in cangjieCT:
        line=line.strip()
        (zrs,qrinp)=line.split(maxsplit=1)
        if zrs in qrdict and zrs not in dupli:
            dupli.append(zrs)
        qrdict[zrs]=qrdict.get(zrs,'')+qrinp+' '

fow=open('duplicates3.txt','w',encoding='utf-8')
for entry in dupli:
    print(entry,qrdict[entry],file=fow)
