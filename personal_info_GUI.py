#This program is a GUI that displays personal info when a button is clicked

import tkinter

class Gui:
    def __init__(self):
        self.main_window = tkinter.Tk()

        #  Create the title for the window
        self.main_window.title('Personal Information')

        # Create frames to organize
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Create a StringVar to display data
        self.name = tkinter.StringVar()
        self.street = tkinter.StringVar()
        self.city = tkinter.StringVar()


        # Create the output labels where data will show in the top frame
        self.name_label = tkinter.Label(self.top_frame, textvariable =
        self.name)
        self.street_label = tkinter.Label(self.top_frame, textvariable =
        self.street)
        self.city_label = tkinter.Label(self.top_frame, textvariable =
        self.city)


        # Pack the widgets for the top frame
        self.name_label.pack()
        self.street_label.pack()
        self.city_label.pack()

        # Create the buttons for the bottom frame
        self.display_button = tkinter.Button(self.bottom_frame, text =
        'Display Information', command = self.display_info)


        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit',
                                          command=self.main_window.destroy)

        # Pack the buttons
        self.display_button.pack(side = 'left', padx = 20, pady = 20 )
        self.quit_button.pack(side = 'left', padx =  20, pady = 20  )


        # Pack the Frames
        self.top_frame.pack()
        self.bottom_frame.pack()



        # Enter the mainloop
        tkinter.mainloop()

    def display_info(self):
        name = str('James Drew')
        street = str('123 Test Ave')
        city = str('Largo Fl 33771')

        self.name.set(name)
        self.street.set(street)
        self.city.set(city)





if __name__ == '__main__':
    my_gui = Gui()
