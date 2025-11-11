# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["TaxUpdateParams"]


class TaxUpdateParams(TypedDict, total=False):
    active: bool
    """Whether this tax is currently active and can be applied"""

    app_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="appIds")]
    """Array of app IDs where this tax should be available"""

    description: str
    """Detailed description of what this tax covers"""

    name: str
    """Tax name for identification and display purposes"""

    percentage: float
    """Tax rate as a percentage (0-100)"""
