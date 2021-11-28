from datetime import datetime
from TicketHandler import TicketHandler


class UI:
    def __init__(self):
        self.ticket_handler = TicketHandler()

    def run(self):
        print('Start')
        if self.__display_page_of_tickets() == -1:
            print('End')
            return
        self.__display_menu()
        while 1:
            command = input('Command: ')
            print()
            if command == '1':
                self.__display_page_of_tickets()
            elif command == '2':
                self.__display_ticket_from_id(1)
            elif command == 'menu':
                self.__display_menu()
            elif command == 'exit':
                break
            else:
                print('Error: Invalid Command')

    # displays a ticket page on console
    # returns -1 if there are no tickets on account
    def __display_page_of_tickets(self):
        tickets = self.ticket_handler.get_page_of_tickets()
        if tickets is None:
            return -1
        for ticket in tickets:
            self.__display_ticket_info(ticket,False)

    # displays a ticket with its description on console if the ticket with id is present
    def __display_ticket_from_id(self, ticket_id):
        ticket = self.ticket_handler.get_ticket_from_id(ticket_id)
        if ticket is not None:
            print()
            self.__display_ticket_info(ticket,True)
        else:
            print(f"Ticket with ID {ticket_id} not found")
            self.__display_menu()

    # format ticket information
    @staticmethod
    def __display_ticket_info(ticket,description):
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
              "-> Enter \'menu\' to view this menu\n"
              "-> Enter \'exit\' to close the program\n"
              "----------------------------------------\n")