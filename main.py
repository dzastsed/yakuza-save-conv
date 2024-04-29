import os
from tkinter import filedialog, Menu, messagebox
from tkinter import *
from tkinter.ttk import *
from binary_reader import BinaryReader
from playsound import playsound


def close():
    exit()


def play():
    playsound('Electrodynamix.mp3')



class File:
    def __init__(self):
        self.input_ps3 = []
        self.input_pc = []
        self.output_ps3 = []
        self.output_pc = []

    def choose_ps3_input(self):
        file = filedialog.askopenfilename()
        if file == "":
            return
        else:
            self.input_ps3.append(file)
            lbl1.configure(text="Chosen save file: " + file)
            print (f"DEBUG: chosen PS3 savefile: {self.input_ps3}")

    def choose_pc_input(self):
        file_pc = filedialog.askopenfilename()
        if file_pc == "":
            return
        else:
            self.input_pc.append(file_pc)
            lbl3.configure(text="Chosen save file: " + file_pc)
            print (f"DEBUG: chosen PC savefile: {self.input_pc}")

    def choose_output_ps3(self):
        dir = filedialog.askdirectory()
        if dir == "":
            return
        else:
            self.output_ps3.append(dir)
            lbl2.configure(text="Chosen PS3 save output path: " + dir)
            print(f"DEBUG: chosen output directory: {self.output_ps3}")

    def choose_output_pc(self):
        dir = filedialog.askdirectory()
        if dir == "":
            return
        else:
            self.output_pc.append(dir)
            lbl4.configure(text="Chosen PC save output path: " + dir)
            print(f"DEBUG: chosen output directory: {self.output_pc}")

    def le_to_be(self):
        output_file_ps3 = os.path.join(*self.output_ps3, "OUTPUT_PC")
        input_file_ps3 = open(os.path.join(*self.input_ps3), "rb")
        save1 = BinaryReader(input_file_ps3.read(), False)
        converted_file = BinaryReader(bytearray(), True)
        bytecount = int(save1.size() / 4)
        for i in range(bytecount):
            test = save1.read_uint32()
            converted_file.write_uint32(test)
        with open(output_file_ps3, "wb") as f:
            f.write(converted_file.buffer())
        print(f"DEBUG: CONVERSION PS3 -> PC SUCCESS!!!")
        messagebox.showinfo('Info','Conversion from PS3 to PC success!!')

    def be_to_le(self):
        output_file_pc = os.path.join(*self.output_pc, "OUTPUT_PS3")
        input_file_pc = open(os.path.join(*self.input_pc), "rb")
        save2 = BinaryReader(input_file_pc.read(), True)
        converted_file = BinaryReader(bytearray(), False)
        bytecount = int(save2.size() / 4)
        for i in range(bytecount):
            test = save2.read_uint32()
            converted_file.write_uint32(test)
        with open(output_file_pc, "wb") as f:
            f.write(converted_file.buffer())
        print(f"DEBUG: CONVERSION PS3 <- PC SUCCESS!!!")
        messagebox.showinfo('Info','Conversion from PC to PS3 success!!')


filemanagement = File()


window = Tk()
window.geometry('600x600')
window.title("Yakuzer save converter proto a0.2")
bg = PhotoImage(file = "background.png")
label1 = Label(window, image = bg)
label1.place(x = 0, y = 0)

menu = Menu(window)
new_item = Menu(menu, tearoff=0)
new_item.add_command(label='Open PC save...', command=filemanagement.choose_pc_input)
new_item.add_command(label='Open PS3 save...', command=filemanagement.choose_ps3_input)
new_item.add_command(label='Exit', command=close)
menu.add_cascade(label='File', menu=new_item)
window.config(menu=menu)

lbl1 = Label(window, text="Selected PS3 save path goes here...") #ps3 save input path
lbl1.pack()
lbl2 = Label(window, text="Selected PC output path goes here...") #output path pc
lbl2.pack(pady=5)
lbl3 = Label(window, text="Selected PC save path goes here...") #pc save input path
lbl3.pack(pady=10)
lbl4 = Label(window, text="Selected PS3 output path goes here...") #output path ps3
lbl4.pack(pady=15)
btn1 = Button(window, text="Choose PS3 output directory", command=filemanagement.choose_output_ps3)
btn1.pack(side="bottom", anchor = NW)
btn4 = Button(window, text="Choose PC output directory", command=filemanagement.choose_output_pc)
btn4.pack(side="bottom", anchor = NW)
btn2 = Button(window, text="Convert PS3 -> PC!!!", command=filemanagement.le_to_be)
btn2.pack(side="bottom", anchor = NW)
btn3 = Button(window, text="Convert PC -> PS3!!!", command=filemanagement.be_to_le)
btn3.pack(side="bottom", anchor = NW)

btn5 = Button(window, text='Music???', command=play)
btn5.pack(side="bottom", anchor = SW)

window.mainloop()