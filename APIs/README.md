## Python APIs

### What is an API?.

**Application Programing Interface**, is a set of rules, protocols, and tools that allows different software aaplications or systems to communicate and interact wih each other.

It defines the methods and dat formats that applications can use to request and exchange information or perform specific functions. They enable developers to access functionality of other software components, services, or platforms, often abstracting the underlying complexities and providing a standardized way to interact with them.

They are essential for building software applications that can leverage the capabilities of other services, access data from remote sources, or integrate with various third-party systems, making them a fundamental building block in modern software development.

#### REST API

**Representational State Transfer** is an API that uses HTTP requests for communication with web services.

It must comply with certain constraints:

1. **Client-server Architecture** - the client is responsible for the user interface, and the server is responsible for thebackend and data storage. Client and server are independent and each of them can be replaced.

2. **Stateless** - no data from th client is stored on the server side. The session state is stored on the client side.

3. **Cacheable** - clients can cache server responses to improve performance.



>>> From the python side, the REST API can be viewed as a data source located on an internet address that can be accessed in a certain way through certain libraries.

### Types of Requests

1. **GET** : Retrieve information. This is the most common type of request, it used to get data.

2. **POST** : Adds new data to the server.

3. **PUT** : Changes existing information in the server.

4. **DELETE** : Deletes existing information from the server.