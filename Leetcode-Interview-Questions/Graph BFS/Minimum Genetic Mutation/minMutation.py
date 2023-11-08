def minMutation(startGene, endGene, bank):
    bank_set = set(bank)
    if endGene not in bank_set:
        return -1

    queue = deque([(startGene, 0])
    visited = set()

    while queue:
        current_gene, mutations = queue.popleft()

        if current_gene == endGene:
            return mutations

        for i in range(8):
            for nucleotide in 'ACGT':
                new_gene = current_gene[:i] + nucleotide + current_gene[i+1:]
                if new_gene in bank_set and new_gene not in visited:
                    queue.append((new_gene, mutations + 1))
                    visited.add(new_gene)

    return -1