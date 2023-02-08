import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
tabela=pd.read_csv(r'C:\Users\Usuário\Downloads\advertising.csv')
print(tabela)

print(tabela.corr())
sns.heatmap(tabela.corr(),cmap='Greens',annot=True)
plt.show()

y=tabela["Vendas"]
x=tabela[["TV","Radio","Jornal"]]
x_treino, x_teste, y_treino, y_teste = train_test_split(x,y)

modelo_linear=LinearRegression()
modelo_arvoredecisao=RandomForestRegressor()

modelo_linear.fit(x_treino,y_treino)
modelo_arvoredecisao.fit(x_treino,y_treino)

p_regressaolinear= modelo_linear.predict(x_teste)
p_arvoredecisao = modelo_arvoredecisao.predict(x_teste)
print(r2_score(y_teste,p_regressaolinear))
print(r2_score(y_teste,p_arvoredecisao))

tabela_auxiliar= pd.DataFrame()
tabela_auxiliar['y_teste'] = y_teste
tabela_auxiliar['Previsao Arvore Decisao'] = p_arvoredecisao
tabela_auxiliar["Previsao RegressaoLinear"]=p_regressaolinear

sns.lineplot(data=tabela_auxiliar)
plt.show()