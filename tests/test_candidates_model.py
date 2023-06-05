import unittest

from exceptions import NotFoundException, EmptyDataException
from main.candidates_model import CandidatesModel


class TestCandidatesModel(unittest.TestCase):
    def setUp(self):
        self.data = [
            {
                'id': 1,
                'uuid': '123',
                'name': 'John Doe',
                'education': ['Bachelor', 'Master'],
                'experience': ['Company A', 'Company B'],
                'skills': ['Python', 'Java']
            },
            {
                'id': 2,
                'uuid': '321',
                'name': 'Jane Smith',
                'education': ['Bachelor'],
                'experience': ['Company C'],
                'skills': ['JavaScript']
            }
        ]
        self.model = CandidatesModel(self.data)

    def test_fetch_all_candidates(self):
        expected_result = [
            {
                'name': 'John Doe',
                'education': ['Bachelor', 'Master'],
                'experience': ['Company A', 'Company B'],
                'skills': ['Python', 'Java']
            },
            {
                'name': 'Jane Smith',
                'education': ['Bachelor'],
                'experience': ['Company C'],
                'skills': ['JavaScript']
            }
        ]
        result = self.model.fetch_all_candidates()
        self.assertEqual(result, expected_result)

    def test_fetch_one_candidate_found(self):
        uuid = '123'
        expected_result = {
                'id': 1,
                'uuid': '123',
                'name': 'John Doe',
                'education': ['Bachelor', 'Master'],
                'experience': ['Company A', 'Company B'],
                'skills': ['Python', 'Java']
            }
        result = self.model.fetch_one_candidate(uuid)
        self.assertEqual(result, expected_result)

    def test_fetch_one_candidate_not_found(self):
        uuid = '3'
        with self.assertRaises(NotFoundException):
            self.model.fetch_one_candidate(uuid)

    def test_fetch_candidate_section_found(self):
        uuid = '321'
        section = 'education'
        expected_result = ['Bachelor']
        result = self.model.fetch_candidate_section(uuid, section)
        self.assertEqual(result, expected_result)

    def test_fetch_candidate_section_not_found(self):
        uuid = '1'
        section = 'address'
        with self.assertRaises(NotFoundException):
            self.model.fetch_candidate_section(uuid, section)

    def test_empty_data_exception(self):
        with self.assertRaises(EmptyDataException):
            CandidatesModel([])

    def test_invalid_data_type(self):
        with self.assertRaises(TypeError):
            CandidatesModel("invalid data")
