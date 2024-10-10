import hashlib
SEED_PATH = 'complete.txt'
WORDLIST_PATH = 'passwords.txt'
passwords:list[str] = []

timestamps = [1727365201,1727365801,
              1727366402,1727367001,
              1727367601,1727368201,
              1727368801]

looking_for_n = 78 - len(timestamps) - 1

with open(SEED_PATH, 'r') as f:
    seeds = f.readlines()

for timestamp in timestamps:
    for i in range(len(seeds)):
        if i == looking_for_n:
            pw = hashlib.sha256(str(seeds[i].replace('\n', '').strip() + str(timestamp)).encode('utf-8')).hexdigest()
            passwords.append(str(timestamp) + ':\t' + pw + '\n')
            looking_for_n += 1
            break

with open(WORDLIST_PATH, 'w') as f:
    f.writelines(passwords[:-1])
    f.write(passwords[-1].replace('\n', ''))
