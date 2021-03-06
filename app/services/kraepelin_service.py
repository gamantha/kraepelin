import datetime
import random
import logging
from flask import json
from sqlalchemy.exc import SQLAlchemyError
from app.models import db
from app.models.kraepelin import Kraepelin
from app.models.user import User
from app.models.scale_ref import ScaleRef
from app.models.config import Config

logger = logging.getLogger(__name__)

class KraepelinService():
    """
    All kraepelin data logic service.
    """

    def get_test_list(self, request):
        """
        get test list
        """
        total_items = Kraepelin.query.count()
        page = request.args.get('page') if request.args.get('page') else 1
        email = request.args.get('email') if request.args.get('email') else None
        # paginate
        query = db.session.query(Kraepelin, User).join(User)
        if email is not None:
            query = query.filter(User.email == email)
        result = query.order_by(Kraepelin.created_at.desc()).paginate(int(page), 10, False)
        return {
            'items': result.items,
            'total': total_items,
            'current_page': int(page),
            'base_url': '?email=' + email + '&' if email is not None else '?' ,
        }

    def prepare_test_data(self):
        """
        Prepare all test data
        @param size - size array [x, y]
        return dict
        """
        # kraepelin_size = size.split('x') if size else ['10', '5']
        size = [61, 45]
        try:
            conf = db.session.query(Config).first()
            if conf is None:
                logger.error("configuration is not set, fallback to default configuration")
            else:
                size = [conf.row, conf.column]
        except Exception as e:
            logger.error('an error occured when reading configuration in database: %s', e)
            raise e
        result = []
        for i in range(size[0]):
            temp_arr = []
            for j in range(size[1]):
                temp_arr.append(random.randint(1, 9))
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
        @return incorrect_count - integer
        @return filled_answer - integer
        @return unfilled_answer - integer
        @return minute_count - integer
        """
        correct_answer = []
        incorrect_answer = []
        filled_answer = []
        unfilled_answer = []
        minute_count = []
        answer_map = []
        for i in range(len(questions)):
            filled_score = 0
            correct_score = 0
            incorrect_score = 0
            unfilled_score = 0
            amap = []
            if (i%2 == 0):
                minute_score = 0
            for j in range(len(answers[i])):
                if answers[i][j] is not None:
                    if answers[i][j] == ((questions[i][j] + questions[i][j+1]) % 10):
                        correct_score += 1
                        amap.append(1)
                    else:
                        incorrect_score += 1
                        amap.append(0)
                    filled_score += 1
                    minute_score += 1
                else:
                    unfilled_score += 1
            filled_answer.append(filled_score)
            unfilled_answer.append(unfilled_score)
            correct_answer.append(correct_score)
            incorrect_answer.append(incorrect_score)
            answer_map.append(amap)
            if (i%2 == 0):
                minute_count.append(minute_score)
        return correct_answer, incorrect_answer, filled_answer, unfilled_answer, minute_count, answer_map
    
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
        correct_count, incorrect_count, filled_answer, unfilled_answer, minute_count, answer_map = self.calculate_result(questions, answers)
        # store to database
        logger.info('begin writing to database.')
        kraepelin = Kraepelin()
        kraepelin.user_id = user_id
        kraepelin.answers = json.dumps(payload['answers'], separators=(',',':'))
        kraepelin.questions = json.dumps(payload['questions'], separators=(',',':'))
        kraepelin.correct_count = json.dumps(correct_count)
        kraepelin.minute_count = json.dumps(minute_count)
        kraepelin.incorrect_count = json.dumps(incorrect_count)
        kraepelin.answer_count = len(payload['answers'])
        kraepelin.filled_count = json.dumps(filled_answer)
        kraepelin.unfilled_count = json.dumps(unfilled_answer)
        kraepelin.answer_map = json.dumps(answer_map)
        kraepelin.starttime = datetime.datetime.strptime(payload['starttime'], "%a, %d %b %Y %H:%M:%S %Z")
        kraepelin.endtime = datetime.datetime.strptime(payload['endtime'], "%a, %d %b %Y %H:%M:%S %Z")
        
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
            scale_ref = db.session.query(ScaleRef).filter_by(scale_name='kraepelin').order_by(ScaleRef.scaled.asc()).all()
            user = db.session.query(User).filter_by(user_id=kraepelin.user_id).first()

            scales = []
            for scale in scale_ref:
                """loop scale."""
                scales.append(scale.__dict__['unscaled'])
            data = {}
            data = kraepelin.__dict__ if kraepelin else None
            return {
                'filled_count': data['filled_count'],
                'answer_map': data['answer_map'],
                'unfilled_count': data['unfilled_count'],
                'incorrect_count': data['incorrect_count'],
                'correct_count': data['correct_count'],
                'minute_count': data['minute_count'],
                'scales': json.dumps(scales),
                'user': user.__dict__
            }
        except Exception as e:
            logger.warning('an error occured when reading database: %s', e)
            raise e
