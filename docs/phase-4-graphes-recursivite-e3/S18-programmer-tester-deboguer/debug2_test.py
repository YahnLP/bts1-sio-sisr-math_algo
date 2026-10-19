assert compte_pairs([4, 7, 8, 10]) == 3 and compte_pairs([2]) == 1 and compte_pairs([]) == 0
assert compte_pairs([1, 3, 5]) == 0 and compte_pairs([6, 1, 1]) == 1
assert est_croissant([1, 2, 2, 5]) is True and est_croissant([3]) is True and est_croissant([]) is True
assert est_croissant([1, 3, 2, 5]) is False and est_croissant([5, 1]) is False
assert est_croissant([1, 2, 3, 2]) is False
assert pourcentage(1, 4) == 25 and pourcentage(3, 4) == 75 and pourcentage(0, 5) == 0
assert pourcentage(5, 5) == 100 and pourcentage(1, 3) > 33.3 and pourcentage(1, 3) < 33.4
assert pourcentage(3, 0) == 0
