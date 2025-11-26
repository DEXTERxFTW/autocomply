import json
import os

def load_json(filepath):
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return {}
    with open(filepath, 'r') as f:
        return json.load(f)

def compare_configs(standard, baseline_rules, actual_config):
    print(f"\nCompliance Check: {standard}")
    print("-" * 50)

    total_checks = 0
    passed_checks = 0

    report_lines = [f"# AutoComply Report: {standard}", ""]

    for key, rule in baseline_rules.items():
        expected_value = rule["expected"]
        severity = rule.get("severity", "LOW").upper()
        actual_value = str(actual_config.get(key))

        total_checks += 1

        if actual_value == expected_value:
            status = "PASS"
            passed_checks += 1
            print(f"{status} - {key}: {actual_value}")
        else:
            status = "FAIL"
            print(f"{status} - {key} [{severity}]: Found '{actual_value}', expected '{expected_value}'")

        report_lines.append(
            f"- **{key}** [{severity}] → `{status}`: Found `{actual_value}`, expected `{expected_value}`"
        )

    score = (passed_checks / total_checks) * 100
    report_lines.insert(1, f"**Compliance Score:** `{score:.2f}%`")

    with open("report.md", "w", encoding="utf-8") as f:
        f.write("\n".join(report_lines))

    print(f"\nCompliance Score: {score:.2f}%")
    print("Report saved to report.md")

def main():
    # Use the script's directory as the base path to locate resources consistently
    base_dir = os.path.dirname(os.path.abspath(__file__))

    available_standards = {
        "nist": os.path.join(base_dir, "baselines", "nist_baseline.json"),
        "hipaa": os.path.join(base_dir, "baselines", "hipaa_baseline.json"),
        "pci": os.path.join(base_dir, "baselines", "pci_baseline.json")
    }

    print("Choose a compliance standard:")
    for name in available_standards:
        print(f"- {name}")

    standard = input("Standard: ").lower()
    if standard not in available_standards:
        print(f"Unsupported standard '{standard}'.")
        return

    baseline_path = available_standards[standard]
    config_path = os.path.join(base_dir, "scans", "sample_env_config.json")

    baseline_data = load_json(baseline_path)
    actual_data = load_json(config_path)

    if "rules" not in baseline_data:
        print("Invalid baseline format. Expected a 'rules' key.")
        return

    compare_configs(standard.upper(), baseline_data["rules"], actual_data)

if __name__ == "__main__":
    main()
