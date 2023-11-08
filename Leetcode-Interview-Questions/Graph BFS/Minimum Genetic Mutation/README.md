## Minimum Genetic Mutation

### Question

A gene string can be represented by an 8-character long string, with choices from *'A', 'C', 'G',* and *'T'*.

Suppose we need to investigate a mutation from a gene string *startGene* to a gene string *endGene* where one mutation is defined as one single character changed in the gene string.

- For example, *"AAXXGGTT" --> "AACCGGTA"* is one mutation.

There is also a gene bank *bank* that records all the valid gene mutations. A gene must be in *bank* to make it a valid gene string.

Given the two gene strings *startGene* and *endGene* and gene bank *bank*, return the minimum number of mutations needed to mutate from *startGene* to *endGene*. If there is no such a mutation, return *-1*.

Note that the starting point is assumed to be valid, so it might not be included in the bank.

#### Implementation

Create a set *bankSet* to store the valid genes from the *bank* list for efficient lookup.

Initialize a queue for BFS and push the *startGene* into it.

Initialize a variable *mutations* to keep track of the number of mutations needed, initially set to 0.

While the queue is not empty, perform the following steps:

    a. Get the current gene from the front of the queue.

    b. Check if the current gene is equal to endGene. If it is, return the current value of mutations as the minimum number of mutations.
    
    c. Otherwise, iterate through all possible mutations of the current gene (changing one character at a time) and check if they are valid (in bank_set) and not visited. If so, add them to the queue and mark them as visited.

    d. Increment mutations by 1 for each level of BFS.

If you exhaust all possibilities and cannot reach *endGene*, return -1, indicating that it's impossible to reach *endGene* from *startGene* using valid mutations.