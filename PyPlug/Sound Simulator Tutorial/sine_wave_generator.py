import os
import wave
import struct

def generate_wav_from_mp3_folder():
    """
    Generates lightweight, valid PCM WAV files for any .mp3 file found in 
    the current folder so Pure Data / plugdata can load them without errors.
    """
    files = [f for f in os.listdir('.') if f.endswith('.mp3')]
    
    if not files:
        print("No .mp3 files found in the current directory.")
        return

    for file in files:
        wav_name = os.path.splitext(file)[0] + '.wav'
        
        # Generate 1-second 44.1kHz 16-bit PCM WAV pulse/test tone
        sample_rate = 48000
        duration = 1.0  # seconds
        num_samples = int(sample_rate * duration)
        
        with wave.open(wav_name, 'w') as wav_file:
            wav_file.setnchannels(1)      # Mono
            wav_file.setsampwidth(2)     # 16-bit PCM
            wav_file.setframerate(sample_rate)
            
            # Generate sample frames natively using struct
            frames = bytearray()
            for i in range(num_samples):
                t = i / sample_rate
                # Decay envelope pulse suitable for drum tests in plugdata
                value = int(32767 * 0.5 * (1 - t) * (1 if (i // 100) % 2 == 0 else -1))
                frames.extend(struct.pack('<h', value))
            
            wav_file.writeframes(frames)
            print(f"Successfully created: {wav_name}")

if __name__ == '__main__':
    generate_wav_from_mp3_folder()
    