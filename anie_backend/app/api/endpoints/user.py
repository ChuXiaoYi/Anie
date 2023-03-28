from fastapi import APIRouter, Query, Depends, Request
from sqlalchemy.exc import IntegrityError

from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.api.endpoints.auth import get_password_hash
from app.contract.wallet import create_wallet_address
from app.models.user import User
from app.schema.user import RegisterReq

router = APIRouter()

