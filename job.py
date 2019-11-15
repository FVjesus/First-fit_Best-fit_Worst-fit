def ff(part, number_part, proc, number_proc):
    allocation = [-1]*number_proc

    for i in range(number_proc):
        for j in range(number_part):
            if(part[j] >= proc[i] and j not in allocation):
                allocation[i] = j
                break
    
    print("\n\t\tFirst - fit solution")
    print("\nNo. Processo \tTamanho Processo\tNo. Particao \t Tamanho Particao \tSobra\n")

    for i in range(number_proc):
        if(allocation[i] == -1):
                print((i+1), "\t", proc[i], "\t", "\tEm espera...")
        else:
            print((i+1), "\t", proc[i], "\t", (allocation[i] + 1), "\t",part[allocation[i]], "\t", (part[allocation[i]] - proc[i]))
    return

def bf(part, number_part, proc, number_proc):
    allocation = [-1]*number_proc

    for i in range(number_proc):
        bestIdx = -1
        for j in range(number_proc):
            if(part[j] >= proc[i] and j not in allocation):
                if(bestIdx == -1):
                    bestIdx = j
                elif (part[bestIdx] > part[j]):
                    bestIdx = j
        allocation[i] = bestIdx

    print("\n\t\tBest - fit solution")
    print("\nNo. Processo \tTamanho Processo\tNo. Particao \t Tamanho Particao \tSobra\n")

    for i in range(number_proc):
        if(allocation[i] == -1):
            print((i+1), "\t", proc[i], "\t", "\tEm espera...")
        else:
            print((i+1), "\t", proc[i], "\t", (allocation[i] + 1), "\t",part[allocation[i]], "\t", (part[allocation[i]] - proc[i]))
    
    return

def wf(part, number_part, proc, number_proc):
    allocation = [-1]*number_proc

    for i in range(number_proc):
        worstIdx = -1
        for j in range(number_proc):
            if(part[j] >= proc[i] and j not in allocation):
                if(worstIdx == -1):
                    worstIdx = j
                elif (part[worstIdx] < part[j]):
                    worstIdx = j
        allocation[i] = worstIdx

    print("\n\t\tWorst - fit solution")
    print("\nNo. Processo \tTamanho Processo\tNo. Particao \t Tamanho Particao \tSobra\n")

    for i in range(number_proc):
        if(allocation[i] == -1):
            print((i+1), "\t", proc[i], "\t", "\tEm espera...")
        else:
            print((i+1), "\t", proc[i], "\t", (allocation[i] + 1), "\t",part[allocation[i]], "\t", (part[allocation[i]] - proc[i]))
    
    return


def main():

    print("\n\tMetodos de Alocacao")
    print("\nDefina o numero de particoes")
    number_part =  int(input())
    print("\nDefina o numero de processos")
    number_proc =  int(input())
    print("\nDefina o tamanho de cada particao:\n")

    part = []
    proc = []

    for i in range(number_part):
        print("Particao No. ",i+1)
        part.append(int(input()))
    
    print("\nDefina o tamanho de cada processo:\n")

    for i in range(number_proc):
        print("Porcesso No. ",i+1)
        proc.append(int(input()))
    
    ff(part.copy(),number_part,proc.copy(),number_proc)
    bf(part.copy(),number_part,proc.copy(),number_proc)
    wf(part.copy(),number_part,proc.copy(),number_proc)

main()