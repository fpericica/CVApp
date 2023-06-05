"""
candidates_model.py

This module defines the structure, relationships, and validation rules associated with the data and enables manipulation and access to it in a consistent and organized manner.

Author: Felix C. Pericică
Date: 2023-06-05
"""
from typing import Union

from exceptions import EmptyDataException, NotFoundException


class CandidatesModel:
    """
    Represents a model for managing candidate(s) data.

    Parameters
    ----------
    data : list
        A list containing candidates data.

    Raises
    ------
    ValueError
    TypeError
        If the provided data is not a list object.

    Methods
    -------
    fetch_all_candidates()
        Returns a list of all candidates.

    fetch_one_candidate(uuid: str)
        Returns a candidate based on a specified UUID.

    fetch_candidate_section(uuid: str)
        Returns the section of a candidate with the specified UUID.
    """
    def __init__(self, data: list):
        self.data = data

        if not self.data:
            raise EmptyDataException("Candidates Data is empty.")
        if not isinstance(self.data, list):
            raise TypeError("Expected a list object.")

    def fetch_all_candidates(self) -> list:
        """
        Retrieves a list of all candidates.

        Returns
        -------
        list
            A list containing all candidates.
        """
        return [
            {key: value for key, value in data.items() if key not in ['id', 'uuid']} for data in self.data
        ]


    def fetch_one_candidate(self, uuid: str) -> dict:
        """
        Retrieves the candidate with the specified UUID.

        Parameters
        ----------
        uuid : str
            The UUID of the candidate to retrieve.

        Returns
        -------
        dict
            A dictionary representing the candidate.

        Raises
        ------
        CandidateNotFoundException
            If no candidate is found for the given UUID.
        """
        for candidate in self.data:
            if candidate['uuid'] == uuid:
                return candidate
    
        raise NotFoundException("No candidate found for the given UUID.")

    def fetch_candidate_section(self, uuid: str, section: str) -> Union[list, str]:
        """
        Retrieves a specific section of the candidate's information.

        Parameters
        ----------
        uuid : str
            The UUID of the candidate.
        section : str
            The section to retrieve (e.g., 'education', 'experience', 'skills').

        Returns
        -------
        Union[list, str]
            The requested section as a list (e.g., for 'skills') or as a string (e.g., for 'name').

        Raises
        ------
        NotFoundException
            If no candidate is found for the given UUID or the provided section is not found.
        """
        candidate = None
        
        for data in self.data:
            if data['uuid'] == uuid:
                candidate = data
    
        if not candidate:
            raise NotFoundException("No candidate found for the given UUID.")
    
        if section not in candidate:
            raise NotFoundException("No provided section found.")
    
        return candidate[section]
