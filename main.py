import pandas as pd

def mediana(lista):
  tamanho_lista = len(lista)
  lista.sort()
  if tamanho_lista % 2 == 0:
    mediana1 = lista[tamanho_lista // 2]
    mediana2 = lista[tamanho_lista//2 - 1]
    mediana = (mediana1 + mediana2) / 2
  else: 
    mediana = lista[tamanho_lista//2]
  return mediana

def retorna_nome_coluna_formatado(nome_coluna):
  fatia_1 = nome_coluna.split('.')
  posicao_final = fatia_1[1].find('1')
  string = fatia_1[1]
  if(posicao_final != -1):
    nome_formatado = string[:posicao_final].strip()
  else:
    nome_formatado = string.strip()
  return nome_formatado


nome_colunas = []
tabela = pd.read_csv('Breast_cancer.csv',sep=",")
for i,nome_coluna in enumerate(list(tabela.columns)):
  if(i==0):
    pass
  else:
    nome_colunas.append(nome_coluna)
 
for nome_coluna in nome_colunas:
  valores_coluna = []
  for numero_linha,dado in enumerate(tabela[nome_coluna]):
    valores_coluna.append(dado) 
    break
  nome_coluna = retorna_nome_coluna_formatado(nome_coluna)
  print(f"Mediana da coluna '{nome_coluna}' é {mediana(valores_coluna)}")

  
    
    



        

      


  
    

    
  
        
      


  
  
  
    


