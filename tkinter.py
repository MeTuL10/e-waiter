import tkinter as tk
import mysql.connector as msql
import matplotlib.pyplot as plt
mname=''     #this will store the name of the submenu taken from sql

#functions
def add():  #to add dishes
    a1=e1.get()
    mycursor.execute('select count(*) from '+mname)
    n=mycursor.fetchall()                               
    n=n[0][0] 

    if a1.isdigit()==False:       
        label2['text']='INVALID ENTRY FOR \nITEM NUMBER'
    
    elif int(a1) not in range(1,n+1):        
        label2['text']='INVALID ENTRY FOR \nITEM NUMBER'

    else:
        mycursor.execute('select name from '+mname+' where no='+str(a1))#2
        name=mycursor.fetchall()
        name=name[0][0]
        mycursor.execute('select price from '+mname+' where no='+str(a1))#2
        price=mycursor.fetchall()
        price=price[0][0]
        mycursor.execute("insert into dish(name,price) values('"+str(name)+"',"+str(price)+')')
        mycursor.execute('select * from dish')
        r=mycursor.fetchall()
        s='DISHES SELECTED\n'
        c='PRICE\n'
        
        for i in r:
            s+=str(i[0])+'\t'+str(i[1])+'\n'
            c+=str(i[2])+'\n'           
        orderlabel['text']=s
        ordercostlabel['text']=c
        label2['text']=' '
        
    if int(a1) in range(1,n+1):
        buttonedit.pack()
        buttonedit.place(relx=0.01,rely=0.685)
        orderlabel.pack()
        orderlabel.place(relx=0.55,rely=0.13)
        ordercostlabel.place(relx=0.85,rely=0.13)
        bill.pack()
        bill.place(relx=0.4,rely=0.13)
        
def editorder(): #shows widgets for removing dishs
    buttonedit.place(relx=1)
    editlabel.pack()
    editlabel.place(relx=0.01,rely=0.685,height=45)
    edittext.pack()
    edittext.place(relx=0.01,rely=0.75,height=30)    
    removebutton.pack()
    removebutton.place(relx=0.115,rely=0.75)
    editerror.pack()
    editerror.place(relx=0.01,rely=0.8)
  

def removed():  #removes items from dishlist
    a=edittext.get()
    mycursor.execute('select count(*) from dish')
    n=mycursor.fetchall()
    n=int(n[0][0])
    
    if a.isdigit()==False:
        editerror['text']='INVALID ENTRY'

    elif int(a) not in range(1,n+1):
        editerror['text']='INVALID ENTRY'

    else:
        mycursor.execute('delete from dish where no='+str(a))
        mycursor.execute('update dish set no=no-1 where no>'+str(a))
        mycursor.execute('alter table dish auto_increment='+str(a))
        mycursor.execute('select * from dish')
        r=mycursor.fetchall()
        s='DISHES SELECTED\n'
        c='PRICE\n'
        for i in r:
            s+=str(i[0])+'\t'+str(i[1])+'\n'
            c+=str(i[2])+'\n'           
        orderlabel['text']=s
        ordercostlabel['text']=c
        editerror['text']=' '

    
def billgen():#generates bill
    showmain.place_forget()
    menulabel.place_forget()
    e1.place_forget()
    b1.place_forget()
    label2.place_forget()
    buttonedit.place_forget()
    editlabel.place_forget()
    edittext.place_forget()
    removebutton.place_forget()
    editerror.place_forget()
    orderlabel.place_forget()
    ordercostlabel.place_forget()
    costlabel.place_forget()
    selectlabel.place_forget()
    bill.place_forget()
    mycursor.execute('select count(*) from dish')
    n=mycursor.fetchall()
    n=n[0][0]
    if int(n)==0:
        text='YOU HAVE NOT ORDERED ANY ITEMS'

    else:
        text='YOU HAVE ORDERED:\nno.\tItem Name\n'
        c='\nPrice\n'
        mycursor.execute('select * from dish')
        r=mycursor.fetchall()
        for i in r:
            text+=str(i[0])+'\t'+i[1]+'\n'
            c+=str(i[2])+'\n'
        mycursor.execute('select sum(price) from dish')
        total=mycursor.fetchall()
        total=total[0][0]
        text=text+"Total is : Rs."+str(total )+'\n'
        text+=("gst: 18% \nService charge 10%\nGrand total is: Rs."+str(int(total+total*18/100+total/10)))

    billlabel.pack()
    billlabel.place(relx=0.38,rely=0.15)
    billcostlabel.pack()
    billcostlabel.place(relx=0.7,rely=0.15)
    billlabel['text']=text
    billcostlabel['text']=c
    paylabel.pack()
    paylabel.place(relx=0.01,rely=0.15)
    cardb.pack()
    cardb.place(relx=0.01,rely=0.23)
    cashb.pack()
    cashb.place(relx=0.08,rely=0.23)
    payb.pack()
    payb.place(relx=0.14,rely=0.23)
    paymsg.pack()
    paymsg.place(relx=0.01,rely=0.3)
    ratelabel.pack()
    ratelabel.place(relx=0.01,rely=0.37)
    yesb.pack()
    yesb.place(relx=0.01,rely=0.44)
    nob.pack()
    nob.place(relx=0.06,rely=0.44)
    mycursor.execute('drop table dish')



