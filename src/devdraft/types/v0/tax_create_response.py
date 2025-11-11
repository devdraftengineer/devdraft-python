# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["TaxCreateResponse"]


class TaxCreateResponse(BaseModel):
    id: Optional[str] = None

    active: Optional[bool] = None

    created_at: Optional[datetime] = None

    description: Optional[str] = None

    name: Optional[str] = None

    percentage: Optional[float] = None

    updated_at: Optional[datetime] = None
