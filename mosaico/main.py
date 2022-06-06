'''
         Trabalho: Mosaico de Imagens
    Desenvolvedor: Geffté Luis de Souza Caetano
         Objetivo: Ler linhas com quatro informações que viram a formar um retangulo.
                   Posteriormente 'printar' o menor retangulo no qual os cabem os demais. 
                   A estratégia utilizada é abrir um .txt com as diversas coordenadas e comparar 
                   uns com os outros.
'''
# Aqui abre o arquivo e le as linhas do .txt para fazer a comparação, onde o "arquivo.txt"
# irá ser interpretado como 'file'. A função with permite abrir e fechar o tal arquivo para
# não haver espaço desperdiçado na memória.
with open('arquivo.txt', 'r') as file: 
    # Importante! Aqui ocorre o instanciamento das variaveis que serão as coordenadas
    # do retângulo final, e é necessário que sejam instanciadas com a primeira linha 
    # para ser comparada com as demais depois.
    xseFinal, yseFinal, xidFinal, yidFinal = map(int, file.readline().split())
    # Nesta parte, há a leitura de cada linha do arquivo pela variável line, com a 
    # finalidade de as comparar. 
    for line in file:
        # Ocorre a leitura dos respectivos dados das linhas do arquivo e armazenamento
        # nas variaveis de comparação, onde eles serão usadas para como auxilio para verificar
        # se há intersecção entre triângulos. 
        xse, yse, xid, yid= map(int, line.split())
        # Verificação se houve aumento no tamanho do retângulo em suas lateralidades no 
        # plano cartesiano. 
        xseFinal = min(xse,xseFinal)
        xidFinal = max(xid,xidFinal)
        yidFinal = min(yid,yidFinal)
        yseFinal = max(yse,yseFinal)
#Imprimndo as coordenadas:
print(f"Coordenadas canto superior esquerdo: | ({xseFinal},{yseFinal}) |")
print(f"Coordenadas canto inferior direito:  | ({xidFinal},{yidFinal}) |")