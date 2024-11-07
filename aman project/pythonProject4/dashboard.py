from tkinter import*
from tkinter import ttk
def employee_form():
       global back_image;
       employee_frame=Frame(root,width=1150,height=670)
       employee_frame.place(x=200,y=100)
       heading_label=Label(employee_frame,text='Manage Employee Details',font=('times new roman',16,'bold'),bg='#0f4d7d',fg='white')
       heading_label.place(x=0,y=0,relwidth=1)
       back_image=PhotoImage(file='left-arrow.png')
       back_button=Button(employee_frame,text='Back',image=back_image,bd=0,cursor='hand2',command=lambda: employee_frame.place_forget())
       back_button.place(x=10,y=30)


       top_frame=Frame(employee_frame,bg='white')
       top_frame.place(x=0,y=70,relwidth=1,height=200)

       search_frame=Frame(top_frame,bg='white')
       search_frame.pack()
       search_combobox=ttk.Combobox(search_frame,values=('ID','Name','Email'),state='readonly',justify=CENTER)
       search_combobox.set('Select By')
       search_combobox.grid(row=0,column=0,padx=20)

       search_entry=Entry(search_frame,font=('times new roman',12),bg='lightyellow')
       search_entry.grid(row=0,column=1)

       search_button=Button(search_frame,text='Search',font=('times new roman',12),width=10,cursor='hand2',fg='white',bg='#0f4d7d')
       search_button.grid(row=0,column=2,padx=20)

       showall_button = Button(search_frame, text='show all', font=('times new roman', 12),width=10,cursor='hand2',fg='white',bg='#0f4d7d')
       showall_button.grid(row=0, column=3)

       horizontal_scroll=Scrollbar(top_frame,orient=HORIZONTAL)
       vertical_scroll=Scrollbar(top_frame,orient=VERTICAL)

       tree_view=ttk.Treeview(top_frame,columns=('empid','name','email','gender','contact','salary','address','DOB')
                              ,show='headings',yscrollcommand=vertical_scroll.set,xscrollcommand=horizontal_scroll.set)
       horizontal_scroll.pack(side=BOTTOM,fill=X)
       horizontal_scroll.pack(side=RIGHT,fill=Y)
       tree_view.pack(pady=(10,0))

       tree_view.heading('empid',text='EmpId')
       tree_view.heading('name', text='Name')
       tree_view.heading('email', text='Email')
       tree_view.heading('gender', text='Gender')
       tree_view.heading('contact', text='Contact')
       tree_view.heading('salary', text='Salary')
       tree_view.heading('address', text='Adress')
       tree_view.heading('DOB', text='Date of birth')

       tree_view.column('empid',width=60)
       tree_view.column('name', width=140)
       tree_view.column('email',width=180)
       tree_view.column('gender', width=80)
       tree_view.column('contact', width=100)
       tree_view.column('salary', width=60)
       tree_view.column('address', width=200)

       tree_view.column('DOB',width=100)
       detail_frame=Frame(employee_frame)

       empid_label=Label(detail_frame,text='EmpId')
       empid_label.grid(row=0,column=0)


#GUI PART
#main tkinter class calling
root=Tk()

root.title('Dashboard')
#setting the width
root.geometry('1500x778+0+0')
root.resizable(0,0)
root.config(bg='white')
#inventary image
inv_image=PhotoImage(file='inventory.png')
#label for heading stock management system
label=Label(root,image=inv_image, compound=LEFT,text='Stock Management System',font=('times new roman',40,'bold'),bg='#962485',fg='white',anchor='w',padx=20)
label.place(x=0,y=0,relwidth=1)

 #label for loghout button
logbutton= Button(root,text='Logout',bg='#2490d0',font=('times new roman',20,'bold'))
logbutton.place(x=1300,y=10)

#subheading for time and date
subtitle=Label(root,text='welcom Aman Rai\t\t Date:01-11-2024\t\t Time:08:20pm',bg='#4d636d',fg='white',font=('times new roman',15))
subtitle.place(x=0,y=70,relwidth=1)

#left frame
leftFrame=Frame(root)
leftFrame.place(x=0,y=102,width=200,height=650)
# logo inside left frame
logoimage=PhotoImage(file='vendor.png')
imagelabel=Label(leftFrame,image=logoimage)
imagelabel.pack()
# menu for left frame

menulabel=Label(leftFrame,text='Menu',font=('times new roman',20),bg='#009688')
menulabel.pack(fill=X)

#employee image of left menu
empphoto=PhotoImage(file='staff.png')

emplyeebutt=Button(leftFrame,image=empphoto,compound=LEFT,text="  Employees",font=('times new roman',20,'bold'),anchor='w',padx=10,command=employee_form)
emplyeebutt.pack(fill=X);

#supplier image of left meny+button
suppphoto=PhotoImage(file='truck.png')
supplierbutt=Button(leftFrame,image=suppphoto,compound=LEFT, text="  Supplier",font=('times new roman',20,'bold'),anchor='w',padx=10)
supplierbutt.pack(fill=X);

