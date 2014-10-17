def english_score(s):
    # The following letter scores are based on the probability of the
    # each English letter taken from
    # http://en.wikipedia.org/wiki/Letter_frequency
    letters = 'zqxjkvbpygfwmucldrhsnioate .,'
    scores = [74, 95, 150, 153, 772, 978, 1492, 1929, 1974, 2015,
              2228, 2360, 2406, 2758, 2782, 4025, 4253, 5987, 6094,
              6327, 6749, 6966, 7507, 8167, 9056, 12702, 5000, 1000, 500]

    s = s.lower()
    r = 0
    for c in s:
        if c in letters:
            i = letters.index(c)
            r += scores[i]
        elif ord(c) < 32 or ord(c) > 127:
            r -= 1000

    return float(r) / len(s) if len(s) > 0 else 0

def xor_with_character(s, c):
    return ''.join([chr(ord(i) ^ ord(c)) for i in s])

if __name__ == '__main__':
    s = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    s = s.decode('hex')

    results = []
    for i in xrange(0, 256):
        candidate = xor_with_character(s, chr(i))
        results.append((english_score(candidate), candidate))

    print 'Likeliest to be English:', max(results, key=lambda i: i[0])[1]
