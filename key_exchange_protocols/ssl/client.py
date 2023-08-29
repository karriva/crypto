import socket
import ssl

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("localhost", 12345))

context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
context.load_verify_locations(cafile="ca.crt")

secure_connection = context.wrap_socket(client_socket, server_hostname="localhost")

secure_connection.send("Hello from client!".encode())

data = secure_connection.recv(1024)
print("Received:", data.decode())

secure_connection.close()
