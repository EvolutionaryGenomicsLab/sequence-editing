# Author: Maria Luiza Andreani

import re # importa as expressões recursivas

file = open('teste_genbank2.fasta','r') #abre o file que vc quer editar
result= open('teste_editado.fasta','r+') #cria ou abre o destino

for line in file: #isso aqui vai pegar cada linha e aplicar o que tiver 
	line = line.rstrip() #tira os espaços
	if 'cf' in line: #if loop
		match = re.search('(\w+)\.(\d+) (\w+) (\w+) (\w+\.) (\w+).+',line)
		match2= re.search('(\w+\.\d+) (\w+) (\w+\.) (\w+)', line)
		if match :
			result.write('>'+ str(match.group(3)) + '_' + str(match.group(4))+ '_' + str(match.group(5)) + '_' + str(match.group(6)) + '_' + str(match.group(1)) + '_' + str(match.group(2)) + '\n') # escrevendo no destino, /n pq ele foi removido
		if match2:
			result.write('>' + str(match2.group(2))+ '_' + str(match2.group(3))+ '_' + str(match2.group(4))+ '_' + str(match2.group(1)) + '\n')# mesma coisa
	else: #se a condição colocada pelo if não é cumprida
		if '>' in line: #pra pegar os headers que sobram
			notcf= re.search('(\w+\.\d+) (\w+) (\w+)',line)
			if notcf:
				result.write('>'+ str(notcf.group(2)) +'_' + str(notcf.group(3))+ '_' + str(notcf.group(1)) + '\n')

		else: #pra pegar as sequencias msm
			result.write(line +'\n')	

result.close() #fecha o arquivo de leitura
file.close() #fecha o arquivo destino
