from tkinter import *

# window = Tk()
# window.title("GUI is amazing")
#
# # size of the tkinter
# window.minsize(width=500, height=300)
#
# # creating components in the window
# # create labels
# my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
# # In tkinter we have a create a component and then have to specify how that component is going to be laid out
# # my_label.pack()
# # let's change the location
# # my_label.pack(side="left")
#
# # let's try place
# # my_label.place(x=100, y=180)
#
# # let's try place
# my_label.grid(column=0, row=0)

# change the label
# my_label["text"] = "New Text"
# my_label.pack(side="left")
# # using config change label
# my_label.config(text="Config Text")


# def button_clicked():
#     new_text = user_input.get()
#     my_label.config(text=new_text)
#
#
# # Button
# button = Button(text="Click Me", command=button_clicked)
# button.pack()
#
#
# # Entry Component
# user_input = Entry(width=10)
# user_input.pack()

window = Tk()
# give it a title
window.title("My GUI")
# size our tkinter
window.minsize(width=500, height=400)

# add padding
window.config(padx=20, pady=20)

# let's create first Label
my_label = Label(text="First Label", font=("Arial", 24, "bold"))
# place it in the first grid
my_label.grid(column=0, row=0)

# let's create button
first_button = Button(text="Click Me")
first_button.grid(column=1, row=1)

# let's create an entry
user_input = Entry()
user_input.grid(column=2, row=2)

# let's create another button
second_button = Button(text="Helllo")
second_button.grid(column=3, row=0)
window.mainloop()
