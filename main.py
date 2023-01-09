import requests
import json
from art import *
from pystyle import Colorate, Colors, Center
from os import system
from time import sleep
import pydantic


from getpass import getpass 

from covid import Covid

#message aux start


header_final = """
  
░██╗░░░░░░░██╗███████╗██████╗░ ░█████╗░░█████╗░██╗░░░██╗██╗██████╗░
░██║░░██╗░░██║██╔════╝██╔══██╗ ██╔══██╗██╔══██╗██║░░░██║██║██╔══██╗
░╚██╗████╗██╔╝█████╗░░██████╦╝ ██║░░╚═╝██║░░██║╚██╗░██╔╝██║██║░░██║
░░████╔═████║░██╔══╝░░██╔══██╗ ██║░░██╗██║░░██║░╚████╔╝░██║██║░░██║
░░╚██╔╝░╚██╔╝░███████╗██████╦╝ ╚█████╔╝╚█████╔╝░░╚██╔╝░░██║██████╔╝
░░░╚═╝░░░╚═╝░░╚══════╝╚═════╝░ ░╚════╝░░╚════╝░░░░╚═╝░░░╚═╝╚═════╝░

---------------------------------------------------------------------

1: Get Total Deaths                3: Get Information By Country

2: Get Total Confirmed cases       4: Get Pourcentage dead currently

---------------------------------------------------------------------
\n\n\n\n"""

#envoyer le message aux start!

print(Colorate.Diagonal(Colors.cyan_to_blue, Center.XCenter(header_final)))


#import data 
covid = Covid()
confirmed = covid.get_total_confirmed_cases()
deaths = covid.get_total_deaths()

#message de verification pour le mode

mode_start = input(Colorate.Diagonal(Colors.cyan_to_green,(f"Send: ")))

#programme pour voir les morts du covid

if mode_start.startswith("1"):
	print(Colorate.Diagonal(Colors.green_to_red,(f"Total Deaths: {deaths}")))
	getpass(Colorate.Diagonal(Colors.yellow_to_red,("Thank for using the programme, Press Enter to close the program ")))

#programme pour voir les cas de covids

if mode_start.startswith("2"):
	print(Colorate.Diagonal(Colors.yellow_to_red,(f"Total Confirmed cases: {confirmed}")))
	getpass(Colorate.Diagonal(Colors.yellow_to_red,("Thank for using the programme, Press Enter to close the program ")))

#programme pour voir les informations du covid par rapport aux pays

if mode_start.startswith("3"):
	info_country = input("Enter the country! ")
	italy_cases = covid.get_status_by_country_name(info_country)
	print(Colorate.Diagonal(Colors.yellow_to_red,(f"Informations: {italy_cases}")))
	getpass(Colorate.Diagonal(Colors.yellow_to_red,("Thank for using the programme, Press Enter to close the program ")))

#programme pour voir le pourcentage de mort qui on eux le covid!

if mode_start.startswith("4"):
	deaths1 = deaths * 100
	total = confirmed / deaths1
	print(Colorate.Diagonal(Colors.yellow_to_red,(f"Total Pourcentage Confirmed Cases Dead : {total} %")))
	getpass(Colorate.Diagonal(Colors.yellow_to_red,("Thank for using the programme, Press Enter to close the program ")))





