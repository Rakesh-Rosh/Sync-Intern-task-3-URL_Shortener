from tkinter import*
import pyshorteners

root = Tk()
root.title('Rakesh Rosh - Link Shortener')
root.geometry("500x500")

def shorten():
    if shorty.get():
        shorty.delete(0, END)

    if my_entry.get():
        #convert to tinyur1
        url = pyshorteners.Shortener().tinyurl.short(my_entry.get()) 
        #output to screen
        shorty.insert(END, url)

        #Reverse URl
        print(pyshorteners.Shortener().tinyurl.expand(url))   

my_label = Label(root, text="Enter Link to Shorten", font=("Helvetica", 34))
my_label.pack(pady=20)

my_entry = Entry(root, font=("Helvetica", 24))
my_entry.pack(pady=20)

my_button = Button(root, text="Shorten Link", command=shorten, font=("Helvetica", 24))
my_button.pack(pady=20)

shorty_label = Label(root, text="shortened Link", font=("Hevetica", 14))
shorty_label.pack(pady=50)

shorty = Entry(root, font=("Helvetica",22),justify=CENTER, width=30, bd=0, bg="systembuttonface")
shorty.pack(pady=10)

root.mainloop()
