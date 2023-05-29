import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_text

data = {'a1': [1, 1, 0, 1, 1], 'a2': [0, 0, 1, 1, 1], 'a3': [0, 1, 0, 1, 0], 'dec': [0, 0, 0, 1, 1]}
df = pd.DataFrame(data=data)

X = df.drop('dec', axis=1)
y = df['dec']

clf = DecisionTreeClassifier()
clf.fit(X,y)

tree_rules = export_text(clf)
print(tree_rules)