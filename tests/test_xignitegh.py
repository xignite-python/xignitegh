import pytest
import xignitegh as xgh


def test_hallo(capsys):
    xgh.hallo("Sam")
    captured = capsys.readouterr()
    assert "Sam" in captured.out
