from tkinter import *


window = Tk()
window.title("Count length of your phrase")


window.config(width=600, height=250, bg="white")


text = Text(width=48, height=7, font=("ariel", 15, "bold"))
text.place(x=20, y=20)



remove_image = PhotoImage(file=r"D:\Pycharm projects\googletraductiontool\remove.png")

def remove_text():
    text.delete("1.0", END)

remove_button = Button(image=remove_image, borderwidth=0, command=remove_text, bg="white")
remove_button.place(x=560, y=20)




label = Label(text=f"0 / 5000", fg="gray", bg="white")
label.place(x=500, y=210)




while True:
    length = len(text.get("1.0", END)) - 1
    label.config(text=f"{length} / 5000")
    window.update_idletasks()
    window.update()




