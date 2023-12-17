### Edit Here ###

# import your machine learning model from sklearn
from sklearn.svm import SVC
#################
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
import pandas as pd
import numpy as np
import random
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

def main():
    ### Edit Here ###
    
    # read data from zoo.csv
    data = pd.read_csv('C:/Users/wjsgy/OneDrive/바탕 화면/데사컴/W11/zoo-1.csv')
    # data: select features
    train = data.drop(['animal_name', 'class_type'], axis=1)
    # label: class_type column
    label = data['class_type']
    # split train set, test set (train:test = 8:2)
    X_train, X_test, y_train, y_test = train_test_split(train, label, test_size=0.2, random_state=23)
    
    print('Classification Report:')
    svm_model = SVC(random_state=2023) 
    svm_model.fit(X_train, y_train)
    y_pred = svm_model.predict(X_test)

    # accuracy
    print(f'Accuracy: {accuracy_score(y_test, y_pred)}')
    # classification
    print(classification_report(y_test, y_pred,digits=2))

    # 새 동물 랜덤 만들기
    import random
    new_animals = []

    for _ in range(10):
        new_animal = [random.randint(0, 1) for _ in range(12)]
        #new_animals.append(new_animal)
        leg = [random.randint(0, 8)]  # 13번째 leg만 값이 0,1 말고 다른 애들 있음
        #new_animals.append(leg)
        new_animals_2 = [random.randint(0, 1) for _ in range(3)]
        temp = new_animal + leg +new_animals_2
        new_animals.append(temp)

    # 데이터프레임을 생성하고 열 이름을 설정
    new_animals_df = pd.DataFrame(new_animals, columns=train.columns)

    for i, row in new_animals_df.iterrows():
        new_animal_features = row.values  # 각 행의 피쳐들을 가져옴

        #new_animal_class = svm_model.predict([new_animal_features])

        decision_function_scores = svm_model.decision_function([new_animal_features])

        top3_classes = (-decision_function_scores).argsort()[:, :3]
        print(f"{i + 1}번째 동물이 속할 가능성이 있는 Top3 동물 분류는 {top3_classes[0]} 입니다.")

    #################

    
if __name__ == "__main__":
    main()
