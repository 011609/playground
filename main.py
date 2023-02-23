import tkinter

window = tkinter.Tk()

window.geometry('400x400+1200+150')
window.title('창 이름')
window.resizable(False, False)

count=0

def countUP():
    global count
    count +=1
    label.config(text=str(count))

label = tkinter.Label(window, text="0")
label.pack()

button = tkinter.Button(window, overrelief="solid", width=15, command=countUP, repeatdelay=1000, repeatinterval=100)
button.pack()

window.mainloop()