import socket
import threading

def handle_client(client_socket, service):
    request = client_socket.recv(1024)
    print(f"[{service}] Received: {request.decode('utf-8')}")
    
    if service == "HTTP":
        response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n<h1>Welcome to my server</h1>"
    else:
        response = f"Welcome to the {service} service."
    
    client_socket.send(response.encode('utf-8'))
    client_socket.close()

def start_server(port, service):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", port))
    server.listen(5)
    print(f"[*] Listening on port {port} for {service} service")

    while True:
        client_socket, addr = server.accept()
        print(f"[*] Accepted connection from {addr[0]}:{addr[1]}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket, service))
        client_handler.start()

if __name__ == "__main__":
    services = {
        "HTTP": 8080,
        "FTP": 21,
        "TELNET": 23
    }

    for service, port in services.items():
        server_thread = threading.Thread(target=start_server, args=(port, service))
        server_thread.start()
