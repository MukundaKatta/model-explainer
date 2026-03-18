"""Tests for ModelExplainer."""
from src.core import ModelExplainer
def test_init(): assert ModelExplainer().get_stats()["ops"] == 0
def test_op(): c = ModelExplainer(); c.track(x=1); assert c.get_stats()["ops"] == 1
def test_multi(): c = ModelExplainer(); [c.track() for _ in range(5)]; assert c.get_stats()["ops"] == 5
def test_reset(): c = ModelExplainer(); c.track(); c.reset(); assert c.get_stats()["ops"] == 0
def test_service_name(): c = ModelExplainer(); r = c.track(); assert r["service"] == "model-explainer"
