import os
import time
from datetime import datetime

import pyfiglet


def clear_terminal ():
	if os.name == "nt":
		os.system ("cls")
	else:
		os.system ("clear")
	print (pyfiglet.figlet_format ("\nPARKING    LOT"))


def user_answer ():
	while True:
		try:
			answer = int (
				input (
					"Select an option to continue:\n"
					"[1] Grab a ticket\n"
					"[2] Pay ticket\n"
					"[0] Exit\n"
				)
			)
			if answer == 0:
				print ("Thank you for your visit!")
				break
			if 1 <= answer <= 3:
				return answer
			else:
				print ("Invalid option. Please select a number between 1 and 3.")
		except ValueError:
			print ("Invalid input. Please enter a valid number.")


class garage:
	def __init__ (self):
		self.available_tickets = [num for num in range (1, 11)]
		self.ticket_records = {}  # Dictionary to store ticket issuance date and time
	
	def issue_ticket (self):
		if self.available_tickets:
			ticket_number = self.available_tickets.pop (0)
			now = datetime.now ()  # Get the current date and time
			self.ticket_records [ticket_number] = now  # Store the issuance date and time
			return ticket_number
		else:
			return None
	
	def return_ticket (self, ticket_number):
		if 1 <= ticket_number <= 10:
			self.available_tickets.append (ticket_number)
			del self.ticket_records [ticket_number]
	
	def interface (self):
		while True:
			clear_terminal ()
			print (f"Parking available: ", len (self.available_tickets), "\n")
			answer_input = user_answer()
			if answer_input == 1:
				ticketID = self.issued_ticket()
				if ticketID is not None:
					clear_terminal()
					print("Print your ticketID:", ticketID)
					current_time = datetime.now()
					print(f' ticket expedite {current_time}\n')
					print("Have a good day!")
					time.sleep(5)
				else:
					print("No spaces available")
					time.sleep(5)
			elif answer_input == 2:
				clear_terminal()
				ticketNumber = int(input(f'Enter your ticket number \n'))
				if ticketNumber in self.ticket_records:
				    current_time = datetime.now()
				    #duration = current_time - self.ticket_records[ticket_number]
				    #totaltime = duration.totalseconds()/60
				    #amount = totaltime*0.5
				    #amountround = round (amount, 2)
				    #print(f' Ticket {ticketNumber} has been paid. ')
				    #print('Parking duration: ', duration)
				    #print('Total charge: $', amountround)
				    input('Click enter')
				    print('Have a good day')
				    clear_terminal()
				    print('You have 15 minutes to leave')
				    time.sleep(5)
				    self.return_ticket(ticketNumber)
                else:
                    print("Record not found")
		
		    
garage = garage ()
garage.interface ()
