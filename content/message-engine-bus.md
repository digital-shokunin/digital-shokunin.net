Title: Message engines & Service Integration Buses
Date: 2013-05-30 21:00
Tags: ibm, websphere
Category: SysAdmin/DevOps
Slug: message-engine-bus
Author: David Mitchell
Summary: Understanding the use of message engines and service integration bus in WebSphere

One of the components that I deal with in my work with WebSphere that seems nebulous to some conceptually, is the service integration bus and it's corresponding message engine. Especially when you're first beginning to learn about WebSphere and JMS. This concept is not unique to WebSphere and similar implementations can be found in JBoss, but my experience with it rests mostly with WebSphere.

A service integration bus lets applications exchange messages between each other within a cell. Think of it like a transport provider for messages within WebSphere that allows for asynchronous communication between applications. One application can place a message on a bus, and all other applications connected to the bus can retrieve the message and perform some work on them, or there is some mediation done before hand. You can have one application handle a web request and put a message on a bus where a cluster of applications that can handle the request will see it and one of them will grab the message and handle the work needed for the request. This is very useful for spreading the workload among a cluster of application servers while ensuring high availability.

The bus has what are called destinations, which are effectively queues or topics similar in concept to what you would find with WebSphere MQ. Destinations are simply where the messages are put and retrieved. There is usually a message producer and consumer. One being the application that creates and places the message on the destination, and the consumer the application that receives the message.

The component that performs all the work is the message engine, it can be an application server or cluster of servers that are members of the bus. They also host the destinations on the bus. There are [ways of configuring the message engine across the members so that there is redundancy and fail-over](http://www.ibm.com/developerworks/websphere/library/techarticles/0704_chilanti/0704_chilanti.html#N100E3). Each of which has advantages and disadvantages which should be weighed for what best suits your environment.

The message engine itself needs somewhere to store the messages, simply keeping them in memory can mean losing messages. The two main options available are either a file store, meaning they are just written directly to disk, or a JDBC data source meaning the messages are placed and stored in database, like DB2 or Oracle. 

Usually the messages are stored on the bus indefinitely until they are retrieved by a consumer. In fact, one problem I've encountered is old messages that no longer have an active transaction associated with them remaining on the destination until they are cleared, this can cause problems with when the message engine is restarted since it processes all the messages on the queue before getting to ones that are associated with a transaction. If there are a lot of messages, this can take a very long time. You need to usually set an expiration for the message either in the [JMS properties in the application code](http://pic.dhe.ibm.com/infocenter/wasinfo/v7r0/index.jsp?topic=%2Fcom.ibm.websphere.nd.doc%2Finfo%2Fae%2Fae%2Frwsf_prjms_timetolive.html) that produces the message or setting a property value on the [destination queue itself](http://pic.dhe.ibm.com/infocenter/wasinfo/v7r0/index.jsp?topic=%2Fcom.ibm.websphere.nd.multiplatform.doc%2Finfo%2Fae%2Fae%2FSIBJMSQueue_DetailForm.html). 

It should also be noted that those with a WebSphere MQ infrastructure in place may [choose to use MQ instead of an SIBus](http://www.ibm.com/developerworks/websphere/library/techarticles/1109_wallis/1109_wallis.html) to exchange messages between applications. One can even [exchange messages between MQ and the SI Bus](http://pic.dhe.ibm.com/infocenter/wasinfo/v7r0/index.jsp?topic=%2Fcom.ibm.websphere.soafep.multiplatform.doc%2Finfo%2Fae%2Fae%2Fcjc0051_.html)

While the concepts may seem daunting and configuring an SI Bus can be complex, its simple to just remember that its ultimate purpose is just to allow one or more applications to exchange messages using the JMS API.
