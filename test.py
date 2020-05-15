import operator

clients = {'Aldrich': 1.97,
           'Enrico': 8.49,
           'Christoper': 9.79,
           'Cherice': 8.53,
           'Margi': 0.43}

clients_sort = sorted(clients.items(), key=operator.itemgetter(1), reverse=True)

for name in enumerate(clients_sort):
    print(name)
    print(name[1][0], 'has spend', name[1][1])