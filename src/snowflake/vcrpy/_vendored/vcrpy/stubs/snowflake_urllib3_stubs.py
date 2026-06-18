"""Stubs for snowflake-connector-python's _vendored urllib3.

These mirror ``urllib3_stubs`` but bind ``_baseclass`` to Snowflake's *own*
vendored urllib3 connection classes. This matters because the real connection
must be constructed with the same urllib3 implementation as the pool that
instantiates it: Snowflake's vendored urllib3 (2.x) passes constructor kwargs
such as ``cert_reqs``/``blocksize`` that an older top-level urllib3 would
reject. Wrapping Snowflake's own class keeps the constructor signatures aligned
regardless of the top-level urllib3 version installed.
"""

try:
    from snowflake.connector.vendored.urllib3.connectionpool import HTTPConnection, VerifiedHTTPSConnection
except ImportError:
    # urllib3 2.x removed the VerifiedHTTPSConnection alias; HTTPSConnection is equivalent.
    from snowflake.connector.vendored.urllib3.connectionpool import HTTPConnection
    from snowflake.connector.vendored.urllib3.connectionpool import HTTPSConnection as VerifiedHTTPSConnection

from ..stubs import VCRHTTPConnection, VCRHTTPSConnection


class VCRRequestsHTTPConnection(VCRHTTPConnection, HTTPConnection):
    _baseclass = HTTPConnection


class VCRRequestsHTTPSConnection(VCRHTTPSConnection, VerifiedHTTPSConnection):
    _baseclass = VerifiedHTTPSConnection