def submenu():  #shows the submenus
    global mname
    a=e1.get()
    if a in [chr(i) for i in range(48,58)]:
        mycursor.execute('select mname from main where m1='+str(a))
        mname=mycursor.fetchall()
        mname=mname[0][0]
        mycursor.execute('select * from '+str(mname))
        r=mycursor.fetchall()
        s=mname+'\n'
        costs='Price\n'
        for i in r:
            s=s+str(i[0])+'\t'+str(i[1])+'\n'
            costs+=str(i[2])+'\n' 
        selectlabel['text']='Enter item number:'
        menulabel['text']=s
        b1['text']='SELECT'  #we are changing the main menu widgets to submenu widgets
        b1['command']=add
        e1['text']=''
        label2['text']=' '
        costlabel['text']=costs

    else:
        label2['text']='INVALID ENTRY FOR \nMENU NUMBER'


def show():   #changes the submenu widgets to mainmenu widgets
    menulabel['text']=str(s)
    selectlabel['text']='Enter menu number:'
    costlabel['text']=''
    b1['text']='SELECT'
    b1['command']=submenu
    e1['text']=''

def pay():
    paymsg['text']='The number for paytm is\n 017623674565'

def card():
    paymsg['text']='Request for swiping machine has been made'

def cash():
    paymsg['text']='A waiter will come and collect your order'

def yes():
    billlabel.place_forget()
    billcostlabel.place_forget()
    paylabel.place_forget()
    payb.place_forget()
    cashb.place_forget()
    cardb.place_forget()
    paymsg.place_forget()
    ratelabel.place_forget()
    yesb.place_forget()
    nob.place_forget()
    cleanlabel.pack()
    cleanlabel.place(relx=0.3,rely=0.15)
    cleane.pack()
    cleane.place(relx=0.75,rely=0.15)
    servicelabel.pack()
    servicelabel.place(relx=0.3,rely=0.25)
    servicee.pack()
    servicee.place(relx=0.75,rely=0.25)
    foodlabel.pack()
    foodlabel.place(relx=0.3,rely=0.35)
    foode.pack()
    foode.place(relx=0.75,rely=0.35)
    s1.pack()
    s1.place(relx=0.47,rely=0.47)
        

def no():
    billlabel.place_forget()
    billcostlabel.place_forget()
    paylabel.place_forget()
    payb.place_forget()
    cashb.place_forget()
    cardb.place_forget()
    paymsg.place_forget()
    ratelabel.place_forget()
    yesb.place_forget()
    nob.place_forget()
    thanklabel.pack()
    thanklabel['text']='THANK YOU!! \n WE HOPE TO SEE SEE YOU AGAIN :)'
    thanklabel.place(relx=0.4,rely=0.2)
    
def submit():
   
    a1=cleane.get()
    a2=servicee.get()
    a3=foode.get()
    if a1.isdigit() and a2.isdigit() and a3.isdigit() and int(a1) in range(11) and int(a2) in range(11) and int(a3) in range(11):
        cleanlabel.place_forget()
        cleane.place_forget()
        servicelabel.place_forget()
        servicee.place_forget()
        foodlabel.place_forget()
        foode.place_forget()
        s1.place_forget()
        mycursor.execute("insert into ratings(clean,service,food) values("+a1+","+a2+","+a3+")" )
        mydb.commit()
        thanklabel.pack()
        thanklabel.place(relx=0.4,rely=0.2)
        thanklabel.config(fg='black')
        thanklabel['text']='THANK YOU!! \n WE HOPE TO SEE SEE YOU AGAIN :)'

        mycursor.execute('select * from ratings')
        r=mycursor.fetchall()
        a=[]
        k=[]
        l=[]
        m=[]
        for i in r:
            a+=[int(i[0])]
            k+=[int(i[1])]
            l+=[int(i[2])]
            m+=[int(i[3])]
        plt.title('RESTAURANT RATINGS')
        plt.xlabel('NUMBER OF CUSTOMERS')
        plt.ylabel('RATINGS')
        plt.plot(a,k,'ro',linestyle='solid',label='Cleanliness rating')
        plt.plot(a,l,'bo',linestyle='solid',label='Service rating')
        plt.plot(a,m,'go',linestyle='solid',label='Food rating')
        plt.legend()
        plt.show()
        
    else:
        thanklabel.pack()
        thanklabel.place(relx=0.44,rely=0.54)
        thanklabel.config(fg='red')
        thanklabel['text']='INVALID ENTRY'   
