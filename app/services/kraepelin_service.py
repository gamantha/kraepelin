import random
import logging
from flask import json
from sqlalchemy.exc import SQLAlchemyError
from app.models import db
from app.models.kraepelin import Kraepelin

logger = logging.getLogger(__name__)

class KraepelinService():
    """
    All kraepelin data logic service.
    """

    def prepare_test_data(self, size):
        """
        Prepare all test data
        @param size - size array [x, y]
        return dict
        """
        result = []
        for i in range(int(size[0])):
            temp_arr = []
            for j in range(int(size[1])):
                temp_arr.append(random.randint(1, 10))
            result.append(temp_arr)
        return result

    def asess_test_data(self, payload):
        """
        Asess test result.
        @param payload - pauload dictionary
        @return dict
        """
        # TODO: calculate result
        # store to database
        kraepelin = Kraepelin()
        kraepelin.answers = json_mylist = json.dumps(payload['answers'], separators=(',',':'))
        db.session.add(kraepelin)
        try:
            logger.info('committing data to database.')
            db.session.commit()
        except SQLAlchemyError as e:
            data = e.orig.args
            logger.warning('an error occured when writing to database: ' + data)
            return False
        return True
    