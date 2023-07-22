def hIndex(citations):
    citations.sort(reverse=True)

    h_index = 0

    for i, citation in enumerate(citations):
        if citations >= i + 1:
            h_index += 1
        else:
            break
    return h_index