#category image of left frame + button
categoryphoto=PhotoImage(file='categories.png')
categorybutt=Button(leftFrame, image=categoryphoto,compound=LEFT,text=" Category",font=('times new roman',20,'bold'),anchor='w',padx=10)
categorybutt.pack(fill=X);

#product image of left frame+button
productimage=PhotoImage(file='products.png')
productbutt=Button(leftFrame, image=productimage,compound=LEFT,text="  Product",font=('times new roman',20,'bold'),anchor='w',padx=10)
productbutt.pack(fill=X);
#sales image of left frame+ button
salesimage=PhotoImage(file='sales.png')
salesbutt=Button(leftFrame, image=salesimage,compound=LEFT,text="  Sales",font=('times new roman',20,'bold'),anchor='w',padx=10)
salesbutt.pack(fill=X);

#exit image +button on left frame
exitimage=PhotoImage(file='button.png')
exitbutt=Button(leftFrame, image=exitimage,compound=LEFT,text="  Exit",font=('times new roman',20,'bold'),anchor='w',padx=10)
exitbutt.pack(fill=X);

#on the middle employee frame
empframe=Frame(root,bg='#2C3E50',bd=3,relief=RIDGE)
empframe.place(x=400,y=125,height=170,width=280)

#employee frame image

total_empimage=PhotoImage(file='total_employees.png')
total_emp_icon_label=Label(empframe,image=total_empimage)
total_emp_icon_label.pack()

#employee frame text total employees
emptotal=Label(empframe,text='Total Employees',bg='#2C3E50',fg='white',font=('times new roman',15,'bold'))
emptotal.pack()
#emp count
empcount=Label(empframe,text='0',bg='#2C3E50',fg='white',font=('times new roman',30,'bold'))
empcount.pack()

emptotalcount=Label(empframe,text="0")

#supplier frame


supframe=Frame(root,bg='#8E44AD',bd=3,relief=RIDGE)
supframe.place(x=800,y=125,height=170,width=280)

#supplier frame image

total_suppimage=PhotoImage(file='supp.png')
total_supp_icon_label=Label(supframe,image=total_suppimage)
total_supp_icon_label.pack()

#supplier frame text total employees
suptotal=Label(supframe,text='Total Supplier',bg='#8E44AD',fg='white',font=('times new roman',15,'bold'))
suptotal.pack()
# supplier count
supcount=Label(supframe,text='0',bg='#8E44AD',fg='white',font=('times new roman',30,'bold'))
supcount.pack()

emptotalcount=Label(empframe,text="0")

#supplier frame
supframe=Frame(root,bg='#8E44AD',bd=3,relief=RIDGE)
supframe.place(x=800,y=125,height=170,width=280)

#supplier frame image

total_suppimage=PhotoImage(file='supp.png')
total_supp_icon_label=Label(supframe,image=total_suppimage)
total_supp_icon_label.pack()

#supplier frame text total employees
suptotal=Label(supframe,text='Total Supplier',bg='#8E44AD',fg='white',font=('times new roman',15,'bold'))
suptotal.pack()
# supplier count
supcount=Label(supframe,text='0',bg='#8E44AD',fg='white',font=('times new roman',30,'bold'))
supcount.pack()

#category frame
catframe=Frame(root,bg='#27AE60',bd=3,relief=RIDGE)
catframe.place(x=400,y=400,height=170,width=280)

#category frame image

total_catimage=PhotoImage(file='categories2.png')
total_cat_icon_label=Label(catframe,image=total_catimage)
total_cat_icon_label.pack()

#category  frame text total employees
cattotal=Label(catframe,text='Total categorie',bg='#27AE60',fg='white',font=('times new roman',15,'bold'))
cattotal.pack()
# category count
catcount=Label(catframe,text='0',bg='#27AE60',fg='white',font=('times new roman',30,'bold'))
catcount.pack()

#product frame
prodframe=Frame(root,bg='#27AE60',bd=3,relief=RIDGE)
prodframe.place(x=800,y=400,height=170,width=280)

#product  frame image

total_prodimage=PhotoImage(file='products2.png')
total_prod_icon_label=Label(prodframe,image=total_prodimage)
total_prod_icon_label.pack()

#product   frame text total employees
prodtotal=Label(prodframe,text='Total product',bg='#27AE60',fg='white',font=('times new roman',15,'bold'))
prodtotal.pack()
#product count
prodcount=Label(prodframe,text='0',bg='#27AE60',fg='white',font=('times new roman',30,'bold'))
prodcount.pack()

#product frame
salesframe=Frame(root,bg='#E74C3C',bd=3,relief=RIDGE)
salesframe.place(x=600,y=600,height=170,width=280)

#product  frame image

total_salesimage=PhotoImage(file='sale1.png')
total_sales_icon_label=Label(salesframe,image=total_salesimage)
total_sales_icon_label.pack()

#product   frame text total employees
salestotal=Label(salesframe,text='Total Sale',bg='#E74C3C',fg='white',font=('times new roman',15,'bold'))
salestotal.pack()
#product count
salescount=Label(salesframe,text='0',bg='#E74C3C',fg='white',font=('times new roman',30,'bold'))
salescount.pack()













root.mainloop()
