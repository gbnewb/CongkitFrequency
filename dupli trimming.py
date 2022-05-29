import CKdata
def has_varn(entry,*varns):
    varncount={}
    for i in range(len(varns)):
        for ckm in entry:
            if varns[i] in ckm:
                varncount[varns[i]]=varncount.get(varns[i],0)+1
    if len(varncount)==len(varns):
        return True
    return False
def main(outfile):
    CKdata.load()
    with open(outfile,'w',encoding='utf-8') as fow:
        for key in CKdata.qraw:
            if len(CKdata.qraw[key])>1:
                if has_varn(CKdata.qraw[key],'pi','pm'):
                    print('勺',key,CKdata.qraw[key],file=fow)
                if has_varn(CKdata.qraw[key],'kni','knk'):
                    print('丸',key,CKdata.qraw[key],file=fow)
                if has_varn(CKdata.qraw[key],'hs','is'):
                    print('戶',key,CKdata.qraw[key],file=fow)
                if has_varn(CKdata.qraw[key],'he','me'):
                    print('反',key,CKdata.qraw[key],file=fow)

if __name__=='__main__':
    main('test.txt')
