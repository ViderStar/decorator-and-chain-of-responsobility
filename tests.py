import unittest
from handler import RequestHandler, RequestLogger, RequestAuthorizer


class TestRequestHandler(unittest.TestCase):
    def setUp(self):
        self.handler = RequestHandler()

    def test_handle_request(self):
        request = {"data": "test_data"}
        result = self.handler.handle_request(request)
        self.assertEqual(result, "Обработка запроса: {'data': 'test_data'}")


class TestRequestLogger(unittest.TestCase):
    def setUp(self):
        self.handler = RequestHandler()
        self.logger = RequestLogger(self.handler)

    def test_handle_request(self):
        request = {"data": "test_data"}
        result = self.logger.handle_request(request)
        self.assertEqual(result, "Обработка запроса: {'data': 'test_data'}")


class TestRequestAuthorizer(unittest.TestCase):
    def setUp(self):
        self.handler = RequestHandler()
        self.authorizer = RequestAuthorizer(self.handler)

    def test_handle_request_authorized(self):
        request = {"data": "test_data", "token": "secret"}
        result = self.authorizer.handle_request(request)
        self.assertEqual(result, "Обработка запроса: {'data': 'test_data', 'token': 'secret'}")

    def test_handle_request_not_authorized(self):
        request = {"data": "test_data", "token": "invalid"}
        result = self.authorizer.handle_request(request)
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()