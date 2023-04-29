from pandas_datareader import data as web
import yfinance as yf

yf.pdr_override()

import matplotlib.pyplot as plt

empresas = [ 'ABEV3','BRAP4','BRKM5','BRML3','CMIG4','CPFE3',
            'CSAN3','CSNA3','EGIE3','EMBR3','ENEV3','EQTL3','EZTC3',
            'FLRY3','GOLL4','ITSA4','JBSS3','LCAM3','MRFG3','MRVE3',
            'MULT3','PCAR3','PETR4','PRIO3','QUAL3','SBSP3','SUZB3',
            'USIM5','VIVT3'
           ]

# cotacao_bovespa = web.get_data_yahoo('^BVSP', start = '2021-03-30', end='2021-07-01')
# print (cotacao_bovespa)
# cotacao_bovespa = cotacao_bovespa["Adj Close"].plot()
# #plt.imshow(img.reshape((28,28)))
# plt.show()

cotacoes = {}
for empresa in empresas:
    cotacao = web.DataReader(f'{empresa}.SA', start = '2021-01-01', end='2022-01-01')

    #for empresa in cotacoes_df["Empresa"].unique():
    cotacoes[empresa] = cotacao

print (cotacoes)




# for empresa in empresas:
#     cotacao = web.get_data_yahoo(f'{empresa}.SA', start = '2021-03-30', end='2021-07-01')
#     print (cotacao)
#     cotacao = cotacao["Adj Close"].plot()
#     #plt.imshow(img.reshape((28,28)))
#     print(empresa)
#     plt.show()
#     print('#'*10)