from tkinter import *
import test_database as td
import Data_Graph as dg
import data_visual as dv



def main():

#list Defaulter command
    def output_database():
        op.delete(0,END)
        op.insert(END, 'Defaulter')
        for i in td.td1():
            op.insert(END, i)
    def clear_text():
        op.delete(0,END)

    def all_data():
        op.delete(0,END)
        op.insert(END,'Name Attendance Subject Subject_Code')
        for i in td.td2():
            op.insert(END, i)

        dg.data()

    def inp_text():
        x = text_entry.get()
        dv.data_vis1(x)
        

    window = Tk()
    text_input = StringVar()
    searc = PhotoImage(file = r'C:\Users\aaris\Downloads\Data-Visualization-Using-Matplotlib-master\search.png')
    search = searc.subsample(20, 20)
    clea = PhotoImage(file = r'C:\Users\aaris\Downloads\Data-Visualization-Using-Matplotlib-master\clear.png')
    clear = clea.subsample(20, 20)
    sho = PhotoImage(file = r'C:\Users\aaris\Downloads\Data-Visualization-Using-Matplotlib-master\find.png')
    show = sho.subsample(20, 20)
    ques = PhotoImage(file = r'C:\Users\aaris\Downloads\Data-Visualization-Using-Matplotlib-master\question.png')
    quest = ques.subsample(20, 20)
    text_entry = Entry(window, textvariable = 'text_input', border= 1,font = (20))
    window.title('Attendance Management System')#Ploting the titlte
    window.iconbitmap(r'C:\Users\aaris\Downloads\Data-Visualization-Using-Matplotlib-master\favicon.ico')
    label = Label(window,text= 'Welcome To Attendance Management System',font = ('bold',16))#ploting the label
    btn = Button(window, text = 'Defaulters',command = output_database, image = quest, compound = LEFT, relief = GROOVE, border = 1 )
    btn2 = Button(window, text = 'Search',  command = inp_text, image = search, compound = LEFT, relief = GROOVE, border = 1)
    btn3 = Button(window, text = 'Show All',command = all_data, image = show, compound = LEFT, relief = GROOVE, border = 1)

    op = Listbox(window, height = 10, width = 100, border = 0)

    scroll = Scrollbar(window)
    #scroll option or scroll config
    op.configure(yscrollcommand = scroll.set)
    scroll.configure(command = op.yview)

    clr_btn = Button(window, text = 'CLear', command = clear_text, image = clear, compound = LEFT, relief = GROOVE, border = 1 )
    
    label.pack()

    btn.place(x = 30, y = 50 )
    
    btn2.place(x = 260, y = 150)
    btn3.place(x = 30, y = 100)
    text_entry.place(x = 30, y = 150, height = 30, width = 200)
    op.place(x = 30, y = 190)
    scroll.place(x = 630,y = 190, height = 160)
    clr_btn.place(x = 630, y = 360)
    
    window.geometry('720x480')
    
    window.mainloop() 

if __name__ == "__main__":
    main()