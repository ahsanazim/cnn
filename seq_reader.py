def read(fname):
    seqs = []
    labels = []
    f = open(fname)
    for line in f:
        line_no_wspace = line.replace(" ","")
        line_no_nwline = line_no_wspace.replace("\n","")
        line_arr = line_no_nwline.split(",")
        label = line_arr[0]
        seq = line_arr[2]
        labels.append(label)
        seqs.append(seq)
    f.close()
    return seqs, labels

if __name__ == "__main__":
    seqs, labels = read("./splice.data.txt")
    print seqs
    print labels
    print len(seqs), len(labels)
