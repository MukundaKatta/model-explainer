"""CLI for model-explainer."""
import sys, json, argparse
from .core import ModelExplainer

def main():
    parser = argparse.ArgumentParser(description="Explain any AI model prediction with SHAP, LIME, and attention visualization")
    parser.add_argument("command", nargs="?", default="status", choices=["status", "run", "info"])
    parser.add_argument("--input", "-i", default="")
    args = parser.parse_args()
    instance = ModelExplainer()
    if args.command == "status":
        print(json.dumps(instance.get_stats(), indent=2))
    elif args.command == "run":
        print(json.dumps(instance.track(input=args.input or "test"), indent=2, default=str))
    elif args.command == "info":
        print(f"model-explainer v0.1.0 — Explain any AI model prediction with SHAP, LIME, and attention visualization")

if __name__ == "__main__":
    main()
