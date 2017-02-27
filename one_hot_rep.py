def word_seq(seq, k, stride=1):
    i = 0
    words = []
    while i <= len(seq) - k:
        words.append(seq[i: i + k])
        i += stride
    return words

def create_dict(nucleotides):
    vec_dict = {}
    perms = k_len_perms(nucleotides, 3)
    perms.sort()
    for idx, seq in enumerate(perms):
        hot_vec = [ 0 for i in range(0, len(perms))]
        hot_vec[idx] = 1
        vec_dict[seq] = hot_vec
    return vec_dict

def k_len_perms(letters, k):
    n = len(letters)
    perms = []
    k_len_perms_hlpr(perms, letters, "", n, k)
    return perms

def k_len_perms_hlpr(perms, letters, prefix, n, k):
    if (k == 0):
        perms.append(prefix)
        return
    for i in range(0, n):
        newPrefix = prefix + letters[i]
        k_len_perms_hlpr(perms, letters, newPrefix, n, k - 1)

def create_rep_mat(words, hot_vec_dict, r_size):
    mat_len = len(words) - r_size + 1
    mat = [[] for i in range(0, mat_len)]
    i = 0
    while i < mat_len:
        j = i
        while j < i + r_size:
            mat[i].append(hot_vec_dict[words[j]])
            j += 1
        i += 1
    return mat

def get_rep_mat(seq):
    words = word_seq(seq, 3)
    hot_vec_dict = create_dict('ACGT')
    rep_mat = create_rep_mat(words, hot_vec_dict, 2)
    return rep_mat

if __name__ == "__main__":
    # running on a test sequence matching example in paper
    seq = 'ACCGATTATGCA'
    words = word_seq(seq, 3)
    hot_vec_dict = create_dict('ACGT')
    rep_mat = create_rep_mat(words, hot_vec_dict, 2)
