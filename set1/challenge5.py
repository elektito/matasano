def repeating_key_xor(s, key):
    result = ''
    for i in xrange(len(s)):
        result += chr(ord(s[i]) ^ ord(key[i % len(key)]))
    return result

if __name__ == '__main__':
    s1 = "Burning 'em, if you ain't quick and nimble\n"
    s2 = "I go crazy when I hear a cymbal"

    expected1 = '0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272'
    expected2 = 'a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f'

    if repeating_key_xor(s1 + s2, 'ICE').encode('hex') == expected1+expected2:
        print 'Match!'
    else:
        print 'Did not match!'
