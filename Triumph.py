'''Here are we,in front of the Python Editor(in fact the QQMail Notebook on Kindle),
preparing to write a testing computer game for ourselves.
What is it?We are afraid that even we the programmers don' know what exactly the GAME is.(:-_-:)
But,let'do it!For it will certainly be a great pleasure writing ourown games.
                                                                                ----Bluehole(Author) 2021/07/07'''

#COPYRIGHT?:  The Daydreamer Co. 2019~2021
#All Rights Reserved.

#FIRST EDITED:2021/07/07 17:23
#LAST EDITION:v0.2.2(2021/07/10)

#OK,time to begin now……

#-----------------------------------------------------------------------

'''DISCUSSION OF THE TEAM:
(Note:sentences begin with '+' were said by Bluehole(The main programmer) 
while others begin with '-' were said by Steven(The main Designer)'''

#+First,let's think about the background of the game. 
#-Hmm,of course it should be set under the World War (Three),just like Fallout? and Sky Hill?. 
#+What's next?
#-Alright,as above,our main character is an honorable sodier in the WWT,his task is to fight against the Evil and save other guys.
#-So,our game is to play this sodier(maybe we should give him a name…Nicholas OK?) to fulfill his mission.
#+But what mission?
#-Didn't I say?He is going to FIGHT!(who their enemies are?…maybe the Second Nazi Kingdom…)
#-Oh gosh!We are doing nothing useful at the moment!
#+Yep,little time left now.It's really the time for starting our project…
#+Anywho,why not begin from the easiest?

#-----------------------------------------------------------------------

import sys
import os
import tkinter as TK

class GameGUI:
    def __init__(self):
        pass
    def run(self):                                                              #Create a game window
        self.GUIwindow = TK.Tk()
        self.GUIwindow.title('A New Project')
        self.GUIwindow.geometry('1200x800')

        #A frame contains the Canvas(to show the map) and the type-and-play area.

        self.game_frame = TK.Frame(self.GUIwindow,bg = 'white',height = 800,width = 900)
        self.game_frame.pack(anchor = 'nw')

        self.game_canvas = TK.Canvas(self.game_frame,bg = 'black',height = 600,width = 900)
        self.game_canvas.pack()

        self.game_console_listbox = TK.Listbox(self.game_frame)
        self.game_console_listbox.pack()

        #A frame to show(and type) the conversation between the NPCs and the player.
        #It is just an experimental idea and may be deleted or combined with $self.game_console$ in the future.

        self.dialog_frame = TK.Frame(self.GUIwindow,bd = 1,bg = 'white',height = 800,width = 300)
        self.dialog_frame.place(x = 900,y = 0)

        self.test_listbox= TK.Listbox(self.dialog_frame)
        self.test_listbox.pack()
        self.test_listbox.insert(TK.END,'Welcome to Triumph?!')

        self.test_button = TK.Button(self.dialog_frame,text = 'Exit',command = self.game_exit)
        self.test_button.pack()

        self.GUIwindow.mainloop()
    def game_exit(self):
        self.GUIwindow.destroy()

def game():                           #The main part of the game
    NewGameGUI = GameGUI()
    NewGameGUI.run()

if __name__ == '__main__':
    game()
