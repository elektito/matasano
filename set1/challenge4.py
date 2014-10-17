from challenge3 import xor_with_character, english_score

def most_likely_xor_char_english_decoding(s):
    results = []
    for i in xrange(0, 256):
        candidate = xor_with_character(s, chr(i))
        results.append((english_score(candidate), candidate, i))
    r = max(results, key=lambda i: i[0])
    return r[1], r[2]

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
        s, char = most_likely_xor_char_english_decoding(l.decode('hex'))
        results.append((english_score(s), s, l, char))

    score, decoding, line, char = max(results, key=lambda i: i[0])
    print 'The most likely line:', line
    print 'Decodes to:', decoding
    print 'The character used for encoding:', char
