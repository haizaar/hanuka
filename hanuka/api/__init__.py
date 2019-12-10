from fastapi import APIRouter, Depends

from . import v1
from .utils import set_log_context


router = APIRouter()
router.include_router(
    v1.router,
    prefix="/v1",
    dependencies=(
        Depends(set_log_context),
    ),
)
