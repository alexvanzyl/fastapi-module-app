from .base import Base  # noqaA

# Import all the models, so that Base has
# them before being imported by Alembic.
from ..user.models import User  # noqa
