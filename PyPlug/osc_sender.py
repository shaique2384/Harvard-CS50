import time
import math
from pythonosc import udp_client

# 1. Define the network target (127.0.0.1 means 'this local computer')
IP_ADDRESS = "127.0.0.1"
PORT = 8000

# 2. Initialize the OSC UDP Client
client = udp_client.SimpleUDPClient(IP_ADDRESS, PORT)

print(f"Streaming data to Plugdata on {IP_ADDRESS}:{PORT}... Press Ctrl+C to stop.")

angle = 0.0

try:
    while True:
        # Calculate a sine wave that smoothly goes up and down
        sine_value = math.sin(angle)
        
        # Scale the value from (-1.0 to 1.0) into a clean audio range (0.0 to 1.0)
        normalized_value = (sine_value + 1.0) / 2.0
        
        # Send the value to the specific OSC address tag '/volume'
        client.send_message("/volume", normalized_value)
        
        # Increment the angle to keep the wave moving
        angle += 0.05
        
        # Wait 20 milliseconds before sending the next value (~50 updates per second)
        time.sleep(0.02)

except KeyboardInterrupt:
    print("\nStream stopped safely.")
