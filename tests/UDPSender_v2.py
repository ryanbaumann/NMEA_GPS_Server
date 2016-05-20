from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor
from twisted.internet.task import LoopingCall
import struct
import sys, time
import socket
import time

class Packet(object):
    def __init__(self, data=None):
        self.packet_type = 1
        self.payload = ''
        self.structure = '!H6s'
        if data == None:
            return

        self.packet_type, self.payload = struct.unpack(self.structure, data)

    def pack(self):
        return struct.pack(self.structure, self.packet_type, self.payload)

    def __str__(self):
        return "Type: {0}\nPayload {1}\n\n".format(self.packet_type, self.payload)

class MyProtocol(DatagramProtocol):
    def datagramReceived(self, data, (host, port)):
        p = Packet(data)
        print p


class MySender(DatagramProtocol):
    def __init__(self, packet, host='127.0.0.1', port=10112):
        self.packet = packet.pack()
        self.host = host
        self.port = port

    def startProtocol(self):
        self.transport.write(self.packet, (self.host, self.port))

if __name__ == "__main__":
    MCAST_GRP = '127.0.0.1'
    MCAST_PORT = 10110
    while True:
        p = Packet()
        p.packet_type = 1
        p.payload = '$GPGGA,184353.07,1929.045,S,02410.506,E,1,04,2.6,100.00,M,-33.9,M,,0000*6D'
        print p.payload
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)
        print "sending packet to " + MCAST_GRP + ", " + str(MCAST_PORT)
        sock.sendto(p.payload, (MCAST_GRP, MCAST_PORT))
        time.sleep(1)
        print 'packet sent'
