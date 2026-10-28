**Goal:** Add `POST /payment/refund/{order_id}` to refund a paid invoice and cancel its invoice and order.
**Context:** Payment operations are in `app/modules/payment`; order status changes must follow `OrderStateMachine`.
**In scope:** Validate the order and associated invoice exist, require the invoice to be `PAID`, then atomically set both statuses to `CANCELLED`; expose the endpoint and document/test its behavior.
**Out of scope:** Refunds for unpaid invoices, partial refunds, and unrelated payment or order lifecycle changes.
**Acceptance:** Successful refunds return the agreed API response and leave both records `CANCELLED`; missing records or non-`PAID` invoices fail explicitly without partial updates; tests cover success and failure cases.
**Stop and ask a human if:** Refund-provider behavior, authorization, response/error contracts, or transaction boundaries cannot be determined from repository conventions.
**Reviewer:** Payment and orders module maintainers.
