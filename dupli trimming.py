mdict={}#倉頡碼Dict
qrdict={}#倉頡碼Dict,value對應qwerty
qkeytom={}#qwerty to congkit
with open('tshuocii qwerty.txt',encoding='utf-8') as qwertyCT: #Define a dictionary that maps qwerty keys to congkit mo.
    for line in qwertyCT:
        line=line.strip('')
        (qkey, tshcm)=line.split()
        qkeytom[qkey]=tshcm
with open('Cangjie5_TC copy 2.txt',encoding='utf-8') as cangjieCT:
    for line in cangjieCT:
        #Take in the data and put them in the qwerty raw dictionary.
        line=line.strip()
        (zrs,qr)=line.split(maxsplit=1)
        qrdict.setdefault(zrs,[]).append(qr)
        #Converting raw qwerty to Congkit code
        tcm=list(qr)
        for i in range(len(tcm)):
            tcm[i]=qkeytom[tcm[i]]
        tcm=''.join(tcm)
        mdict.setdefault(zrs,[]).append(tcm)
'''while True:
    inp=input('請輸入欲査詢倉頡碼(五代)之字: ')
    if inp == '0':
        break
    print(f'「{inp}」五代倉頡碼: {mdict[inp]} len:{len(mdict[inp])}')'''
with open('duplicates4.txt','w',encoding='utf-8') as fow:
    for key in qrdict:
        if len(qrdict[key])>1:
            print(key,qrdict[key],file=fow)
