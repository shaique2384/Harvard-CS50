import time
from pythonosc import dispatcher, osc_server, udp_client

# Address configuration
LISTEN_IP = "127.0.0.1"
LISTEN_PORT = 5001  # Port Python receives from Pd

SEND_IP = "127.0.0.1"
SEND_PORT = 5000    # Port Python sends to Pd

# Handler for incoming messages from Pure Data
def message_handler(address, *args):
    print(f"Received from Pd [{address}]: {args}")

# Setup server (Receiver)
disp = dispatcher.Dispatcher()
disp.map("/from_pd", message_handler)  # Listens for messages sent to /from_pd

server = osc_server.ThreadingOSCUDPServer((LISTEN_IP, LISTEN_PORT), disp)

# Run server in background thread so main loop can send data
import threading
server_thread = threading.Thread(target=server.serve_forever)
server_thread.daemon = True
server_thread.start()

# Setup client (Sender)
client = udp_client.SimpleUDPClient(SEND_IP, SEND_PORT)

print("Python OSC Server running...")

# Main loop: send data to Pd every second
try:
    counter = 0
    for _ in range(100):
        # Sends a float/int message to address /to_pd
        client.send_message("/to_pd", counter)
        print(f"Sent to Pd [/to_pd]: {counter}")
        counter += 1
        time.sleep(1)
except KeyboardInterrupt:
    print("\nStopping script...")