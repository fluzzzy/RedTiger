import os
import time



from Options.Options import *


TitrePage("Red-Tiger | Info")


LAPprint(couleur.RED + "\nRecherche d'information..")
time.sleep(1)

LAPprint(f"""\n{couleur.RED}Informations:
{couleur.YELLOW}Username      :  {couleur.CYAN}{nom_utilisateur}
{couleur.YELLOW}Nom Tool      :  {couleur.CYAN}{nom}
{couleur.YELLOW}Version       :  {couleur.CYAN}{version}
{couleur.YELLOW}Codage        :  {couleur.CYAN}{codage}
{couleur.YELLOW}Language      :  {couleur.CYAN}{language}
{couleur.YELLOW}Risque Virus  :  {couleur.CYAN}Aucun
{couleur.YELLOW}Token Grabb   :  {couleur.CYAN}Aucun
{couleur.YELLOW}Créateur      :  {couleur.CYAN}{createur}
{couleur.YELLOW}Discord [02]  :  {couleur.CYAN}{discord}
""" + couleur.RESET)

input(couleur.RED + "\nFais entrer pour continuer -> " + couleur.RESET)
Reset()

os.system("pause")