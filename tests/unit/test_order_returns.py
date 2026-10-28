from unittest.mock import MagicMock

import pytest

from app.modules.orders import models, repository, service
from app.modules.orders.exceptions import OrderOwnershipError
from app.modules.orders.service import InvalidOrderTransition, OrderStateMachine


def test_order_status_includes_returned():
    assert models.OrderStatus.RETURNED.value == "returned"


def test_delivered_order_can_be_returned():
    OrderStateMachine.validate_transition(
        models.OrderStatus.DELIVERED,
        models.OrderStatus.RETURNED,
    )


def test_returned_order_is_terminal():
    assert OrderStateMachine.TRANSITIONS[models.OrderStatus.RETURNED] == []
    with pytest.raises(InvalidOrderTransition):
        OrderStateMachine.validate_transition(
            models.OrderStatus.RETURNED,
            models.OrderStatus.CANCELLED,
        )


def test_cancel_order_rejects_returned_order():
    order = MagicMock(spec=models.Order)
    order.status = models.OrderStatus.RETURNED
    repo = MagicMock(spec=repository.OrderRepository)
    repo.get_order.return_value = order
    db = MagicMock()

    with pytest.raises(OrderOwnershipError, match="returned"):
        service.cancel_order(db, repo, 1)

    assert order.status == models.OrderStatus.RETURNED
    db.commit.assert_not_called()
