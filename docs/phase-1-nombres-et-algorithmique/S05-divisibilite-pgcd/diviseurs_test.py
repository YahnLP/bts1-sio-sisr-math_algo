assert diviseurs(1) == [1]
assert diviseurs(13) == [1, 13]
assert diviseurs(36) == [1, 2, 3, 4, 6, 9, 12, 18, 36]
assert diviseurs(84) == [1, 2, 3, 4, 6, 7, 12, 14, 21, 28, 42, 84]
assert len(diviseurs(360)) == 24
