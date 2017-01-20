from RWQS5cCEodqSWx4bR import stringsRearrangement

true_arrays = []
false_arrays = []
false_arrays.append(["aba", "bbb", "bab"])  # false
true_arrays.append(["ab", "bb", "aa"])  # true
false_arrays.append(["q", "q"])  # false
true_arrays.append(["zzzab", "zzzbb", "zzzaa"])  # true
false_arrays.append(["ab", "ad", "ef", "eg"])  # false
false_arrays.append(["abc", "abx", "axx", "abc"])  # false
true_arrays.append(["abc", "abx", "axx", "abx", "abc"])  # true
true_arrays.append(["f", "g", "a", "h"])  # true


for array in true_arrays:
    if not stringsRearrangement(array):
        assert()
for array in false_arrays:
    if stringsRearrangement(array):
        assert()
