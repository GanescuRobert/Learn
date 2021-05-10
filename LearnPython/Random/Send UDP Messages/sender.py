# SENDER

import socket

ip = "127.0.0.1"
port = 5000
msg = bytearray(input(), 'utf-8')

print(f"Sending {msg} to {ip}:{port}")

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.sendto(msg, (ip, port))
