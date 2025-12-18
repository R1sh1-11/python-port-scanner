#Single Port Scanner
import socket

target = #Enter target
port = #Enter port

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

response_code = client.connect_ex((target, port))

if response_code == 0:
    print(f"Port {port} is OPEN!")
else:
    print(f"Port {port} is CLOSED.")

client.close()