def hex2dec(s):
    return int(s, 16)

def b64digit(d):
    if 0 <= d <= 25:
        return chr(ord('A') + d)
    elif 26 <= d <= 51:
        return chr(ord('a') + (d - 26))
    elif 52 <= d <= 61:
        return chr(ord('0') + (d - 52))
    elif d == 62:
        return '+'
    elif d == 63:
        return '/'
    else:
        raise Exception('Invalid base64 digit.')

def dec2b64(n):
    s = ''
    while n > 64:
        d = n % 64
        n = n / 64
        s += b64digit(d)

    s += b64digit(n)

    return s[::-1]

def hex2base64(s):
    return dec2b64(hex2dec(s))

n = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
expected = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

result = hex2base64(n)

print 'Input is:', n
print 'Expected:', expected
print 'Result:', result
print 'Match!' if result == expected else 'Did not match!'
