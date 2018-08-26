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
        for i in range(len(arr[0])):
            row = []
            for j in range(len(arr)):
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
        @return filled_answer - integer
        """
        correct_answer = 0
        filled_answer = []
        for i in range(len(questions)):
            filled_score = 0
            for j in range(len(answers[i])):
                if answers[i][j] is not None:
                    if answers[i][j] == ((questions[i][j] + questions[i][j+1]) % 10):
                        correct_answer += 1
                    filled_score += 1
            filled_answer.append(filled_score)
        return correct_answer, filled_answer
    
    def calculate_filled(self, questions, answers):
        """
        Calculate filled
        @param questions - 2d array
        @param answers - 2d array
        @return filled_count - integer
        """
        filled_answer = []
        for i in range(len(questions)):
            score = 0
            for j in range(len(answers[i])):
                if answers[i][j] is not None:
                    score += 1
            filled_answer.append(score)
        return filled_answer

    def asess_test_data(self, payload, user_id):
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
        correct_count, filled_answer = self.calculate_result(questions, answers)
        # store to database
        logger.info('begin writing to database.')
        kraepelin = Kraepelin()
        kraepelin.user_id = user_id
        kraepelin.answers = json.dumps(payload['answers'], separators=(',',':'))
        kraepelin.questions = json.dumps(payload['questions'], separators=(',',':'))
        kraepelin.correct_count = correct_count
        kraepelin.answer_count = len(payload['answers'])
        kraepelin.filled_count = json.dumps(filled_answer)
        db.session.add(kraepelin)
        try:
            logger.info('committing data to database.')
            db.session.commit()
            return {
                'correct_count': correct_count,
                'questions': questions,
                'answers': answers,
                'id': kraepelin.id,
            }
        except SQLAlchemyError as e:
            data = e.orig.args
            logger.warning('an error occured when writing to database: ' + data)
            raise e
    

    def get_filled_answer(self, id):
        try:
            logger.info('getting kraepelin data with id: %d', id)
            kraepelin = db.session.query(Kraepelin).filter_by(id=id).first()
            data = {}
            data = kraepelin.__dict__ if kraepelin else None
            return data['filled_count']
        except Exception as e:
            logger.warning('an error occured when reading database: %s', e)
            raise e
