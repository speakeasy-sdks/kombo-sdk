"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum

class GetHrisEmployeesParameterEmploymentStatus(str, Enum):
    r"""**(⚠️ Deprecated)** Filter by the `employment_status` field."""
    ACTIVE = 'ACTIVE'
    PENDING = 'PENDING'
    INACTIVE = 'INACTIVE'
    LEAVE = 'LEAVE'
