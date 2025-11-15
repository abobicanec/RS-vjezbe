import heapq

def dijkstra(graph, start):
    udaljenosti = {node: float('inf') for node in graph}
    udaljenosti[start] = 0

    heap = [(0, start)]

    while heap:
        trenutna_udaljenost, trenutni_cvor = heapq.heappop(heap)

        if trenutna_udaljenost > udaljenosti[trenutni_cvor]:
            continue

        for susjed, tezina in graph.get(trenutni_cvor, []):
            udaljenost_do_susjeda = trenutna_udaljenost + tezina
            if udaljenost_do_susjeda < udaljenosti[susjed]:
                udaljenosti[susjed] = udaljenost_do_susjeda
                heapq.heappush(heap, (udaljenost_do_susjeda, susjed))

    return udaljenosti

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

print(dijkstra(graph, 'A'))