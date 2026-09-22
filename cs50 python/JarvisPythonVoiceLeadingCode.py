import sys
import json
from music21 import stream, note, chord, voiceLeading

def analyze_voice_leading(data):
    try:
        # data format expected: {"epoch": "tonal", "chords": [[60, 64, 67], [61, 65, 68]]}
        epoch = data.get("epoch", "tonal")
        chord_data = data.get("chords", [])
        
        # 1. Reconstruct into music21 Chords
        m21_chords = [chord.Chord(midi_notes) for midi_notes in chord_data]
        
        results = {
            "status": "success",
            "parallel_fifths": False,
            "parallel_octaves": False,
            "errors": []
        }
        
        # 2. Sequential voice leading analysis (Example: Tonal rule-checking)
        if len(m21_chords) >= 2:
            for i in range(len(m21_chords) - 1):
                ch1 = m21_chords[i]
                ch2 = m21_chords[i+1]
                
                # Pairwise checker for every voice combo
                vlq_pairs = voiceLeading.VoiceLeadingQuartet.createMultipleFromChords(ch1, ch2)
                for vlq in vlq_pairs:
                    if epoch == "tonal":
                        if vlq.parallelFifth():
                            results["parallel_fifths"] = True
                            results["errors"].append(f"Parallel 5th between {vlq.v1n1} and {vlq.v2n1}")
                        if vlq.parallelOctave():
                            results["parallel_octaves"] = True
                            results["errors"].append(f"Parallel 8ve detected.")
                            
        return results
    except Exception as e:
        return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    # Continuous listening loop for Node messages
    for line in sys.stdin:
        if not line.strip():
            continue
        payload = json.loads(line)
        analysis = analyze_voice_leading(payload)
        print(json.dumps(analysis))
        sys.stdout.flush() # Forces output to go straight to Node