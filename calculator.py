import tkinter as tk
h = tk.Tk()
h.geometry("900x600")
h.title("Calculator")
label = tk.Label(h,text="Calculator",font=("Arial",20))
label.pack()
tbx = tk.Text(h,height='3',font=('Arial',18))
tbx.pack(padx=10)
tbx.config(state= 'disabled')
buttonframe = tk.Frame(h)
buttonframe.columnconfigure(0,weight=1)
buttonframe.columnconfigure(1,weight=1)
buttonframe.columnconfigure(2,weight=1)
buttonframe.columnconfigure(3,weight=1)
buttonframe.columnconfigure(4,weight=1)
def dis1():
    tbx.config(state= 'normal')
    tbx.insert(tk.END, '1')
    tbx.config(state="disabled")
def dis2():
    tbx.config(state= 'normal')
    tbx.insert(tk.END, '2')
    tbx.config(state="disabled")
def dis3():
    tbx.config(state= 'normal')
    tbx.insert(tk.END, '3')
    tbx.config(state="disabled")
def dis4():
    tbx.config(state= 'normal')
    tbx.insert(tk.END, '4')
    tbx.config(state="disabled") 
def dis5():
    tbx.config(state= 'normal')
    tbx.insert(tk.END, '5')
    tbx.config(state="disabled")
def dis6():
    tbx.config(state= 'normal')
    tbx.insert(tk.END, '6')
    tbx.config(state="disabled")
def dis7():
    tbx.config(state= 'normal')
    tbx.insert(tk.END, '7')
    tbx.config(state="disabled")
def dis8():
    tbx.config(state= 'normal')
    tbx.insert(tk.END, '8')
    tbx.config(state="disabled")
def dis9():
    tbx.config(state= 'normal')
    tbx.insert(tk.END, '9')
    tbx.config(state="disabled")
def dis0():
    tbx.config(state= 'normal')
    tbx.insert(tk.END, '0')
    tbx.config(state="disabled")
def disP():
    tbx.config(state = 'normal')
    tbx.insert(tk.END, '+')
    tbx.config(state = 'disabled')
def disS():
    tbx.config(state = 'normal')
    tbx.insert(tk.END, '-')
    tbx.config(state = 'disabled')
def disD():
    tbx.config(state = 'normal')
    tbx.insert(tk.END, '÷')
    tbx.config(state = 'disabled')
def disM():
    tbx.config(state = 'normal')
    tbx.insert(tk.END, 'x')
    tbx.config(state = 'disabled')
def disR():
    text = tbx.get("1.0", "end")
    if len(text ) > 1:
        tbx.config(state = 'normal')
        tbx.delete("end-2c", "end-1c")
        tbx.config(state ='disabled')
def disEq():
        all__text = tbx.get("1.0", "end-1c")
        for op in ("÷",'x','+','-') :
            if op in all__text:
                itext = all__text.replace("÷","/").replace("x","*")
                try:
                    itext2 = eval(itext)
                    tbx.config(state = 'normal')
                    tbx.insert("end", '\n')
                    tbx.insert("end", itext2)
                    tbx.config(state = 'disabled')
                    fond_operator = True
                except ZeroDivisionError:
                    tbx.config(state = 'normal')
                    tbx.insert("end", '\n')
                    tbx.insert("end", "undefined")
                    tbx.config(state = 'disabled')
                    fond_operator = True
                    break
            if not fond_operator:
                print(itext2)
            
        
def disC():
    tbx.config(state = 'normal')
    tbx.delete("1.0","end")
    tbx.config(state = 'disabled')
        


bt1 =  tk.Button(buttonframe,text='1',font=('Arial',40),command=dis1)
bt1.grid(row= 0 ,column=0 , stick =tk.W+tk.E)
bt2 =  tk.Button(buttonframe,text='2',font=('Arial',40),command=dis2)
bt2.grid(row= 0 ,column=1 , stick =tk.W+tk.E)
bt3 =  tk.Button(buttonframe,text='3',font=('Arial',40),command=dis3)
bt3.grid(row= 0 ,column=2 , stick =tk.W+tk.E)
bt4 =  tk.Button(buttonframe,text='4',font=('Arial',40),command=dis4)
bt4.grid(row= 0 ,column=3 , stick =tk.W+tk.E)
bt5 =  tk.Button(buttonframe,text='5',font=('Arial',40),command=dis5)
bt5.grid(row= 0 ,column=4 , stick =tk.W+tk.E)
bt6 =  tk.Button(buttonframe,text='6',font=('Arial',40),command=dis6)
bt6.grid(row= 1 ,column=0 , stick =tk.W+tk.E)
bt7 =  tk.Button(buttonframe,text='7',font=('Arial',40),command=dis7)
bt7.grid(row= 1 ,column=1 , stick =tk.W+tk.E)
bt8 =  tk.Button(buttonframe,text='8',font=('Arial',40),command=dis8)
bt8.grid(row= 1 ,column=2 , stick =tk.W+tk.E)
bt9 =  tk.Button(buttonframe,text='9',font=('Arial',40),command=dis9)
bt9.grid(row= 1,column=3 , stick =tk.W+tk.E)
bt0 =  tk.Button(buttonframe,text='0',font=('Arial',40),command=dis0)
bt0.grid(row= 1 ,column=4 , stick =tk.W+tk.E)
btP =  tk.Button(buttonframe,text='+',font=('Arial',30),command=disP)
btP.grid(row= 2 ,column=0 , stick =tk.W+tk.E)
btS =  tk.Button(buttonframe,text='-',font=('Arial',30),command=disS)
btS.grid(row= 2 ,column=1 , stick =tk.W+tk.E)
btD =  tk.Button(buttonframe,text='÷',font=('Arial',30),command=disD)
btD.grid(row= 2 ,column=2 , stick =tk.W+tk.E)
btM =  tk.Button(buttonframe,text='x',font=('Arial',30),command=disM)
btM.grid(row= 2 ,column=3 , stick =tk.W+tk.E)
btR = tk.Button(buttonframe,text='Remove',font=('Arial',30),command=disR)
btR.grid(row= 2 ,column=4 , stick =tk.W+tk.E)
btEq = tk.Button(buttonframe,text='=',font=('Arial',30),command=disEq)
btEq.grid(row= 3 ,column=0 , stick =tk.W+tk.E)
btC = tk.Button(buttonframe,text='C',font=('Arial',30),command=disC)
btC.grid(row= 3 ,column=1 , stick =tk.W+tk.E)
buttonframe.pack(fill='x')

h.mainloop()