from mido import MidiFile, MidiTrack, Message

# Yeni bir MIDI dosyası oluştur
midi = MidiFile()
track = MidiTrack()
midi.tracks.append(track)

# Tempo ve kanal bilgisi
tempo = 120
track.append(Message('program_change', program=81, time=0))  # Program 81: Lead Synth

# Lead synth notaları
lead_notes = [72, 74, 76, 79, 76, 74, 72, 74]  # Oktav yüksek parlak melodi
note_duration = 240  # Yarım ölçü
velocity = 100  # Parlak synth için yüksek ses seviyesi

# Lead notalarını çal
for note in lead_notes:
    track.append(Message('note_on', note=note, velocity=velocity, time=0))
    track.append(Message('note_off', note=note, velocity=velocity, time=note_duration))

# Dosyayı kaydet
file_path = "Track5_Lead_Synth.mid"
midi.save(file_path)
file_path
