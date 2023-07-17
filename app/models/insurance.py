from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class Insurance(models.Model):
    """Модель страхования"""
    id = fields.IntField(pk=True)
    cargo_type = fields.CharField(max_length=10)
    rate = fields.FloatField()
    date = fields.DateField()

    class Meta:
        unique_together = ("cargo_type", "date")


Insurance_pydantic = pydantic_model_creator(Insurance, name="Insurance")
InsuranceIn_pydantic = pydantic_model_creator(
    Insurance,
    name="InsuranceIn",
    exclude_readonly=True,
)
