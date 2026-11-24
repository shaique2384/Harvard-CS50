|Active Project Folder|Existing Skill / Template You Already Built|How It Connects & Ships Fast|
|:---|:---|:---|
|Voice-Leading & Chord Suggestion Engine (2_code / 4_output/score)|music21 .py templates (Code Meowstro) + LLM-from-scratch .ipynb (freeCodeCamp)   |Use music21 pitch/chord/interval/stream objects for the Tonal Chapter procedural rule-scorer (2- to 4-part, 2- to 4-chord spans). Use your transformer/sequence-modeling intuition from the LLM-from-scratch notebook to train a lightweight next-chord preference reranker over legal tonal progressions.|
|Caeneus / Tube-DI-IR Deformation & Ferneyhough Rhythms (3_plugdata_pd / 2_code)|Sound Simulator .pd patches + Python CS50 / NumPy + BUET Rhino/GH   |Route audio/signal descriptors from your .pd patches via OSC/TCP into Python to compute local deformation matrices, driving Rhino/Grasshopper geometry and Gem/Unreal visuals, documented in Paper Caeneus.|
|Schenkerian Analysis Archive (1_sketches / 4_output/images)|Hand-drawn architectural drafting (BUET) + LACM harmonic analysis|Hand-render the tonal 2-to-4-part graphs first, scan cleanly, and pair them with your music21 voice-leading outputs.|
|Demucs + FFT Automatic Tab (2_code / 4_output/score)|Python CS50 / music21 .py templates|Run Demucs stem separation $\rightarrow$ FFT pitch tracking $\rightarrow$ music21 fretboard/tab .musicxml export.|

$$\text{ }$$
$$\text{ }$$
$$\text{ }$$

|phd_portfolio_2027||
|:---|:---|
|├── 1_sketches|                     |# Hand-drawn conceptual & architectural/system sketches of all projects|
|├── 2_code||
|│   ├── schenkerian.py               |# Middleground reductions & voice-leading syntax from Holdsworth ("Proto Cosmos")|
|│   ├── layered_approach.py          |# Multi-stratum decomposition ("crystals" of structure vs. improv freedom)|
|│   ├── tonal_voice_leading.py       |# 2/3/4-part, 2/4-chord span procedural rule engine + ranking|
|│   ├── fft_decoder.py               |# Real-time/chunked FFT pitch & chord/voicing decoder for duo input|
|│   ├── duo_orchestrator.py          |# Manages 4/4 x 4-bar loop, 4 voices, 16-bar role switch, & PD/MIDI/OSC I/O|
|│   ├── chords_gen.ipynb             |# Transformer: FFT melody/harmonic context + regulations -> 4-voice next chord|
|│   └── melody_gen.ipynb             |# Transformer: FFT decoded voicings + regulations + theme -> melody line|
|├── 3_plugdata_pd||
|│   ├── caeneus_tube_ir_gem.pd       |# Tube/DI/IR signal descriptors -> matrix deformation -> Gem 3D visuals|
|│   └── ferneyhough_gem.pd           |# Real-time rhythmic/architectural visual & audio system in Gem|
|├── 4_output||
|│   ├── score                       |# .mid & .musicxml (Holdsworth reductions, generated melodies, tabs)|
|│   ├── executables/                 |# Standalone scripts/patches|
|│   ├── charts                      |# Regulation distributions, reduction graphs, transformer loss/eval plots|
|│   └── images                      |# Scanned hand sketches, Gem captures, Manim diagrams|
|└── 5_paper_caeneus                 |# Paper Caeneus + ~10-page thesis excerpt ("Fusion's Dance") for writing samples|

