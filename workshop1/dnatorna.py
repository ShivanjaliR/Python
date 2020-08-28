def generaterna(dna):
    dic = {"G":"C","C":"G","A":"T","T":"A"}
    result = ""

    for ch in dna:
        result = result + dic[ch]

    print(f'RNA is {result}')

if __name__ == '__main__':
    dna = 'GCTAGCCTACG'
    generaterna(dna)