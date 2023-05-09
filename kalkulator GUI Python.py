from tkinter import *

window = Tk()
window.title("Kalkulator GUI dengan Python")
window.geometry('640x240')
window['bg']= 'Aqua'

lbl = Label(window,text="Masukkan Nilai Pertama(X): ", anchor="e", width=20,background='aqua')
lbl.grid(column=0, row=0,pady=10)

lbl2 = Label(window,text="Masukkan Nilai Kedua(Y)): ", anchor="e", width=20,background='aqua')
lbl2.grid(column=0, row=1, pady=10)

lbl3 = Label(window,text="Hasil: ", anchor="e", width=20,background='aqua')
lbl3.grid(column=0, row=10)

nilai1 = Entry(window, width=20)
nilai1.grid(column=1, row=0,ipadx=30)

nilai2 = Entry(window, width=20)
nilai2.grid(column=1, row=1,ipadx=30)

hasil = Label(window, anchor="w",width=20)
hasil.grid(column=1,row=10)

def tambah():
    hasil.configure(text=(float(nilai1.get())+float(nilai2.get())))
def kurang():
    hasil.configure(text=(float(nilai1.get())-float(nilai2.get())))
def kali():
    hasil.configure(text=(float(nilai1.get())*float(nilai2.get())))
def bagi():
    hasil.configure(text=(float(nilai1.get())/float(nilai2.get())))
def xpangkaty():
    hasil.configure(text=(float(nilai1.get())**float(nilai2.get())))
def ypangkatx():
    hasil.configure(text=(float(nilai2.get())**float(nilai1.get())))
def modulus():
    hasil.configure(text=(float(nilai1.get())%float(nilai2.get())))
def xakary():
    hasil.configure(text=(float(nilai1.get())**(1/float(nilai2.get()))))
def yakarx():
    hasil.configure(text=(float(nilai2.get())**(1/float(nilai1.get()))))

    
btn = Button(window, text="Tambah", command=tambah)
btn.grid(column=0,row=4,pady=10, ipadx=10,ipady=5)
    
btn = Button(window, text="Kurang", command=kurang)
btn.grid(column=1,row=4,pady=10, ipadx=10,ipady=5)
    
btn = Button(window, text="Kali", command=kali)
btn.grid(column=2,row=4,pady=10, ipadx=10,ipady=5)
    
btn = Button(window, text="Bagi", command=bagi)
btn.grid(column=0,row=6,pady=10, ipadx=10,ipady=5)

btn = Button(window, text="X Pangkat Y", command=xpangkaty)
btn.grid(column=1,row=6,pady=10, ipadx=10,ipady=5)

btn = Button(window, text="Y Pangkat X", command=ypangkatx)
btn.grid(column=2,row=6,pady=10, ipadx=10,ipady=5)

btn = Button(window, text="Modulus", command=modulus)
btn.grid(column=3,row=6,padx=10,pady=10, ipadx=10,ipady=5)

btn = Button(window, text="X Akar Y", command=xakary)
btn.grid(column=3,row=4,padx=10,pady=10, ipadx=10,ipady=5)

btn = Button(window, text="Y Akar X", command=yakarx)
btn.grid(column=4,row=4,padx=10,pady=10, ipadx=10,ipady=5)

window.mainloop()