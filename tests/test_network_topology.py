import sys, pytest
from src.modules.network_topology import NetworkTopology

@pytest.fixture
def networkTopology():
    return NetworkTopology()

def test_scan_topology(networkTopology):
    target = "192.168.100.1/24"


    results = networkTopology.scan_network(target)

    # No assertion for testing.
