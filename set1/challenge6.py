from challenge4 import most_likely_xor_char_english_decoding
import base64
from itertools import izip_longest

def byte_hamming_distance(b1, b2):
    # This sets all differing bits to one.
    i = ord(b1) ^ ord(b2)

    # Now count the number of ones. Adopted from the code in this
    # Stack Overflow answer:
    # http://stackoverflow.com/questions/109023/how-to-count-the-number-of-set-bits-in-a-32-bit-integer
    i = i - ((i >> 1) & 0x55)
    i = (i & 0x33) + ((i >> 2) & 0x33)
    return (((i + (i >> 4)) & 0x0f) * 0x01)

def hamming_distance(s1, s2):
    if len(s1) != len(s2):
        raise Exception('Size mismatch.')

    return sum(byte_hamming_distance(b1, b2) for b1, b2 in zip(s1, s2))

def likeliest_key_sizes(data, minsize, maxsize, n):
    '''Returns the likeliest key-sizes for an repeating-key encrypted
piece of data.

    `data` is the encrypted data. `minsize` and `maxsize` determine
    the range of key-sizes to try. `n` is the number of the likeliest
    key-sizes to return.

    '''
    distances = []
    for keysize in xrange(minsize, maxsize + 1):
        # find the hamming distances between pairs of keysize bytes
        dists = [hamming_distance(data[i:i+keysize], data[i+keysize:i+2*keysize])
                 for i in xrange(0, len(data) - 2*keysize, keysize)]

        # now normalize the distances
        d = sum(dists) / float(len(dists))

        distances.append((keysize, float(d) / keysize))
    distances.sort(key=lambda i: i[1])

    return [i[0] for i in distances[:n]]

def split_string(s, n):
    return [s[i:i+n] for i in xrange(0, len(s), n)]

def break_repeating_key_with_keysize(data, keysize):
    # break the ciphertext into blocks of keysize
    chunks = split_string(data, keysize)

    # transpose the chunks (i.e. create a list of strings in which the
    # first string contains all first characters of the chunks, the
    # second string contains all second characters and so on).
    chunks = map(lambda i: ''.join(i),
                 izip_longest(*chunks, fillvalue=''))

    # now solve each chunk for one character
    chunks = [most_likely_xor_char_english_decoding(i.encode('hex'))
              for i in chunks]

    # transpose again
    chunks = map(lambda i: ''.join(i),
                 izip_longest(*chunks, fillvalue=''))

    return ''.join(chunks)

if __name__ == '__main__':
    with open('6.txt') as i:
        data = i.read()
    data = base64.b64decode(data)

    keysizes = likeliest_key_sizes(data, 2, 50, 5)
    print 'likeliest keysize:', keysizes[0]
    print
    print break_repeating_key_with_keysize(data, keysizes[0])
