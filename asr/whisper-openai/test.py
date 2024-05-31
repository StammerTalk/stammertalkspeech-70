#!/fs/scratch/users/rong_gong/2021/envs/venvs/wenet/bin/python
import os
from openai import OpenAI

os.environ["OPENAI_API_KEY"] = ''

client = OpenAI()

ps = []
with open('/fs/scratch/users/rong_gong/2021/wenet/examples/wenetspeech_stutter_verbatim/s0/data/test/wav.scp') as f:
    lines = f.readlines()
    for line in lines:
        _, p = line.strip().split()
        ps.append(p)
ps = ps[2088:]

out = open('transcriptions.txt', 'w')
for i, p in enumerate(ps):
    audio_file=open(p, "rb")
    print(audio_file)
    transcription = client.audio.transcriptions.create(
      model="whisper-1",
      file=audio_file,
      language="zh"
    )
    out.write(f'utt: {p}\n')
    out.write(f'trans: {transcription.text}\n')
    out.write('\n')

    if i % 100 == 0:
        print(f'Processed {i}/{len(ps)}')
out.close()
