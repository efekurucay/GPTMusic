from mido import MidiFile, MidiTrack, Message

# Yeni bir MIDI dosyası oluştur
midi = MidiFile()
track = MidiTrack()
midi.tracks.append(track)

# Tempo ve kanal bilgisi
tempo = 120
track.append(Message('program_change', program=5, time=0))  # Program 5: Electric Piano 1

# Arpeggio için notalar
arpeggio = {
    "Am": [57, 60, 64],
    "F": [53, 57, 60],
    "C": [48, 52, 55],
    "G": [43, 47, 50]
}

progression = ["Am", "F", "C", "G"]
note_duration = 120  # Her nota için 120 ticks
velocity = 80  # Elektrik piyano için ses seviyesi

# Arpeggio notalarını sırayla çal
for chord in progression:
    for _ in range(2):  # 2 kez tekrar et
        for note in arpeggio[chord]:
            track.append(Message('note_on', note=note, velocity=velocity, time=0))
            track.append(Message('note_off', note=note, velocity=velocity, time=note_duration))

# Dosyayı kaydet
file_path = "Track7_Arpeggio.mid"
midi.save(file_path)
file_path
