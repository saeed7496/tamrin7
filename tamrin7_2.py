
from cmath import nan

word_file=[]
def load():
    t=open('translate.txt','r')
    tr=t.read()
    t.close()
    tra=tr.split('\n')
    for i in range(len(tra)):
        dic={}
        if i%2==0:
            dic['english']=tra[i]
            dic['persion']=tra[i+1]
            word_file.append(dic)

def show_menu():
    menu={1:'add new word', 2:'translation english2persion', 3:'translation persion2english', 4:'exit'}
    for i,m in menu.items():
        print(i,'=',m)

def englih2persion():
    scan=input('inter english sentence: ')
    lst_sentence=scan.split('.')
    for s in lst_sentence:
        lst_scan=s.split(' ')
        for i in lst_scan:
            for j in range(len(word_file)):
                if word_file[j]['english']==i:
                    print(word_file[j]['persion'],end=' ')
                    break
                elif j==len(word_file)-1:
                    print('!!',repr(i), 'not found !!',end=' ')
    print()

def persion2english():
    scan=input('inter persion sentence: ')
    lst_sentence=scan.split('.')
    for s in lst_sentence:
        lst_scan=s.split(' ')
    for i in lst_scan:
        for j in range(len(word_file)):
            if word_file[j]['persion']==i:
                print(word_file[j]['english'],end=' ')
                break
            elif j==len(word_file)-1:
                print('!!',repr(i), 'peyda nashod!!',end=' ')
    print()

def add_word():
    while True:
        new_word={'english':nan, 'persion':nan}
        english_word=input('pleaz inter new english word: ')
        for j in range(len(word_file)):
            if word_file[j]['english']==english_word:           #kalame az ghabl nabood#
                print('this word is exist')
                break
            elif j==len(word_file)-1:
                persion_word=input('pleaz inter new persion word: ')
                new_word['english']=english_word
                new_word['persion']=persion_word
                word_file.append(new_word)
                t=open('translate.txt','a')
                t.write('\n')
                t.write(english_word)
                t.write('\n')
                t.write(persion_word)
                t.close()
        choose=int(input('1_continue\n2_exit: '))
        if choose==2:
            break

load()
print('welcom...')
while True:
    show_menu()
    choose=int(input('pleaz select a number: '))
    if choose==1:
        add_word()
        print('word added to file')
    elif choose==2:
        englih2persion()
    elif choose==3:
        persion2english()
    elif choose==4:
        print('so long')
        break

