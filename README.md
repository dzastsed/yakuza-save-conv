# yakuza-save-conv - a work in progress yakuza cross platform save converter

## Introduction
The tool that you find in this repository is a work in progress Yakuza videogame (Yakuza 5 for now) cross-platform save converter. Basically, it allows you to convert, let's say, Playstation 3 Yakuza 5 save file into PC Yakuza 5 Remaster compatible format. 

> Warning - this tool is still experimental. So far only PC -> PS3 conversion works acceptably.

## How it works?
This tool utilizes a library called `BinaryReader` which can do various operations with byte order, swapping and editing in files. 

For now all this tool does is swap byte order from Little Endian (PS3) to Big Endian (PC) and vice-versa. While this makes the saves somewhat usable, there is still much more research needed to make them fully work (see known issues).

## How to use?
### Requirements
* Python 3.12
* Requirements installed from requirements.txt file (`pip -r requirements.txt`).
* Windows system - while code should be cross-platform compatible, I programmed it with Windows in mind.

### Launching and using the tool
The usage is very simple, as this tool has GUI interface.  You run it with command `python main.py`. After the GUI loads up, you will need to select `File` and then select either PC or PS3 save as input. 

Then, select output directory by pressing `Choose output directory`.

That's it! If you selected PS3 save as input, press `Convert PS3 -> PC` button, and converted save will be output to your selected directory.
## Implementation
This tool implements 4 required OOP pillars which I'll go about in-depth now:

### Polymorphism and abstraction:
An abstraction and polymorphism example is included with class called `Startup` - it gets initiated as an abstract class, and class `File` overrides it. 
### Inheritance:
This code inherits all user interface code from `ui.py` file.
### Encapsulation:
This code encapsulates variables `self.__input_ps3`, `self.__input_pc` and `self.__output` as private.

This code also utilizes 2 design patterns: 
### Singleton:
Whole `ui.py` file is written with singleton design pattern in mind.
### Decorator:
Decorator gets initiated in `File` class where it checks if the hour at running this tool matches 0 (Midnight) - if requirements are met, a function called `easteregg` will be called, and will play a music file (this, however, works only on Windows due to using a Windows-exclusive library). If requirements are unmet, it will print `easter egg music requirements unmet :(` to the console.

## Results
As mentioned before, all this code does for now is swap byte order. This does make saves load in PC version of the game.

For this preview, I will use RPCS3 emulator with PS3 version of Yakuza 5 installed.

1. First of all we take a save game from `\dev_hdd0\home\00000001\savedata\NPUB31658L01`. It will be called `USER01`.
>Note - if you use a save exported from real PS3 console, you will need to decrypt it either with Apollo save tool or PS3 save bruteforcer.
2. Copy `USER01` somewhere else, like on your desktop.
3. Open up this tool, and select `USER01` as PS3 save. 
4. Select output directory.
5. Click `Convert PS3 -> PC`.
6. Rename the output file to `savegame0.sav`.
7. Run corresponding script from [here](https://github.com/dzastsed/yakuzer-remotecache.vdf-maker/tree/main).
8. Your save should be ready to use, enjoy!

Here are pictures of before and after:

placeholder1

placeholder2


## Known issues
* If converted from PS3 to PC, there will be some sort of debug save mode toggled, which has an annoying watermark during gameplay.
* Inventory, current level and time played data gets corrupted, but your progress in story carries over.

## Conclusion
Writing this tool was a fun experience. I learned how to make TKInter GUI,  but, most importantly, learned how to make code less "spaghetti". This is also not the end for this tool! I intend to eventually add support for other titles, and fix up issues mentioned before. Eventually I also plan to combine it with another tool I made a while back which allows importing saves to steam cloud save folders.

