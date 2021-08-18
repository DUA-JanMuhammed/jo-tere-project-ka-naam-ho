from tkinter import *
from tkinter import ttk as TTK

import PIL
from PIL import Image,ImageTk




#=========login window===============
class login_window():
    def login(self):
        second_window = Toplevel(self.root)
        obj_login_window2=login_window2(second_window)
        
            
          
    def __init__(self,root):
        self.root = root
        titlespace = " "
        self.root.title(160 * titlespace + "PEARL HOTEL")
        self.root.geometry("1050x600+100+50")
        self.root.resizable(height = False, width = False)
        self.root.config(bg = "grey6")
      
     
        #===========backgroung==========
        
        self.bg = ImageTk.PhotoImage(resize_image)
        bg = Label(self.root, image= self.bg).place(x=250, y= 0 , relwidth=1 , relheight = 1)
        
        #===========left image============
        self.frame1 = Frame(self.root,bg = "black").place(x=80, y= 100 , width=300 , height = 400)
        self.li = ImageTk.PhotoImage(resize_image2)
        li = Label(self.frame1, image= self.li).place(x=80, y= 100 )
        
        #================mainframe==========
        self.frame2  =Frame(self.root,bg = "white").place(x=380, y= 100 , width=600 , height = 405) 
        self.heading = Label(self.frame2,text="PEARL HOTEL",bg="white",fg="black",font=("Times New Roman ",40,"italic")).place(x=500, y= 150)
        self.username = Label(self.frame2,text="USERNAME",fg="black",bg="white",font=("Times New Roman",20,"italic")).place(x=500,y=230)
        self.user_entry=Entry(self.frame2,bg="gray",font=("Times New Roman",15),width=20).place(x=660,y=230)
        self.passwaord = Label(self.frame2,text="PASSWORD",fg="black",bg="white",font=("Times New Roman",20,"italic")).place(x=500,y=300)
        self.pass_entry=Entry(self.frame2,bg="gray",font=("Times New Roman",15),show="*",width=20).place(x=660,y=300)
        login_button=Button(self.frame2,text="Login",command =self.login,fg="#A99C94",bg="#12121A",bd=4,width = 15,font=("Times New Roman",15,"bold")).place(x=600,y=400)
        
        
            
            
            
class login_window2():
    def func_manage_customers(self):
        manage_customers_window = Toplevel(self.master)
        obj_manage_customer=manage_customer(manage_customers_window)
    
    
    
    
    def exit1(self):
        manage_customers_window.destroy()
    
    
    def __init__(self,master):
        self.master = master
        titlespace = " "
        self.master.title(160 * titlespace + "PEARL HOTEL")
        self.master.geometry("1050x600+100+50")
        self.master.resizable(height = False, width = False)
        self.master.config(bg = "black")
        
          #===========backgroung==========
        
        self.bg = ImageTk.PhotoImage(resize_image)
        bg = Label(self.master, image= self.bg)
        bg.place(x=0, y= 0 , relwidth=1 , relheight = 1)
        bg.photo =  self.bg
        #===========left image============
        self.frame1 = Frame(self.master,bg = "black")
        self.frame1 .place(x=80, y= 100 , width=300 , height = 400)
        self.li = ImageTk.PhotoImage(resize_image2)
        li = Label(self.master, image= self.li)
        li.place(x=80, y= 100 )
        li.photo = self.li
        
        #================mainframe==========
        self.frame2  =Frame(self.master,bg = "white")
        self.frame2.place(x=380, y= 100 , width=600 , height = 405) 
        self.heading = Label(self.master,text="PEARL HOTEL",bg="white",fg="black",font=("Times New Roman ",40,"italic"))
        self.heading.place(x=500, y= 150) 
        #===============buutons pics=================
        self.hotel = ImageTk.PhotoImage(resize_hotelimage)
        
        self.restaurent = ImageTk.PhotoImage(resize_resturentimage2)
        
        
        #================buttons==========
        self.button_retaurent = Button(self.master, image =self.hotel,text = 'Manage Restaurent!',font=("Times New Roman",20,"bold"))
        self.button_retaurent.place(x=700, y= 240)
        
        self.button_customer = Button(self.master, image =self.restaurent, text = 'Manage customers',command =self.func_manage_customers ,font=("Times New Roman",20,"bold"))
        self.button_customer.place(x=450, y= 240)
        self.button_customer.image = self.hotel
        
        
        
        
        
