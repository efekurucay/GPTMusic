from mido import MidiFile, MidiTrack, Message

# Yeni bir MIDI dosyası oluştur
midi = MidiFile()
track = MidiTrack()
midi.tracks.append(track)

# Tempo ve kanal bilgisi (isteğe bağlı)
tempo = 120
track.append(Message('program_change', program=0, time=0))  # Program 0: Acoustic Grand Piano

# Akorlar (Harmoni Katmanı)
chords = {
    "Am": [57, 60, 64],  # A, C, E
    "F": [53, 57, 60],   # F, A, C
    "C": [48, 52, 55],   # C, E, G
    "G": [43, 47, 50]    # G, B, D
}

# Akor sırası: Am → F → C → G
progression = ["Am", "F", "C", "G"]
time_division = 480  # 1 ölçü için ticks
velocity = 70  # Piyano ses seviyesi

# Akorları çal
for chord in progression:
    for note in chords[chord]:
        track.append(Message('note_on', note=note, velocity=velocity, time=0))
    track.append(Message('note_off', note=chords[chord][0], velocity=velocity, time=time_division))

# Dosyayı kaydet
file_path = "Track3_Harmony_Chords.mid"
midi.save(file_path)
file_path
