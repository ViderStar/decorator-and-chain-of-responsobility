## Связка паттернов Декоратор и Цепочка обязанностей 

Данный код демонстрирует принцип работы паттерна "Декоратор" и паттерна "Цепочка обязанностей", а также показывает, как эти паттерны можно использовать вместе для обработки запросов.

- **handler.py** — определены базовый абстрактный класс Handler и два его наследника - класс RequestHandler и класс Decorator. Класс RequestHandler реализует базовую обработку запросов, а класс Decorator - обертку для других обработчиков запросов. Также в файле определены два декоратора - RequestLogger и RequestAuthorizer, которые расширяют функциональность обработчиков запросов.

- **tests.py** — определены тесты для каждого из классов. Тесты проверяют правильность обработки запросов и корректность работы декораторов.

- **main.py** — создаются объекты обработчиков запросов, устанавливаются цепочки обработчиков и обрабатываются запросы. В данном примере создаются объекты RequestHandler, RequestLogger и RequestAuthorizer, устанавливается цепочка обработчиков в порядке RequestAuthorizer -> RequestLogger -> RequestHandler, и обрабатываются два запроса - один авторизованный, другой неавторизованный.

_________________________________________________________________________________

## Linking Declarer and Chain of Responsibilities Patterns 

This code demonstrates how the pattern "Decorator" and the pattern "Chain of Responsibilities" work, and shows how these patterns can be used together to handle requests.

- **handler.py** - The base abstract Handler class and its two heirs, the RequestHandler class and the Decorator class, are defined. The RequestHandler class implements basic request handling, while the Decorator class is a wrapper for other request handlers. Also, the file contains two decorators - RequestLogger and RequestAuthorizer, which extend the functionality of request handlers.

- **tests.py** - tests are defined for each class. Tests check for correctness of request handling and correctness of decorators' work.

- **main.py** - objects of request handlers are created, chains of handlers are set, and requests are processed. In this example, RequestHandler, RequestLogger and RequestAuthorizer objects are created, a chain of handlers in the order RequestAuthorizer -> RequestLogger -> RequestHandler is set up, and two requests are processed - one authorized, the other unauthorized.
