from tkinter import *
from tkinter.ttk import *


class UserInterface(Tk):
    def __init__(self, file_manager):
        super().__init__()
        self.geometry('600x600')
        self.title("Yakuza save converter proto a0.3")
        self.bg = PhotoImage(file="background.png") #optional but added for le funny
        self.label = Label(self, image=self.bg)
        self.label.place(x=0, y=0)

        menu = Menu(self)
        self.new_item = Menu(menu, tearoff=0)
        menu.add_cascade(label='File', menu=self.new_item)
        self.new_item.add_command(label='Open PC save...', command=file_manager.choose_pc_input)
        self.new_item.add_command(label='Open PS3 save...', command=file_manager.choose_ps3_input)
        self.new_item.add_command(label='Exit', command=file_manager.close)
        self.config(menu=menu)

        self.lbl1 = Label(self, text="Selected PS3 save path goes here...")  # ps3 save input path
        self.lbl1.pack()
        self.lbl2 = Label(self, text="Selected PC output path goes here...")  # output path pc
        self.lbl2.pack(pady=5)
        self.lbl3 = Label(self, text="Selected PC save path goes here...")  # pc save input path
        self.lbl3.pack(pady=10)
        self.lbl4 = Label(self, text="Selected PS3 output path goes here...")  # output path ps3
        self.lbl4.pack(pady=15)
        self.btn1 = Button(self, text="Choose PS3 output directory", command=file_manager.choose_output_ps3)
        self.btn1.pack(side="bottom", anchor=NW)
        self.btn4 = Button(self, text="Choose PC output directory", command=file_manager.choose_output_pc)
        self.btn4.pack(side="bottom", anchor=NW)
        self.btn2 = Button(self, text="Convert PS3 -> PC!!!", command=file_manager.le_to_be)
        self.btn2.pack(side="bottom", anchor=NW)
        self.btn3 = Button(self, text="Convert PC -> PS3!!!", command=file_manager.be_to_le)
        self.btn3.pack(side="bottom", anchor=NW)
