# for `main`
from one_hot_rep import get_rep_mats, conv_labels

def load_data(fname):
    seqs = []
    labels = []
    f = open(fname)
    for line in f:
        line_no_wspace = line.replace(" ","")
        line_no_nwline = line_no_wspace.replace("\n","")
        line_arr = line_no_nwline.split(",")
        label = line_arr[0]
        seq = line_arr[2]
        ##### ONLY FOR SPLICE DATA SET
        seq = seq.replace("N","A")
        seq = seq.replace("D","G")
        seq = seq.replace("S","C")
        seq = seq.replace("R","G")
        ##############
        labels.append(label)
        seqs.append(seq)
    f.close()
    return seqs, labels

if __name__ == "__main__":
    # reading in splice junction input data and converting to required format
    seqs, labels = load_data("./splice.data.txt")
    lbls_mod = conv_labels(labels)
    seqs_mod = get_rep_mats(seqs)
    print len(seqs_mod)
    print len(lbls_mod)
