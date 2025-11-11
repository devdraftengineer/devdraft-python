# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["TaxCreateParams"]


class TaxCreateParams(TypedDict, total=False):
    name: Required[str]
    """Tax name. Used to identify and reference this tax rate."""

    percentage: Required[float]
    """Tax percentage rate. Must be between 0 and 100."""

    active: bool
    """Whether this tax is currently active and can be applied."""

    app_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="appIds")]
    """Array of app IDs where this tax should be available.

    If not provided, tax will be available for the current app.
    """

    description: str
    """Optional description explaining what this tax covers."""
