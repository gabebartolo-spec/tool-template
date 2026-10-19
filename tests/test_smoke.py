import tomllib
from pathlib import Path

import app

ROOT = Path(__file__).resolve().parents[1]


def test_package_imports_with_version():
    assert app.__version__


def test_example_config_has_every_section():
    config = tomllib.loads((ROOT / "config.example.toml").read_text(encoding="utf-8"))
    assert "app" in config
    assert config["app"]["host"] == "127.0.0.1", "the app must bind to localhost only"
