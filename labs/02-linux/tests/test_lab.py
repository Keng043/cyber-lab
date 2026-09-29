from pathlib import Path

ROOT = Path(__file__).parents[1]
README = ROOT / "README.md"


def test_lab_files_exist() -> None:
    assert README.is_file()


def test_lab_mentions_core_linux_topics() -> None:
    text = README.read_text(encoding="utf-8")
    for topic in ("permissions", "processes", "network", "least-privileged"):
        assert topic in text
