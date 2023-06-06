# Author: Lucas Freitas

arquivo = open("/dados/genomas/arquivo.transcripts.fasta", "r")
dic_fasta = {}
for line in arquivo:
	line = line.rstrip()
	if line.startswith(">"):
		key_name = line[1:]
		dic_fasta[key_name] = ""
	else:
		dic_fasta[key_name] = dic_fasta[key_name] + str(line)

for key, value in dic_fasta.items():
	if key == "sequenciaencontrada":
		print(">" + str(key) + "\n" + str(value[120:2000]) + "\n")
		print(">"+ str(key) + "\n" + str(value[2044:2153]) + "\n")
	elif key == "sequenciaencontrada":
		print(">"+ str(key) + "\n" + str(value[14:80]) + "\n")
	else:
		pass

  # """
