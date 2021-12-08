# This progam converts Celsius to Fahrenheit using a GUI

import tkinter


class Gui:
    def __init__(self):
        # Create the main window
        self.main_window = tkinter.Tk()

        # Create the title for the window
        self.main_window.title('Celsius to Fahrenheit converter')

        # Create the frames to organize widgets
        self.input_frame = tkinter.Frame(self.main_window)
        self.display_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        # Create Widget for input
        self.entry_text = tkinter.Label(self.input_frame,
                                        text = 'Enter degrees in Celsius:')
        self.entry = tkinter.Entry(self.input_frame, width = 10)

        # Pack widgets for Input Frame
        self.entry_text.pack(side = 'left')
        self.entry.pack(side = 'left')

        # Create widgets for the Display Frame

        # Create a StringVar for output
        self.display = tkinter.StringVar()

        self.display_label = tkinter.Label(self.display_frame, textvariable
        = self.display)

        # Pack widgets for the Display Frame
        #self.display.pack()
        self.display_label.pack()

        # Create the Buttons
        self.convert_button = tkinter.Button(self.button_frame, text =
        'Convert', command = self.convert)
        self.quit_button = tkinter.Button(self.button_frame, text = 'Quit',
                                          command = self.main_window.destroy)

        # Pack the buttons
        self.convert_button.pack(side = 'left')
        self.quit_button.pack(side = 'left')

        # Pack the frames
        self.input_frame.pack()
        self.display_frame.pack()
        self.button_frame.pack()

        # Enter the mainloop
        tkinter.mainloop()



    def convert(self):
        # Get the data from the entry

        try:
            c = float(self.entry.get())
            total = (c * 9 / 5) + 32
        except ValueError:
            total = str('Please enter a valid Integer.')
        self.display.set(total)





        # Return the total to the StringVar for display
        self.display.set(total)









        tkinter.mainloop()

if __name__ == '__main__':
    gui = Gui()




