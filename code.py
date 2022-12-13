from tkinter import *
import tkinter.messagebox
tk = Tk()
tk.title('tic tac toe game ')
playerA = StringVar()
playerB = StringVar()
player1name = Entry(tk, textvariable=playerA, bd=5)
player1name.grid(row=1, column=1, columnspan=8)
player2name = Entry(tk, textvariable=playerB, bd=5)
player2name.grid(row=2, column=1, columnspan=8)
bclick = True
flag = 0


def clickbutton(button):
    global bclick, flag
    if button['text'] == ' ' and bclick == True:
        button['text'] = 'X'
        bclick = False
        flag=flag+1
        checkforwin()
        
    elif button['text'] == ' ' and bclick == False:
        button['text'] = 'O'
        bclick = True
        flag = flag+1
        checkforwin()
        


def disablebuttons():
    button1.configure(state=DISABLED)
    button2.configure(state=DISABLED)
    button3.configure(state=DISABLED)
    button4.configure(state=DISABLED)
    button5.configure(state=DISABLED)
    button6.configure(state=DISABLED)
    button7.configure(state=DISABLED)
    button8.configure(state=DISABLED)
    button9.configure(state=DISABLED)


def checkforwin():
    if (button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X'
       or button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X'
       or button7['text'] == 'X' and button8['text'] == 'X' and button9['text'] == 'X'
       or button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X'
       or button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X'
       or button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X'
       or button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X'
       or button3['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X'):
        disablebuttons()
        tkinter.messagebox.showinfo('tik-tak-toe', playerA.get() +' Wins!!')
    elif (button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O'
       or button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O'
       or button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O'
       or button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O'
       or button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O'
       or button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O'
       or button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O'
       or button3['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O'):
        disablebuttons()
        tkinter.messagebox.showinfo('tik-tak-to', playerB.get() + ' Wins!!')
    elif (flag==9):
        tkinter.messagebox.showinfo('tik-tak-toe','Its a draw')


label = Label(tk, text='Player 1:', font='Times 20 bold',
              bg='white', fg='black', height=1, width=8)
label.grid(row=1, column=0)
label = Label(tk, text='Player 2:', font='Times 20 bold',
              bg='white', fg='black', height=1, width=8)
label.grid(row=2, column=0)
button1 = Button(tk, text=' ', font='Times 20 bold', bg='grey',
                 fg='black', height=4, width=8, command=lambda: clickbutton(button1))
button1.grid(row=3, column=0)
button2 = Button(tk, text=' ', font='Times 20 bold', bg='grey',
                 fg='black', height=4, width=8, command=lambda: clickbutton(button2))
button2.grid(row=3, column=1)
button3 = Button(tk, text=' ', font='Times 20 bold', bg='grey',
                 fg='black', height=4, width=8, command=lambda: clickbutton(button3))
button3.grid(row=3, column=2)
button4 = Button(tk, text=' ', font='Times 20 bold', bg='grey',
                 fg='black', height=4, width=8, command=lambda: clickbutton(button4))
button4.grid(row=4, column=0)
button5 = Button(tk, text=' ', font='Times 20 bold', bg='grey',
                 fg='black', height=4, width=8, command=lambda: clickbutton(button5))
button5.grid(row=4, column=1)
button6 = Button(tk, text=' ', font='Times 20 bold', bg='grey',
                 fg='black', height=4, width=8, command=lambda: clickbutton(button6))
button6.grid(row=4, column=2)
button7 = Button(tk, text=' ', font='Times 20 bold', bg='grey',
                 fg='black', height=4, width=8, command=lambda: clickbutton(button7))
button7.grid(row=5, column=0)
button8 = Button(tk, text=' ', font='Times 20 bold', bg='grey',
                 fg='black', height=4, width=8, command=lambda: clickbutton(button8))
button8.grid(row=5, column=1)
button9 = Button(tk, text=' ', font='Times 20 bold', bg='grey',
                 fg='black', height=4, width=8, command=lambda: clickbutton(button9))
button9.grid(row=5, column=2)
tk.mainloop()
