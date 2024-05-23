# File Manager

Con questo piccolo software scritto in Python con il quale è possibile crittografare tutti i tipi di file, l'unica cosa che bisnogna fare è quella di crearsi un account.
Questo account deve essere provvisto di un username e una password che l'utente si appresta a inserire ogni volta che desidera accedere ai suoi file crittografati.
In questa repository è presenta la cartella:
 * nevn, che contiene l' ambiente virtuale su cui si basa il software.
 * software, che contiene tutti i file che permettono il funzionamento del software
  
## Come si presenta:

Prima di tutto si crea un account, inserendo un nome e una password

![new_account](https://github.com/bruno-galluzzo22/file-manager/assets/165049537/bb0d5abf-4e52-4fd5-b947-88e3fb10fe32)

Dopo di che avviene la creazione di un piccolo menu:

![empty](https://github.com/bruno-galluzzo22/file-manager/assets/165049537/b2e46874-bea2-4c92-87bf-ef8a27b58d34)

In seguito si clicca sul pulsante al centro per inserire un file;

![file](https://github.com/bruno-galluzzo22/file-manager/assets/165049537/ac243886-e52f-491f-8f1a-c416a34d3c31)
![add_file](https://github.com/bruno-galluzzo22/file-manager/assets/165049537/f98d98d8-9238-4a5d-b1fe-f8c88659dcb7)

quello che viene salvato sul disco è questo:

![criptography](https://github.com/bruno-galluzzo22/file-manager/assets/165049537/140c0fac-fac6-49e2-9ca6-6c6be8e7f7a9)

Inoltre la password dell'account è stata criptografata usando l'algoritmo hashes.SHA256

![password](https://github.com/bruno-galluzzo22/file-manager/assets/165049537/a36a224b-44d6-4411-8c00-28d6012d99bf)

## Quali librerie ho usato

Le libreria che ho usato per la realizzazione di questo software sono:
 * [customtkinter](https://pypi.org/project/customtkinter/) : per la realizzazione dell'interfaccia grafica
 * [cripthography](https://pypi.org/project/cryptography/): per criptografare la password dell'utente utilizzando l'algoritmo [hashes.SHA256](https://www.hola-cripto.com/glossario-criptovalute/sha256-significato/)
 * [pyAesCrypt](https://pypi.org/project/pyAesCrypt/): per la criptografare i file di ogni utente 
 * [CTkMessagebox](https://pypi.org/project/CTkMessagebox/): per far apparire i vari messaggi 