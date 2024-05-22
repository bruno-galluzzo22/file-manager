import tkinter
import customtkinter as CTk
from data.manager import Manager
from PIL import Image, ImageTk
from CTkMessagebox import CTkMessagebox
import json

CTk.set_appearance_mode("System")
CTk.set_default_color_theme("blue")

class Login():
    
    def __init__(self):
        
        self.disk = ""
        
        window.grid_columnconfigure(1, weight=1)
        window.geometry(f"{data['size']['login']['x']}x{data['size']['login']['y']}")
        
        self.label_image_disk = CTk.CTkLabel(window,text = "",image = images['disk'])
        self.label_image_disk.grid(row = 0,column = 0,padx = (20,5),pady = (20,10))
        self.combobox = CTk.CTkComboBox(window,values = file_manager.list_disk(data),corner_radius = 10,font = ("Open Sans",25),dropdown_font = ("Open Sans",20),state = "readonly",command = self.combobox_choice)
        self.combobox.grid(row = 0, column = 1, columnspan = 2 ,sticky = "nsew",padx = (5,20),pady = (20,10))
        self.combobox.set("select a disk")
        
        self.label_image_username = CTk.CTkLabel(window,text = "",image = images['login'])
        self.label_image_username.grid(row = 1,column = 0,padx = (20,5),pady = (10,10))
        self.entry_username = CTk.CTkEntry(window,font = ("Open Sans",25),placeholder_text= "username",corner_radius = 10)
        self.entry_username.grid(row = 1,column = 1,columnspan = 2,sticky = "nsew",padx = (5,20),pady = (10,10))
        
        self.label_image_password = CTk.CTkLabel(window,text = "",image = images['password'])
        self.label_image_password.grid(row = 2,column = 0,padx = (20,5),pady = (10,10))
        self.entry_password = CTk.CTkEntry(window,font = ("Open Sans",25),placeholder_text= "password",corner_radius = 10,show = "*")
        self.entry_password.grid(row = 2,column = 1,columnspan = 2,sticky = "nsew",padx = (5,20),pady = (10,10))
        
        self.button_login = CTk.CTkButton(window,text="",image = images["enter"],command = self.function_login,corner_radius = 10)
        self.button_login.grid(row = 3,column = 0,columnspan = 2,sticky = "nsew",padx = (20,5),pady = (10,10))
        self.button_new_account = CTk.CTkButton(window,text="",image = images["new_account"],command = self.new_account_function,corner_radius = 10)
        self.button_new_account.grid(row = 3,column = 2,columnspan = 1,sticky = "nsew",padx = (5,20),pady = (10,10))
        
    def reset(self):
        self.entry_username.delete(0,tkinter.END)
        self.entry_password.delete(0,tkinter.END)
        self.entry_username.configure(placeholder_text = "username") 
        self.entry_password.configure(placeholder_text = "password") 
        self.combobox.set("select a disk")
        self.disk = ""   
        
    def combobox_choice(self,choice):
        self.disk = choice
        
    def check_data(self):
        self.username = self.entry_username.get()
        self.password = self.entry_password.get()
        
        self.message = ""
        if self.disk == "":
            self.message += str("\n - disk")
        if self.username == "":
            self.message += str("\n - username")
        if self.password == "":
            self.message += str("\n - password")
            
        if self.message != "":
            msg = CTkMessagebox(title="Error", message=f"Insert: {self.message}!", icon="cancel",font = ("Open Sans",20),width=300,option_1="Ok")
            if msg.get() == "Ok":
                self.reset()  
        
    def function_login(self):
        self.check_data() 

        if self.message == "":
            check,message = file_manager.login(self.disk,self.username,self.password)
            if check:
                clear()
                Main(self.disk,self.username,self.password)
            else:
                msg = CTkMessagebox(title="Error", message=message, icon="cancel",font = ("Open Sans",20),option_1="Ok",width = 400)
                if msg.get() == "Ok":
                    self.reset()
                    
    def new_account_function(self):
        self.check_data() 
            
        if self.message == "":
            if file_manager.new_account(self.disk,self.username,self.password):
                self.message = CTkMessagebox(title="Info", message="your account has been created!",font = ("Open Sans",20), option_1="Ok",icon = "check")
                if self.message.get() == "Ok":
                    clear()
                    Main(self.disk,self.username,self.password)
    
    
