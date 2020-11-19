# -*- coding: utf-8 -*-
"""Data Science - Introdução a Testes.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lwVl1eBctYU88rN8sjDqvzk48ipZhOJs
"""

import pandas as pd

tmdb = pd.read_csv("tmdb_5000_movies.csv")
tmdb.head()

tmdb.describe()

import seaborn as sns

ax = sns.distplot(tmdb.vote_average)
ax.set(xlabel="Nota média", ylabel="Densidade")
ax.set_title("Média de votos em filmes no TMDB 5000")

import seaborn as sns

ax = sns.distplot(tmdb.vote_average, norm_hist = False, kde = False)
ax.set(xlabel="Nota média", ylabel="Frequência")
ax.set_title("Média de votos em filmes no TMDB 5000")

ax = sns.boxplot(x=tmdb.vote_average)
ax.set(xlabel="Nota média do filme")
ax.set_title("Distribuição de nota média dos filmes do TMDB 5000")

"""Tem algo de estranho com meus dados... não faz sentido filmes cuja nota média é 0 ou 10.... vamos ver?"""

tmdb.query("vote_average == 0").head()

tmdb.query("vote_average==10").head()

"""Detectamos que alguns filmes tiveram poucos votos (ou até mesmo nenhum voto). Decidimos que esses filmes não devem pertencer a nossa análise"""

tmdb_com_mais_de_10_votos = tmdb.query("vote_count >= 10")
tmdb_com_mais_de_10_votos.describe()

ax = sns.distplot(tmdb_com_mais_de_10_votos.vote_average, norm_hist = False, kde = False)
ax.set(xlabel="Nota média", ylabel="Frequência")
ax.set_title("Média de votos em filmes no TMDB 5000 dentre os filmes com 10 ou mais votos")

ax = sns.distplot(tmdb_com_mais_de_10_votos.vote_average)
ax.set(xlabel="Nota média", ylabel="Densidade")
ax.set_title("Média de votos em filmes no TMDB 5000 dentre os filmes com 10 ou mais votos")

ax = sns.distplot(tmdb_com_mais_de_10_votos.vote_average,
                          hist_kws = {'cumulative':True},
                          kde_kws = {'cumulative':True})
ax.set(xlabel="Nota média", ylabel="% acumulada de filmes")
ax.set_title("Média de votos em filmes no TMDB 5000 com 10 ou mais votos")

ax = sns.boxplot(x=tmdb_com_mais_de_10_votos.vote_average)
ax.set(xlabel="Nota média do filme")
ax.set_title("Distribuição de nota média dos filmes do TMDB 5000 dentre os filmes com 10 ou mais votos")

"""# Analisaremos também o movielens"""

notas = pd.read_csv("ratings.csv")
notas.head()

nota_media_por_filme = notas.groupby("movieId").mean()["rating"]
nota_media_por_filme.head()

ax = sns.distplot(nota_media_por_filme.values)
ax.set(xlabel="Nota média", ylabel="Densidade")
ax.set_title("Média de votos em filmes no Movielens 100k")

quantidade_de_votos_por_filme = notas.groupby("movieId").count()
filmes_com_pelo_menos_10_votos = quantidade_de_votos_por_filme.query("rating >= 10").index
filmes_com_pelo_menos_10_votos.values

nota_media_dos_filmes_com_pelo_menos_10_votos = nota_media_por_filme.loc[filmes_com_pelo_menos_10_votos.values]
nota_media_dos_filmes_com_pelo_menos_10_votos.head()

ax = sns.distplot(nota_media_dos_filmes_com_pelo_menos_10_votos.values)
ax.set(xlabel="Nota média", ylabel="Densidade")
ax.set_title("Média de votos em filmes no Movielens 100k com 10 ou mais votos")

ax = sns.distplot(nota_media_dos_filmes_com_pelo_menos_10_votos.values,
                          hist_kws = {'cumulative':True},
                          kde_kws = {'cumulative':True})
