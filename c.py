
from tkinter import *
# from turtle import width
root=Tk()
def send():
    send="you=>"+e.get()
    txt.insert(END,"\n"+send)
    if (e.get()=="hello"):
        txt.insert(END,"\n"+"                                                                                                       bot=>hi")
    elif  (e.get()=="hi"):
        txt.insert(END,"\n"+"                                                                                                       bot=>hello")
    elif  (e.get()=="how are you"):
        txt.insert(END,"\n"+"                                                                                                      bot=>i am fine and you")
    elif  (e.get()=="i am fine and you"):
        txt.insert(END,"\n"+"                                                                                                       bot=>nice to hear")
    elif  (e.get()=="can you help me"):
        txt.insert(END,"\n"+"                                                                                                       bot=>yes")
    else:
        txt.insert(END,"\n"+"                                                                                                       bot=>sorry i didnt get it")
    e.delete(0,END)

txt=Text(root)
txt.grid(row=0,column=0,columnspan=7)
e=Entry(root,width=70)
send=Button(root,text="send",bg="green",command=send).grid(row=1,column=1)
e.grid(row=1,column=0)
root.title("CHATBOT")
root.mainloop()

