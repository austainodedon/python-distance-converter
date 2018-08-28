
from tkinter import *

def convert_mile():
    words = miletext.get()
    miles = float(words)
    metrebox.delete(0, END)
    metrebox.insert(0, '%.2f' % (mtometre(miles)))
    inchbox.delete(0, END)
    inchbox.insert(0, '%.2f' % (mtoinch(mtometre(miles))))
    yardbox.delete(0, END)
    yardbox.insert(0, '%.2f' % (itoyard(mtoinch(mtometre(miles)))))
    return

def convert_inch():
    words = inchtext.get()
    inches = float(words)
    metrebox.delete(0, END)
    metrebox.insert(0, '%.2f' % (itometre(inches)))
    milebox.delete(0, END)
    milebox.insert(0, '%.2f' % (mtomile(itometre(inches))))
    yardbox.delete(0, END)
    yardbox.insert(0, '%.2f' % (itoyard(inches)))

def convert_metre():
    words = metretext.get()
    metres = float(words)
    inchbox.delete(0, END)
    inchbox.insert(0, '%.2f' % (mtoinch(metres)))
    milebox.delete(0, END)
    milebox.insert(0, '%.2f' % (mtomile(metres)))
    yardbox.delete(0, END)
    yardbox.insert(0, '%.2f' % (itoyard(mtoinch(metres))))

def convert_yard():
    words = yardtext.get()
    yards = float(words)
    inchbox.delete(0, END)
    inchbox.insert(0, '%.2f' % (ytoinch(yards)))
    metrebox.delete(0, END)
    metrebox.insert(0, '%.2f' % (itometre((ytoinch(yards)))))
    milebox.delete(0, END)
    milebox.insert(0, '%.2f' % (mtomile(itometre(ytoinch(yards)))))

def mtometre(mile):
    return mile * 1601

def mtoinch(metre):
    return metre * 39.37

def itometre(inch):
    return inch * 0.0254

def mtomile(metre):
    return metre * 0.00062

def itoyard(inch):
    return inch * 0.0278

def ytoinch(yard):
    return yard * 36

app = Tk()
app.title('Distance converter')



inchlabel = Label(app, text = 'Inch')
inchlabel.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = E)

milelabel = Label(app, text = 'Mile')
milelabel.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = E)

metrelabel = Label(app, text = 'Metre')
metrelabel.grid(row = 2, column = 0, padx = 5, pady = 5, sticky = E)

yardlabel = Label(app, text = 'Yard')
yardlabel.grid(row = 3, column = 0, padx = 5, pady = 5, sticky = E)

inchtext = StringVar()
inchtext.set('')
inchbox = Entry(app, textvariable=inchtext)
inchbox.grid(row = 0, column = 1, padx = 5, pady = 5)

miletext = StringVar()
miletext.set('')
milebox = Entry(app, textvariable=miletext)
milebox.grid(row = 1, column = 1, padx = 5, pady = 5)

metretext = StringVar()
metretext.set('')
metrebox = Entry(app, textvariable=metretext)
metrebox.grid(row = 2, column = 1, padx = 5, pady = 5)

yardtext = StringVar()
yardtext.set('')
yardbox = Entry(app, textvariable=yardtext)
yardbox.grid(row = 3, column = 1, padx =5, pady = 5)

ingobutton = Button(app, text = 'Go', command = convert_inch)
ingobutton.grid(row = 0, column = 2, padx = 5, pady = 5, sticky = N+S+E+W)

migobutton = Button(app, text = 'Go', command = convert_mile) 
migobutton.grid(row = 1, column = 2, padx = 5, pady = 5, sticky = N+S+E+W)

megobutton = Button(app, text = 'Go', command = convert_metre)
megobutton.grid(row = 2, column = 2, padx = 5, pady = 5, sticky = N+S+E+W)

yagobutton = Button(app, text = 'Go', command = convert_yard)
yagobutton.grid(row = 3, column = 2, padx = 5, pady = 5, sticky = N+S+E+W)

exitbutton = Button(app, text = 'Exit', command = quit)
exitbutton.grid(row = 4, column = 0, padx = 5, pady = 5, sticky = N+S+E+W, columnspan = 3)

app.mainloop()

# produce inches, yard, metre mile converter
# austaino from tclassified.com, www.jambwaecnecouni.com
