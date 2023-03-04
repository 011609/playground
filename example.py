import tkinter as tk

# create the window
window = tk.Tk()

# function to be executed when a key is pressed
def key_pressed(event):
    print('Key:', event.char, 'pressed')

# bind the key press event to the function
window.bind('<Key>', key_pressed)

# run the window
window.mainloop()


