import os
import quizcomp.quiz
import tests.base

class TestTotalPoints(tests.base.BaseTest):
    """
    Test the total_points property of the Quiz class.
    """

    def test_single_question_points(self):
        
        path = os.path.join('tests', 'quizzes', 'good', 'single-question', 'quiz.json')
        quiz = quizcomp.quiz.Quiz.from_path(path)
        self.assertEqual(quiz.total_points, 10, "Quiz should have exactly 10 points")

    def test_all_basic_questions_points(self):
       
        path = os.path.join('tests', 'quizzes', 'good', 'all-basic-questions', 'quiz.json')
        
        if os.path.exists(path):
            quiz = quizcomp.quiz.Quiz.from_path(path)
            self.assertIsNotNone(quiz.total_points)