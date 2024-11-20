from mido import MidiFile, MidiTrack, Message

# Yeni bir MIDI dosyası oluştur
midi = MidiFile()
track = MidiTrack()
midi.tracks.append(track)

# Tempo ve kanal bilgisi (isteğe bağlı)
tempo = 120
track.append(Message('program_change', program=33, time=0))  # Program 33: Electric Bass (MIDI Standart)

# Akorların kök notaları (Bassline)
bass_notes = [45, 41, 48, 43]  # Am, F, C, G kök notaları
time_division = 480  # 1 ölçü için ticks
velocity = 80  # Bas ses seviyesi

# 4 ölçü boyunca döngü
for note in bass_notes:  # Am → F → C → G
    track.append(Message('note_on', note=note, velocity=velocity, time=0))
    track.append(Message('note_off', note=note, velocity=velocity, time=time_division))

# Dosyayı kaydet
file_path = "Track2_Bassline.mid"
midi.save(file_path)
file_path
