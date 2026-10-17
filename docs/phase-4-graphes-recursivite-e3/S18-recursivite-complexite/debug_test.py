assert maximum([3, 9, 4]) == 9 and maximum([-5, -2, -9]) == -2 and maximum([7]) == 7
assert somme_positifs_moyenne([4, -2, 6]) == 5 and somme_positifs_moyenne([-1, -2]) == 0 and somme_positifs_moyenne([]) == 0
assert somme_positifs_moyenne([0, 4, 0]) == 4
original = [3, 1, 2]
assert trie_sans_modifier(original) == [1, 2, 3]
assert original == [3, 1, 2]
