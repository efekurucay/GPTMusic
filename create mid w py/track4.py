from mido import MidiFile, MidiTrack, Message

# Yeni bir MIDI dosyası oluştur
midi = MidiFile()
track = MidiTrack()
midi.tracks.append(track)

# Tempo ve kanal bilgisi (isteğe bağlı)
tempo = 120
track.append(Message('program_change', program=81, time=0))  # Program 81: Lead Synth

# Melodi notaları (Am dizisinden seçilen notalar)
melody_notes = [60, 62, 64, 67, 64, 62, 60, 62]  # Basit bir melodi
note_duration = 240  # Yarım ölçü için ticks
velocity = 90  # Melodi ses seviyesi

# Melodi notalarını çal
for note in melody_notes:
    track.append(Message('note_on', note=note, velocity=velocity, time=0))
    track.append(Message('note_off', note=note, velocity=velocity, time=note_duration))

# Dosyayı kaydet
file_path = "Track4_Melody_Lead.mid"
midi.save(file_path)
file_path
