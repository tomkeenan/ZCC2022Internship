from datetime import datetime
from TicketHandler import TicketHandler


class UI:
    def __init__(self):
        self.ticket_handler = TicketHandler()

    def run(self):
        self.__start_menu()
        # exit program if there are no tickets in account
        if self.__display_page_of_tickets() == -1:
            print('There are no tickets in the account')
            self.__goodbye()
            return
        self.__display_menu()
        # read user input until user exits program
        while 1:
            command = input('Command: ')
            print()
            if command == '1':
                self.__display_page_of_tickets()
            elif command == '2':
                self.__read_ticket_id_from_user()
            elif command == '+':
                if self.ticket_handler.page_next() is None:
                    self.__display_page_of_tickets()
                else:
                    print('Error: There is no next page\n')
            elif command == '-':
                if self.ticket_handler.page_prev() is None:
                    self.__display_page_of_tickets()
                else:
                    print('Error: There is no previous page\n')
            elif command == 'menu':
                self.__display_menu()
            elif command == 'exit':
                self.__goodbye()
            else:
                print('Error: Invalid Command')

    # displays a ticket page on console
    # returns -1 if there are no tickets on account
    def __display_page_of_tickets(self):
        tickets = self.ticket_handler.get_page_of_tickets()
        if tickets is None:
            return -1
        print()
        for ticket in tickets:
            self.__display_ticket_info(ticket, False)
        print(f'Page {self.ticket_handler.get_page()}\n')

    # displays a ticket with its description on console if the ticket with id is present
    def __display_ticket_from_id(self, ticket_id):
        ticket = self.ticket_handler.get_ticket_from_id(ticket_id)
        if ticket is not None:
            print()
            self.__display_ticket_info(ticket, True)
            self.__display_menu()
        else:
            print(f"Ticket with ID {ticket_id} not found")
            self.__display_menu()

    def __read_ticket_id_from_user(self):
        while 1:
            ticket_id = input("Enter ID of ticket: ")
            print()
            try:
                ticket_id = int(ticket_id)
                self.__display_ticket_from_id(ticket_id)
                break
            except ValueError:
                print("Error: Not a valid ticket ID -> Must be a number")

    # Reads user input until program is started or exited
    def __start_menu(self):
        print("Welcome to the Zendesk Ticket Viewer\n"
              "Created by Tom Keenan for the 2022 Zendesk Internship Coding Challenge\n"
              "->Enter \'start\' to view tickets\n"
              "->Enter \'exit\' to close\n")
        while 1:
            command = input('Command: ')
            if command == 'start':
                return
            elif command == 'exit':
                self.__goodbye()
            else:
                print('Error: Invalid Command')

    # format ticket information
    @staticmethod
    def __display_ticket_info(ticket, description):
        created_at = str(datetime.strptime(
            ticket["created_at"], '%Y-%m-%dT%H:%M:%SZ')).split(' ')
        date_time = f'at {created_at[1]} on the {created_at[0]}'

        append = ''
        if description:
            append = f'\nDescription:\n{ticket["description"]}\n'

        print(f'TICKET ID: {ticket["id"]}\n'
              f'Requested by: {ticket["requester_id"]}\n'
              f'Subject: "{ticket["subject"]}"\n'
              f'Created: {date_time}\n'
              f'Current status: {ticket["status"].upper()}\n{append}')

    # displays menu on console
    @staticmethod
    def __display_menu():
        print("\n----------------------------------------\n"
              "-> Enter 1 to view all tickets on current page\n"
              "-> Enter 2 to view a ticket by it's ID\n"
              "-> Enter \'+\' to view the next page\n"
              "-> Enter \'-\' to view the previous page\n"
              "-> Enter \'menu\' to view this menu\n"
              "-> Enter \'exit\' to close the program\n"
              "----------------------------------------\n")

    @staticmethod
    def __goodbye():
        print("\nThank you for using the Zendesk Ticket Viewer\n"
              "Have a wonderful day!\n")
        exit()
