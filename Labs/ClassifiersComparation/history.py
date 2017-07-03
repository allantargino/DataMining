import numpy as np
import matplotlib.pyplot as plt

#importando o pacote de base de dados do sklearn
from sklearn import datasets

#importando a base de dados iris do pacote do sklearn
digits = datasets.load_digits()

#checando o tamanho da base de dados
len(digits.data)
len((digits.data)[1])

#checando um exemplo de uma instancia
((digits.data)[1])

#separando os atributos dos rotulos
X = digits.data
y = digits.target

#um parenteses para apresentar um comando de embaralhamento mais completo do que o da aula passada
import sklearn
Xs,ys = sklearn.utils.shuffle(X,y,random_state=0)

#plotando a imagem de uma das instancias
plt.figure(1,figsize=(3,3))
plt.imshow(digits.images[10],cmap=plt.cm.gray_r, interpolation='nearest')
plt.show()

#trabalhando com o K-fold CV diretamente com os folds
from sklearn.cross_validation import StratifiedKFold
#na versao mais recente fazer:
#from sklearn.model_selection import StratifiedKFold

folds = StratifiedKFold(y,10)

#testando com um conjunto de rotulos menor para melhor visualizacao
ymenor=[0,0,0,0,0,1,1,1,1,1,1,1,1,1,1]

#StratifiedKFold gera um iterador
folds2 = StratifiedKFold(ymenor,4)

#visualizando os folds (o comando list converte o iterador para lista)
list(folds2)
list(folds2)[0]
list(folds2)[1]
list(folds2)[2]
list(folds2)[3]

from sklearn import neighbors

#criando um classificador knn com k==3
clf = neighbors.KNeighborsClassifier(3)

#"treinando" o classificador com a primeira configuracao de folds de treinamento
clf.fit(X[list(folds)[0][0]],y[list(folds)[0][0]])

#testando o classicador na primeira configuracao de fold de teste e comparando com os rotulos originais
clf.predict(X[list(folds)[0][1]])==y[list(folds)[0][1]]

#fazendo a mesma coisa usando o metodo score
clf.score(X[list(folds)[0][1]],y[list(folds)[0][1]])


#trabalhando com k-fold cv em conjunto com o classificador
from sklearn.cross_validation import cross_val_score

#este comando realiza, para as 10 configuracoes de folds, treinamento e teste com o classificador, instancias e rotulos passados por parametro
#as acuracias de cada fold sao retornadas
cross_val_score(clf,X,y,cv=10)

#calculando a media e o desvio padrao de cada fold
res=cross_val_score(clf,X,y,cv=10)
np.mean(res); np.std(res)

#repetindo o procedimento com outro classificador, agora knn com k==1
clf2 = neighbors.KNeighborsClassifier(1)
res2=cross_val_score(clf2,X,y,cv=10)
np.mean(res2); np.std(res2)

#a forma com a qual o procedimento anterior foi realizado apresenta um erro de metodologia: os folds utilizados para testar cada classificador sao diferentes, pois sao gerados novamente para clf2
#para corrigir isso, o parametro cv pode ser usado para receber os proprios folds, ao inves de um numero
#dessa forma, os folds podem ser criados com o comando StratifiedKFold e passados por parametro para o cross_val_score
res=cross_val_score(clf,X,y,cv=folds)
np.mean(res); np.std(res)

res2=cross_val_score(clf2,X,y,cv=folds)
np.mean(res2); np.std(res2)

#os experimentos anteriores usaram a medida de avaliacao acuracia (default)
#para usar outras medidas como AUC (vista em aula) basta setar o parametro scoring
#as opcoes podem ser vista neste endereco: http://scikit-learn.org/stable/modules/model_evaluation.html
#a AUC nao funcionara na digits pois ela contem mais do que duas classes




