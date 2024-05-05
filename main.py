import os
from binary_reader import BinaryReader
import ui
from tkinter import filedialog, messagebox
from abc import ABC, abstractmethod


class Startup(ABC):

    @abstractmethod
    def on(self):
        pass


class File(Startup):
    def __init__(self, ui_instance):
        self.__input_ps3 = []
        self.__input_pc = []
        self.__output_ps3 = []
        self.__output_pc = []
        self.ui = ui_instance

    def on(self):
        messagebox.showinfo('Hello!', 'Welcome to Yakuza save converter prototype!')

    def choose_ps3_input(self):
        file = filedialog.askopenfilename()
        if file:
            self.__input_ps3.append(file)
            self.ui.lbl1.configure(text="Chosen save file: " + file)
            print(f"DEBUG: chosen PS3 savefile: {file}")

    def choose_pc_input(self):
        file_pc = filedialog.askopenfilename()
        if file_pc:
            self.__input_pc.append(file_pc)
            self.ui.lbl3.configure(text="Chosen save file: " + file_pc)
            print(f"DEBUG: chosen PC savefile: {file_pc}")

    def choose_output_ps3(self):
        dir = filedialog.askdirectory()
        if dir:
            self.__output_ps3.append(dir)
            self.ui.lbl2.configure(text="Chosen PS3 save output path: " + dir)
            print(f"DEBUG: chosen output directory: {dir}")

    def choose_output_pc(self):
        dir = filedialog.askdirectory()
        if dir:
            self.__output_pc.append(dir)
            self.ui.lbl4.configure(text="Chosen PC save output path: " + dir)
            print(f"DEBUG: chosen output directory: {dir}")

    def le_to_be(self):
        output_file_ps3 = os.path.join(*self.__output_ps3, "OUTPUT_PC")
        input_file_ps3 = open(os.path.join(*self.__input_ps3), "rb")
        save1 = BinaryReader(input_file_ps3.read(), False)
        converted_file = BinaryReader(bytearray(), True)
        bytecount = int(save1.size() / 4)
        for i in range(bytecount):
            test = save1.read_uint32()
            converted_file.write_uint32(test)
        with open(output_file_ps3, "wb") as f:
            f.write(converted_file.buffer())
        print(f"DEBUG: CONVERSION PS3 -> PC SUCCESS!!!")
        messagebox.showinfo('Info', 'Conversion from PS3 to PC success!!')

    def be_to_le(self):  # just a small test as main focus is PS3->PC conversion at this moment
        output_file_pc = os.path.join(*self.__output_pc, "OUTPUT_PS3")
        input_file_pc = open(os.path.join(*self.__input_pc), "rb")
        save2 = BinaryReader(input_file_pc.read(), True)
        converted_file = BinaryReader(bytearray(), False)
        bytecount = int(save2.size() / 4)
        for i in range(bytecount):
            test = save2.read_uint32()
            converted_file.write_uint32(test)
        with open(output_file_pc, "wb") as f:
            f.write(converted_file.buffer())
        print(f"DEBUG: CONVERSION PS3 <- PC SUCCESS!!!")
        messagebox.showinfo('Info', 'Conversion from PC to PS3 success!!')

    def close(self):
        exit()


def main():
    file_manager = File(None)
    file_manager.on()
    main_app = ui.UserInterface(file_manager)
    file_manager.ui = main_app
    main_app.mainloop()


if __name__ == "__main__":
    main()
