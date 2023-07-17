from datetime import date, datetime

from pydantic import BaseModel, Field

DATE_EXAMPLE = datetime(2020, 6, 1).strftime("%Y-%m-%d")
CARGO_TYPE_EXAMPLE = "Glass"
CARGO_PRICE_EXAMPLE = 1000


class InsuranceRequest(BaseModel):
    """Схема для запроса стоимости страхования"""
    cargo_price: int = Field(example=CARGO_PRICE_EXAMPLE)
    cargo_type: str = Field(example=CARGO_TYPE_EXAMPLE)
    cargo_date: date = Field(example=DATE_EXAMPLE)
