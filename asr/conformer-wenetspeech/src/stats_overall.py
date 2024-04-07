"""
Calculate overall WER from individual utterance metrics
"""

import sys, os
import json
import re
from collections import defaultdict

def calc_wer(wer):
    ref_all, cor_all, sub_all, del_all, ins_all = 0, 0, 0, 0, 0
    
    for ref, cor, sub, dele, ins in wer:
        ref_all += ref
        cor_all += cor
        sub_all += sub
        del_all += dele
        ins_all += ins
    err_all = sub_all + del_all + ins_all
    return f'WER={(err_all / ref_all) * 100:5.2f}% N={int(ref_all):6d} C={int(cor_all):6d} D={int(del_all):4d} S={int(sub_all):4d} I={int(ins_all):4d}\n'


if __name__ == '__main__':	
    exp_dir, stats_file = sys.argv[1:]

    wer = list()

    WER=r'WER: .+ N=(.+) C=(.+) S=(.+) D=(.+) I=(.+)'

    with open(os.path.join(exp_dir, 'wer')) as f:
        for l in f:
            l = l.strip()
            if not l: continue
            if l.startswith('WER:'):
                m = re.match(WER, l)
                assert m is not None
                wer.append((float(m.group(1)), float(m.group(2)), float(m.group(3)), float(m.group(4)), float(m.group(5))))

    with open(stats_file, 'w') as f:
        f.write(calc_wer(wer))