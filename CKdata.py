codes={} #倉頡碼Dictionary
qraw={} #倉頡碼Dictionary,value對應qwerty
qrToCode={} #qwerty to tshuocii
def load():
    print('加載中...')
    with open('tshuocii qwerty.txt',encoding='utf-8') as qwertyCT: #Define a dictionary that maps qwerty keys to tshuocii mo.
        for line in qwertyCT:
            (qkey, qrToCode[qkey])=line.strip().split()
    with open('Cangjie5_TC copy 2.txt',encoding='utf-8') as cangjieCT:
        for line in cangjieCT:
            #Take in the data and put them in the qwerty raw dictionary.
            (zrs,qr)=line.strip().split(maxsplit=1)
            qraw.setdefault(zrs,[]).append(qr)
            #Converting raw qwerty to Congkit code
            tcm=''.join([qrToCode[x] for x in qr])
            codes.setdefault(zrs,[]).append(tcm)
