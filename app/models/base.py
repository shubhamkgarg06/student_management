"""
This module consists of a base class for all models in the database. 
It provides common fields for tracking creation and update timestamps, 
as well as the users responsible for these actions.
"""
from datetime import datetime,timezone
from sqlalchemy import Column, DateTime, String


class DBBase:
    """Mixin class to add common timestamp and user tracking fields."""

    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc),
                    onupdate=lambda: datetime.now(timezone.utc))

    created_by = Column(String, nullable=True)
    updated_by = Column(String, nullable=True)
