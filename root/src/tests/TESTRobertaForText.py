# Import necessary Classes
import unittest
from client.src.api.RobertaForText import question_answering_from_text


class TESTRobertaForText(unittest.TestCase):
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
        result = question_answering_from_text(self.sample_questions, self.sample_context)

        # Expected result
        expected_result = {
            "What is the capital of France?": "Paris",
            "What is the tower name?": "Eiffel Tower",
            "Who is Modi?": "Sorry, I don't have enough information to provide an answer."
        }

        # Check if the result is as expected
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    # Run the test cases
    unittest.main()
