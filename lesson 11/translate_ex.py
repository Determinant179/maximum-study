import goslate

gt = goslate.Goslate()

string = "Привет, как дела?"

result = gt.translate(string, "en")

print(result)