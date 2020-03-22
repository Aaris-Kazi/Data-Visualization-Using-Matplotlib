from tkinter import *
import test_database as td
import Data_Graph as dg
import data_visual as dv


def clear_text():
    print('')

def main():
    window = Tk()
    text_input = StringVar()
    text_entry = Entry(window, textvariable = 'text_input', border= 1,font = (20))
    window.title('Attendance Management System')#Ploting the titlte
    label = Label(window,text= 'Welcome To Attendance Management System',font = ('bold',16))#ploting the label
    btn = Button(window, text = 'To show all defaulter',command = td.td )
    btn1 = Button(window, text = 'To show all Graph Data',command = dg.data)
    btn2 = Button(window, text = 'To show Specific Graph Data',command = dv.data_vis)

    
    
    op = Listbox(window, height = 10, width = 100, border = 0)

    scroll = Scrollbar(window)
    #scroll option or scroll config
    op.configure(yscrollcommand = scroll.set)
    scroll.configure(command = op.yview)
    #list lcearing command
    for i in dg.show():
        op.insert(END, i)

    clr_btn = Button(window, text = 'CLear', command = clear_text() )
    label.pack()

    btn.place(x = 30, y = 50 )
    btn1.place(x = 30, y = 100)
    btn2.place(x = 260, y = 150)
    text_entry.place(x = 30, y = 150, height = 30, width = 200)
    op.place(x = 30, y = 190)
    scroll.place(x = 630,y = 190, height = 160)
    clr_btn.place(x = 630, y = 360)
    window.geometry('720x480')

    window.mainloop() 

if __name__ == "__main__":
    main()
