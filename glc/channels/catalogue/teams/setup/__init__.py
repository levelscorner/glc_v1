"""Setup utilities for the Microsoft Teams adapter.

These are operator-facing tools that run outside the agent runtime:

- ``trust_setup`` — CLI for pairing/unpairing trusted Teams users
  against the ``glc.security.pairing`` store that the adapter
  consults at runtime via ``classify("teams", ...)``.
"""

from __future__ import annotations
