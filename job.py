def ff(part,number_part,proc,number_proc):
	allocation = [-1]*number_proc

	for i in range(number_proc):
		for j in range(number_part):
			if (part[j] >= proc[i] and j not in allocation):
				allocation[i] = j
				break
	
	print("\n\nNo. Processo \tTamanho Processo\tNo. Particao \t Tamanho Particao \tSobra\n")

	for i in range(number_part):
		print(i+1,"\t", proc[i], "\t", allocation[i],"\t", part[allocation[i]],"\t", part[allocation[i] - proc[i])
	return

def bf(part,number_part,proc,number_proc):
	allocation = [-1]*number_proc

	for i in range(number_proc):
		for j in range(number_part):
			if (part[j] >= proc[i] and ): #falta fazer
				allocation[i] = j
				break
	
	print("\n\nNo. Processo \tTamanho Processo\tNo. Particao \t Tamanho Particao \tSobra\n")
	for i in range(number_part):
		print(i+1,"\t", proc[i], "\t", allocation[i],"\t", part[allocation[i]],"\t", part[allocation[i] - proc[i])
	return


def wf(part,number_part,proc,number_proc):
	allocation = [-1]*number_proc

	for i in range(number_proc):
		for j in range(number_part):
			if (part[j] >= proc[i] and ): #falta fazer
				allocation[i] = j
				break
	
	print("\n\nNo. Processo \tTamanho Processo\tNo. Particao \t Tamanho Particao \tSobra\n")
	for i in range(number_part):
		print(i+1,"\t", proc[i], "\t", allocation[i],"\t", part[allocation[i]],"\t", part[allocation[i] - proc[i])
	return


print("\n\tMetodo de Alocacao")
print("\nDefina o numero de particoes")
number_part =  int(input())
print("\nDefina o numero de processos")
number_proc =  int(input())
print("\nDefina o tamanho de cada particao:\n)

part = []
proc = []

for i in range(number_part):
	part.append(int(input()))

print("\nDefina o tamanho de cada processo:\n")

for i in range(number_proc):
	proc.append(int(input()))

ff(part,number_part,proc,number_proc)
bf(part,number_part,proc,number_proc)
wf(part,number_part,proc,number_proc)
	

