import pandas

# Read Pima dataset
names = ['Preg', 'Glucose', 'BloodPress', 'SkinThickness', 'Insulin', 'BMI', 'Pref', 'Age', 'Outcome']
pima_data_df = pandas.read_csv('pima-indians-diabetes.csv', names=names)
array = pima_data_df.values

print("Pima Data\n", pima_data_df)

X = array[:,0:8]
Y = array[:,8]

from sklearn import model_selection
from sklearn.neighbors import KNeighborsClassifier

kfold = model_selection.KFold(n_splits=5, random_state=7,shuffle=True)
model = KNeighborsClassifier()

scoring = 'accuracy'
results = model_selection.cross_val_score(model, X, Y, cv=kfold, scoring=scoring)

print("Accuracy evaluation: %.3f (KNN accuracy is %.3f)" % (results.mean()*100, results.std()*100))

# F1-score evaluation
diabetes_knn = KNeighborsClassifier(n_neighbors=3).fit(X, Y)

from sklearn import metrics
y_pred = diabetes_knn.predict(X)

report = metrics.classification_report(Y, y_pred, target_names=['No Diabetes', 'Diabetes'])
print(report)

# Confusion matrix 


