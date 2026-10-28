**Goal:** Refuse cancellation of a DELIVERED order: `POST /orders/{id}/cancel` must respond with HTTP 400 and leave the order unchanged.
**Context:** `cancel_order` currently only refuses an already-CANCELLED order, although `OrderStateMachine` treats DELIVERED as terminal. The cancel route maps `OrderOwnershipError` to HTTP 400 and delegates cancellation, including invoice handling, to the orders service.
**In scope:** Add delivered-order refusal to the order cancellation behavior and focused regression coverage for the service/API behavior. Preserve the existing response behavior for other order states.
**Out of scope:** Changes to unrelated order behavior or modules; `alembic/`, `.github/`, `pyproject.toml`, and any new dependency.
**Acceptance:**
- A test creates or mocks an owned order with status DELIVERED and calls `POST /orders/{id}/cancel`; the response status is 400.
- The refusal does not change the order status or commit an order cancellation.
- The refusal does not cancel the order's associated invoice.
- Regression tests confirm existing supported cancellation behavior and the existing 404 response for a missing order remain unchanged.
**Stop and ask a human if:** The requested 400 response conflicts with established API conventions, or enforcing the refusal would require changing cancellation behavior for order states other than DELIVERED.
**Reviewer:** Orders module maintainer.
