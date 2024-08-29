def DNAReplacing(a):
    a = a.replace('A', 't').replace('T', 'a').replace('C', 'g').replace('G', 'c')
    return a.upper()
def Quanty(s):
    return s.count("A"), s.count("G"), s.count("C"), s.count("T")
def RNA_STUFF():
    F = ('UUU', 'UUC')
    L = ('UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG')
    S = ('UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC')
    Y = ('UAU', 'UAC')
    C = ('UGU', 'UGC')
    W = ('UGG')
    P = ('CCU', 'CCC', 'CCA', 'CCG')
    H = ('CAU', 'CAC')
    Q = ('CAA', 'CAG')
    R = ('CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG')
    I = ('AUU', 'AUC', 'AUA')
    M = ('AUG')
    T = ('ACU', 'ACC', 'ACA', 'ACG')
    N = ('AAU', 'AAC')
    K = ('AAA', 'AAG')
    S = ('AGU', 'AGC')
    V = ('GUU', 'GUC', 'GUA', 'GUG')
    A = ('GCU', 'GCC', 'GCA', 'GCG')
    D = ('GAU', 'GAC')
    E = ('GAA', 'GAG')
    G = ('GGU', 'GGC', 'GGA', 'GGG')
    RNA_Dict = {F: 'F', L: 'L', S: 'S', Y: 'Y', C: 'C', W: 'W', P: 'P', H: 'H', Q: 'Q', R: 'R', I: 'I', M: 'M', T: 'T', N: 'N', K: 'K', S: 'S', V: 'V', A: 'A', D: 'D', E: 'E', G: 'G'}
    return RNA_STUFF