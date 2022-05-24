mdict={}#倉頡碼Dict
qrdict={}#倉頡碼Dict,value對應qwerty
qrdict2={}#collecting duplicates
qkeytom={}#qwerty to tshuocii
'''
take a entry in the qrdict and variations as arguments
'''
def has_varn(entry,*varns):
    varncount={}
    for i in range(len(varns)):
        for ckm in entry:
            if varns[i] in ckm:
                varncount[varns[i]]=varncount.get(varns[i],0)+1
    if len(varncount)==len(varns):
        return True
    return False
def has_varn_print(entry,file,*varns):
    if has_varn(entry,*varns):
        print(entry,file=file) 
with open('tshuocii qwerty.txt',encoding='utf-8') as qwertyCT: #Define a dictionary that maps qwerty keys to tshuocii mo.
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
with open('variation dupli.txt','w',encoding='utf-8') as fow:
    for key in qrdict:
        if len(qrdict[key])>1:
            if has_varn(qrdict[key],'pi','pm'):
                print('勺',key,qrdict[key],file=fow)
            if has_varn(qrdict[key],'kni','knk'):
                print('丸',key,qrdict[key],file=fow)
            if has_varn(qrdict[key],'hs','is'):
                print('戶',key,qrdict[key],file=fow)
            if has_varn(qrdict[key],'he','me'):
                print('反',key,qrdict[key],file=fow)
