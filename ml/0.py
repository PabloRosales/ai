from utils import col2float, col2int, load_csv, minmax, normalize

pima = load_csv("pima-indians-diabetes.csv")
pima = pima[1:] # Remove CSV headers
for i in range(len(pima[0])):
    col2float(pima, i)

print(pima[0])

iris = load_csv("iris.csv")
for i in range(4):
    col2float(iris, i)

lookup = col2int(iris, 4)
iris_mm = minmax(iris)

print(iris[0])
print(lookup)
print(iris_mm)

normalize(iris, iris_mm)
print(iris)