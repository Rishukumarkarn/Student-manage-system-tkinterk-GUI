from  tkinter import *
from tkinter import ttk
import pymysql

class Student:
     def __init__(self,root):
         self.root=root
         self.root.title('Student Management System')
         self.root.geometry("1350x700+0+0")
         

         title=Label(self.root,text="Student Management System",bd=10,font=("time new roman",40,"bold"),fg="dark violet",bg='light grey')
         title.pack(side=TOP,fill=X)

# All variable
         self.Roll_No_var=StringVar()

         self.Name_var=StringVar()

         self.Email_var=StringVar()
         self.Gender_var=StringVar()
         self.Contact_var=StringVar()
         self.Dob_var=StringVar()

         # search variable
         self.search_by=StringVar()
         self.search_txt=StringVar()


# manage frame
         manage_frame=Frame(self.root,relief=RIDGE,bg="#3E6AA5",bd=4)
         manage_frame.place(x=20,y=100,width=450,height=570)

         m_title=Label(manage_frame,text="Manage Student",font=("time new roman",30,"bold"),bg="#3E6AA5", fg="dark goldenrod")
         m_title.grid(row=0,columnspan=2,pady=10,padx=50)
         lbl_Roll=Label(manage_frame,text="Roll No. :-",font=("time new roman",15,"bold"),bg="#3E6AA5")
         lbl_Roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")

         txt_Roll=Entry(manage_frame,textvariable=self.Roll_No_var,font=("time new roman",15,"bold"),bd=3,relief=GROOVE)
         txt_Roll.grid(row=1, column=1, pady=10, padx=15, sticky="w")

         lbl_Name = Label(manage_frame, text="Name :-", font=("time new roman", 15, "bold"), bg="#3E6AA5")
         lbl_Name.grid(row=2, column=0, pady=10, padx=20, sticky="w")

         txt_Name = Entry(manage_frame,textvariable=self.Name_var, font=("time new roman", 15, "bold"), bd=3, relief=GROOVE)
         txt_Name.grid(row=2, column=1, pady=10, padx=15, sticky="w")

         lbl_Email = Label(manage_frame, text="Email :-", font=("time new roman", 15, "bold"), bg="#3E6AA5")
         lbl_Email.grid(row=3, column=0, pady=10, padx=20, sticky="w")

         txt_Email = Entry(manage_frame,textvariable=self.Email_var, font=("time new roman", 15, "bold"), bd=3, relief=GROOVE)
         txt_Email.grid(row=3, column=1, pady=10, padx=15, sticky="w")

         lbl_Gender = Label(manage_frame, text="Gender :-", font=("time new roman", 15, "bold"), bg="#3E6AA5")
         lbl_Gender.grid(row=4, column=0, pady=10, padx=20, sticky="w")

         combo_Gender=ttk.Combobox(manage_frame,textvariable=self.Gender_var,width=23, font=("time new roman", 13, "bold"),state="readonly")
         combo_Gender['values']=("Male","Female","other")
         combo_Gender.grid(row=4,column=1, pady=10, padx=15, sticky="w")


         lbl_Contact = Label(manage_frame, text="Contact :-", font=("time new roman", 15, "bold"), bg="#3E6AA5")
         lbl_Contact.grid(row=5, column=0, pady=10, padx=20, sticky="w")

         txt_Contact = Entry(manage_frame,textvariable=self.Contact_var, font=("time new roman", 15, "bold"), bd=3, relief=GROOVE)
         txt_Contact.grid(row=5, column=1, pady=10, padx=15, sticky="w")

         lbl_Dob = Label(manage_frame, text="D.O.B :-", font=("time new roman", 15, "bold"), bg="#3E6AA5")
         lbl_Dob.grid(row=6, column=0, pady=10, padx=20, sticky="w")

         txt_Dob = Entry(manage_frame,textvariable=self.Dob_var, font=("time new roman", 15, "bold"), bd=3, relief=GROOVE)
         txt_Dob.grid(row=6, column=1, pady=10, padx=15, sticky="w")

         lbl_Address = Label(manage_frame, text="Address :-", font=("time new roman", 15, "bold"), bg="#3E6AA5")
         lbl_Address.grid(row=7, column=0, pady=10, padx=20, sticky="w")

         self.txt_Address=Text(manage_frame,width=28,height=4,bd=2)
         self.txt_Address.grid(row=7,column=1, pady=10, padx=15, sticky="w")
# Bottom frame

         Btn_frame = Frame(manage_frame, relief=RIDGE, bg="#3E6AA5", bd=2)
         Btn_frame.place(x=10, y=510, width=420)

         Addbtn=Button(Btn_frame,text="Add",width=10,command=self.add_students,bg="#581845").grid(row=0,column=0,padx=10,pady=6)
         Updatebtn=Button(Btn_frame,text="Update",width=10,command=self.update_data,bg="#FF5733").grid(row=0,column=1,padx=10,pady=6)
         Deletebtn = Button(Btn_frame, text="Delete", width=10,command=self.delete_data,bg="#C70039").grid(row=0, column=2, padx=10,pady=6)
         Clearbtn = Button(Btn_frame, text="Clear", width=10,command=self.clear,bg="#900C3F").grid(row=0, column=3, padx=10,pady=6)






