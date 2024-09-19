# Defining the network topology
network_topology = {
    'nodes': [
        {'id': 'R1', 'type': 'router'},
        {'id': 'R2', 'type': 'router'},
        {'id': 'S1', 'type': 'switch'},
        {'id': 'H1', 'type': 'host'},
        {'id': 'H2', 'type': 'host'}
    ],
    'edges': [
        {'from': 'R1', 'to': 'S1', 'cost': 1},
        {'from': 'R1', 'to': 'R2', 'cost': 2},
        {'from': 'R2', 'to': 'S1', 'cost': 3},
        {'from': 'S1', 'to': 'H1', 'cost': 1},
        {'from': 'S1', 'to': 'H2', 'cost': 2}
    ]
}