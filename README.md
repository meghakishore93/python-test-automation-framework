# Python Test Automation Framework

A modular **Test Automation Framework** built with **Python, Pytest, and Requests** — designed for **API testing**, with configuration-driven design, logging, and HTML reporting.

---

# Features

✅ Modular folder structure  
✅ YAML-based configuration  
✅ Logging system for traceability  
✅ Pytest fixtures and reusable APIs  
✅ Auto-generated HTML reports  

---

# Tech Stack

| Component | Tool |
|------------|------|
| Test Runner | Pytest |
| API Calls | Requests |
| Config Management | YAML |
| Reporting | Pytest-HTML |
| Logging | Python Logging Module |

---

## Project Structure

python-test-automation-framework/
├── api/
├── config/
├── tests/
├── utils/
├── reports/
└── conftest.py


---

## How to Run

```bash
1. Clone the repo
git clone https://github.com/<your-username>/python-test-automation-framework.git
cd python-test-automation-framework

2. Install dependencies
pip install -r requirements.txt

3. Run tests
pytest -v --html=reports/report.html

4. Reports
* Report will be created in /reports/report.html
* Report will be created in /reports/report.html

# Sample Ouput
tests/test_api_users.py::test_get_users PASSED
tests/test_api_users.py::test_create_user PASSED



