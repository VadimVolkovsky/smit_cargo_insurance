import logging
from http import HTTPStatus

from fastapi import APIRouter, HTTPException
from tortoise import exceptions

from app.models.insurance import (Insurance, Insurance_pydantic,
                                  InsuranceIn_pydantic)
from app.schemas.insurance import InsuranceRequest

router = APIRouter()


@router.post(
    "/create_rate",
    response_model=Insurance_pydantic,
)
async def create_rate(insurance: InsuranceIn_pydantic):
    """Создание ставки страхования на указанные дату и тип груза"""
    insurance_obj = await Insurance.create(
        **insurance.dict(exclude_unset=True),
    )
    logging.info(f'Создан объект insurance: {insurance_obj}')
    return await Insurance_pydantic.from_tortoise_orm(insurance_obj)


@router.post(
    "/get_insurance",
)
async def get_insurance_price(customer_request: InsuranceRequest) -> dict:
    """Рассчитывает стоимость страхования груза на указанную дату"""
    logging.info(
        f'Получен запрос на расчет стоимости страхования: {customer_request}')
    try:
        insurance_obj = await Insurance_pydantic.from_queryset_single(
            Insurance.get(
                cargo_type=customer_request.cargo_type,
                date=customer_request.cargo_date,
            ),
        )
        insurance_price = customer_request.cargo_price * insurance_obj.rate
        logging.info(f'Рассчитана стоимость страхования: {insurance_price}')
        return {"insurance_price": insurance_price}
    except exceptions.DoesNotExist:
        message = "На указанную дату и тип груза нет вариантов страхования"
        logging.info(message)
        raise HTTPException(HTTPStatus.NOT_FOUND, message)
