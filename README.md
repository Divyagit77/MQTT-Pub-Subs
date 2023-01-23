HiveMQ MQTT Python Client
================================

This document describes the source code for the `HiveMQ <broker.hivemq.com>`_ MQTT Python client library.

This code provides a client class which enable applications to connect to an `MQTT broker to publish messages, and to subscribe to topics and receive published messages. 

It supports Python 2.7.9+ or 3.6+.

The MQTT protocol is a machine-to-machine (M2M)/"Internet of Things" connectivity protocol. Designed as an extremely lightweight publish/subscribe messaging transport, it is useful for connections with remote locations where a small code footprint is required and/or network bandwidth is at a premium.

Paho is an `Eclipse Foundation <https://www.eclipse.org/org/foundation/>`_ project.
HiveMQ is a MQTT broker - a messaging platform for fast, efficient and reliable data movement to and from connected IoT devices and enterprise systems.

Contents
--------

* `HiveMQ Account set up - Broker`_
* `Visual Studio Code Installation`_
* `Virtual Environment Set up and paho package installation`_
* `Python Code - Subscribe & Publish Messages (Clients)`_
* `WebSocket and Webclient Execution`_


HiveMQ Account Set up - Broker
------------
Visit: https://www.hivemq.com/
Go to 'Get HiveMQ'
Click on Sign up 'HiveMQ Cloud'
Shift to sign up page from log in page 'set email id & password'
Confirmation mail will be sent your mail id - 'Confirm my account'
Complete your profile by providing name, job profile, company
Set up credential for your IoT devices - set username and password
Tools: Choose MQTT Webclient
Under connection settings: Provide your IoT device credentials set before and click on connect
Cluster set up:
Using cluster option, you can create new cluster if needed. (Note that for free account maximum of 2 clusters only be created)
When setting up cluster, you can choose the cloud provider (Example: Microsoft Azure or AWS)


Visual Studio Code Installation
------------
Visual Studio Code is a streamlined code editor with support for development operations like debugging, task running, and version control. We will be developing our code using this software.
Download and install the software
Link to download software: https://code.visualstudio.com/

Virtual Environment Setup and paho package installation
------------
A Python virtual environment is a tool used to create isolated Python environments on a single machine, which can each have their own installed packages and Python version. This allows for easy management of dependencies and isolation of different projects, so that they do not interfere with each other. It also makes it easy to switch between different versions of packages and Python versions, as well as to share a specific set of packages with others. This is particularly useful when working on projects with different requirements or when sharing code with others.

Steps:
Open Vistual Studio code application from your system
Create a folder in your system
1. In VS code--> Go to Files-->Open Folder-->'Open the folder you created'
2. Go to Terminal-->New Terminal-->Type: python -m venv 'Name_for_your_virtualenvironment'
As a confirmation of successful virtual environment creation, you will see set of new folders under the explorer tab
3. Now to active the envrionment, in terminal type: 'Name_for_your_virtualenvironment'/Scripts/Activate.bat
4. To select interpreter go to View-->Command Palatt-->type python: Select Interpreter-->Enter interpreter path-->Find-->'Open the folder you created'-->Python.exe
Create a new terminal and confirm that your environment is changed to the new virtual environment you created

Note: Run this in command terminal, powershell terminal requires special permission which may not excute the command.

Paho Installation
-------------
Paho-MQTT is an open-source client library for the MQTT (MQ Telemetry Transport) protocol, written in Python. It allows developers to connect and publish/subscribe to MQTT brokers, making it a useful tool for building Internet of Things (IoT) applications. The library is part of the Eclipse Paho project, which provides several other MQTT client implementations in different programming languages.
To install paho-mqtt library to the virtual environment created, type below in the terminal
::

    pip install paho-mqtt

On successful installation, you will see a message stating installed.

Python Coding: Subscribe and Publish Messages
--------------

Here is a code to subscribe and publish messages to mqtt client
.. code:: python

    import time
    import paho.mqtt.client as paho
    from paho import mqtt

    # setting callbacks for different events to see if it works, print the message etc.
    def on_connect(client, userdata, flags, rc, properties=None):
      print("CONNACK received with code %s." % rc)

    # with this callback you can see if your publish was successful
    def on_publish(client, userdata, mid, properties=None):
      print("mid: " + str(mid))

    # print which topic was subscribed to
    def on_subscribe(client, userdata, mid, granted_qos, properties=None):
      print("Subscribed: " + str(mid) + " " + str(granted_qos))

    # print message, useful for checking if it was successful
    def on_message(client, userdata, msg):
      print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

    # using MQTT version 3.1.1: MQTTv311, for 3.1: MQTTv31, for 5: MQTTV5
    # userdata is user defined data of any type, updated by user_data_set()
    # client_id is the given name of the client
    client = paho.Client(client_id="clientname", userdata=None, protocol=paho.MQTTv311, transport='websockets')
    client.on_connect = on_connect

    # enable TLS for secure connection
    #client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
    # set username and password
    #client.username_pw_set("usernane", "password")


    # connect to HiveMQ Cloud on port 8883 (default for MQTT)
    # client.connect("a9da7498ddbd475eb817b02fb90e73e9.s1.eu.hivemq.cloud", 8883)
    # Connect to HiveMQ Websocket portal on port 8000
    client.connect("broker.mqttdashboard.com", 8000)


    # setting callbacks, use separate functions like above for better visibility
    client.on_subscribe = on_subscribe
    client.on_message = on_message
    client.on_publish = on_publish

    # subscribe to all topics of encyclopedia by using the wildcard "#"
    client.subscribe("testtopic/1356585", qos=1)

    # a single publish, this can also be done in loops, etc.
    client.publish("testtopic/68144686", payload="Hello world!", qos=1)


    # loop_forever for simplicity, here you need to stop the loop manually
    # you can also use loop_start and loop_stop
    client.loop_forever()

Web Client Execution
--------------
For Web clieht execution, use client.connect function as below.
.. code:: 
     # connect to HiveMQ Cloud on port 8883 (default for MQTT)
       client.connect("a9da7498ddbd475eb817b02fb90e73e9.s1.eu.hivemq.cloud", 8883)
Steps
1. Login in to HiveMQ Cloud
2. Go to Web client under manage cluster option
3. Provide the user name and password, then click on connnect
4. Subscribe the topic 'testtopic/68144686' - to receive messages from paho client (i.e. python code)
5. Publish the topic 'testtopic/1356585' - to send messages to paho client (i.e.python code)
6. On successful execution, messages will be sent and received from paho client to the broker.

Web Socket Execution
--------------
For Web socket execution, use client.connect function as below.
.. code:: 
    # Connect to HiveMQ Websocket portal on port 8000
      client.connect("broker.mqttdashboard.com", 8000)
Steps
1. Go to http://www.hivemq.com/demos/websocket-client/
2. Go to Web client under manage cluster option
3. Provide the user name and password, then click on connnect
4. Subscribe the topic 'testtopic/68144686' - to receive messages from paho client (i.e. python code)
5. Publish the topic 'testtopic/1356585' - to send messages to paho client (i.e.python code)
6. On successful execution, messages will be sent and received from paho client to the broker.
