from tkinter import*
import math,random,os
from tkinter import messagebox
class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bg_color="#074463"
        title=Label(self.root,text="Billing Software",bd=12,relief=GROOVE,bg=bg_color,fg="White",font=("times new roman",30,"bold"),pady=2).pack(fill=X)

        # ========Variables========
        # ========Cosmetics========
        self.soap=IntVar()
        self.Face_cream=IntVar()
        self.Face_wash=IntVar()
        self.spray=IntVar()
        self.gell=IntVar()
        self.loshan=IntVar()
        # ========Glocery========
        self.rice=IntVar()
        self.food=IntVar()
        self.daal=IntVar()
        self.wheat=IntVar()
        self.sugar=IntVar()
        self.tea=IntVar()
        # ========Cold Drinks========
        self.coke=IntVar()
        self.maza=IntVar()
        self.Frooti=IntVar()
        self.thumbsup=IntVar()
        self.limca=IntVar()
        self.sprite=IntVar()
        
        # ========Total Price & Tax Variables========
        self.cosmetic_price=StringVar()
        self.grocery_price=StringVar()
        self.cold_drink_price=StringVar()

        self.cosmetic_tax=StringVar()
        self.grocery_tax=StringVar()
        self.cold_drink_tax=StringVar()
        
        # ========Customer========
        self.c_name=StringVar()
        self.c_phone=StringVar()
        self.bill=StringVar()
        x=random.randint(1000,9999)
        self.bill.set(str(x))
        self.search=StringVar()
      

        # ============Customer Details Frame
        F1=LabelFrame(self.root,text="Customer Details",bd=7,relief=GROOVE,bg=bg_color,fg="gold",font=("times new roman",15,"bold"))
        F1.place(x=0,y=80,relwidth=1)

        cname_lbl=Label(F1,text="Customer Name",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(F1,width=15,textvariable=self.c_name,font="arial 15",bd=5,relief=SUNKEN).grid(row=0,column=1,padx=5,pady=10)
        
        cphn_lbl=Label(F1,text="Phone No",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=2,padx=20,pady=5)
        cphn_txt=Entry(F1,width=15,textvariable=self.c_phone,font="arial 15",bd=5,relief=SUNKEN).grid(row=0,column=3,padx=5,pady=10)
        
        c_bill_lbl=Label(F1,text="Customer Bill No",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=4,padx=20,pady=5)
        c_bill_txt=Entry(F1,width=15,textvariable=self.bill,font="arial 15",bd=5,relief=SUNKEN).grid(row=0,column=5,padx=5,pady=10)
        
        bill_btn=Button(F1,command=self.find_bill,textvariable=self.search,fg="blue",width=10,bd=7,text="ngg",font=("arial",12,"bold")).grid(row=0,column=6,padx=1,pady=1)
        
        # =============Cosmetic Frame
        F2=LabelFrame(self.root,text="Cosmetics",bd=7,relief=GROOVE,bg=bg_color,fg="gold",font=("times new roman",15,"bold"))
        F2.place(x=5,y=180,width=325,height=380)

        bath_lbl=Label(F2,text="Bath Soap",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        bath_txt=Entry(F2,textvariable=self.soap,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=10,padx=10,pady=10)
        
        Face_cream_lbl=Label(F2,text="Face Cream",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        Face_cream_txt=Entry(F2,width=10,textvariable=self.Face_cream,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=10,padx=10,pady=10)
        
        Face_w_lbl=Label(F2,text="Face Wash",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        Face_w_txt=Entry(F2,width=10,textvariable=self.Face_wash,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=10,padx=10,pady=10)
        
        Hair_s_lbl=Label(F2,text="Hair Spray",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        Hair_s_txt=Entry(F2,width=10,textvariable=self.spray,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=10,padx=10,pady=10)
        
        Hair_g_lbl=Label(F2,text="Hair Gel",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        Hair_g_txt=Entry(F2,width=10,textvariable=self.gell,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=10,padx=10,pady=10)
        
        Body_lbl=Label(F2,text="Body Lotion",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        Body_txt=Entry(F2,width=10,textvariable=self.loshan,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=10,padx=10,pady=10)
       
        # =============Grocery Frame
        F3=LabelFrame(self.root,text="Grocery",bd=7,relief=GROOVE,bg=bg_color,fg="gold",font=("times new roman",15,"bold"))
        F3.place(x=340,y=180,width=325,height=380)

        g1_lbl=Label(F3,text="Rice",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        g1_txt=Entry(F3,width=10,textvariable=self.rice,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=10,padx=10,pady=10)
        
        g2_lbl=Label(F3,text="Food Oil",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        g2_txt=Entry(F3,width=10,textvariable=self.food,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=10,padx=10,pady=10)
        
        g3_lbl=Label(F3,text="Daal",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        g3_txt=Entry(F3,width=10,textvariable=self.daal,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=10,padx=10,pady=10)
        
        g4_lbl=Label(F3,text="Wheat",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        g4_txt=Entry(F3,width=10,textvariable=self.wheat,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=10,padx=10,pady=10)
        
        g5_lbl=Label(F3,text="Sugar",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        g5_g_txt=Entry(F3,width=10,textvariable=self.sugar,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=10,padx=10,pady=10)
        
        g6_lbl=Label(F3,text="Tea Powder",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        g6_txt=Entry(F3,width=10,textvariable=self.tea,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=10,padx=10,pady=10)
        
        # =============Cold Drinks Frame
        F4=LabelFrame(self.root,text="Cold Drinks",bd=7,relief=GROOVE,bg=bg_color,fg="gold",font=("times new roman",15,"bold"))
        F4.place(x=670,y=180,width=325,height=380)

        c1_lbl=Label(F4,text="Coke",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        c1_txt=Entry(F4,width=10,textvariable=self.coke,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=10,padx=10,pady=10)
        
        c2_lbl=Label(F4,text="Maza",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        c2_txt=Entry(F4,width=10,textvariable=self.maza,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=10,padx=10,pady=10)
        
        c3_lbl=Label(F4,text="Frooti",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        c3_txt=Entry(F4,width=10,textvariable=self.Frooti,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=10,padx=10,pady=10)
        
        c4_lbl=Label(F4,text="Thumbs Up",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        c4_txt=Entry(F4,width=10,textvariable=self.thumbsup,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=10,padx=10,pady=10)
        
        c5_lbl=Label(F4,text="Limca",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        c5_txt=Entry(F4,width=10,textvariable=self.limca,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=10,padx=10,pady=10)
        
        c6_lbl=Label(F4,text="Sprite",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        c6_txt=Entry(F4,width=10,textvariable=self.sprite,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=10,padx=10,pady=10)
        
        #========= Bill Area =======
        
        F5=LabelFrame(self.root,relief=GROOVE,bd=10)
        F5.place(x=1010,y=180,width=350,height=380)
        bill_title=Label(F5,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)

        # =============Button Frame=========

        F6=LabelFrame(self.root,text="Billing Menu",bd=7,relief=GROOVE,bg=bg_color,fg="gold",font=("times new roman",15,"bold"))
        F6.place(x=0,y=560,relwidth=1,height=140)
        
        m1_lbl=Label(F6,text="Total Cosmetic Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        m1_txt=Entry(F6,width=18,textvariable=self.cosmetic_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)
        
        m2_lbl=Label(F6,text="Total Grocery Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky="w")
        m2_txt=Entry(F6,width=18,textvariable=self.grocery_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)
    
        m3_lbl=Label(F6,text="Total Cold Drinks Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky="w")
        m3_txt=Entry(F6,width=18,textvariable=self.cold_drink_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)


        c1_lbl=Label(F6,text="Cosmetic Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=2,padx=20,pady=1,sticky="w")
        c1_txt=Entry(F6,width=18,textvariable=self.cosmetic_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)
        
        c2_lbl=Label(F6,text="Grocery Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=2,padx=20,pady=1,sticky="w")
        c2_txt=Entry(F6,width=18,textvariable=self.grocery_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)
    
        c3_lbl=Label(F6,text="Cold Drinks Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=2,padx=20,pady=1,sticky="w")
        c3_txt=Entry(F6,width=18,textvariable=self.cold_drink_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)

        btn_F=Frame(F6,bd=7,relief=GROOVE)
        btn_F.place(x=750,width=580,height=105)

        Total_btn=Button(btn_F,text="Total",command=self.total,bg="cadetblue",fg="white",pady=15,width=10,font="arial 14 bold",bd=2).grid(row=0,column=0,padx=5,pady=5)
        G_Bill_btn=Button(btn_F,text="Generate Bill",command=self.bill_area,bg="cadetblue",fg="white",pady=15,width=10,font="arial 14 bold",bd=2).grid(row=0,column=1,padx=5,pady=5)
        Clear_btn=Button(btn_F,text="Clear",bg="cadetblue",command=self.clear_data,fg="white",pady=15,width=10,font="arial 14 bold",bd=2).grid(row=0,column=2,padx=5,pady=5)
        Exit_btn=Button(btn_F,text="Exit",bg="cadetblue",command=self.Exit_app,fg="white",pady=15,width=10,font="arial 14 bold",bd=2).grid(row=0,column=3,padx=5,pady=5)
        self.welcome_bill()

    def total(self):
        self.c_s_p=self.soap.get()*40
        self.c_fc_p=self.Face_cream.get()*120
        self.c_fw_p=self.Face_wash.get()*60
        self.c_hs_p=self.spray.get()*180
        self.c_hg_p=self.gell.get()*140
        self.c_bl_p=self.loshan.get()*180
                
        self.total_cosmetic_price=float(
                                self.c_s_p+
                                self.c_fc_p+
                                self.c_fw_p+
                                self.c_hs_p+
                                self.c_hg_p+
                                self.c_bl_p
                                )
        self.cosmetic_price.set("Rs. "+str(self.total_cosmetic_price))
        self.c_tax=round((self.total_cosmetic_price*0.05),2)
        self.cosmetic_tax.set("Rs. "+str(self.c_tax))


        self.g_r_p=self.rice.get()*180
        self.g_f_p=self.food.get()*180
        self.g_d_p=self.daal.get()*60
        self.g_w_p=self.wheat.get()*240
        self.g_s_p=self.sugar.get()*54
        self.g_t_p=self.tea.get()*150


        self.total_grocery_price=float(
                                self.g_r_p+
                                self.g_f_p+
                                self.g_d_p+
                                self.g_w_p +
                                self.g_s_p +
                                self.g_t_p
                                )                               
        self.grocery_price.set("Rs. "+str(self.total_grocery_price))
        self.g_tax=round((self.total_grocery_price*0.10),2)
        self.grocery_tax.set("Rs. "+str(self.g_tax))


        self.d_f_p=self.Frooti.get()*60
        self.d_m_p=self.maza.get()*60
        self.d_c_p=self.coke.get()*60
        self.d_l_p=self.limca.get()*50
        self.d_s_p=self.sprite.get()*45
        self.d_t_p=self.thumbsup.get()*40


        self.total_cold_drink_price=float(
                                self.d_m_p+
                                self.d_f_p+
                                self.d_c_p+
                                self.d_l_p+
                                self.d_s_p+
                               self.d_t_p
                                )
        self.cold_drink_price.set("Rs. "+str(self.total_cold_drink_price))
        self.d_tax=round((self.total_cold_drink_price*0.05),2)
        self.cold_drink_tax.set("Rs. "+str(self.d_tax))
    
        self.total_bill = float(self.total_cosmetic_price +
                            self.total_grocery_price + 
                            self.total_cold_drink_price +
                            self.c_tax +
                            self.g_tax +
                            self.d_tax
                        )

    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\t Welcome Webcode Retail \n")
        self.txtarea.insert(END,f"\n Bill Number : {self.bill.get()}")
        self.txtarea.insert(END,f"\n Customer Name :{self.c_name.get()}")
        self.txtarea.insert(END,f"\n Phone Number : {self.c_phone.get()}")
        self.txtarea.insert(END,f"\n =====================================")
        self.txtarea.insert(END,f"\n Products\t\tQty\t\tPrice")
        self.txtarea.insert(END,f"\n =====================================")

    def bill_area(self):
        if self.c_name.get()=="" or self.c_phone.get()=="":
            messagebox.showerror("Error","Customer details are must")
        elif self.cosmetic_price.get()=="Rs 0.0" and self.total_grocery_price.get()=="Rs 0.0" and self.total_cold_drink_price.get()=="Rs 0.0" :
            messagebox.showerror("Error","No Product Purchased")
        
        else :        
            self.welcome_bill()
            # ========Cosmetic==========
            if self.soap.get()!=0:
                self.txtarea.insert(END,f"\nBath Soap \t\t{self.soap.get()}\t\t{self.c_s_p}")
            if self.Face_cream.get()!=0:
                self.txtarea.insert(END,f"\nFace Cream \t\t{self.Face_cream.get()}\t\t{self.c_fc_p}")
            if self.Face_wash.get()!=0:
                self.txtarea.insert(END,f"\nFace Wash \t\t{self.Face_wash.get()}\t\t{self.c_fw_p}")
            if self.spray.get()!=0:
                self.txtarea.insert(END,f"\nHair Spray \t\t{self.spray.get()}\t\t{self.c_hs_p}")
            if self.gell.get()!=0:
                self.txtarea.insert(END,f"\nHair Gel \t\t{self.gell.get()}\t\t{self.c_hg_p}")
            if self.loshan.get()!=0:
                self.txtarea.insert(END,f"\nBody Lotion \t\t{self.loshan.get()}\t\t{self.c_bl_p}")
            # ========Grocery==========
            if self.rice.get()!=0:
                self.txtarea.insert(END,f"\nRice \t\t{self.rice.get()}\t\t{self.g_r_p}")
            if self.food.get()!=0:
                self.txtarea.insert(END,f"\nFood Oil\t\t{self.food.get()}\t\t{self.g_f_p}")
            if self.daal.get()!=0:
                self.txtarea.insert(END,f"\nDaal \t\t{self.daal.get()}\t\t{self.g_d_p}")
            if self.wheat.get()!=0:
                self.txtarea.insert(END,f"\nWheat \t\t{self.wheat.get()}\t\t{self.g_w_p}")
            if self.sugar.get()!=0:
                self.txtarea.insert(END,f"\nSugar \t\t{self.sugar.get()}\t\t{self.g_s_p}")
            if self.tea.get()!=0:
                self.txtarea.insert(END,f"\nTea Powder \t\t{self.tea.get()}\t\t{self.g_t_p}")
            # ========Cold Drinks==========
            if self.Frooti.get()!=0:
                self.txtarea.insert(END,f"\nFrooti \t\t{self.Frooti.get()}\t\t{self.d_f_p}")
            if self.coke.get()!=0:
                self.txtarea.insert(END,f"\nCoca Cola \t\t{self.coke.get()}\t\t{self.d_c_p}")
            if self.sprite.get()!=0:
                self.txtarea.insert(END,f"\nSprite \t\t{self.sprite.get()}\t\t{self.d_s_p}")
            if self.thumbsup.get()!=0:
                self.txtarea.insert(END,f"\nThumbs UP \t\t{self.thumbsup.get()}\t\t{self.d_t_p}")
            if self.limca.get()!=0:
                self.txtarea.insert(END,f"\nLimca \t\t{self.limca.get()}\t\t{self.d_l_p}")
            if self.maza.get()!=0:
                self.txtarea.insert(END,f"\nMaaza \t\t{self.maza.get()}\t\t{self.d_m_p}")


            self.txtarea.insert(END,f"\n -----------------------------------")
            if self.cosmetic_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END,f"\n Cosmetic Tax\t\t{self.cosmetic_tax.get()}")
            if self.grocery_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END,f"\n Grocery Tax\t\t{self.grocery_tax.get()}")
            if self.cold_drink_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END,f"\n Cold Drink Tax\t\t{self.cold_drink_tax.get()}")
            
            # self.txtarea.insert(END,f"\n =====================================")
            self.txtarea.insert(END,f"\n Total Bill :\t\t Rs.{str(self.total_bill)}")
            self.txtarea.insert(END,f"\n ---------------------------------")
            self.save_bill()

    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the Bill?")
        if op>0:
            self.bill_data=self.txtarea.get('1.0',END)
            f1=open("bills/"+ str(self.bill.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill No : {self.bill.get()} Saved Successfully")
        else:
            return

    def find_bill(self):
        present="no"
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.bill.get():
                f1=open(f"bills/{i}","r")
                self.txtarea.delete('1.0',END)
                for d in f1:
                    self.txtarea.insert(END,d)
                f1.close()
                present="yes"
        if present=="no":
           messagebox.showerror("Error","Invalid Bill No.")

    
    def clear_data(self):
        op=messagebox.askyesno("Clear","Do you really want to Clear Data?")
        if op>0 :
            # ========Variables========
            # ========Cosmetics========
            self.soap.set(0)
            self.Face_cream.set(0)
            self.Face_wash.set(0)
            self.spray.set(0)
            self.gell.set(0)
            self.loshan.set(0)
            # ========Glocery========
            self.rice.set(0)
            self.food.set(0)
            self.daal.set(0)
            self.wheat.set(0)
            self.sugar.set(0)
            self.tea.set(0)
            # ========Cold Drinks========
            self.coke.set(0)
            self.maza.set(0)
            self.Frooti.set(0)
            self.thumbsup.set(0)
            self.limca.set(0)
            self.sprite.set(0)
            
            # ========Total Price & Tax Variables========
            self.cosmetic_price.set("")
            self.grocery_price.set("")
            self.cold_drink_price.set("")

            self.cosmetic_tax.set("")
            self.grocery_tax.set("")
            self.cold_drink_tax.set("")
            
            # ========Customer========
            self.c_name.set("")
            self.c_phone.set("")
            self.bill.set("")
            x=random.randint(1000,9999)
            self.bill.set(str(x))
            
            self.search.set("")
            self.welcome_bill

    def Exit_app(self):
        op=messagebox.askyesno("Exit","Do you really want to exit?")
        if op>0 :
            self.root.destroy()

root=Tk()
obj = Bill_App(root)
root.mainloop()