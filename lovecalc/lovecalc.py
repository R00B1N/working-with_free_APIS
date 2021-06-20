#!/usr/bin/python3
#
# lovecalc: script que utiliza una api, la cual mide la compatibilidad de 2 personas segun el nombre.
# By Blackster.

import os
import requests
from pyfiglet import Figlet
from colorama import Fore, init
init()

banner = Figlet(font='slant')

def inicio():
	os.system('clear')
	print(Fore.RED)
	print(banner.renderText('LoveCalc *.*'))
	print("\tBy Blackster")

if __name__ == '__main__':
	while True:
		inicio()
		ask_first_name = str(input("\n[*]Introduce un nombre >> "))
		ask_second_name = str(input("[*]Introduce el nombre de la otra persona "))
		url = "https://love-calculator.p.rapidapi.com/getPercentage"
		querystring = {"fname": + ask_first_name,"sname": + ask_second_name}
		headers = {
		'x-rapidapi-key': "1ea0c39aa8msh10f547604891135p1101abjsnf2a2f631b709",
		'x-rapidapi-host': "love-calculator.p.rapidapi.com"
		}
		response = requests.request("GET", url, headers=headers, params=querystring)
		print(response.text)