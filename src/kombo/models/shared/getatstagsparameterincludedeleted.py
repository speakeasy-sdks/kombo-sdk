"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum

class GetAtsTagsParameterIncludeDeleted(str, Enum):
    r"""By default, deleted entries are not returned. Use the `include_deleted` query param to include deleted entries too."""
    TRUE = 'true'
    FALSE = 'false'
