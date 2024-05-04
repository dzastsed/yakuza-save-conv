import os
from binary_reader import BinaryReader
from tkinter import filedialog, messagebox
from abc import ABC, abstractmethod
from ui import SingletonClass
import winsound
import datetime
from datetime import time, datetime


class Startup(ABC):

    @abstractmethod
    def on(self):
        pass


class File(Startup):
    def __init__(self, ui_instance):
        self.__input_ps3 = []
        self.__input_pc = []
        self.__output = []
        self.ui = ui_instance

    def on(self):
        messagebox.showinfo('Hello!', 'Welcome to Yakuza save converter prototype!')

    def choose_ps3_input(self):
        file = filedialog.askopenfilename()
        if file:
            self.__input_ps3.append(file)
            self.ui.lbl1.configure(text="Chosen save file: " + file)
            print(f"DEBUG: chosen PS3 savefile: {file}")
        else:
            print(f"DEBUG: no PS3 savefile chosen")

    def choose_pc_input(self):
        file_pc = filedialog.askopenfilename()
        if file_pc:
            self.__input_pc.append(file_pc)
            self.ui.lbl2.configure(text="Chosen save file: " + file_pc)
            print(f"DEBUG: chosen PC savefile: {file_pc}")
        else:
            print(f"DEBUG: no PC savefile chosen")

    def choose_output(self):
        dir = filedialog.askdirectory()
        if dir:
            self.__output.append(dir)
            self.ui.lbl3.configure(text="Chosen output path: " + dir)
            print(f"DEBUG: chosen output directory: {dir}")
        else:
            print(f"DEBUG: no output dir chosen")

    def le_to_be(self):
        if self.__output and self.__input_ps3:
            output_file_pc = os.path.join(*self.__output, "OUTPUT_PC")
            input_file_ps3 = open(os.path.join(*self.__input_ps3), "rb")
            save1 = BinaryReader(input_file_ps3.read(), False)
            converted_file = BinaryReader(bytearray(), True)
            bytecount = int(save1.size() / 4)
            for i in range(bytecount):
                test = save1.read_uint32()
                converted_file.write_uint32(test)
            with open(output_file_pc, "wb") as f:
                f.write(converted_file.buffer())
            print(f"DEBUG: CONVERSION PS3 -> PC SUCCESS!!!")
            messagebox.showinfo('Info', 'Conversion from PS3 to PC success!!')
        elif not self.__output:
            print(f"DEBUG: Output path not selected.")
            messagebox.showinfo('Info', 'You did not select output path!')
        else:
            print(f"DEBUG: no PS3 savefile chosen")
            messagebox.showinfo('Info', 'You did not select PS3 save file!')

    def be_to_le(self):  # just a small test as main focus is PS3->PC conversion at this moment
        if self.__output and self.__input_pc:
            output_file_ps3 = os.path.join(*self.__output, "OUTPUT_PS3")
            input_file_pc = open(os.path.join(*self.__input_pc), "rb")
            save2 = BinaryReader(input_file_pc.read(), True)
            converted_file = BinaryReader(bytearray(), False)
            bytecount = int(save2.size() / 4)
            for i in range(bytecount):
                test = save2.read_uint32()
                converted_file.write_uint32(test)
            with open(output_file_ps3, "wb") as f:
                f.write(converted_file.buffer())
            print(f"DEBUG: CONVERSION PC -> PS3 SUCCESS!!!")
            messagebox.showinfo('Info', 'Conversion from PC to PS3 success!!')
        elif not self.__output:
            print(f"DEBUG: Output path PC -> PS3 not selected.")
            messagebox.showinfo('Info', 'You did not select output path!')
        else:
            print(f"DEBUG: no PC savefile chosen")
            messagebox.showinfo('Info', 'You did not select PC save file!')

    def close(self):
        exit()


def my_decorator(func):
    def wrapper():
        sample_time = 0
        now = datetime.now().hour
        if sample_time == now:
            return func()
        else:
            print("easter egg music requirements unmet :(")

    return wrapper


@my_decorator
def easteregg():
    winsound.PlaySound('easteregg.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)


if __name__ == "__main__":
    easteregg()
    file_manager = File(None)
    file_manager.on()
    main_app = SingletonClass(file_manager)
    file_manager.ui = main_app
    main_app.mainloop()
