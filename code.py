from time import strftime
from tkinter import Label, Tk

window = Tk()
window.title("")
window.geometry("200x80")
window.configure(bg="red")  # =======Background of the clock=====
window.resizable(False, False)  # =====setting a fixed window size =======

clock_label = Label(
    window, bg="red", fg="white", font=("Times", 30, "bold"), relief="flat"
)
clock_label.place(x=20, y=20)


def update_label():
    """
    This function will update the clock
    every 80 milliseconds
    """
    current_time = strftime("%H: %M: %S")
    clock_label.configure(text=current_time)
    clock_label.after(80, update_label)


update_label()
window.mainloop()