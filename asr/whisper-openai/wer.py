import re
import string
from hanziconv import HanziConv

ref = '/fs/scratch/users/rong_gong/2021/wenet/examples/wenetspeech_stutter_verbatim/s0/data/test/text'
hyp = 'transcriptions.txt'
hyp_out = 'transcriptions_cleaned.txt'

def remove_punc(txt):
  punc = "！？｡。＂＃＄％＆＇（）＊＋，－／：；＜＝＞＠［＼］＾＿｀｛｜｝～｟｠｢｣､、〃《》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟〰〾〿–—‘’‛“”„‟…‧﹏.·"
  return re.sub(r"[%s]+" %punc, "",txt)

uttids = []
with open(ref) as f:
    ref_lines = f.readlines()
    for l in ref_lines:
        uttid = l.split()[0]
        if uttid:
            uttids.append(uttid)

hyp_dict = dict()    
with open(hyp) as f:
    hyp_lines = f.readlines()
    for l in hyp_lines:
        if l.startswith('utt:'):
            uttid = l.split()[1][:-4]
            hyp_dict[uttid] = ''
        if l.startswith('trans'):
            hyp_dict[uttid] = remove_punc(l[7:]).replace(' ', '')
            hyp_dict[uttid] = HanziConv.toSimplified(hyp_dict[uttid].translate(str.maketrans('', '', string.punctuation)))

with open(hyp_out, 'w') as f:
    for uttid in uttids:
        f.write(f'{uttid} {hyp_dict[uttid]}')