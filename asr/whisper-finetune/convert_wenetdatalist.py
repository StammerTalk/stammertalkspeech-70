"""Convert wenet data.list to whisper format"""
import json
import sys
import soundfile as sf

datalist, whisper_data = sys.argv[1:]

with open(datalist) as f, open(whisper_data, 'w') as fo:
    for l in f:
        data = json.loads(l)
        wav = data['wav']
        txt = data['txt']
        with sf.SoundFile(wav) as fs:
            dur = fs.frames / fs.samplerate
        
        json_string = json.dumps({"audio": {"path": wav}, "sentence": txt, "duration": dur, "sentences": [{"start": 0, "end": dur, "text": txt}]}, ensure_ascii = False)
        fo.write(json_string+'\n')