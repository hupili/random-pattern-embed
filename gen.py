'''
Usage:
  gen.py <number> <length> <patterns>...
'''

import random
from docopt import docopt

CHAR_SET = [chr(i) for i in range(ord('a'), ord('z'))] \
  + [chr(i) for i in range(ord('A'), ord('Z'))] \
  + [chr(i) for i in range(ord('0'), ord('9'))]
for c in ['o', 'O', '0', 'i', '1']:
    CHAR_SET.remove(c)


if __name__ == '__main__':
    args = docopt(__doc__)
    number = int(args['<number>'])
    length = int(args['<length>'])
    patterns = args['<patterns>']
    #print(random.choice(CHAR_SET))
    results = []
    while number:
        number -= 1
        tmp = ''
        for _ in range(length):
            tmp += random.choice(CHAR_SET)
        rep = random.choice(patterns)
        idx = random.randint(0, len(tmp) - len(rep))
        tmp = tmp[:idx] + rep + tmp[idx + len(rep):]
        results.append(tmp)
    print('\n'.join(results))
        

    
