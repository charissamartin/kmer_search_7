from itertools import product
dna = "AGCATGTACCATGATACCTTGTCCGTTTAAGGCGCGCCGAATATGCGTTGTGAGCTGTTTGCATGTTGCCACGGCGGCCTATCATATAATATCCTTAAGAAGGGCGACATTACATGAGCGAGTTCCCACACGCACATTCTCCGCATGGTCCGGCAGAGCGACGCCACGTTTAGCTCCCGTCATCAACTGAGAGGACATACACACACCCAGAGGCGAGGCTTCACCAATCAGGACAAATCAATTTGGAGCCTAAACAAAGTCTGATGTCCTGTTCACTAGCTGTAAAAACACATTTTAGGTAGATCTACCCTTACTTTTTACGCTACCTAATATATTGCTTCAATGTGTTAAACCCCAGACGGGGTGTATGGGGCTGATTAAACGGACCGCCTTGTGAATTCTAGAACGGTTGAGCCTAACAATCCATAGCCCAAGCTTTGTGTCCAGACTTGATAGTATATTACAGCCTAAACACGAGCCCGGGGTGCTGCTATACAAGCATGTCTCACTATACGTAAAGCAGATTTCTCATAAGGCAATCTACGTGCGGAGGGGGCTAACCTATGCTGCAGGACATGCACAATGGTAGGCGTAACGCTTCATCCAATTTGCCAAGCGATTACGTTCATAGGATGCTTCTACACGCAGATAAGGCTGAAATTCCCCATCCTTCATGCACTCCAC"
kmers = sorted(list(product('ACTG', repeat = 7)))
kmers = [''.join(x) for x in kmers]
dnary = {x : 0 for x in kmers}
length = 7
for x in range(len(dna) - length + 1):
    dnary[dna[x : x + length]] +=1
print(' '.join([str(x) for x in dnary.values()]))
