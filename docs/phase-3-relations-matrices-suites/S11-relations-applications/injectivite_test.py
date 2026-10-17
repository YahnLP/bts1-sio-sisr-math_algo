f1 = {1: "a", 2: "b", 3: "a", 4: "c"}
f2 = {1: "a", 2: "b", 3: "c", 4: "d"}
f3 = {1: "a", 2: "b", 3: "c"}
assert est_injective(f1) is False and est_surjective(f1, "abc") is True and est_bijective(f1, "abc") is False
assert est_injective(f2) is True and est_surjective(f2, "abcd") is True and est_bijective(f2, "abcd") is True
assert est_injective(f3) is True and est_surjective(f3, "abcd") is False and est_bijective(f3, "abcd") is False
mod5 = {x: x % 5 for x in range(10)}
assert est_injective(mod5) is False and est_surjective(mod5, range(5)) is True
assert est_injective({}) is True
