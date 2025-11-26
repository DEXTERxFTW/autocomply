# AutoComply

**Automated Configuration Drift & Cybersecurity Compliance Checker**

AutoComply is a lightweight, CLI-based tool designed to scan system or application environment configurations against major cybersecurity compliance standards like **NIST**, **HIPAA**, and **PCI-DSS**. It detects configuration drift, flags non-compliant settings, and generates a Markdown report with a compliance score and severity levels.

---

## 🚀 Features

- ✅ Supports multiple compliance standards (NIST, HIPAA, PCI-DSS)
- 📊 Generates detailed Markdown reports with:
  - PASS/FAIL status
  - Compliance Score (in %)
  - Severity levels: HIGH / MEDIUM / LOW
- 🔁 Easy to extend with new rules and standards
- 📁 JSON-based rule definitions

---

## 📁 Project Structure

```

autocomply/
├── src/
│   ├── scanner.py              # Main script
│   └── __init__.py
├── report.md                   # Generated compliance report
├── scans/
│   └── sample\_env\_config.json  # Input environment config (to scan)
└── baselines/
├── nist\_baseline.json
├── hipaa\_baseline.json
└── pci\_baseline.json


````

---

## 🛠️ How It Works

1. You provide a system/environment configuration as a JSON file.
2. Select a compliance standard (NIST, HIPAA, PCI).
3. AutoComply compares your config against that standard’s baseline.
4. Generates a `report.md` with results, score, and severity levels.
---

## 🧪 Example Usage

You can run the tool interactively or by passing arguments.

**Interactive Mode:**
```bash
python src/scanner.py
```

**Automated Mode (CLI Arguments):**
```bash
python src/scanner.py --standard nist
python src/scanner.py --standard pci --config /path/to/my_config.json
```

**Arguments:**
- `-s`, `--standard`: Specify compliance standard (`nist`, `hipaa`, `pci`).
- `-c`, `--config`: Specify path to a custom JSON config file.

---

View the output in your terminal and in `report.md`.

---

## 🐳 Docker Usage

You can run AutoComply using Docker to ensure a consistent environment without needing to install Python or manage dependencies directly.

#### 1. Build the Docker Image

Navigate to the root of the project and build the Docker image:

```bash
docker build -t autocomply .
```

#### 2. Run the Docker Container

Run the tool in an interactive container, mounting your current directory to access the generated `report.md`:

```bash
docker run -it -v $(pwd):/app autocomply
```

Follow the prompts to choose a compliance standard. The `report.md` will be saved in your project's root directory.

---

## 📄 Sample Baseline Rule

```json
"USE_SSL": {
  "expected": "True",
  "severity": "HIGH"
}
```

---

## ✅ Example Config (`scans/sample_env_config.json`)

```json
{
  "DEBUG": "False",
  "USE_SSL": "True",
  "SECURE_HSTS_SECONDS": "11100000",
  "ALLOWED_HOSTS": ["localhost", "127.0.0.1"],
  "SESSION_COOKIE_SECURE": "True",
  "CSRF_COOKIE_SECURE": "False",
  "ENCRYPTED_STORAGE": "True",
  "AUDIT_LOGGING_ENABLED": "True",
  "SESSION_TIMEOUT": "15",
  "ACCESS_CONTROL_ENFORCED": "True",
  "BACKUP_ENABLED": "True",
  "TWO_FACTOR_AUTH": "True",
  "CARD_DATA_ENCRYPTED": "True",
  "LOGGING_ENABLED": "True",
  "FIREWALL_ENABLED": "True",
  "DEFAULT_PASSWORDS_CHANGED": "True",
  "ACCESS_RESTRICTED": "True",
  "PATCHING_UP_TO_DATE": "True"
}
```


## 💡 Extend It

To add your own standard or modify rules, edit files inside the `baselines/` folder. Each rule must include:

* `expected`: expected value
* `severity`: LOW / MEDIUM / HIGH

---

## 📚 Standards Covered

* [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)
* [HIPAA Security Rule](https://www.hhs.gov/hipaa/)
* [PCI-DSS](https://www.pcisecuritystandards.org/)

---

## 🔒 Disclaimer

AutoComply is for educational and prototype/demo purposes. Always consult security professionals before relying on automated tools for compliance in production environments.

---

## 👨‍💻 Author

Built by a cybersecurity enthusiast interested in malware analysis, reverse engineering, and secure system design.

