import sys, pytest
from src.modules.port_scanner import TcpScanner


@pytest.fixture
def tcp_scanner():
    return TcpScanner()

def test_scan_open_port(tcp_scanner):
    target = "8.8.8.8"
    ports = "53"
    report = "Off"

    results = tcp_scanner.scan(target, ports, report)

    assert len(results) == 1
    assert results[0]["port"] == 53
    assert results[0]["open"] is True
    assert results[0]["service"] == 'domain'
    assert results[0]["protocol"] == 'tcp'

def test_scan_close_port(tcp_scanner):
    target = "8.8.8.8"
    ports = "22"
    report = "Off"

    results = tcp_scanner.scan(target, ports, report)

    assert len(results) == 1
    assert results[0]["port"] == 22
    assert results[0]["open"] is False
    assert report == "Off"
