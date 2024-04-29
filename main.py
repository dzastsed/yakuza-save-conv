import os
from tkinter import filedialog, Menu
from tkinter import *
from tkinter.ttk import *
from binary_reader import BinaryReader


class File:
    def __init__(self):
        self.input = []
        self.output = []

    def choose_input(self):
        file = filedialog.askopenfilename()
        if file == "":
            return
        else:
            self.input.append(file)
            lbl1.configure(text="Chosen save file: " + file)
            print (f"DEBUG: chosen PS3 savefile: {self.input}")

    def choose_output(self):
        dir = filedialog.askdirectory()
        if dir == "":
            return
        else:
            self.output.append(dir)
            lbl2.configure(text="Chosen output path: " + dir)
            print(f"DEBUG: chosen output directory: {self.output}")

    def le_to_be(self):
        output_file = os.path.join(*self.output, "OUTPUT")
        input_file = open(os.path.join(*self.input), "rb")
        save = BinaryReader(input_file.read(), False)
        converted_file = BinaryReader(bytearray(), True)
        bytecount = int(save.size() / 4)
        for i in range(bytecount):
            test = save.read_uint32()
            converted_file.write_uint32(test)
        with open(output_file, "wb") as f:
            f.write(converted_file.buffer())
        print(f"DEBUG: CONVERSION SUCCESS!!!")


filemanagement = File()


window = Tk()
window.geometry('600x600')
window.title("Yakuzer save converter proto a0.1")
bg = PhotoImage(file = "background.png")
label1 = Label(window, image = bg)
label1.place(x = 0, y = 0)

menu = Menu(window)
new_item = Menu(menu, tearoff=0)
new_item.add_command(label='Open PC save...')
new_item.add_command(label='Open PS3 save...', command=filemanagement.choose_input)
menu.add_cascade(label='File', menu=new_item)
window.config(menu=menu)

lbl1 = Label(window, text="Selected save path goes here...") #ps3 save input path
lbl1.grid(column=0, row=0)
lbl2 = Label(window, text="Selected output path goes here...") #output path
lbl2.grid(column=0, row=3)
btn1 = Button(window, text="Choose output directory", command=filemanagement.choose_output)
btn1.grid(column=12, row=5)
btn2 = Button(window, text="Convert!!!", command=filemanagement.le_to_be)
btn2.grid(column=12, row=6)


window.mainloop()