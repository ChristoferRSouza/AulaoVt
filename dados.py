# pip install pandas
import pandas as pd

dados = pd.read_csv('athlete_events.csv')

#Dados do arquivo
dados.head() #5 primeiras linhas
dados.shape #Qtd de linhas e colunas
dados.describe() #dados matematicos como maximo, minimo, media, contador, desvio padrao
dados['Medal'].value_counts() #Coluna medalha conta valores difentes
dados['City'].value_counts()


#filtros
dados['Name'] #Filtra pelo nome da coluna
dados.loc[[0,3,6,8]] #Filtra pelo indice da tabela
dados.loc[0:3] #Filtra pelo indice da tabela de -> até

dados.loc[dados['Name']=='Edgar Lindenau Aabye'] #filtra valor na coluna especifica (Coluna name o nome edgar...)

primeiraslinhas = dados.loc[0:5]

#altera dados
dados.rename(columns={'Name':'Nome', 'Sex':'Sexo', 'Age':'Idade'})

#excluir dados
dados.drop('ID', axis = 1, inplace=True) #Dropa / Apaga a coluna passada Obs.: axis = 1 indica coluna, 
                                         #inplace = true não imprime valor na hora

dados2 = dados.dropna() # Dropa / apaga dados faltantes = NaN
dados2

enulo = dados.isnull() # Marca valor se existe ou não como boleano(true/false)
enulo

faltantes = dados.isnull().sum() # Soma quantidade de dados faltantes por coluna
faltantes

faltantes_percentual = (dados.isnull().sum() / len(dados['ID']))*100 # % de dados faltantes Obs.: Len ve o tamanho dos dados

dados['Medal'].fillna('Nenhuma') # Substitui NaN por Nenhuma
dados['Age'].fillna(dados['Age'].mean()) # Substitui NaN pela media de idade (mean)
dados['Height'].fillna(dados['Height'].mean()) # Substitui NaN pela media de idade (mean)
dados['Weight'].fillna(dados['Weight'].mean()) # Substitui NaN pela media de idade (mean)