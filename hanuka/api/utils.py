import secrets

from starlette.requests import Request

from .. import bindings as b


async def set_log_context(r: Request):
    rid: str = r.headers.get(b.settings.server.rid_header)
    rid = rid or str(secrets.randbits(b.settings.server.rid_bits))

    b.rid.set(rid)
