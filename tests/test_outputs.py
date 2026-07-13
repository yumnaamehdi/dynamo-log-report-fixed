import json
from pathlib import Path

REPORT_PATH = Path("/app/report.json")
EXPECTED_KEYS = {"total_requests", "unique_ips", "top_path"}

def load_report():
try:
return json.loads(REPORT_PATH.read_text(encoding="utf-8"))
except FileNotFoundError as exc:
raise AssertionError("/app/report.json was not created") from exc
except UnicodeDecodeError as exc:
raise AssertionError(
"/app/report.json must be encoded as valid UTF-8"
) from exc
except json.JSONDecodeError as exc:
raise AssertionError(
"/app/report.json must contain valid JSON"
) from exc

def test_success_criterion_1_output_file_and_format():
"""
Verifies instruction.md success criterion:
Create /app/report.json as a valid UTF-8 JSON object containing exactly
total_requests, unique_ips, and top_path.
"""
report = load_report()

```
assert isinstance(report, dict), (
    "/app/report.json must contain a JSON object"
)
assert set(report.keys()) == EXPECTED_KEYS, (
    "/app/report.json must contain exactly the keys "
    "total_requests, unique_ips, and top_path"
)
```

def test_success_criterion_2_total_requests():
"""
Verifies instruction.md success criterion:
total_requests must equal the number of non-empty log entries.
"""
report = load_report()

```
assert report["total_requests"] == 6, (
    "total_requests must be 6"
)
assert type(report["total_requests"]) is int, (
    "total_requests must be a JSON integer"
)
```

def test_success_criterion_3_unique_ips():
"""
Verifies instruction.md success criterion:
unique_ips must equal the number of distinct client IP addresses.
"""
report = load_report()

```
assert report["unique_ips"] == 3, (
    "unique_ips must be 3"
)
assert type(report["unique_ips"]) is int, (
    "unique_ips must be a JSON integer"
)
```

def test_success_criterion_4_top_path():
"""
Verifies instruction.md success criterion:
top_path must be the most frequently requested URL path.
"""
report = load_report()

```
assert report["top_path"] == "/index.html", (
    "top_path must be /index.html"
)
assert isinstance(report["top_path"], str), (
    "top_path must be a JSON string"
)
```
