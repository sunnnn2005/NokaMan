from __future__ import annotations

from nokaman.eval.metrics import batch_evaluate, placement_test


def test_batch_evaluate() -> None:
    report = batch_evaluate()
    assert report["n_samples"] >= 1
    assert "rows" in report


def test_placement_test() -> None:
    result = placement_test(
        "en",
        [
            "I study English every day and write short notes.",
            "Hello my name is Sam.",
        ],
    )
    assert result["cefr"]
    assert result["n_items"] == 2
