import json
import requests


# class to handle tickets returned by Zendesk API
class TicketHandler:
    def __init__(self):
        self._user_info = self._read_user_info()
        self._url = f'https://{self._user_info["subdomain"]}.zendesk.com/api/v2/tickets.json?page[size]=25'
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

    def get_page_of_tickets(self):
        data = self._request_data(self._url)
        tickets = data['tickets']
        if tickets is not None:
            return tickets
        else:
            return None

    @staticmethod
    def _read_user_info():
        with open("user_info.json", 'r') as file:
            credentials = json.load(file)
            return credentials