class manage_customer(login_window2):
    
        
        
    def exit(self):
        ob = login_window2.exit1()
    
    
    
    def __init__(self,window3,*args,**kwargs):
        self.window3 = window3
        titlespace = " "
        self.window3.title(160 * titlespace + "PEARL HOTEL")
        self.window3.geometry("1050x600+100+50")
        self.window3.resizable(height = False, width = False)
        self.window3.config(bg = "black")
        #self.window3.wm_attributes('-transparentcolor', self.window3['bg'])
        #==============background=============
        self.bg = ImageTk.PhotoImage(resize_image)
        bg = Label(self.window3, image= self.bg)
        bg.place(x=0, y= 0 , relwidth=1 , relheight = 1)
        bg.photo =  self.bg
        #===================frames============
        #self.frame3 = Frame(self.window3, bd= 10,relief = RIDGE ,bg = "grey54").place(x=10, y= 5 , width=1030 , height = 100)
        self.heading_2 = Label(self.window3,text="PEARL HOTEL(Customer)",fg="white",bg= "black",font=("Times New Roman ",45,"italic")).place(x=200, y= 20)
        #self.frame4 = Frame(self.window3, bd= 10,relief = RIDGE ,bg = "grey54").place(x=10, y= 110 , width=200 , height = 480)
        #self.frame5 = Frame(self.window3, bd= 10,relief = RIDGE ,bg = "grey54").place(x=215, y= 110 , width=826 , height = 250)
        frame6 = Frame(self.window3, bd= 10,relief = RIDGE ,bg = "grey54")
        frame6.place(x=215, y= 365 , width=826 , height = 225)
        
        #=================textvariables=================
        gender = StringVar()
        
        #============buttons=====================
        self.button_Ad_cust = Button(self.window3, text = 'Add Customer!',fg="#12121A",bg="white",bd=4,width = 13,height = 2,font=("Times New Roman",14,"bold")).place(x=30, y= 130)
        self.button_del_cust = Button(self.window3, text = 'Delete Customer!',fg="#12121A",bg="white",bd=4,width = 13,height = 2,font=("Times New Roman",14,"bold")).place(x=30, y= 200)
        self.button_UP_cust = Button(self.window3, text = 'Update Customer!',fg="#12121A",bg="white",bd=4,width = 13,height = 2,font=("Times New Roman",14,"bold")).place(x=30, y= 270)
        self.button_view_cust = Button(self.window3, text = 'View Customer!',fg="#12121A",bg="white",bd=4,width = 13,height = 2,font=("Times New Roman",14,"bold")).place(x=30, y= 340)
        self.button_reset = Button(self.window3, text = 'Reset!',fg="#12121A",bg="white",bd=4,width = 13,height = 2,font=("Times New Roman",14,"bold")).place(x=30, y= 410)
        self.button_exit = Button(self.window3, command = exit, text = 'Exit!',fg="#12121A",bg="white",bd=4,width = 13,height = 2,font=("Times New Roman",14,"bold")).place(x=30, y= 480)
        
        
        #===================label frame==============
        #self.labelframe =LabelFrame(self.window3, bd= 5,text = "Personal Information",font=("Times New Roman",15,"italic"),relief = RIDGE )
        #self.labelframe.place(x=230, y= 120 , width=350 , height = 220)
        #self.labelframe2=LabelFrame(self.window3, bd= 5,text = "Reservation Information",font=("Times New Roman",15,"italic"),relief = RIDGE )
        #self.labelframe2.place(x=600, y= 120 , width=420 , height = 220)
        
        
        #===============labels=================
        
        self.Name = Label(self.window3,text="Name",fg="black",font=("Times New Roman",17,"bold")).place(x=240,y=140)
        self.Gender = Label(self.window3,text="Gender",fg="black",font=("Times New Roman",17,"bold")).place(x=240,y=170)
        self.address = Label(self.window3,text="Address",fg="black",font=("Times New Roman",17,"bold")).place(x=240,y=200)
        self.Age = Label(self.window3,text="Age",fg="black",font=("Times New Roman",17,"bold")).place(x=240,y=230)
        self.CNIC = Label(self.window3,text="CNIC",fg="black",font=("Times New Roman",17,"bold")).place(x=240,y=260)
        self.phoneNo = Label(self.window3,text="Phone No.",fg="black",font=("Times New Roman",17,"bold")).place(x=240,y=290)
         #==================entries==================
        self.NameEnt = Entry(self.window3,bd = 5,fg="black",bg="white",font=("Times New Roman",15,"bold")).place(x=350,y=140,width=200)
        self.GenderEnt = Entry(self.window3,bd = 5,fg="black",bg="white",font=("Times New Roman",15,"bold")).place(x=350,y=170,width=200)
        self.addressEnt = Entry(self.window3,bd = 5,fg="black",bg="white",font=("Times New Roman",15,"bold")).place(x=350,y=200,width=200)
        self.AgeEnt = Entry(self.window3,bd = 5,fg="black",bg="white",font=("Times New Roman",15,"bold")).place(x=350,y=230, width=200)
        self.CNICEnt = Entry(self.window3,bd = 5,fg="black",bg="white",font=("Times New Roman",15,"bold")).place(x=350,y=260, width=200)
        self.phoneNoEnt = Entry(self.window3,bd = 5,fg="black",bg="white",font=("Times New Roman",15,"bold")).place(x=350,y=290, width=200)
        #===============label in 2nd labelframe===================
        
        self.room_no = Label(self.window3,text="Room No",fg="black",bg="grey54",font=("Times New Roman",17,"bold")).place(x=610,y=140)
        self.dateOfReserv = Label(self.window3,text="Reservation Date",fg="black",bg="grey54",font=("Times New Roman",17,"bold")).place(x=610,y=170)
        self.stayDays = Label(self.window3,text="How Many Days?",fg="black",bg="grey54",font=("Times New Roman",17,"bold")).place(x=610,y=200)
        self.Amount = Label(self.window3,text="Amount",fg="black",bg="grey54",font=("Times New Roman",17,"bold")).place(x=610,y=230)
        self.Pay_method = Label(self.window3,text="Payment Method",fg="black",bg="grey54",font=("Times New Roman",17,"bold")).place(x=610,y=260)
        self.credit_card = Label(self.window3,text="Credit Card No.",fg="black",bg="grey54",font=("Times New Roman",17,"bold")).place(x=610,y=290)
        #=====================entries in 2nd Frame====================
        self.room_noEnt = Entry(self.window3,bd = 5,fg="black",bg="white",font=("Times New Roman",15,"bold")).place(x=800,y=140,width=200)
        self.sdateOfReservEnt = Entry(self.window3,bd = 5,fg="black",bg="white",font=("Times New Roman",15,"bold")).place(x=800,y=170,width=200)
        self.stayDaysEnt = Entry(self.window3,bd = 5,fg="black",bg="white",font=("Times New Roman",15,"bold")).place(x=800,y=200,width=200)
        self.AmountEnt = Entry(self.window3,bd = 5,fg="black",bg="white",font=("Times New Roman",15,"bold")).place(x=800,y=230, width=200)
        self.Pay_methodEnt = Entry(self.window3,bd = 5,fg="black",bg="white",font=("Times New Roman",15,"bold")).place(x=800,y=260, width=200)
        self.credit_cardEnt = Entry(self.window3,bd = 5,fg="black",bg="white",font=("Times New Roman",15,"bold")).place(x=800,y=290, width=200)
        
        
        #==================treeview and scroll bar========================
        scroll_bar1 = Scrollbar(frame6, orient = VERTICAL)
        scroll_bar1.pack(side = RIGHT , fill = Y )
        scroll_bar2 = Scrollbar(frame6, orient = HORIZONTAL)
        scroll_bar2.pack(side = BOTTOM , fill = X )
        tv = TTK.Treeview(frame6, columns=(1, 2, 3,4,5,6,7,8), show='headings', height=8 , yscrollcommand =scroll_bar1.set ,xscrollcommand =scroll_bar2.set )
        scroll_bar2.config(command=tv.xview)
        scroll_bar1.config(command=tv.yview)
        tv.pack(side=LEFT , fill = BOTH , expand = 1)

        tv.heading(1, text="Name")
        tv.heading(2, text="Gender")
        tv.heading(3, text="CNIC")
        tv.heading(4, text="Phone No")
        tv.heading(5, text="Room No")
        tv.heading(6, text="Date Of Reservation")
        tv.heading(7, text="Stay Days")
        tv.heading(8, text="Amount")
        
        tv.column(1 , width = 70)
        tv.column(2 , width = 200)
        tv.column(3 , width = 200)
        tv.column(4 , width = 200)
        tv.column(5 , width = 200)
        tv.column(6 , width = 200)
        tv.column(7 , width = 100)
        tv.column(8 , width = 100)
        
        
        
        
        
        
if __name__ == '__main__':
    root = Tk()
    image = Image.open("bg2.jpg")
    resize_image = image.resize((1200, 600))
    
    image2 = Image.open("img2.jpg")
    resize_image2 = image2.resize((300, 400))
   


    hotel_image = Image.open("hotel1.jpg")
    resize_hotelimage = hotel_image.resize((200, 200))
    
    
    resturent_image = Image.open("restaurent 2.jpg")
    resize_resturentimage2 = resturent_image.resize((200, 200))
    
    obj = login_window(root)
    root.mainloop()
    