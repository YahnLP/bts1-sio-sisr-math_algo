assert meme_fonction(lambda a, b: a or (a and b), lambda a, b: a, 2) is True
assert meme_fonction(lambda a, b: not (a and b), lambda a, b: (not a) or (not b), 2) is True
assert meme_fonction(lambda a, b: a or b, lambda a, b: a and b, 2) is False
assert meme_fonction(lambda a, b, c: (a and b) or (not a and c) or (b and c), lambda a, b, c: (a and b) or (not a and c), 3) is True
assert meme_fonction(lambda a, b, c: (a and not b) or (a and b and c), lambda a, b, c: a and not b, 3) is False
