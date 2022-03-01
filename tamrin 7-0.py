
from pyfiglet import Figlet

produact=[]
factor=[]
info=['id', 'name', 'price', 'stock']
def load():
    print('loading...')
    file_open=open('data.txt', 'r')
    file_product=file_open.read()
    file_open.close()
    info_product=file_product.split('\n')
    for i in range(len(info_product)):
        my_dict={}
        information=info_product[i].split(',')
        my_dict['id']=int(information[0])
        my_dict['name']=information[1]
        my_dict['price']=float(information[2])
        my_dict['stock']=int(information[3])
        produact.append(my_dict)
    print('program is ready')

def show_list():
    for j in produact:
        print(j)

def show_menu():
    dict_menu={1:'Add product', 2:'Edit product', 3:'Delet product',
           4:'search', 5:'show list', 6:'buy', 7:'qrcode', 8:'save & exit'}

    for i,j in dict_menu.items():
        print(i,'=',j)

def search_product():
    while True:
        scan=input('pleaz inter id or name of product:')
        for i in range(len(produact)):
            if str(produact[i]['id'])==scan or produact[i]['name']==scan:
                print(produact[i])
                if produact[i]['stock']==0:
                    print('not exist')
                break
            elif i == len(produact)-1:
                print('not found!!!\npleaz check id and try again')
        ask=int(input('1_exit\n2_continue: '))
        if ask ==1:
            break

def append_product():
    dic_append={}
    r=int(input('pleaz inter row of new product: '))
    dic_append['id']=int(input('pleaz add new id: '))
    dic_append['name']=input('pleaz add new name: ')
    dic_append['price']=float(input('pleaz add new price: '))
    dic_append['stock']=int(input('pleaz add new stock: '))
    produact.insert(r-1,dic_append)

def delet_product():
    scan=input('pleaz inter id or name of product:')
    for i in range(len(produact)):
        if str(produact[i]['id'])==scan or produact[i]['name']==scan:
            produact.pop(i)
            break
        elif i == len(produact)-1:
            print('not found!!!\npleaz check id and try again')

def edit_product():
    scan=input('pleaz inter id or name of product for edit:')
    for i in range(len(produact)):
        if str(produact[i]['id'])==scan or produact[i]['name']==scan:
            print(produact[i])
            choice_edit=int(input('pleaz choice selction:\n1_ id\t\t2_ name\n3_ price\t4_ stock\n: '))
            if choice_edit==1:
                produact[i]['id']=int(input('pleaz enter new id: '))
                break
            elif choice_edit==2:
                produact[i]['name']=input('pleaz enter new name: ')
                break
            elif choice_edit==3:
                produact[i]['price']=float(input('pleaz enter new price: '))
                break
            elif choice_edit==4:
                produact[i]['stock']=int(input('pleaz enter new stock: '))
                break
        elif i == len(produact)-1:
            print('not found!!!\npleaz check id and try again')

def buy():
    while True:
        scan=input('pleaz inter id or name of product for buy:')
        for i in range(len(produact)):
            if str(produact[i]['id'])==scan or produact[i]['name']==scan:
                print(produact[i])
                cont=int(input('pleaz enter count: '))
                if cont<=produact[i]['stock']:
                    my_factor={'cont':cont,'price':produact[i]['price'],'sum':cont*produact[i]['price']}
                    factor.append(my_factor)
                    produact[i]['stock']-=cont
                    break
                else:
                    print('count not available stock= ',produact[i]['stock'])
                    break
            elif i == len(produact)-1:
                print('not found!!!\npleaz check id and try again')
                break
        ex=int(input('1_countinue\n2_exit\n: '))
        if ex==2:
            break

def append_file():
    t=open('data.txt','w').close()
    for i in range(len(produact)):
        t=open('data.txt', 'a')
        for m in info:
            st=str(produact[i][m])
            t.write(st)
            t.write(',')
        if i <= len(produact)-2:
            t.write('\n')
        t.close()
def qr():
    import qrcode
    scan=input('pleaz inter id or name of product:')
    for i in range(len(produact)):
        if str(produact[i]['id'])==scan or produact[i]['name']==scan:
            img=qrcode.make(produact[i])
            img.save(f'qrcode{i}.png')
def factors():
    sum_factor=0
    for i in range(len(factor)):
        sum_factor+=factor[i]['sum']
        print(factor[i])
    print('sum =',sum_factor)
    

f=Figlet(font='standard')
print(f.renderText('s a e e d stor'))
load()
while True:
    show_menu()
    choos=int(input('pleaz inter number from menu '))
    if choos == 1:
        append_product()
        print('add complete')
        
    elif choos ==2:
        edit_product()
        print('edit coplete')

    elif choos ==3:
        delet_product()
        print('delet complete')
    elif choos ==4:
        search_product()     
    elif choos ==5:
        show_list()

    elif choos ==6:
        buy()
    elif choos==7:
        qr()
    elif choos ==8:
        factors()
        append_file()
        print('tanks for your shopping')
        exit()
