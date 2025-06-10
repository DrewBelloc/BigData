import pandas as pd
from sklearn import tree
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

def train(option, entrada1=0, entrada2=0, entrada3=0, entrada4=0):
    # Ler o banco de dados
    df = pd.read_csv('data.csv')

    # Cria uma copia do banco de dados com a coluna de saida removida
    X = df.drop('taxa', axis=1)
    # Separa os dados para o aprendizado de maquina
    y = df['taxa']
    X_train, X_test, y_train, y_test = train_test_split(
        X,y,test_size = 0.3,random_state = 1
    )

    # treina o modelo
    clf = tree.DecisionTreeClassifier()
    clf.fit(X_train, y_train)

    # Faz testes no modelo criado
    y_prediction = clf.predict(X_test)
    precisao = accuracy_score(y_test, y_prediction) # gera a taxa de precisão do modelo

    if option == 1: # Caso só queira saber o desempenho
        return precisao
    elif option == 2: # Caso queira saber a taxa de entrega de algum endereço
        # Cria um dataframe com os dados passados e tenta prever o resultado
        df_para_classificar = pd.DataFrame(
            [[entrada1, entrada2, entrada3, entrada4]], columns=
                ["rua","numero","lote","quadra"])
        y_prediction = clf.predict(df_para_classificar)
        return y_prediction, precisao # retorna a previsão para o programa principal e a precisão do modelo

    elif option == 3: # Mostrar arvore de decisão
        data_feature_names = ['sepal length', 'sepal width', 'petal length', 'petal width']
        data_class_names = ['Iris-setosa','Iris-versicolor', 'Iris-virginica']
        tree.plot_tree(clf, feature_names = data_feature_names,
                       class_names= data_class_names, filled = True)
        plt.show()
        