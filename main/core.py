"""
core.py

This module contains the core functionality of the application.
"""
from flask import jsonify

from main.candidates_data import CANDIDATES_DATA
from main.candidates_model import CandidatesModel, EmptyDataException, NotFoundException


candidates_model = CandidatesModel(CANDIDATES_DATA)


# Handler function for the home route.
def home():
    return "Hello, world!"


def get_all_candidates():
    """
    Retrieves all candidates from the candidates model.

    Returns
    -------
    flask.Response
        A JSON response containing the candidates' data as message and the related status code.

    Raises
    ------
    EmptyDataException
        If there are no candidates available.
    """
    try:
        data = candidates_model.fetch_all_candidates()
        status_code = 201
    except EmptyDataException as error:
        data = str(error)
        status_code = 404

    response = jsonify(data)
    response.status_code = status_code

    return response


def get_candidate_by_uuid(uuid: str):
    """
    Retrieves a candidate based on the provided UUID.

    Parameters
    ----------
    uuid : str
        The UUID of the candidate to retrieve.

    Returns
    -------
    flask.Response
        A JSON response containing the candidate's data as message and the related status code.

    Raises
    ------
    NotFoundException
        If no candidate is found for the given UUID.
    """
    try:
        data = candidates_model.fetch_one_candidate(uuid)
        status_code = 201
    except NotFoundException as error:
        data = str(error)
        status_code = 404

    response = jsonify(data)
    response.status_code = status_code

    return response


def get_candidate_section(uuid: str, section: str):
    """
    Retrieves a specific section from a candidate's information.

    Parameters
    ----------
    uuid : str
        The UUID of the candidate.
    section : str
        The section to retrieve (e.g., 'education', 'experience', 'skills').

    Returns
    -------
    flask.Response
        A JSON response containing the requested section of the candidate's information and a status code.

    Raises
    ------
    NotFoundException
        If no candidate is found for the given UUID or the provided section is not found.
    """
    try:
        data = candidates_model.fetch_candidate_section(uuid, section)
        status_code = 201
    except NotFoundException as error:
        data = str(error)
        status_code = 404

    response = jsonify(data)
    response.status_code = status_code

    return response
