import pyperclip
import tkinter
import random
import string

def copyPassword (password):
    pyperclip.copy(password)

def generate():
    
    try:
        length = int(lengthVar.get())    
    
    except ValueError:
        lengthVar.set("10")
        return

    characters = string.ascii_lowercase + string.ascii_uppercase
    
    if symbolVar.get() == 1:
        characters += string.punctuation
    if numberVar.get() == 1:
        characters += string.digits
    
    passwordList = random.choices(characters, k = length)
    password = "".join(passwordList)
    
    passwordWindow = tkinter.Toplevel()
    passwordWindow.title("Password")
    passwordWindow.geometry("+85+40")
    window.call("wm", "iconphoto", passwordWindow._w, tkinter.PhotoImage(file = "Password_Generator.png"))
    
    passwordLabel = tkinter.Label(passwordWindow, text = password, font = ("Calibiri", 23))
    passwordLabel.grid(row = 0, column = 0, padx = 10, pady = 10)

    copyButton = tkinter.Button(passwordWindow, command = lambda : copyPassword(password))
    copyButton.config(text = "Copy to clipboard", font = ("Calibiri", 19))
    copyButton.grid(row = 1, column = 0, padx = 10, pady = 10)
    
    passwordWindow.mainloop()

window = tkinter.Tk()
window.title("Password Generator")
window.geometry("+520+130")
window.resizable("False", "False")
window.call("wm", "iconphoto", window._w, tkinter.PhotoImage(file = "Password_Generator.png"))

lengthLabel = tkinter.Label(window, text = "Password Length", font = ("Calibiri", 22))
lengthLabel.grid(row = 0, column = 0, pady = 10, padx = 10)

lengthVar = tkinter.StringVar()
lengthVar.set("10")
lengthSpin = tkinter.Spinbox(window, from_ = 1, to = 50, text = lengthVar, font = ("Calibiri", 15))
lengthSpin.grid(row = 0, column = 1, padx = 20)

symbolVar = tkinter.IntVar()
symbolCheck = tkinter.Checkbutton(window, variable = symbolVar, onvalue = 1, offvalue = 0)
symbolCheck.config(text = "Symbols", font = ("Calibiri", 20))
symbolCheck.grid(row = 1, column = 0, pady = 10)

numberVar = tkinter.IntVar()
numberCheck = tkinter.Checkbutton(window, variable = numberVar, onvalue = 1, offvalue = 0)
numberCheck.config(text = "Numbers", font = ("Calibiri", 20))
numberCheck.grid(row = 1, column = 1)

generateButton = tkinter.Button(window, text = "Generate", font = ("Calibiri", 18), command = generate)
generateButton.grid(row = 2, column = 0, columnspan = 2, pady = 15)

window.mainloop()