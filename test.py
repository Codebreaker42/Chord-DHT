from chord import Chord
from dht import DHT

def test_chord_ring():
    # Initialize a Chord ring with a 3-bit identifier space for simplicity
    chord = Chord(bits=3)
    # print(chord.bits)
    # Add nodes to the ring
    node_ids = [1, 3, 2,10,12,8,5,9,11]
    for node_id in node_ids:
        chord.add_node(node_id)
    
    # Check node relationships
    for node in chord.nodes:
        print(f"Node ID: {node.node_id}")
        print(f"Successor: {node.successor.node_id}")
        print(f"Predecessor: {node.predecessor.node_id}")
        # print(f"Finger Table: {[n.node_id if n else None for n in node.finger_table]}")
        # print('-' * 30)
    dht= DHT(chord)
    # dht.put("fruit","apple")
    # print(dht.get("fruit"))
    chord.remove_node(1)

    for node in chord.nodes:
        print(f"Node ID: {node.node_id}")
        print(f"Successor: {node.successor.node_id}")
        print(f"Predecessor: {node.predecessor.node_id}")
    
    for node in chord.nodes:
        print(f"Node ID: {node.node_id}")
        print(f"Successor: {node.successor.node_id}")
        print(f"Predecessor: {node.predecessor.node_id}")
        print(f"Finger Table: {[n.node_id if n else None for n in node.finger_table]}")
        print('-' * 30)


def test_data_storage():
    # Initialize a Chord ring with a larger identifier space
    chord = Chord(bits=4)
    node_ids = [2, 5, 8, 12]
    for node_id in node_ids:
        chord.add_node(node_id)
    
    # Store data in the ring
    chord.nodes[0].store_data("key1", "value1")
    chord.nodes[1].store_data("key2", "value2")
    
    # Test data retrieval
    for node in chord.nodes:
        data1 = node.lookup_data("key1")
        data2 = node.lookup_data("key2")
        print(f"Node ID: {node.node_id}")
        print(f"Data for 'key1': {data1}")
        print(f"Data for 'key2': {data2}")
        print('-' * 30)

if __name__ == "__main__":
    print("=== Testing Chord Ring ===")
    test_chord_ring()
    
    # print("=== Testing Data Storage and Retrieval ===")
    # test_data_storage()
