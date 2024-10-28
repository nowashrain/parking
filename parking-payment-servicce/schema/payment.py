from pydantic import BaseModel
from typing import Optional

# 결제 기본 정보 스키마
class PaymentBase(BaseModel):
    payment: str
    paydate: str
    parkingtime: str
    carnum: str

    class Config:
        orm_mode = True  # SQLAlchemy 모델과 연동

# 새로운 결제 생성 시 필요한 필드를 상속
class PaymentCreate(PaymentBase):
    pass

# 결제 조회 시 사용되는 스키마
class Payment(PaymentBase):
    payid: int

# 결제 목록 조회 시 사용되는 스키마
class PaymentList(BaseModel):
    payid: int
    payment: str
    paydate: str
    parkingtime: str
    carnum: str

    class Config:
        orm_mode = True
