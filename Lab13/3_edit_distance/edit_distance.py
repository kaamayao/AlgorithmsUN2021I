def edit_distance(seq1, seq2):
    d={}
    for i in range(len(seq1)+1):
        d[i]={}
        d[i][0]=i
    for i in range(len(seq2)+1):
        d[0][i] = i
    for i in range(1, len(seq1)+1):
        for j in range(1, len(seq2)+1):
            deletion = d[i][j-1]+1
            insertion = d[i-1][j]+1
            cost = not seq1[i-1] == seq2[j-1]
            substitution = d[i-1][j-1] + cost
            d[i][j] = min(deletion,insertion,substitution)
    return d[len(seq1)][len(seq2)] 

if __name__ == "__main__":
    print(edit_distance(input(), input()))