class Main():
    
    def __init__(self,disk,username,password):
        
        self.disk = disk
        self.username = username
        self.password = password
        
        window.grid_columnconfigure(1, weight=0)
        window.geometry(f"{data['size']['main']['x']}x{data['size']['main']['y']}")
        
        button_back = CTk.CTkButton(window,image = images["home"],text = "",command = self.back)
        button_back.grid(row = 0,column = 0,padx = (20,10),pady = (20,10))
        button_add = CTk.CTkButton(window,image = images["add"],text = "",command = self.file_dialog)
        button_add.grid(row = 0,column = 1,padx = (10,10),pady = (20,10)) 
        button_del_account = CTk.CTkButton(window,image = images["delete_account"],text = "",command = self.delete_account)
        button_del_account.grid(row = 0,column = 2,padx = (10,20),pady = (20,10)) 
        
        self.show()

    def show(self):
        
        self.frame = CTk.CTkScrollableFrame(window,width = data['size']['main']['x']-60,height = 200)
        self.frame.grid(row = 1,column = 0,columnspan = 3)
        
        row = 0
        
        if file_manager.list_file(self.disk,self.username) == []:
            
            label_file = CTk.CTkLabel(self.frame,text = "Insert file",font = ("Open Sans",20),width = data['size']['main']['x']-60,height = 200)
            label_file.grid(row = 0,column = 0,columnspan = 9,sticky = "nwes")

        for file in file_manager.list_file(self.disk,self.username):

            file,extension = file_manager.get_file(file)

            label_file = CTk.CTkLabel(self.frame,text = file,font = ("Open Sans",20))
            label_file.grid(row = row,column = 0,columnspan = 9,padx = (5,0),pady = (10,5),sticky = "w")

            button_open = CTk.CTkButton(self.frame,text = "",image = images["open"],command = lambda file = file : self.open_file(file))
            button_open.grid(row = (row+1),column = 0,columnspan = 3,padx = (5,0),pady = (0,20),sticky = "w")
            button_delete_file = CTk.CTkButton(self.frame,text = "",image = images["delete_file"],command = lambda: self.delete_file(file) )
            button_delete_file.grid(row = (row+1),column = 4,columnspan = 3,padx = 5,pady = (0,20),sticky = "w")
            button_encript = CTk.CTkButton(self.frame,text = "",image = images["rename"],command = lambda file = file : self.rename(file))
            button_encript.grid(row = (row+1),column = 7,columnspan = 3,padx = (0,5),pady = (0,20),sticky = "w")

            row += 2
            
    def clear(self):
        list = self.frame.winfo_children()
        for i in list:
            i.destroy()
    
    def file_dialog(self):
        filetypes = (('text files', '*.txt'),('All files', '*.*'))
        filename = tkinter.filedialog.askopenfilename(title='Open a file',initialdir='/',filetypes=filetypes)
        
        check, file = file_manager.add_file(self.disk,self.username,filename)
        
        if check:
            file_manager.encript(self.disk,self.username,self.password,file)
            self.message = CTkMessagebox(title="Info", message="your file has been added!",font = ("Open Sans",20), option_1="Ok",icon = "check")
            self.clear()
            self.show()
        elif file == "already exsist":
            self.message = CTkMessagebox(title="Info", message=" your file already exists! \n you want to replace it?",font = ("Open Sans",20), option_1="Yes",option_2="No",width = 500,icon = "warning")
            if self.message.get() == "Yes":
                check, file = file_manager.add_file(self.disk,self.username,filename,True)
                file_manager.encript(self.disk,self.username,self.password,file)
                self.clear()
                self.show()

    def encrypt_all(self):
        
        for file in file_manager.list_file(self.disk,self.username):
            
            head,extension = file_manager.get_file(file)
            
            if extension != ".aes": 
                file_manager.encript(self.disk,self.username,self.password,file)

        window.destroy()

    def rename(self,file):
        
        def disable():
            list = self.frame.winfo_children()
            for i in list:
                try:
                    i.configure(state = "disabled")
                except:
                    pass
                
            list = window.winfo_children()
            for i in list:
                try:
                    i.configure(state = "disabled")
                except:
                    pass
            
        def activate():
            list = self.frame.winfo_children()
            for i in list:
                try:
                    i.configure(state = "normal")
                except:
                    pass
                
            list = window.winfo_children()
            for i in list:
                try:
                    i.configure(state = "normal")
                except:
                    pass
            
            top_level.destroy()
        
        def ren_file():
            if entry.get() != "" and not "." in entry.get() and not " " in entry.get():
                print("ciao")
                file_manager.rename_file(self.disk,self.username,file,entry.get())
                top_level.destroy()
                self.clear()
                self.show()
                activate()
            else:
                self.message = CTkMessagebox(title="warning", message="dot and space are not allowed!",font = ("Open Sans",20), option_1="Ok",icon = "warning")
        
        disable()
        
        top_level = CTk.CTkToplevel(window)
        top_level.title("")
        top_level.geometry("%d+%d" % (window.winfo_x()+30,window.winfo_y()+30))
        top_level.geometry(f"{data['size']['top_level']['x']}x{data['size']['top_level']['y']}")
        top_level.wm_attributes('-topmost', True)
        top_level.resizable(False,False)
        
        entry = CTk.CTkEntry(top_level,placeholder_text = "new name",width = 150,font = ("Open Sans",20))
        entry.grid(row = 0,column = 0,padx = (5,0),pady = (10,10))
        
        button = CTk.CTkButton(top_level,text = "", image = images["enter"],width = 50,command =  ren_file)
        button.grid(row = 0,column = 1,padx = (0,5),pady = (10,10))
        
        top_level.protocol('WM_DELETE_WINDOW',activate)

    def open_file(self,file):

        file_manager.decript(self.disk,self.username,self.password,file)
        file_manager.open_file(self.disk,self.username,file)
        window.protocol('WM_DELETE_WINDOW',self.encrypt_all)
 
    def delete_file(self,file):
        self.message = CTkMessagebox(title="Question", message="Do you want delete your file?",font = ("Open Sans",20), option_1="Yes",option_2="No",width = 500,icon = "warning")
        if self.message.get() == "Yes":
            file_manager.delete_file(self.disk,self.username,file)
            self.message = CTkMessagebox(title="Info", message="your file has been destroyed!",font = ("Open Sans",20), option_1="Ok")
            if self.message.get() == "Ok": 
                self.clear()
                self.show()

    def delete_account(self):
        self.message = CTkMessagebox(title="Question", message="Do you want delete your account?",font = ("Open Sans",20), option_1="Yes",option_2="No",width = 500,icon = "warning")
        if self.message.get() == "Yes":
            file_manager.delete_account(self.disk,self.username)
            self.message = CTkMessagebox(title="Info", message="your account has been destroyed!",font = ("Open Sans",20), option_1="Ok")
            if self.message.get() == "Ok": 
               clear()
               Login()
    
    def back(self):
        clear()
        Login() 

