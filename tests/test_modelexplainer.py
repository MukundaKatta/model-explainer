"""Tests for ModelExplainer."""
import pytest
from src.modelexplainer import ModelExplainer

def test_init():
    obj = ModelExplainer()
    stats = obj.get_stats()
    assert stats["total_ops"] == 0

def test_operation():
    obj = ModelExplainer()
    result = obj.explain_prediction(input="test")
    assert result["processed"] is True
    assert result["operation"] == "explain_prediction"

def test_multiple_ops():
    obj = ModelExplainer()
    for m in ['explain_prediction', 'compute_shap', 'compute_lime']:
        getattr(obj, m)(data="test")
    assert obj.get_stats()["total_ops"] == 3

def test_caching():
    obj = ModelExplainer()
    r1 = obj.explain_prediction(key="same")
    r2 = obj.explain_prediction(key="same")
    assert r2.get("cached") is True

def test_reset():
    obj = ModelExplainer()
    obj.explain_prediction()
    obj.reset()
    assert obj.get_stats()["total_ops"] == 0

def test_stats():
    obj = ModelExplainer()
    obj.explain_prediction(x=1)
    obj.compute_shap(y=2)
    stats = obj.get_stats()
    assert stats["total_ops"] == 2
    assert "ops_by_type" in stats
