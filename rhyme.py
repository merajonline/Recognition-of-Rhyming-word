from nltk.corpus import cmudict

def getPronunciation(in_word, entries):
    for word, pron in entries:
        if word == in_word:
            return pron

def rhymes_with(in_word, entries):
    in_pron = getPronunciation(in_word, entries)
    if in_pron is None:
        return None # word not in corpus
    matches = []
    for word, pron in entries:
        if word == in_word:
            continue
        i=1 # reverse iterator
        n=0 # number of consecutive matching syllables
        while True:      
            if len(in_pron) < i or len(pron) < i:
                break
            elif pron[-i] != in_pron[-i]:
                break
            else:
                i+=1
                n+=1
            if n>0:
                matches.append((n,word))
    matches.sort()
    matches.reverse()
    return matches

if __name__ == '__main__':   
    while True:
        pronDict = cmudict.entries()
        target = raw_input("Rhymes with ('x' to exit): ")    
        target = target.lower()
        if target == 'x':
            break
        results = rhymes_with(target, pronDict)
        if results is not None:
            if len(results) > 10:
                results = results[0:10]
            for r in results:
                print(r)
