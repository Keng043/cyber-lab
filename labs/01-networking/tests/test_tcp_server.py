from pathlib import Path

ROOT = Path(__file__).parents[1]
SERVER = ROOT / "src" / "tcp_server.py"
CLIENT = ROOT / "src" / "tcp_client.py"
PROBE = ROOT / "src" / "port_probe.py"

def test_server_and_client_exist() -> None:
    assert SERVER.is_file()
    assert CLIENT.is_file()
    assert PROBE.is_file()

def test_probe_stays_localhost() -> None:
    probe_text = PROBE.read_text(encoding="utf-8")
    assert 'HOST = "127.0.0.1"' in probe_text
    assert "connect_ex" in probe_text

def test_lab_uses_localhost_only() -> None:
    server_text = SERVER.read_text(encoding="utf-8")
    client_text = CLIENT.read_text(encoding="utf-8")
    assert 'HOST = "127.0.0.1"' in server_text
    assert 'HOST = "127.0.0.1"' in client_text
