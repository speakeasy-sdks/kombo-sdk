"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum

class GetAtsApplicationsParameterOutcome(str, Enum):
    r"""**(⚠️ Deprecated)** Filter applications by outcome. This allows you to get applications that are for example `PENDING`, `HIRED`, or `DECLINED`."""
    PENDING = 'PENDING'
    HIRED = 'HIRED'
    DECLINED = 'DECLINED'