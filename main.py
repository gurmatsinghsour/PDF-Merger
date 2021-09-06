from tkinter import *
from tkinter import filedialog
import PyPDF2
import PyPDF2.filters
from PyPDF2 import PdfFileReader


root = Tk()


def savefile():
    file = filedialog.askdirectory()
    fildir=[]
    fildir.append(file)
    return fildir

def openwindow():
    newwindow = Toplevel(root)
    newwindow.title("Operation")
    newwindow.geometry("200x200")
    newwindow.resizable(False,False)
    Label(newwindow, text = "Operation sucess").place(x=50, y=80)
    newwindow.config(bg="lightpink")
    p3 = PhotoImage(file='Images/sucess.png')
    newwindow.iconphoto(False, p3)


def helpbutton():
    file = open('Info/info.txt', 'r')
    filetext = file.read()

    anotherwindow = Toplevel(root)
    anotherwindow.title("Help")
    anotherwindow.geometry("930x80")
    Label(anotherwindow, text=filetext).place(x=0, y=0)
    p4 = PhotoImage(file = 'Images/help.png')
    anotherwindow.iconphoto(False, p4)



def pdfmerger(filedirectory):
    merger = PyPDF2.PdfFileMerger()
    for f in filedirectory:
        merger.append(PdfFileReader(open(f, "rb")))


    outputname=e1.get()
    if outputname:
        name = savefile()
        finalname = str(name[0]) + "/" + outputname + ".pdf"
        merger.write(finalname)
        openwindow()

    else:
        name = savefile()

        filename = str(name[0]) + "/Merged.pdf"
        merger.write(filename)
        openwindow()

def filebrowsing():
    file = filedialog.askopenfilenames(filetypes=[("PDF Files", "*.pdf")]
    )
    filename = []
    filename.append(file)
    if len(file) <= 1:
        anotherwindow = Toplevel(root)
        anotherwindow.title("ERROR")
        anotherwindow.geometry("500x100")
        Label(anotherwindow, text="ERROR! Please select more than one pdf file.").place(x=120, y=40)
        anotherwindow.resizable(False, False)
        anotherwindow.config(bg="lightpink")
        p2 = PhotoImage(file = 'Images/cross.png')
        anotherwindow.iconphoto(False, p2)



    else:
        filedirectory = list(filename[0])
        pdfmerger(filedirectory)



# def helpButton():
#
#     tkMessageBox.showinfo("Press the select button and select your pdf files. Once you've selected the pdf file, it's gonna open another tab to select the save file directory. ")
#




# GUI
root.geometry('520x120')
root.title("PDF Merger")
root.config(bg='lightpink')
root.resizable(False, False)
button_1 = Button(root, text='Start', command=filebrowsing)
button_1.config(width=10, height=1)
button_1.place(x=20, y=90)
button_2 = Button(root, text='Help', command = helpbutton)
button_2.config(width=10, height=1)
button_2.place(x=120, y=90)
label_1 = Label(root, text="Thank you! UwU")
label_1 = label_1.place(x=220, y=0)
label_2 = Label(root, text="Please enter the name of merged pdf.")
label_2 = label_2.place(x=20,y=30)
e1 = Entry(root)
e1.place(width= 480, height=20, x=20, y=50)
p1 = PhotoImage(file='Images/main.png')
root.iconphoto(False, p1)
watermarklabel  = Label(root, text="By Gurmatsinghsour@Arcy")
watermarklabel = watermarklabel.place(x=350, y=93)


if __name__ == "__main__":
    root.mainloop()


