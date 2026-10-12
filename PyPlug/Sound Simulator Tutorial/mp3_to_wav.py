import os
import subprocess


def batch_convert_mp3_to_wav():
    """Scans the current directory for .mp3 files and converts them to .wav using ffmpeg."""
    mp3_files = [f for f in os.listdir(".") if f.endswith(".mp3")]

    if not mp3_files:
        print("No .mp3 files found in the current directory.")
        return

    print(f"Found {len(mp3_files)} MP3 file(s). Starting conversion...")

    for file in mp3_files:
        output_wav = file.replace(".mp3", ".wav")
        print(f"Converting: {file} -> {output_wav}")

        # Run ffmpeg command
        subprocess.run(["ffmpeg", "-i", file, output_wav])

    print("Batch conversion completed!")


if __name__ == "__main__":
    batch_convert_mp3_to_wav()

