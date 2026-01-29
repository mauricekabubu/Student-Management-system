# importing tkinter for gui,messagebox for notifications,sqlite3 for database
import tkinter    # for graphical user interface
from tkinter import *
from  tkinter import messagebox   # for notifications as short messages
import sqlite3  # for database management
from tkinter.ttk import Combobox
import database



conn = sqlite3.connect('student.db')
database.create_table(conn)

# creating a class to define the student management system
class Student():
    def __init__(self,win):
        self.win = win

        win.title('STUDENT MANAGEMENT SYSTEM')
        win.geometry('600x400')
        win.config(bg='light grey')
        # creating labels,frames and buttons for main window
        frame0 = Frame(win, bg='light green', width=600, height=60)
        frame0.pack(side=TOP)
        label0 = Label(frame0, text='Student Management System', bg='light green', fg='blue',
                       font=('britannic bold', 25))
        label0.place(x=100, y=0)
        label1 = Label(win, text='Email or username', bg='light grey', fg='grey',
                       font=('britannic bold', 15))
        label1.place(x=200, y=60)
        entry0 = Entry(win, bg='white', width=50, bd=0, borderwidth=0)
        entry0.place(x=130, y=90)
        label2 = Label(win, text='password', bg='light grey', fg='grey',
                       font=('britannic bold', 15))
        label2.place(x=220, y=120)
        entry1 = Entry(win, bg='white', width=50, bd=0, borderwidth=0, show='*')
        entry1.place(x=130, y=150)
        button0 = Button(win, text='Forgot_password', bg='light grey', fg='blue',
                         font=('arial bold', 12), width=20, bd=0)
        button0.place(x=240, y=170)
        button1 = Button(win, text='Login', bg='green', fg='white',
                         font=('arial bold', 15), width=20, bd=0,command=lambda:self.main_window())
        button1.place(x=160, y=220)
        button2 = Button(win, text='create account', bg='green', fg='white',
                         font=('arial bold', 15), width=20,bd=0,command=lambda :self.create_account_window())
        button2.place(x=160, y=270)

    def create_account_window(self):
        self.delete_window()
        win.geometry('700x500')
        label11 = Label(win, text='first name', bg='light grey', fg='grey',
                       font=('britannic bold', 15))
        label11.place(x=80, y=10)
        entry10 = Entry(win, bg='white', width=40, bd=0, borderwidth=0)
        entry10.place(x=10, y=40)
        label20 = Label(win, text='last name', bg='light grey', fg='grey',
                       font=('britannic bold', 15))
        label20.place(x=80, y=60)
        entry11 = Entry(win, bg='white', width=40, bd=0, borderwidth=0)
        entry11.place(x=10, y=90)
        label12 = Label(win, text='phone number', bg='light grey', fg='grey',
                        font=('britannic bold', 15))
        label12.place(x=500, y=10)
        entry11 = Entry(win, bg='white', width=40, bd=0, borderwidth=0)
        entry11.place(x=430, y=40)
        label21 = Label(win, text='Email address', bg='light grey', fg='grey',
                        font=('britannic bold', 15))
        label21.place(x=500, y=60)
        entry12 = Entry(win, bg='white', width=40, bd=0, borderwidth=0)
        entry12.place(x=430, y=90)
        label22 = Label(win, text='Admission no.', bg='light grey', fg='grey',
                        font=('britannic bold', 15))
        label22.place(x=500, y=115)
        entry13 = Entry(win, bg='white', width=40, bd=0, borderwidth=0)
        entry13.place(x=430, y=145)
        label22 = Label(win, text='Nationality', bg='light grey', fg='grey',
                        font=('britannic bold', 15))
        label22.place(x=500, y=170)
        entry14 = Entry(win, bg='white', width=40, bd=0, borderwidth=0)
        entry14.place(x=430, y=195)
        label40 = Label(win, text='Course duration', bg='light grey', fg='grey',
                        font=('britannic bold', 15))
        label40.place(x=80, y=115)
        choices2 = ['1','2','3','4']
        drop_down2 = Combobox(win, values=choices2, font=('arial bold', 10), width=31)
        drop_down2.place(x=10, y=145)
        label42 = Label(win, text='Admission date', bg='light grey', fg='grey',
                        font=('britannic bold', 15))
        label42.place(x=80, y=170)
        entry43 = Entry(win, bg='white', width=40, bd=0, borderwidth=0)
        entry43.place(x=10, y=195)
        label44 = Label(win, text='Religion', bg='light grey', fg='grey',
                        font=('britannic bold', 15))
        label44.place(x=80, y=220)
        choices1 = ['Christianity','Islamic','Hindu','others']
        drop_down1 = Combobox(win, values=choices1, font=('arial bold', 10), width=31)
        drop_down1.place(x=10, y=245)
        label46 = Label(win, text='County no.', bg='light grey', fg='grey',
                        font=('britannic bold', 15))
        label46.place(x=500, y=220)
        choices0 = ['1','2','3','4','5','6','7','8','9','10']
        drop_down0 = Combobox(win, values=choices0, font=('arial bold', 10), width=31)
        drop_down0.place(x=430, y=245)
        label48 = Label(win, text='Guardian phone', bg='light grey', fg='grey',
                        font=('britannic bold', 15))
        label48.place(x=500, y=275)
        entry49 = Entry(win, bg='white', width=40, bd=0, borderwidth=0)
        entry49.place(x=430, y=300)
        label50 = Label(win, text='Form', bg='light grey', fg='grey',
                        font=('britannic bold', 15))
        label50.place(x=80, y=275)
        choices = ['1','2','3','4']
        drop_down = Combobox(win,values=choices,font=('arial bold',10),width=31)
        drop_down.place(x=10,y=300)

        check_box = Checkbutton(win,bg='white',text='male',width=5,bd=0,font=('arial bold',13))
        check_box.place(x=10,y=340)
        check_box = Checkbutton(win, bg='white', text='female', width=5, bd=0, font=('arial bold', 13))
        check_box.place(x=100, y=340)
        check_box = Checkbutton(win, bg='white', text='trans', width=5, bd=0, font=('arial bold', 13))
        check_box.place(x=190, y=340)
        label52 = Label(win, text='password', bg='light grey', fg='grey',
                        font=('britannic bold', 15))
        label52.place(x=500, y=320)
        entry53 = Entry(win, bg='white', width=40, bd=0, borderwidth=0,show='*')
        entry53.place(x=430, y=345)

        button10 = Button(win, text='create', bg='green', fg='white',
                         font=('arial bold', 15), width=20,bd=0)
        button10.place(x=180, y=380)
        button20 = Button(win, text='Back', bg='green', fg='white',
                         font=('arial bold', 15), width=20, bd=0, command=lambda: self.login_window())
        button20.place(x=180, y=430)

    def login_window(self):
        self.delete_window()
        win.geometry('600x400')
        frame0 = Frame(win, bg='light green', width=600, height=60)
        frame0.pack(side=TOP)
        label0 = Label(frame0, text='Student Management System', bg='light green', fg='blue',
                       font=('britannic bold', 25))
        label0.place(x=100, y=0)
        label1 = Label(win, text='Email or username', bg='light grey', fg='grey',
                       font=('britannic bold', 15))
        label1.place(x=200, y=60)
        entry0 = Entry(win, bg='white', width=50, bd=0, borderwidth=0)
        entry0.place(x=130, y=90)
        label2 = Label(win, text='password', bg='light grey', fg='grey',
                       font=('britannic bold', 15))
        label2.place(x=220, y=120)
        entry1 = Entry(win, bg='white', width=50, bd=0, borderwidth=0, show='*')
        entry1.place(x=130, y=150)
        button0 = Button(win, text='Forgot_password', bg='light grey', fg='blue',
                         font=('arial bold', 12),width=20,bd=0,command=lambda :database.insert(conn,entry1.get()))
        button0.place(x=240, y=170)
        button1 = Button(win, text='Login', bg='green', fg='white',
                         font=('arial bold', 15),width=20,bd=0,command=lambda :self.main_window())
        button1.place(x=160, y=220)
        button2 = Button(win, text='create account', bg='green', fg='white',
                         font=('arial bold', 15), width=20, bd=0, command=lambda: self.create_account_window())
        button2.place(x=160, y=270)

    def main_window(self):
        self.delete_window()
        win.geometry('1200x500')
        l0 = Label(win,text='Welcome to the:\n'
                            'STUDENT MANAGEMENT SYSTEM',bg='light grey',fg='purple',
                   font=('black adder ITC bold',40))
        l0.place(x=150,y=150)
        frame1 = Frame(win,bg='light green',width=1200,height=40)
        frame1.pack(side=TOP)
        button20 = Button(frame1, text='Home', bg='light green', fg='blue',
                         font=('arial bold', 15), width=20, bd=0)
        button20.place(x=10, y=0)

        button21 = Button(frame1,text='Account',bg='light green',fg='blue',
                         font=('arial bold',15),width=20,bd=0,command=self.account_window)
        button21.place(x=190, y=0)

        button22 = Button(frame1, text='Academics', bg='light green', fg='blue',
                         font=('arial bold',15),width=20,bd=0,command=self.academics_account)
        button22.place(x=370, y=0)

        button23 = Button(frame1, text='Fees', bg='light green', fg='blue',
                          font=('arial bold', 15), width=20, bd=0,command=self.fees_window)
        button23.place(x=550, y=0)

        button24 = Button(frame1, text='Courses', bg='light green', fg='blue',
                          font=('arial bold', 15), width=20,bd=0,command=lambda :self.course_window())
        button24.place(x=730, y=0)

        button25 = Button(frame1, text='Settings', bg='light green', fg='blue',
                          font=('arial bold',15),width=20,bd=0,command=self.settings_window)
        button25.place(x=910, y=0)

    def course_window(self):
        self.delete_window()
        win.geometry('800x400')
        win.config(bg='light green')
        win.title('Student Account Settings Window')
        frame10 = Frame(win,bg='light yellow',width=800,height=20)
        frame10.pack(side=TOP)
        l20 = Label(win,text='Select courses:',bg='light grey',fg='red',
                    font=('gotham bold',25))
        l20.place(x=300,y=25)
        check_box1 = Checkbutton(win, bg='white', text='MATHS', width=10,bd=0,font=('arial bold', 13))
        check_box1.place(x=30, y=70)
        check_box2 = Checkbutton(win, bg='white', text='ENGLISH', width=10, bd=0,font=('arial bold', 13))
        check_box2.place(x=30, y=100)
        check_box3 = Checkbutton(win, bg='white', text='SWAHILI', width=10, bd=0,font=('arial bold', 13))
        check_box3.place(x=30, y=130)
        check_box4 = Checkbutton(win, bg='white', text='PHYSICS', width=10, bd=0, font=('arial bold', 13))
        check_box4.place(x=30, y=160)
        check_box5 = Checkbutton(win, bg='white', text='CHEMISTRY', width=10, bd=0, font=('arial bold', 13))
        check_box5.place(x=30, y=190)
        check_box6 = Checkbutton(win, bg='white', text='BIOLOGY', width=10, bd=0, font=('arial bold', 13))
        check_box6.place(x=30, y=220)
        check_box7 = Checkbutton(win, bg='white', text='HISTORY', width=10, bd=0, font=('arial bold', 13))
        check_box7.place(x=250, y=70)
        check_box8 = Checkbutton(win, bg='white', text='GEOGRAPHY', width=10, bd=0, font=('arial bold', 13))
        check_box8.place(x=250, y=100)
        check_box9 = Checkbutton(win, bg='white', text='CRE', width=10, bd=0, font=('arial bold', 13))
        check_box9.place(x=250, y=130)
        check_box10 = Checkbutton(win, bg='white', text='GERMAN', width=10, bd=0, font=('arial bold', 13))
        check_box10.place(x=250, y=160)
        check_box11 = Checkbutton(win, bg='white', text='FRENCH', width=10, bd=0, font=('arial bold', 13))
        check_box11.place(x=250, y=190)
        check_box12 = Checkbutton(win, bg='white', text='SPANISH', width=10, bd=0, font=('arial bold', 13))
        check_box12.place(x=250, y=220)
        check_box13 = Checkbutton(win, bg='white', text='MUSIC', width=10, bd=0, font=('arial bold', 13))
        check_box13.place(x=470, y=70)
        check_box14 = Checkbutton(win, bg='white', text='ART', width=10, bd=0, font=('arial bold', 13))
        check_box14.place(x=470, y=100)
        check_box15 = Checkbutton(win, bg='white', text='COMPUTING', width=10, bd=0, font=('arial bold', 13))
        check_box15.place(x=470, y=130)
        button50 = Button(win, text='Send', bg='blue', fg='white',
                          font=('arial bold', 15), width=20, bd=0)
        button50.place(x=280, y=280)
        button60 = Button(win, text='Back', bg='red', fg='white',
                          font=('arial bold', 15), width=20, bd=0,command=lambda: self.main_window())
        button60.place(x=280, y=320)

        check_box = Checkbutton(win, bg='white', text='WOODWORK', width=10, bd=0, font=('arial bold', 13))
        check_box.place(x=470, y=160)
        check_box = Checkbutton(win, bg='white', text='DESIGN', width=10, bd=0, font=('arial bold', 13))
        check_box.place(x=470, y=190)
        check_box = Checkbutton(win, bg='white', text='IRE', width=10, bd=0, font=('arial bold', 13))
        check_box.place(x=470, y=220)
        check_box = Checkbutton(win, bg='white', text='WRITING', width=10, bd=0, font=('arial bold', 13))
        check_box.place(x=670, y=70)
        check_box = Checkbutton(win, bg='white', text='CODING', width=10, bd=0, font=('arial bold', 13))
        check_box.place(x=670, y=100)
        check_box = Checkbutton(win, bg='white', text='BUSINESS', width=10, bd=0, font=('arial bold', 13))
        check_box.place(x=670, y=130)
        check_box = Checkbutton(win, bg='white', text='ROBOTICS', width=10, bd=0, font=('arial bold', 13))
        check_box.place(x=670, y=160)
        check_box = Checkbutton(win, bg='white', text='ONLINE', width=10, bd=0, font=('arial bold', 13))
        check_box.place(x=670, y=190)
        check_box = Checkbutton(win, bg='white', text='MARKETING', width=10, bd=0, font=('arial bold', 13))
        check_box.place(x=670, y=220)

    def fees_window(self):
        self.delete_window()
        win.geometry('600x400')
        win.config(bg='light blue')
        list_box0 = Listbox(win,bg='white',width=50,height=20)
        list_box0.pack(side=RIGHT)
        but0 = Button(win,text='pay fees',bg='green',fg='white',font=('arial bold',15),
                      width=20,bd=0,command=self.pay_fee)
        but0.place(x=20,y=50)
        but1 = Button(win, text='Check balance', bg='green', fg='white', font=('arial bold', 15),
                      width=20, bd=0)
        but1.place(x=20, y=110)
        but2 = Button(win, text='Fees Statement', bg='green', fg='white', font=('arial bold', 15),
                      width=20, bd=0)
        but2.place(x=20, y=170)
        but3 = Button(win, text='Back', bg='yellow', fg='black', font=('arial bold', 15),
                      width=20, bd=0,command=self.main_window)
        but3.place(x=20, y=230)

    def pay_fee(self):
        self.delete_window()
        win.geometry('600x200')
        win.config(bg='white')
        label100 = Label(win, text='Enter account no:', bg='white',fg='black',
                       font=('britannic bold', 15))
        label100.place(x=200, y=10)
        entry100 = Entry(win, bg='light grey', width=50, bd=0, borderwidth=0)
        entry100.place(x=130, y=40)
        label200 = Label(win, text='Enter password', bg='white', fg='black',
                       font=('britannic bold', 15))
        label200.place(x=220, y=60)
        entry101 = Entry(win, bg='light grey', width=50, bd=0, borderwidth=0, show='*')
        entry101.place(x=130, y=90)
        butt3 = Button(win, text='Send', bg='green', fg='black', font=('arial bold', 15),
                      width=20, bd=0)
        butt3.place(x=160, y=130)

    def account_window(self):
        self.delete_window()
        win.geometry('800x500')
        win.title('Student Account')
        win.config(bg='light grey')
        frame10 = Frame(win,bg='light green',width=800,height=50)
        frame10.pack(side=TOP)
        l10 = Label(frame10,text='Student Details',bg='light green',
                    fg='blue',font=('gotham bold',20))
        l10.place(x=200,y=0)

        def toggle_frame():
            frame_toggle = Frame(win,bg='green',width=200,height=500)
            frame_toggle.pack(side=LEFT)
            butt7 = Button(win, text='<<<', bg='green', fg='white',
                          font=('arial bold', 13), width=10, bd=0,command=self.account_window)
            butt7.place(x=0, y=50)
            but0 = Button(win,text='Student profile',bg='green',fg='white',
                          font=('arial bold',15),width=15,bd=0)
            but0.place(x=0,y=80)
            but1 = Button(win, text='Update Profile', bg='green', fg='white',
                          font=('arial bold', 15), width=15, bd=0)
            but1.place(x=0, y=120)
            but2 = Button(win, text='Certify', bg='green', fg='white',
                          font=('arial bold', 15), width=15, bd=0)
            but2.place(x=0, y=160)
            but3 = Button(win, text='Register', bg='green', fg='white',
                          font=('arial bold', 15), width=15, bd=0)
            but3.place(x=0, y=200)
            but4 = Button(win, text='Principal evaluation', bg='green', fg='white',
                          font=('arial bold', 15), width=15, bd=0)
            but4.place(x=0, y=240)
            but5 = Button(win, text='Academic guide', bg='green', fg='white',
                          font=('arial bold', 15), width=15, bd=0)
            but5.place(x=0, y=280)
            but6 = Button(win, text='Term registration', bg='green', fg='white',
                          font=('arial bold', 15), width=15, bd=0)
            but6.place(x=0, y=320)
            but7 = Button(win, text='School links', bg='green', fg='white',
                          font=('arial bold', 15), width=15, bd=0)
            but7.place(x=0, y=360)
            but8 = Button(win, text='Results', bg='green', fg='white',
                          font=('arial bold', 15), width=15, bd=0)
            but8.place(x=0, y=400)
            but9 = Button(win, text='Comments', bg='green', fg='white',
                          font=('arial bold', 15), width=15, bd=0)
            but9.place(x=0, y=440)




        toggle_button = Button(frame10,text='=',bg='light green',font=('arial bold',30),
                               width=0,bd=0,fg='grey',command=toggle_frame)
        toggle_button.place(x=0,y=0)
        first_name = Label(win,text='First name:',bg='light grey',fg='black',
                           font=('arial bold',15))
        first_name.place(x=10,y=60)
        list_box10 = Listbox(win, bg='white', width=30, height=1)
        list_box10.place(x=140, y=70)
        last_name = Label(win, text='Last name:', bg='light grey', fg='black',
                           font=('arial bold', 15))
        last_name.place(x=10, y=90)
        list_box11 = Listbox(win,bg='white',width=30,height=1)
        list_box11.place(x=140,y=100)
        email = Label(win, text='Email add:', bg='light grey', fg='black',
                           font=('arial bold', 15))
        email.place(x=10, y=120)
        list_box12 = Listbox(win, bg='white', width=30, height=1)
        list_box12.place(x=140, y=130)
        phone = Label(win, text='Phone no:', bg='light grey', fg='black',
                           font=('arial bold', 15))
        phone.place(x=10, y=150)
        list_box13 = Listbox(win, bg='white', width=30, height=1)
        list_box13.place(x=140, y=160)
        nationality = Label(win, text='Nationality:', bg='light grey', fg='black',
                      font=('arial bold', 15))
        nationality.place(x=10, y=180)
        list_box14 = Listbox(win, bg='white', width=30, height=1)
        list_box14.place(x=140, y=190)
        religion = Label(win, text='Religion:', bg='light grey', fg='black',
                      font=('arial bold', 15))
        religion.place(x=10, y=210)
        list_box15 = Listbox(win, bg='white', width=30, height=1)
        list_box15.place(x=140, y=220)
        admission = Label(win, text='Admission no:', bg='light grey', fg='black',
                      font=('arial bold', 15))
        admission.place(x=10, y=240)
        list_box16 = Listbox(win, bg='white', width=30, height=1)
        list_box16.place(x=160, y=250)
        date = Label(win, text='Admission date:', bg='light grey', fg='black',
                      font=('arial bold', 15))
        date.place(x=10, y=270)
        list_box17 = Listbox(win, bg='white', width=30, height=1)
        list_box17.place(x=160, y=280)
        county = Label(win, text='County no:', bg='light grey', fg='black',
                      font=('arial bold', 15))
        county.place(x=10, y=300)
        list_box18 = Listbox(win, bg='white', width=30, height=1)
        list_box18.place(x=140, y=310)
        course_dur = Label(win, text='Course dur:', bg='light grey', fg='black',
                      font=('arial bold', 15))
        course_dur.place(x=10, y=330)
        list_box19 = Listbox(win, bg='white', width=30, height=1)
        list_box19.place(x=140, y=340)
        form = Label(win, text='Form:', bg='light grey', fg='black',
                      font=('arial bold', 15))
        form.place(x=10, y=360)
        list_box20 = Listbox(win, bg='white', width=30, height=1)
        list_box20.place(x=140, y=370)
        courses_done = Label(win,text='Courses selected',bg='light grey',fg='red',
                             font=('arial bold',20))
        courses_done.place(x=450,y=50)
        main_list = Listbox(win,bg='yellow',width=50,height=20)
        main_list.place(x=400,y=80)

    def academics_account(self):
        self.delete_window()
        win.geometry('700x500')
        win.config(bg='light grey')
        win.title('Academics Report')
        frame_a = Frame(win,bg='light green',width=800,height=30)
        frame_a.pack(side=TOP)
        courses_done1 = Label(win, text='Courses selected', bg='light grey', fg='red',
                             font=('arial bold', 20))
        courses_done1.place(x=30, y=50)
        main_list100 = Listbox(win, bg='yellow', width=50, height=20)
        main_list100.place(x=0, y=80)
        grades = Label(win, text='Results', bg='light grey', fg='red',
                             font=('arial bold', 20))
        grades.place(x=480, y=50)
        main_list101 = Listbox(win, bg='yellow', width=50, height=20)
        main_list101.place(x=395, y=80)

    def settings_window(self):
        self.delete_window()
        win.geometry('600x400')
        win.title('Settings')
        win.config(bg='light green')
        butt30 = Button(win,text='Change password',bg='white',fg='black',
                        font=('arial bold',15),width=20,bd=0)
        butt30.place(x=180,y=10)
        options = ['English','Swahili','Spanish','German','French','Italian']
        label_a = Label(win,text='Select Language',bg='light green',fg='grey',
                        font=('arial bold',15))
        label_a.place(x=200,y=50)
        menu_button = Combobox(win,values=options,background='light green',foreground='white',
                               font=('gotham bold',15))
        menu_button.place(x=180,y=80)
        butt31 = Button(win, text='Light mode', bg='white', fg='black',
                        font=('arial bold', 15),width=20,bd=0,command=self.settings_window1)
        butt31.place(x=180, y=120)
        butt32 = Button(win, text='Change password', bg='white', fg='black',
                        font=('arial bold', 15), width=20, bd=0)
        butt32.place(x=180, y=180)
        butt33 = Button(win, text='create new account', bg='white', fg='black',
                        font=('arial bold',15),width=20,bd=0,command=self.create_account_window)
        butt33.place(x=180, y=240)
        butt34 = Button(win, text='Switch account', bg='white', fg='black',
                        font=('arial bold', 15), width=20, bd=0)
        butt34.place(x=180, y=300)

    def settings_window1(self):
        self.delete_window()
        win.geometry('600x400')
        win.title('Settings')
        win.config(bg='black')
        butt30 = Button(win,text='Change password',bg='white',fg='blue',
                        font=('arial bold',15),width=20,bd=0)
        butt30.place(x=180,y=10)
        options = ['English','Swahili','Spanish','German','French','Italian']
        label_a = Label(win,text='Select Language',bg='black',fg='grey',
                        font=('arial bold',15))
        label_a.place(x=200,y=50)
        menu_button = Combobox(win,values=options,background='light green',foreground='white',
                               font=('gotham bold',15))
        menu_button.place(x=180,y=80)
        butt31 = Button(win, text='Dark mode', bg='grey', fg='black',
                        font=('arial bold', 15),width=20,bd=0,command=self.settings_window)
        butt31.place(x=180, y=120)
        butt32 = Button(win, text='Change password', bg='white', fg='blue',
                        font=('arial bold', 15), width=20, bd=0)
        butt32.place(x=180, y=180)
        butt33 = Button(win, text='create new account', bg='white', fg='blue',
                        font=('arial bold',15),width=20,bd=0,command=self.create_account_window)
        butt33.place(x=180, y=240)
        butt34 = Button(win, text='Switch account', bg='white', fg='blue',
                        font=('arial bold', 15), width=20, bd=0)
        butt34.place(x=180, y=300)


    def delete_window(self):
        for item in win.winfo_children():
            item.destroy()




win = Tk()
object = Student(win)

win.mainloop()




