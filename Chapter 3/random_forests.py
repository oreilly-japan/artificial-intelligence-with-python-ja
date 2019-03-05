
# coding: utf-8

# In[8]:

import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.metrics import classification_report 
from sklearn import model_selection
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier 
from sklearn.metrics import classification_report 

from utilities import visualize_classifier 

classifier_type = 'erf'  # 'rf'ならランダムフォレスト、それ以外ならERT

input_file = 'data_random_forests.txt' 
data = np.loadtxt(input_file, delimiter=',') 
X, y = data[:, :-1], data[:, -1] 

class_0 = np.array(X[y==0]) 
class_1 = np.array(X[y==1]) 
class_2 = np.array(X[y==2]) 

plt.figure() 
plt.scatter(class_0[:, 0], class_0[:, 1], s=75, facecolors='white', 
            edgecolors='black', linewidth=1, marker='s') 
plt.scatter(class_1[:, 0], class_1[:, 1], s=75, facecolors='white', 
            edgecolors='black', linewidth=1, marker='o') 
plt.scatter(class_2[:, 0], class_2[:, 1], s=75, facecolors='white', 
            edgecolors='black', linewidth=1, marker='^') 
plt.title('Input data') 
plt.show()


# In[9]:

X_train, X_test, y_train, y_test = model_selection.train_test_split( 
            X, y, test_size=0.25, random_state=5) 

params = {'n_estimators': 100, 'max_depth': 4, 'random_state': 0} 
if classifier_type == 'rf': 
      classifier = RandomForestClassifier(**params) 
else: 
      classifier = ExtraTreesClassifier(**params) 
        
classifier.fit(X_train, y_train) 
visualize_classifier(classifier, X_train, y_train, 'Training dataset') 


# In[10]:

y_test_pred = classifier.predict(X_test) 
visualize_classifier(classifier, X_test, y_test, 'Test dataset')
class_names = ['Class-0', 'Class-1', 'Class-2'] 
print("\n" + "#"*40) 
print("\nClassifier performance on training dataset\n") 
print(classification_report(y_train, classifier.predict(X_train), 
                            target_names=class_names)) 
print("#"*40 + "\n") 

print("#"*40) 
print("\nClassifier performance on test dataset\n") 
print(classification_report(y_test, y_test_pred, target_names=class_names)) 
print("#"*40 + "\n") 


# In[ ]:



