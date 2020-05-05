import numpy as np
from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import pickle
from sklearn.compose import make_column_transformer
import time

from utils import *


train = pd.read_csv("NSL_KDD/KDDTrain+.csv",header=None,names= feature)
test = pd.read_csv("NSL_KDD/KDDTest+.csv",header=None,names= feature)

train = train.replace({'label':attack_type_dict})
test = test.replace({'label':attack_type_dict})

trim_train =  train[(train.label == 'normal' )|( train.label == 'dos')]
test =  test[(test.label == 'normal' )|( test.label == 'dos')]

y_train = trim_train['label'] 
y_test = test['label'] 
x_train = trim_train[select]
x_test = test[select]


from sklearn.compose import make_column_transformer
from sklearn.preprocessing import OneHotEncoder 
preprocessor = make_column_transformer(
    (OneHotEncoder(categories='auto'),[1]),remainder="passthrough")
preprocessor.fit(train[select])
x_test = preprocessor.transform(x_test)
x_train = preprocessor.transform(x_train)



# from sklearn.feature_selection import SelectKBest, f_classif,chi2
# selector = SelectKBest(f_classif, k=20)
# selector.fit(x_train, y_train)
# print(x_train.columns[selector.get_support()])

# x_train = selector.transform(x_train)
# x_test = selector.transform(x_test)


from sklearn.preprocessing import StandardScaler 
scaler = StandardScaler(with_mean=False)
scaler.fit(x_train)
x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)

print('start')
start = time.time()
# clf = svm.SVC(C=0.1,kernel='linear')
# clf.fit(x_train,y_train)
clf = RandomForestClassifier(n_estimators=300)
clf.fit(x_train,y_train)


print('train time',time.time()-start)
start = time.time()


print(clf.score(x_test,y_test))
print('predict time',time.time()-start)




model = {"classifier":clf,"scaler":scaler,"preprocessor":preprocessor}
with open('model', 'wb') as f:
        pickle.dump(model,f)