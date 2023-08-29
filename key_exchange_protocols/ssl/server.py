import socket
import ssl

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("localhost", 12345))
server_socket.listen(1)

print("Server is listening...")

connection, client_address = server_socket.accept()
print("Connection established with:", client_address)

context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile="server.crt", keyfile="server.key")

secure_connection = context.wrap_socket(connection, server_side=True)

data = secure_connection.recv(1024)
print("Received:", data.decode())

secure_connection.send("Hello from server!".encode())

secure_connection.close()
server_socket.close()
