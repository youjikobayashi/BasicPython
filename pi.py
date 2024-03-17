text = """
    How I want a drink, alcoholic of course, after the heavy chapters involving
    quantum mechanics. All of thy geometry, Herr Planck, is fairly hard.
"""

# TODO
a = list(map(len,text.replace(",","").replace(".","").split()))
b = map(str,a)
c = list(b)
d = "".join(c)
print(d)


