# Internal filename: .\obfuscator.py
# Bytecode version: 3.8.0rc1+ (3413)
# Source timestamp: 2023-09-30 09:58:34 UTC (1696067914)

import hashlib
import sys
SEED_PATH = 'seed.txt'
with open(SEED_PATH, 'r') as f:
    line = f.readline()
if len(line.split('\t')) == 2:
    n = int(line.split('\t')[0])
    seed = line.split('\t')[1].strip()
    if n == 0:
        print('For the first run, please just place your password in the ' + SEED_PATH + ' file.')
        exit(1)
else:
    n = 0
    seed = line.strip()
pw = hashlib.sha256(str(seed + str(sys.argv[1])).encode('utf-8'))
print(pw.hexdigest())
next_seed = hashlib.sha256(str(seed).encode('utf-8'))
with open(SEED_PATH, 'w') as f:
    f.write(str(n + 1) + '\t' + next_seed.hexdigest())