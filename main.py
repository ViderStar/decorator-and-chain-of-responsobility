from handler import RequestHandler, RequestLogger, RequestAuthorizer
import tests

if __name__ == "__main__":
    handler = RequestHandler()
    logger_decorator = RequestLogger(handler)
    authorizer_decorator = RequestAuthorizer(logger_decorator)

    request = {"data": "test_data", "token": "secret"}
    response = authorizer_decorator.handle_request(request)
    print(response)

    request = {"data": "test_data", "token": "invalid"}
    response = authorizer_decorator.handle_request(request)
    print(response)

    # Запустите тесты
    tests.unittest.main(argv=[""], exit=False)