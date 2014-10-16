from challenge3 import xor_with_character, english_score

def most_likely_xor_char_english_decoding(s):
    results = []
    for i in xrange(0, 256):
        candidate = xor_with_character(s, chr(i)).decode('hex')
        results.append((english_score(candidate), candidate))
    return max(results, key=lambda i: i[0])[1]

def readlines(filename):
    lines = []
    with open(filename) as i:
        l = i.readline()
        while l != '':
            if l.endswith('\n'):
                l = l[:-1]
            lines.append(l)
            l = i.readline()

    return lines

if __name__ == '__main__':
    lines = readlines('4.txt')

    results = []
    for l in lines:
        s = most_likely_xor_char_english_decoding(l)
        results.append((english_score(s), s, l))

    score, decoding, line = max(results, key=lambda i: i[0])
    print 'The most likely line:', line
    print 'Decodes to:', decoding
