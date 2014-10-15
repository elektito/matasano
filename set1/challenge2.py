def xor(s1, s2):
    if len(s1) != len(s2):
        raise Exception('Buffer length mismatch.')

    return hex(int(s1, 16) ^ int(s2, 16))[2:-1]

expected = '746865206b696420646f6e277420706c6179'
s1 = '1c0111001f010100061a024b53535009181c'
s2 = '686974207468652062756c6c277320657965'
result = xor(s1, s2)

print 's1:', s1
print 's2:', s2
print 'expected:', expected
print 'result:', result
print 'Match!' if result == expected else 'Did not match!'
