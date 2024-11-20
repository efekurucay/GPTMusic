from mido import MidiFile, MidiTrack, Message

# Yeni bir MIDI dosyası oluştur
midi = MidiFile()
track = MidiTrack()
midi.tracks.append(track)

# Tempo ve kanal bilgisi (isteğe bağlı)
tempo = 120
track.append(Message('program_change', program=0, time=0))

# Kick ve Snare için notalar ve ritim
kick = 36  # MIDI standardında Kick Drum
snare = 38  # MIDI standardında Snare Drum
time_division = 480  # 1 ölçü için ticks

# Ritim döngüsü: Kick ve Snare
pattern = [
    (kick, 0),  # Kick: 1. vuruş
    (snare, time_division // 2),  # Snare: 2. vuruş
    (kick, time_division),  # Kick: 3. vuruş
    (snare, time_division + (time_division // 2))  # Snare: 4. vuruş
]

# 4 ölçü boyunca döngü
for i in range(4):  # 4 ölçü
    for note, t in pattern:
        track.append(Message('note_on', note=note, velocity=64, time=t))
        track.append(Message('note_off', note=note, velocity=64, time=120))  # 120 ticks uzunluk

# Dosyayı kaydet
file_path = "Track1_Rhythm_Drum.mid"
midi.save(file_path)
file_path