def clear():
    list = window.winfo_children()
    for l in list:
        l.destroy()    

if __name__ == "__main__":
    
    file_manager = Manager()
    data = json.load(open("software\\data\\data.json"))
    images = {
       "login": CTk.CTkImage(Image.open(data['images']['login']), size=(30, 30)), 
       "new_account": CTk.CTkImage(Image.open(data['images']['new_account']), size=(30, 30)),
       "lock": CTk.CTkImage(Image.open(data['images']['lock']), size=(30, 30)),
       "enter": CTk.CTkImage(Image.open(data['images']['enter']), size=(30, 30)),
       "disk": CTk.CTkImage(Image.open(data['images']['disk']), size=(30, 30)),
       "delete_account": CTk.CTkImage(Image.open(data['images']['delete_account']), size=(30, 30)),
       "home": CTk.CTkImage(Image.open(data['images']['home']), size=(30, 30)),
       "unlock": CTk.CTkImage(Image.open(data['images']['unlock']), size=(30, 30)),
       "open": CTk.CTkImage(Image.open(data['images']['open']), size=(30, 30)),
       "delete": CTk.CTkImage(Image.open(data['images']['delete']), size=(30, 30)),
       "add": CTk.CTkImage(Image.open(data['images']['add']), size=(30, 30)),
       "delete_file": CTk.CTkImage(Image.open(data['images']['delete_file']), size=(30, 30)),
       "password": CTk.CTkImage(Image.open(data['images']['password']), size=(30, 30)),
       "rename": CTk.CTkImage(Image.open(data['images']['rename']), size=(30, 30)),
    }
    
    window = CTk.CTk()
    window.title("")
    window.resizable(False,False)
    Login()
    window.mainloop()