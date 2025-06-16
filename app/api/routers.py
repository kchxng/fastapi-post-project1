from fastapi import APIRouter
api_router=APIRouter()
from app.api.auth import auth
from app.api.products import product
from app.api.orders import transaction

# ----------------------------------------------------------------
#  Desc: Include router or match router
# ----------------------------------------------------------------
# ******* auth *******
api_router.include_router(auth.router,prefix="/auth", tags=["auth"])
# **** product *******
api_router.include_router(product.router,prefix="/product", tags=["product"])
# **** Transaction *******
api_router.include_router(transaction.router,prefix="/transaction", tags=["transaction"])

