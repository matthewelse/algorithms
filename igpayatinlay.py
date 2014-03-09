vowels = {'a', 'e', 'i', 'o', 'u'}
consonants = {'b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z'}

def igpayatinlay(word):
    suffix = 'ay'
    if word[0] in vowels:
        suffix = 'way'

    end = 1
    if word[0] not in vowels:
        for i in range(1,len(word)):
            if word[i] in vowels:
                end = i
                break

    return word[end:len(word)]+word[0:end]+suffix
