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

    def normalize_questions(self, arr):
        """
        Transpose and flatten questions array
        @param arr - question 2 array
        @return result - transposed question array
        """
        result = []
        for i in range(len(arr)):
            row = []
            for j in range(len(arr[0])):
                row.append(arr[j][i])
            result.append(row)
        return result

    def normalize_answers(self, ans_arr, ques_arr):
        """
        normalize answers
        @param ans_arr - array of answers
        @return result - 2d array of answers
        """
        result = []
        col_count = len(ques_arr[0])
        row_count = len(ques_arr) - 1
        for i in range(col_count):
            row = []
            for j in range(row_count):
                row.append(ans_arr[i + (j*col_count)])
            result.append(row)
        return result

    def calculate_result(self, questions, answers):
        """
        Calculate result
        @param questions - 2d array
        @param answers - 2d array
        @return correct_count - integer
        """
        correct_answer = 0
        for i in range(len(questions)):
            for j in range(len(answers[i])):
                if answers[i][j] == ((questions[i][j] + questions[i][j+1]) % 10):
                    correct_answer += 1
        return correct_answer

    def asess_test_data(self, payload):
        """
        Asess test result.
        @param payload - pauload dictionary
        @return dict
        """
        # TODO: calculate result
        logger.info('normalizing input.')
        questions = self.normalize_questions(payload['questions'])
        answers = self.normalize_answers(payload['answers'], payload['questions'])
        logger.info('calculating result.')
        correct_count = self.calculate_result(questions, answers)
        # store to database
        logger.info('begin writing to database.')
        kraepelin = Kraepelin()
        kraepelin.user_id = payload['user_id']
        kraepelin.answers = json.dumps(payload['answers'], separators=(',',':'))
        kraepelin.questions = json.dumps(payload['questions'], separators=(',',':'))
        kraepelin.correct_count = correct_count
        kraepelin.answer_count = len(payload['answers'])
        db.session.add(kraepelin)
        try:
            logger.info('committing data to database.')
            db.session.commit()
            return {
                'correct_count': correct_count,
                'questions': questions,
                'answers': answers,
            }
        except SQLAlchemyError as e:
            data = e.orig.args
            logger.warning('an error occured when writing to database: ' + data)
            raise e
    