import os,shutil
import pyAesCrypt
from data.criptography import do_criptography,do_decriptography

class Manager():
    
    disk = []

    def list_disk(self,data):
        self.disk.clear()
        for i in data['disk']:
            if os.path.exists(f"{i}:\\"):
                self.disk.append(f"{i}:")
        return self.disk
    
    def new_account(self,disk,username,password):
        if os.path.exists(f"{disk}\\") and not os.path.exists(f"{disk}\\file_manager\\{username}"):
            try:
                os.mkdir(f"{disk}\\file_manager")
            except:
                pass
            os.mkdir(f"{disk}\\file_manager\\{username}")
            os.mkdir(f"{disk}\\file_manager\\{username}\\file")
            file_pwd = open(f"{disk}\\file_manager\\{username}\\password.txt","w")
            file_pwd.write(do_criptography(password,password))
            file_pwd.close()
            return True
        
    def login(self,disk,username,password):
        if os.path.exists(f"{disk}\\file_manager\\{username}\\password.txt"):
            if do_decriptography(open(f"{disk}\\file_manager\\{username}\\password.txt", "r").read(),password) == password:
                return True,""
            else:
                return False,"passoword wrong"
        else:
            return False,"account doesn't exsist"
        
    def list_file(self,disk,username):
        return os.listdir(f"{disk}\\file_manager\\{username}\\file")
        
    def get_file(self,file):
        return os.path.splitext(file)
        
    def add_file(self,disk,username,file,replace = False):
        try:
            head, name = os.path.split(file)
            if replace:
                shutil.copy(file,f"{disk}\\file_manager\\{username}\\file")
                return True,name
            else:
                if os.path.exists(f"{disk}\\file_manager\\{username}\\file\\{name}.aes"):
                    return False,"already exsist"
                else:
                    shutil.copy(file,f"{disk}\\file_manager\\{username}\\file")
                    return True,name
        except Exception:
            return False,Exception
        
    def encript(self,disk,username,password,file):
        pyAesCrypt.encryptFile(f"{disk}\\file_manager\\{username}\\file\\{file}", f"{disk}\\file_manager\\{username}\\file\\{file}.aes", password,1024*128)
        os.remove(f"{disk}\\file_manager\\{username}\\file\\{file}")
    
    def decript(self,disk,username,password,file):
        pyAesCrypt.decryptFile(f"{disk}\\file_manager\\{username}\\file\\{file}.aes", f"{disk}\\file_manager\\{username}\\file\\{file}", password)
        os.remove(f"{disk}\\file_manager\\{username}\\file\\{file}.aes")

    def open_file(self,disk,username,file):
        os.system(f"start {disk}\\file_manager\\{username}\\file\\{file}")

    def delete_file(self,disk,username,file):
        if os.path.exists(f"{disk}\\file_manager\\{username}\\file\\{file}.aes"):
            os.remove(f"{disk}\\file_manager\\{username}\\file\\{file}.aes")
        else:
            os.remove(f"{disk}\\file_manager\\{username}\\file\\{file}")

    def rename_file(self,disk,username,file,new_file):
        head,extension = os.path.splitext(file)
        if os.path.exists(f"{disk}\\file_manager\\{username}\\file\\{file}.aes"):
            os.rename(f"{disk}\\file_manager\\{username}\\file\\{file}.aes",f"{disk}\\file_manager\\{username}\\file\\{new_file}{extension}.aes")
        else:
            os.rename(f"{disk}\\file_manager\\{username}\\file\\{file}",f"{disk}\\file_manager\\{username}\\file\\{new_file}{extension}")

    def delete_account(self,disk,username):
        shutil.rmtree(f"{disk}\\file_manager\\{username}")