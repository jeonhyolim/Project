from sklearn.model_selection import train_test_split
from collections import Counter
import numpy as np
import pandas as pd

class ClassificationReport:
    def __init__(self, num_class):
        self.num_class = num_class

    def confusion_matrix(self, pred, target):
        cnfs_mat = [{'TP': 0, 'FP': 0, 'FN': 0, 'TN': 0} for _ in range(self.num_class)]
        for class_idx in range(self.num_class):
            for idx in range(len(target)):
                #### Edit here ####
                # get TP, FP, FN, TN for each class
                if target.iloc[idx] == class_idx:
                    if pred[idx] == class_idx:
                        cnfs_mat[class_idx]['TP'] += 1
                    else:
                        cnfs_mat[class_idx]['FN'] += 1
                else:
                    if pred[idx] == class_idx:
                        cnfs_mat[class_idx]['FP'] += 1
                    else:
                        cnfs_mat[class_idx]['TN'] += 1
                
                ####################################
        return cnfs_mat

    def precision(self, TP, FP, FN, TN):
        prc = None
        #### Edit here ####
        # calculate precision
        if TP + FP == 0:
            return 0
        else:
            prc = TP / (TP+FP)
        ###################
        return prc

    def recall(self, TP, FP, FN, TN):
        rc = None
        #### Edit here ####
        # calculate recall
        if TP + FN == 0:
            return 0
        else:
            rc =TP/(TP+FN)
        ###################
        return rc

    def f_measure(self, precision, recall):
        fm = None
        #### Edit here ####
        # calculate f_measure
        fm =2*(precision*recall)/(precision+recall) 

        ###################
        return fm

    def multiclass_evaluation(self, pred, target):
        f_measure_, precision_, recall_ = [], [], []
        
        #### Edit here ####
        # get f_measure, precision, recall for each class
        # print f_measure, precision, recall for each class and calculate accuracy
        results = []
        support_ = []
        for class_idx in range(self.num_class):
            TP, FP, FN, TN = 0, 0, 0, 0
            for idx in range(len(target)):
                if target.iloc[idx] == class_idx:
                    if pred[idx] == class_idx:
                        TP += 1
                    else:
                        FN += 1
                else:
                    if pred[idx] == class_idx:
                        FP += 1
                    else:
                        TN += 1
            
            precision = self.precision(TP, FP, FN, TN)
            recall = self.recall(TP, FP, FN, TN)
            f_measure = self.f_measure(precision, recall)
            support = sum(target == class_idx)

            f_measure_.append(round(f_measure,2))
            precision_.append(round(precision,2))
            recall_.append(round(recall,2))
            support_.append(round(support,2))

            
            results.append({
                "Class": class_idx,
                "Precision": round(precision,2),
                'Recall': round(recall,2),
                "f1-score": round(f_measure,2),
                "Support":support,
            })

        # Calculate accuracy
        total_samples = len(target)
        correct_predictions = sum([1 for p, t in zip(pred, target) if p == t])
        accuracy = correct_predictions / total_samples
        f1_score_accuracy = round(accuracy,2)

        results.append({
            "Class": "accuracy:",
            "Precision": None, #round(accuracy, 2),
            "Recall": None,
            "f1-score": f1_score_accuracy,
            "Support": sum(support_),
        })

        result_df = pd.DataFrame(results)  # 
        print(result_df)  # 

        return f_measure_, precision_, recall_, accuracy
        ####################


#### Edit here ####
# split the data into train-test data
# train each model and evaluate
# tune svm and evaluate
from sklearn.svm import SVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv('W10/mobile_data-2.csv')

X_train, X_test, y_train, y_test = train_test_split(df[:len(df)], df['price_range'], test_size=0.33, random_state=2023)

print('SVM 분류 결과:')
svm_model = SVC(random_state=2023) 
svm_model.fit(X_train, y_train)
y_pred = svm_model.predict(X_test)

report = ClassificationReport(num_class=4)
f_measure, precision, recall, accuracy = report.multiclass_evaluation(y_pred, y_test)
print(report) 

print('Decision Tree 분류 결과:')
dt_model = DecisionTreeClassifier(random_state=2023) 
dt_model.fit(X_train, y_train)
y_pred = dt_model.predict(X_test)

report = ClassificationReport(num_class=4)
f_measure, precision, recall, accuracy = report.multiclass_evaluation(y_pred, y_test)
print(report) 

print('Naive Bayes 분류 결과:')
nb_model = MultinomialNB() 
nb_model.fit(X_train, y_train)
y_pred = nb_model.predict(X_test)

report = ClassificationReport(num_class=4)
f_measure, precision, recall, accuracy = report.multiclass_evaluation(y_pred, y_test)
print(report) 

print('KNeighbors 분류 결과:')
k_model = KNeighborsClassifier() 
k_model.fit(X_train, y_train)
y_pred = k_model.predict(X_test)

report = ClassificationReport(num_class=4)
f_measure, precision, recall, accuracy = report.multiclass_evaluation(y_pred, y_test)
print(report) 

print('Random Forest분류 결과:')
rf_model = RandomForestClassifier(random_state=2023) 
rf_model.fit(X_train, y_train)
y_pred = rf_model.predict(X_test)

report = ClassificationReport(num_class=4)
f_measure, precision, recall, accuracy = report.multiclass_evaluation(y_pred, y_test)
print(report) 

print('Tuning 후 SVM 분류 결과:')
svm_model = SVC(random_state=2023, kernel='linear') 
svm_model.fit(X_train, y_train)
y_pred = svm_model.predict(X_test)

report = ClassificationReport(num_class=4)
f_measure, precision, recall, accuracy = report.multiclass_evaluation(y_pred, y_test)
print(report) 
###################
