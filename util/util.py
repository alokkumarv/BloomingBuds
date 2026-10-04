from typing import TypeVar
import logging
logger = logging.getLogger(__name__)
from sqlalchemy.inspection import inspect
def sql_model_to_dict(obj):
    try:
        result = {}

        for column in obj.__table__.columns:
            result[column.name] = getattr(obj, column.name)

        return result
    except Exception as ex:
        logger.info("Exception occured as {}",format(ex))


from typing import Any, TypeVar

T = TypeVar("T")

def dict_to_model(model: type[T], data: dict[str, Any]) -> T:
    mapper = inspect(model)

    model_fields = {
        column.key.lower(): column.key
        for column in mapper.columns
    }

    normalized_data = {
        model_fields.get(key.lower(), key): value
        for key, value in data.items()
    }

    return model(**normalized_data)