mydb=msql.connect(host='localhost',user='root',passwd='user123')
mycursor=mydb.cursor()
mycursor.execute('use restaurant')
mycursor.execute("create table dish(no int primary key auto_increment , name char(50),price int)")

top=tk.Tk()         
name=tk.Label(top, text='E-WAITER')
name.config(font=("Courier", 44))
mycursor.execute('select * from main')
r=mycursor.fetchall()
s='MENU: \n'
for i in r:
    for j in i:
        s+=str(j)+'\t'
    s+='\n'
menulabel=tk.Label(top,text=str(s),justify='left')
menulabel.config(font=("Courier",14))
e1=tk.Entry(top)
b1=tk.Button(top,text='SELECT',command=submenu)
b1.config(font=("Courier",12))
selectlabel=tk.Label(top,text='Enter menu number:')
selectlabel.config(font=("Courier",14))
costlabel=tk.Label(top)
costlabel.config(font=("Courier",14))
label2=tk.Label(top,justify='left',fg='red')
label2.config(font=("Courier",14))
buttonedit=tk.Button(top,text='edit order',command=editorder)
buttonedit.config(font=("Courier",12))
editlabel=tk.Label(top,text='Enter item number to be removed:')
editlabel.config(font=("Courier",14))
edittext=tk.Entry(top)
removebutton=tk.Button(top,text='remove item',command=removed)
removebutton.config(font=("Courier",12))
editerror=tk.Label(top,fg='red')
editerror.config(font=("Courier",12))
orderlabel=tk.Label(top,justify='left')
orderlabel.config(font=("Courier",14))
ordercostlabel=tk.Label(top,justify='left')
ordercostlabel.config(font=("Courier",14))
bill=tk.Button(top,text='generate bill',command=billgen)
bill.config(font=("Courier",12))
billlabel=tk.Label(top,justify='left')
billlabel.config(font=("Courier",14))
billcostlabel=tk.Label(top,justify='left')
billcostlabel.config(font=("Courier",14))
showmain=tk.Button(top,text='SHOW MAIN MENU',command=show)
showmain.config(font=("Courier",12))
paylabel=tk.Label(top,text='Select payment method')
paylabel.config(font=("Courier",14))
cardb=tk.Button(top,text='Card',command=card)
cardb.config(font=("Courier",14))
cashb=tk.Button(top,text='Cash',command=cash)
cashb.config(font=("Courier",14))
payb=tk.Button(top,text='Paytm',command=pay)
payb.config(font=("Courier",14))
paymsg=tk.Label(top)
paymsg.config(font=("Courier",14))
ratelabel=tk.Label(top,text='Would you like to rate our \nrestaurant?',justify='left')
yesb=tk.Button(top,text='YES',command=yes)
yesb.config(font=("Courier",14))
nob=tk.Button(top,text='NO',command=no)
nob.config(font=("Courier",14))
ratelabel.config(font=("Courier",14))
thanklabel=tk.Label(top)
thanklabel.config(font=("Courier",14))
cleanlabel=tk.Label(top)
cleanlabel.config(font=("Courier",14),text='How much will you  rate our restaurant in terms of \ncleanliness out of 10?')
cleane=tk.Entry(top)
s1=tk.Button(top,text='SUBMIT',command=submit)
s1.config(font=("Courier",14))
foodlabel=tk.Label(top,text='How much will you  rate our restaurant in terms of \nfood quality out of 10?')
foodlabel.config(font=("Courier",14))
foode=tk.Entry(top)
servicelabel=tk.Label(top,text='How much will you  rate our restaurant in terms of \nservice out of 10?')
servicelabel.config(font=("Courier",14))
servicee=tk.Entry(top)
name.pack()
name.place(relx=0.41)
menulabel.pack()
menulabel.place(relx=0.01,rely=0.13)
costlabel.pack()
costlabel.place(relx=0.3,rely=0.13)
selectlabel.pack()
selectlabel.place(relx=0.01,rely=0.5)
e1.pack()
e1.place(relx=0.01,rely=0.55,height=30)
b1.pack()
b1.place(relx=0.11,rely=0.55)
showmain.pack()
showmain.place(relx=0.175,rely=0.55)
label2.pack()
label2.place(relx=0.01,rely=0.6)
buttonedit.pack_forget()
orderlabel.pack_forget()
ordercostlabel.pack_forget()
editlabel.pack_forget()
edittext.pack_forget()
removebutton.pack_forget()
editerror.pack_forget()
billlabel.pack()
billlabel.place(relx=0.7,rely=0.13)
billlabel.pack_forget()
billcostlabel.pack_forget()
paylabel.pack_forget()
cardb.pack_forget()
cashb.pack_forget()
paymsg.pack_forget()
payb.pack_forget()
top.mainloop()
