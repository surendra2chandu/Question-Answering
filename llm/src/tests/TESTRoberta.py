# Import necessary Classes
import unittest
from llm.src.api.Roberta import roberta_question_answering


class TESTRoberta(unittest.TestCase):
    def setUp(self):
        """
        Initialize the sample context and questions
        :return: None
        """
        self.sample_context = "The capital of France is Paris. The Eiffel Tower is located in Paris."
        self.sample_questions = ["What is the capital of France?", "What is the tower name?", "Who is Modi?"]

    def test_question_answering(self):
        """
        Test the question_answering function
        :return: None
        """
        # Call the question_answering_from_text function
        result = roberta_question_answering(self.sample_questions, self.sample_context)

        # Expected result
        expected_result = [{'score': 0.9595003724098206, 'start': 25, 'end': 30, 'answer': 'Paris'},
                           {'score': 0.7237449884414673, 'start': 36, 'end': 48, 'answer': 'Eiffel Tower'},
                           {'score': 2.543833033996634e-06, 'start': 25, 'end': 69,
                            'answer': 'Paris. The Eiffel Tower is located in Paris.'}]

        # Check if the result is as expected
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    # Run the test cases
    unittest.main()
