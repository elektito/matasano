import base64

def hex2base64(s):
    return base64.b64encode(s.decode('hex'))

if __name__ == '__main__':
    n = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    expected = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

    result = hex2base64(n)

    print 'Input is:', n
    print 'Expected:', expected
    print 'Result:', result
    print 'Match!' if result == expected else 'Did not match!'
