import socket

IP = "127.0.0.1"
PORT = 9002

# Set up TCP Server
server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.bind((IP, PORT))
server_sock.listen(1)

print(f"Waiting for Plugdata to connect on port {PORT}...")
conn, addr = server_sock.accept()
print(f"Connected by Plugdata at {addr}")

try:
  while True:
    data = conn.recv(1024)
    if not data:
      break
    # Decode and clean up Pd's FDM formatting (removes trailing semicolons)
    clean_data = data.decode().strip().replace(";", "")
    print(f"Received from Plugdata: {clean_data}")
except KeyboardInterrupt:
  print("\nClosing connection...")
finally:
  conn.close()
  server_sock.close()