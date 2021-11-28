import json
import requests


# class to handle tickets returned by Zendesk API
class TicketHandler:
    _PAGE_LENGTH = 25

    def __init__(self):
        self._user_info = self._read_user_info()
        self._url = f'https://{self._user_info["subdomain"]}.zendesk.com/api/v2/tickets.json?page[size]={self._PAGE_LENGTH}'
        self._current_page = 1

    # public for testing purposes
    def get_response(self,url):
        return requests.get(url, auth=(self._user_info["name"], self._user_info["password"]))

    def _request_data(self, url):
        response = self.get_response(url)
        if response.status_code != 200:
            print('Status:', response.status_code, 'Problem connecting to the API. Exiting.')
            exit()
        data = response.json()
        return data

    # returns page of tickets if present on account
    # returns None otherwise
    def get_page_of_tickets(self):
        data = self._request_data(self._url)
        tickets = data['tickets']
        if tickets is not None:
            return tickets
        else:
            return None

    # finds ticket using its unique id
    # returns ticket if present
    # returns None otherwise
    def get_ticket_from_id(self, ticket_id):
        url = f'https://{self._user_info["subdomain"]}.zendesk.com/api/v2/tickets/{ticket_id}.json'
        response = self.get_response(url)
        if response.status_code != 200:
            return None
        data = response.json()
        return data['ticket']

    # requests next page of tickets
    # returns -1 if there is no next page
    def page_next(self):
        data = self._request_data(self._url)
        if data['meta']['has_more']:
            self._current_page += 1
            self._url = data['links']['next']
            self.get_page_of_tickets()
        else:
            return -1

    # requests previous page of tickets
    # returns -1 if there is no previous page
    def page_prev(self):
        data = self._request_data(self._url)
        if self._current_page > 1:
            self._url = data['links']['prev']
            self._current_page -= 1
            self.get_page_of_tickets()
        else:
            return -1

    def get_page(self):
        return self._current_page

    @staticmethod
    def _read_user_info():
        with open("user_info.json", 'r') as file:
            credentials = json.load(file)
            return credentials

