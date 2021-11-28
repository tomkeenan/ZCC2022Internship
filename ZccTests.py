import unittest
from TicketHandler import TicketHandler


class ZccTests(unittest.TestCase):

    def test_user_info_valid(self):
        # correct response should have status code == 200
        url = self._url = f'https://zcctomkeenan.zendesk.com/api/v2/tickets.json?page[size]=25'
        th = TicketHandler()
        response = th.get_response(url)
        self.assertEqual(response.status_code, 200)

    def test_user_info_invalid(self):
        # incorrect response should have status code != 200
        url = self._url = f'https://wrongsubdomain.zendesk.com/api/v2/tickets.json?page[size]=25'
        th = TicketHandler()
        response = th.get_response(url)
        self.assertNotEqual(response.status_code, 200)


