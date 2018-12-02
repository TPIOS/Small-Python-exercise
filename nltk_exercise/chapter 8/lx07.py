import pandas as pd
data = pd.read_csv("./iris.data.txt", names=["sepal length","sepal width", "petal length", "petal width", "Cat"], header=None)
# print(data.head())
# print("describe:", data.describe())
# sepal_len_cnt = data['sepal length'].value_counts()
# print(sepal_len_cnt)
# print(data['Cat'].value_counts())
# print(data['Cat']=='Iris-setosa')
sntsosa = data[data['Cat']=='Iris-setosa']
print(sntsosa[:5])
