# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestTransactionsController(BaseTestCase):
    """TransactionsController integration test stubs"""

    def test_transaction_analyses_get(self):
        """Test case for transaction_analyses_get

        test summary
        """
        response = self.client.open(
            'transaction/analyses',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
