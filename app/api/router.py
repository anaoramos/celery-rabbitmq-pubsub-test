"""
API Router
"""

from typing import Union

from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.api.views import create_processing_job

router = APIRouter()

router.add_api_route(
    path="/submit_job", endpoint=create_processing_job, methods=["POST"], response_class=JSONResponse)
