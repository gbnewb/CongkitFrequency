mdict={}#倉頡碼Dict
qrdict={}#倉頡碼Dict,value對應qwerty
qrdict2={}#collecting duplicates
qkeytom={}#qwerty to tshuocii
with open('tshuocii qwerty.txt',encoding='utf-8') as qwertyCT: #Define a dictionary that maps qwerty keys to tshuocii mo.
    for line in qwertyCT:
        line=line.strip('')
        (qkey, tshcm)=line.split()
        qkeytom[qkey]=tshcm
with open('Cangjie5_TC copy 2.txt',encoding='utf-8') as cangjieCT:
    for line in cangjieCT:
        line=line.strip()
        (zrs,qr)=line.split(maxsplit=1)
        tcm=list(qr)
        if zrs in qrdict and qr[0] !='x':#With an acceptable minor flaw
            qrdict2[zrs]=qrdict2.get(zrs,qrdict[zrs])+qr+' '
        qrdict[zrs]=qrdict.get(zrs,'')+qr+' '
        for i in range(len(tcm)):
            tcm[i]=qkeytom[tcm[i]]
        tcm=''.join(tcm)
        mdict[zrs]=mdict.get(zrs,'')+tcm+' '

with open('inputdata.txt','r',encoding='utf-8') as inpdt:
    fow=open('output.txt','w',encoding='utf-8')
    while True:
        istrm=inpdt.read(1)
        if not istrm:
            print('End of File')
            break
        if istrm in qrdict:
            print(istrm,mdict[istrm],file=fow)
