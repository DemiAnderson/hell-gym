from gym.config import PRINT_ITEMS_PER_PAGE
from gym.db_utilities import GymSession


def get_recent_entries(model_object, limit=PRINT_ITEMS_PER_PAGE, offset=0):
    with GymSession.get_session() as session:
        query = session.query(model_object).order_by(model_object.id)
        if limit:
            query = query.limit(limit).offset(offset)
        data = query.all()
    return data
