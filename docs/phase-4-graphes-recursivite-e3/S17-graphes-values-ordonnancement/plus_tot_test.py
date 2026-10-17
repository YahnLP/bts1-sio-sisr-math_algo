projet = {"A": (3, []), "B": (2, ["A"]), "C": (6, ["B"]), "D": (4, ["A"]), "E": (5, ["D"]), "F": (4, ["C", "E"]), "G": (3, ["B"]), "H": (2, ["F", "G"])}
assert dates_au_plus_tot(projet) == {"A": 0, "B": 3, "C": 5, "D": 3, "E": 7, "F": 12, "G": 5, "H": 16}
mig = {"A": (2, []), "B": (4, []), "C": (3, ["A", "B"]), "D": (2, ["C"]), "E": (5, ["B"]), "F": (1, ["D", "E"])}
assert dates_au_plus_tot(mig) == {"A": 0, "B": 0, "C": 4, "D": 7, "E": 4, "F": 9}
assert dates_au_plus_tot({"X": (1, ["Y"]), "Y": (1, ["X"])}) is None
assert dates_au_plus_tot({"X": (5, [])}) == {"X": 0}
