from tkinter import *   
from time import strftime  

root = Tk()
root.geometry("500x500")  
root.resizable(0, 0)  
root.title('Python Clock')  

Label(root, text='by sandeep yadav', font='arial 20 bold').pack(side=BOTTOM)

def time():
    string = strftime('%H:%M:%S %p')  #  AM/PM
    mark.config(text=string)  # Update the label with the current time
    mark.after(1000, time)  # Call the time function again after 1000 milliseconds (1 second)

mark = Label(root,
             font=('calibri', 40, 'bold'),  # Set font type, size, and style
             pady=150,  # Add padding to the y-axis
             foreground='red')  # Set text color

mark.pack(anchor='center')  # Place the label in the center of the window
time()  # Call the time function to initialize the clock

mainloop()  # Start the Tkinter event loop to run the application