ax.set(xlabel="Nota média", ylabel="% acumulada de filmes")
ax.set_title("Média de votos em filmes no Movielens 100k com 10 ou mais votos")

ax = sns.boxplot(x=nota_media_dos_filmes_com_pelo_menos_10_votos.values)
ax.set(xlabel="Nota média do filme")
ax.set_title("Distribuição de nota média dos filmes do MovieLens 100k dentre os filmes com 10 ou mais votos")

"""# Analisando a distribuição dos dados capturados de outros campos do TMDB"""

ax = sns.distplot(tmdb_com_mais_de_10_votos.vote_count)
ax.set(xlabel="Número de votos", ylabel="Densidade")
ax.set_title("Número de votos em filmes no TMDB 5000 com 10 ou mais votos")

ax = sns.distplot(tmdb.query("budget > 0").budget)
ax.set(xlabel="Budget (gastos)", ylabel="Densidade")
ax.set_title("Gastos em filmes no TMDB 5000")

ax = sns.distplot(tmdb.popularity)
ax.set(xlabel="Popularidade", ylabel="Densidade")
ax.set_title("Popularidade em filmes no TMDB 5000")

ax = sns.distplot(tmdb.runtime)
ax.set(xlabel="Tempo de duração", ylabel="Densidade")
ax.set_title("Tempo de duração em filmes no TMDB 5000")

tmdb.runtime.isnull().sum()

ax = sns.distplot(tmdb.query("runtime>0").runtime.dropna())
ax.set(xlabel="Tempo de duração", ylabel="Densidade")
ax.set_title("Tempo de duração em filmes no TMDB 5000")

ax = sns.distplot(tmdb.query("runtime>0").runtime.dropna(),
                 hist_kws={'cumulative': True},
                 kde_kws={'cumulative': True}
                 )
ax.set(xlabel="Tempo de duração", ylabel="% de filmes")
ax.set_title("Tempo de duração em filmes no TMDB 5000")

tmdb.query("runtime>0").runtime.dropna().quantile(0.8)

"""# Movielens: média dos filmes com pelo menos 10 votos"""

print("Média dos filmes com pelo menos 10 votos", nota_media_dos_filmes_com_pelo_menos_10_votos.mean())

import matplotlib.pyplot as plt
import numpy as np

np.random.seed(75243)
temp = nota_media_dos_filmes_com_pelo_menos_10_votos.sample(frac=1)

medias = [temp[0:i].mean() for i in range(1, len(temp))]

plt.plot(medias)

from statsmodels.stats.weightstats import zconfint

zconfint(nota_media_dos_filmes_com_pelo_menos_10_votos)

from statsmodels.stats.weightstats import DescrStatsW

descr_todos_com_10_votos = DescrStatsW(nota_media_dos_filmes_com_pelo_menos_10_votos)
descr_todos_com_10_votos.tconfint_mean()

"""# Vamos ver o filme 1..."""

filmes = pd.read_csv("movies.csv")
filmes.query("movieId==1")

notas1 = notas.query("movieId == 1")
notas1.head()

ax = sns.distplot(notas1.rating)
ax.set(xlabel="Nota", ylabel="Densidade")
ax.set_title("Distribuição das notas para o Toy Story")

ax = sns.boxplot(notas1.rating)
ax.set(xlabel="Nota")
ax.set_title("Distribuição das notas para o Toy Story")

notas1.rating.mean()

notas1.rating.count()

zconfint(notas1.rating)

from statsmodels.stats.weightstats import ztest

ztest(notas1.rating, value = 3.4320503405352594)

np.random.seed(75241)
temp = notas1.sample(frac=1).rating

def calcula_teste(i):
  media = temp[0:i].mean()
  stat, p = ztest(temp[0:i], value = 3.4320503405352594)
  return (i,media, p)

valores = np.array([calcula_teste(i) for i in range(2, len(temp))])

plt.plot(valores[:,0], valores[:,1])
plt.plot(valores[:,0], valores[:,2])
plt.hlines(y = 0.05, xmin = 2, xmax = len(temp), colors='r')

valores

