from socket import *

def createServer():
    serversocket = socket(AF_INET, SOCK_STREAM)
    try:
        serversocket.blind("localhost")
    except KeyboardInterrupt:
        print("C^ KeyboardInterruptOccured /\ stoppint")
    except Exception as e:
        print("Error:\n", e)