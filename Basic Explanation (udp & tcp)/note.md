A socket is a communication endpoint
(It doesn't need to be an internet commincation, we can have sockets inside an os)

MAKING SOCKETS:

- What category of socket? Internet? Bluetooth?
Socket.AF_INET ==> an internet sockets
Socket.AF__BLUETOOTH ==> an bluetooth socket (sockets can be anything)

AF_INET are the sockets that we will work on, this uses IPv4 ip addresses
and AF_INET6 uses IPv6 IP Addresses

- Types of socket:
SOCK_STREAM: this is about tcp (Transmission Control Protocol), this is for connection based socket*
SOCK_DGRAM: this is about udp (User Datagram Protocol), this is used when we just want to send messages but not caring about terminating the connection after the exchanging is done

* Means that if we want to exchange messages between two connected endpoints, then when the exchanging finishes, the connection closes

- TCP: is more reliable, since its connection based because pacet loss is detected and responses are returned, it's also sequential meaning that it keeps the oder the messages arre sent and in the same order the other endpoint will receive the messages, it's also byte-stream, it keeps up a connection and terminates when we're done exchanging messages

- UDP: is not eliable, sends one datagram and it's not sequential so each message is not connected with each other, there is not guarantee, no order on messages, no response when there is packet loss
BUT: it's faster and has less network and pc stress, it's more "real-time"

TCP should be used when we dont want to allow packet loss! 
UDP is used for real-time video connection, audio connection, streaming, gaming- where not every single bit is impotant and we want high speed while also allowing packet loss


EXAMPLE ===> Skype Application:
For calls and videocalls UDP is used, BUT for the call requests and ringing TCP is used!