import unittest
from src.TicketHandler import TicketHandler


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

    def test_get_page_of_tickets(self):
        # there are tickets present on account -> should return not null
        th = TicketHandler()
        tickets = th.get_page_of_tickets()
        self.assertIsNotNone(tickets)

    def test_get_ticket_from_id(self):
        # check method has correct return values
        th = TicketHandler()

        # present in account
        ticket = th.get_ticket_from_id(1)
        self.assertIsNotNone(ticket)

        # not present in account
        ticket = th.get_ticket_from_id(9999)
        self.assertIsNone(ticket)

    def test_page_next(self):
        # check method only pages when there is a next page
        # should return -1 when paging is not possible
        th = TicketHandler()
        # testing on account with 101 tickets using PAGE_LENGTH 25
        self.assertIsNone(th.page_next())
        self.assertIsNone(th.page_next())
        self.assertIsNone(th.page_next())
        self.assertIsNone(th.page_next())
        self.assertEqual(th.page_next(),-1)

    def test_page_prev(self):
        # check method only pages when there is a previous page
        # should return -1 when paging is not possible
        th = TicketHandler()
        # testing on account with 101 tickets using PAGE_LENGTH 25
        self.assertEqual(th.page_prev(), -1)
        th.page_next()
        th.page_next()
        self.assertIsNone(th.page_prev())
        self.assertIsNone(th.page_prev())


