# RESTful APIs & Microservices
***

## APIs vs Microservices: How  do they work together?
- Microservices function as the “building‐blocks” of the application by performing various services, while “RESTful APIs” function as the “glue” that integrates the microservices into an application.
***

## Why were microservices created?
- Suppose that you have an application with tightly coupled components comprising of databases, servers, the user interface, business logic, and so on.
- This type of architecture can be considered a monolithic application, but if a single component fails, other components fail, and possibly the entire application fails. In a microservices approach, application components are loosely coupled, thus if a single component fails, the other components continue to work. 
***

## HTTP vs. REST APIs
APIs can be categorised into various types based on application designs and other constraints, such as Web API, HTTP API, REST API, and many more.
  - REST API is a Software Architectural Style that is used to guide the creation and design of the architecture of the World Wide Web. In other words, REST APIs establish a set of guidelines for how a distributed system’s architecture should function. REST APIs add no new capability to HTTP APIs. REST APIs are ideal for creating scalable general-purpose applications. 
  - On the other hand, HTTP API is an application that communicates between two systems using the Hypertext Transfer Protocol. HTTP APIs make endpoints available as API gateways, allowing HTTP queries to connect to a server. The majority of HTTP APIs are on the verge of becoming completely RESTful.
***

## REST vs. Sockets
- REST is a simple way for computers to share information, but it can only be used for one-way communication.
- Sockets allow computers to have a two-way conversation. This can be useful for things like video games or chat apps, where the computers need to be able to send messages back and forth in real-time.
***

## When an API can be called REST API?
The requirements are:
   - Client-Server: A server oversees the application’s data and state in REST applications. The server connects with a client, which is responsible for handling user interactions. The two components are separated by a clear separation of responsibilities. As a result, you’ll be able to update and upgrade them in separate tracks.
   - Stateless: Client state is not maintained by servers; instead, clients handle their own application state. All of the information needed to process the client’s requests are contained in the requests to the server.
   - Cacheable: Servers must indicate whether or not their responses are cacheable. To boost performance, systems and clients might cache replies when it is convenient. They also get rid of non-cacheable data, so no client has to deal with stale data.
   - Uniform Interface: REST’s most well-known characteristics are that the emphasis on a uniform interface between components is the primary aspect that distinguishes the REST architectural style from other network-based approaches. Data is provided as resources through REST services, which have a consistent namespace.
   - Layered System: The system’s components can’t look beyond their own layer. This limited scope makes it simple to add load-balancers and proxies to increase authentication security and performance
***

## References
- [Introduction to Microservices, Docker, and Kubernetes](https://www.youtube.com/watch?v=1xo-0gCVhTU)
- [Unleashing the power of WebSockets for real-time Model Inference](https://pub.towardsai.net/unleashing-the-power-of-websockets-for-real-time-model-inference-e100d597c7a2)
***
