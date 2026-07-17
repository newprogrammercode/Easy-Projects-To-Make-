from tkinter import *
from cryptography.fernet import Fernet
import os

class Main:
    def __init__(self):
        self.root = Tk()
        self.root.title("Encoder")
        self.root.geometry("720x600")
        self.root.config(bg = "#000")
        self.status = Label(self.root , text = "" , fg = "green" , font = ("Comic Sans MS", 12 , "bold") , pady = 2 , padx = 2, bg = "#000")
        self.status.pack()
        self.original_text = Text(self.root , font = ("Comic Sans MS" , 12 , "bold") , fg = "lime" , padx = 2 , pady = 2, bg = "white", height = 10)
        self.original_text.pack(fill = "x")
        
       
        self.original_text.bind("<Return>", lambda event: self.main("the_key_of_the_proggram.key"))
        
        self.button = Button(self.root , text="Encrypt", font = ("Comic Sans MS" ,  12 , "bold") , fg = "red" , padx = 2 , pady = 2,borderwidth= 0 , bd = 0 , command=lambda: self.main("the_key_of_the_proggram.key"))
        self.button.pack(pady = 10)
        self.encrypted_text = Text(self.root , font = ("Comic Sans MS" , 12 , "bold") , fg = "lime" , pady = 2, padx = 2 , bg = "white", height = 10)
        self.encrypted_text.pack(fill = "x")
    def main(self , file):
        def load_key(file):
            if os.path.exists(file):
                with open(file , "rb") as f:
                    return f.read()
            else:
                key = Fernet.generate_key()
                with open(file , "wb") as f:
                    f.write(key)
                    return key
        key = load_key(file)
        f = Fernet(key)
        or_text = self.original_text.get("1.0" , "end-1c")
        encoded_text = f.encrypt(or_text.encode())
        self.encrypted_text.config(state="normal")
        self.encrypted_text.delete("1.0" , END)
        self.encrypted_text.insert("1.0" , encoded_text.decode())
        self.encrypted_text.config(state="disabled")
        self.status.configure(text = "Success!!!")
        self.root.after(2000 , lambda: self.status.configure(text = ""))
        return "break" 
    def run(self):
        self.root.mainloop()

m = Main()
m.run()
