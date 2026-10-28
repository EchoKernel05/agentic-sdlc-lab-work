---
description: "Use when creating or changing tests under tests/. Covers unit-test boundaries, test naming, behavior focus, and regression-test safeguards."
applyTo: "tests/**"
---
# Test Instructions

- Unit tests call service functions directly with `MagicMock` repositories; do not use a database or HTTP client.
- Test one behavior per test.
- Name tests `test_<function>_<situation>`.
- For a bug fix, first add a test that fails on the current code.
- Never weaken or delete an existing assertion. Stop and ask before making a change that would require doing so.
