from nokaman.models.toy import ToyAbilityModel
from nokaman.eval.pipeline import evaluate_demo


def test_en_framework_bands() -> None:
    r = ToyAbilityModel("en").score_text(
        "Although remote work is common, hybrid schedules help collaboration.",
        skill="writing",
    )
    assert "framework_bands" in r
    assert "ielts_approx" in r["framework_bands"]


def test_demo_includes_frameworks() -> None:
    d = evaluate_demo("ja")
    assert "framework_bands" in d
    assert d["framework_bands"].get("jlpt")