# Detil frame

         detail_frame=Frame(self.root,relief=RIDGE,bg="#3E6AA5",bd=4)
         detail_frame.place(x=500,y=100,width=800,height=570)

         lbl_Search = Label(detail_frame, text="Search By", font=("time new roman", 20, "bold"), bg="#3E6AA5",fg="dark goldenrod")
         lbl_Search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

         combo_Search = ttk.Combobox(detail_frame,width=10,textvariable=self.search_by, font=("time new roman", 13, "bold"), state="readonly")
         combo_Search['values'] = ("Roll_No", "Name", "Class","Contact")
         combo_Search.grid(row=0, column=1, pady=10, padx=15, sticky="w")

         txt_Search = Entry(detail_frame,textvariable=self.search_txt ,font=("time new roman", 12, "bold"), bd=3, relief=GROOVE)
         txt_Search.grid(row=0, column=2, pady=10, padx=15, sticky="w")

         Searchbtn = Button(detail_frame,command=self.search_data, text="Search", width=10,bg="#DAF7A6").grid(row=0, column=3, padx=10, pady=6)
         Showallbtn = Button(detail_frame, command=self.fetch_data,text="Show All", width=10,bg="#FFC300").grid(row=0, column=4, padx=10, pady=6)

# Table frame
         table_frame = Frame(detail_frame, relief=RIDGE, bg="crimson", bd=2)
         table_frame.place(x=10, y=70, width=780, height=470)

         scroll_x=Scrollbar(table_frame,orient=HORIZONTAL)
         scroll_y=Scrollbar(table_frame,orient=VERTICAL)
         self.Student_table=ttk.Treeview(table_frame,columns=("Roll","Name","Email","Gender","Contact","D.O.B","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
         scroll_x.pack(side=BOTTOM,fill=X)
         scroll_y.pack(side=RIGHT,fill=Y)
         scroll_x.config(command=self.Student_table.xview)
         scroll_y.config(command=self.Student_table.yview)
         self.Student_table.heading("Roll",text="Roll No.")
         self.Student_table.heading("Name",text="Name")
         self.Student_table.heading("Email",text="Email")
         self.Student_table.heading("Gender",text="Gender")
         self.Student_table.heading("Contact",text="Contact")
         self.Student_table.heading("D.O.B",text="D.O.B")
         self.Student_table.heading("Address",text="Address")
         self.Student_table['show']='headings'
         self.Student_table.column("Roll",width=50)
         self.Student_table.column("Name",width=100)
         self.Student_table.column("Email",width=150)
         self.Student_table.column("Gender",width=30)
         self.Student_table.column("Contact",width=50)
         self.Student_table.column("D.O.B",width=50)
         self.Student_table.column("Address",width=150)
         self.Student_table.pack(fill=BOTH,expand=1)
         self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)
         self.fetch_data()

     def add_students(self):
        con=pymysql.connect(host="localhost",user="root",passwd="",db="stmm")
        cur=con.cursor()
        cur.execute("insert into students value(%s,%s,%s,%s,%s,%s,%s)",(
            self.Roll_No_var.get(),
            self.Name_var.get(),
            self.Email_var.get(),
            self.Gender_var.get(),
            self.Contact_var.get(),
            self.Dob_var.get(),
            self.txt_Address.get("1.0",END)
        ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

     def fetch_data(self):
         con = pymysql.connect(host="localhost", user="root", passwd="", db="stmm")
         cur = con.cursor()
         cur.execute("SELECT * FROM `students` ")
         rows=cur.fetchall()
         if len(rows)!=0:
             self.Student_table.delete(*self.Student_table.get_children())
             for row in rows:
                 self.Student_table.insert('',END,values=row)
             con.commit()
         con.close()
     def clear(self):
         self.Roll_No_var.set(""),
         self.Name_var.set(""),
         self.Email_var.set(""),
         self.Gender_var.set(""),
         self.Contact_var.set(""),
         self.Dob_var.set(""),
         self.txt_Address.delete("1.0", END)

     def get_cursor(self,ev):
            cursor_row=self.Student_table.focus()
            contents=self.Student_table.item(cursor_row)
            row=contents['values']
            print(row)
            self.Roll_No_var.set(row[0]),
            self.Name_var.set(row[1]),
            self.Email_var.set(row[2]),
            self.Gender_var.set(row[3]),
            self.Contact_var.set(row[4]),
            self.Dob_var.set(row[5]),
            self.txt_Address.delete("1.0", END)
            self.txt_Address.insert(END,row[6])
     def update_data(self):

         con = pymysql.connect(host="localhost", user="root", passwd="", db="stmm")
         cur = con.cursor()
         cur.execute("update students set Name=%s,Email=%s,Gender=%s,Contact=%s , Dob=%s , Address=%s where Roll_NO=%s", (

             self.Name_var.get(),
             self.Email_var.get(),
             self.Gender_var.get(),
             self.Contact_var.get(),
             self.Dob_var.get(),
             self.txt_Address.get("1.0", END),
             self.Roll_No_var.get()

         ))
         con.commit()
         self.fetch_data()
         self.clear()
         con.close()
     def delete_data(self):
         con = pymysql.connect(host="localhost", user="root", passwd="", db="stmm")
         cur = con.cursor()
         cur.execute("DELETE FROM `students` WHERE Roll_No=%s ",self.Roll_No_var.get())
         con.commit()
         con.close()
         self.fetch_data()
         self.clear()

     def search_data(self):
         con = pymysql.connect(host="localhost", user="root", passwd="", db="stmm")
         cur = con.cursor()
         cur.execute("SELECT * FROM students WHERE " + str(self.search_by.get()) + "= %s", (str(self.search_txt.get()) ))
         rows=cur.fetchall()
         if len(rows)!=0:
             self.Student_table.delete(*self.Student_table.get_children())
             for row in rows:
                 self.Student_table.insert('',END,values=row)
             con.commit()
         con.close()

root=Tk()
ob=Student(root)
root.mainloop()
