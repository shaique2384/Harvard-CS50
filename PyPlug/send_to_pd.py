import socket
import time

# Create a TCP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Connecting to Plugdata...")
s.connect(("127.0.0.1", 9001))
print("Connected!")

count = 0
for i in range(31):
  # Standard Pure Data FDM formatting: space before semicolon, newline at end
  msg = f"{count} ;\n"
  s.sendall(msg.encode())
  print(f"Sent to Plugdata: {count}")
  count += 1
  time.sleep(1)

s.close()