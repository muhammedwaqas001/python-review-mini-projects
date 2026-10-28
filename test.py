
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    force = True
)

logger = logging.getLogger(__name__)


class InsufficientBalanceError(Exception):
    pass


def withdraw(balance, amount):
    if amount <= 0:
        raise ValueError("Amount must be positive.")

    if amount > balance:
        raise InsufficientBalanceError("Insufficient balance.")

    remaining_balance = balance - amount
    logger.info("Withdrawal successful.")

    return remaining_balance


try:
    remaining_balance = withdraw(1000, 1500)

except (ValueError, InsufficientBalanceError):
    print("EXCEPT BLOCK EXECUTED")
    logger.exception("Withdrawal failed.")

else:
    print("Remaining balance:", remaining_balance)

print("Program continues normally.")
