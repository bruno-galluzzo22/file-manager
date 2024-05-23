# File Manager

Con questo piccolo software scritto in Python con il quale è possibile crittografare tutti i tipi di file, l'unica cosa che bisnogna fare è quella di crearsi un account.
Questo account deve essere provvisto di un username e una password che l'utente si appresta a inserire ogni volta che desidera accedere ai suoi file crittografati.
In questa repository è presenta la cartella:
 * nevn, che contiene l' ambiente virtuale su cui si basa il software.
 * software, che contiene tutti i file che permettono il funzionamento del software
  
## Come si presenta:

Prima di tutto si crea un account, inserendo un nome e una password

![](images\new_account.png)

Dopo di che avviene la creazione di un piccolo menu:

![](images\empty.png)

In seguito si clicca sul pulsante al centro per inserire un file;

![](images\file.png)
![](images\file_added.png)

quello che viene salvato sul disco è questo:

![](images\criptography.png)

Inoltre la password dell'account è stata criptografata usando l'algoritmo hashes.SHA256

![](images\password.png)

## Quali librerie ho usato

Le libreria che ho usato per la realizzazione di questo software sono:
 * [customtkinter](https://pypi.org/project/customtkinter/) : per la realizzazione dell'interfaccia grafica
 * [cripthography](https://pypi.org/project/cryptography/): per criptografare la password dell'utente utilizzando l'algoritmo [hashes.SHA256](https://www.hola-cripto.com/glossario-criptovalute/sha256-significato/)
 * [pyAesCrypt](https://pypi.org/project/pyAesCrypt/): per la criptografare i file di ogni utente 
 * [CTkMessagebox](https://pypi.org/project/CTkMessagebox/): per far apparire i vari messaggi 