"""
candidates_data.py

This module provides a sample data structure representing a CV (Curriculum Vitae) with various fields and information.

The CV data structure is organized into the following sections:
    1. Personal Information (full name, email, and location);
    2. Education;
    3. The most relevant skills;
    4. Work experience;
    5. Hobbies.
    
It aims to store relevant details commonly found in a CV for an individual.
"""
CANDIDATES_DATA = [
    {
        'id': 1,
        'uuid': '0a51a58c-3622-4aef-8c7a-f6a4d478524d',
        'full_name': 'John Smith',
        'email': 'john.smith@example.com',
        'location': 'New York, USA',
        'education': 'ABC University',
        'skills': ['Python', 'JavaScript', 'Data Analysis'],
        'work_experience': [
            {
                'job_title': 'Software Engineer',
                'company': 'ABC Inc.',
                'duration': '2018-2021',
            },
            {
                'job_title': 'Data Analyst',
                'company': 'XYZ Corp.',
                'duration': '2015-2018',
            }
        ],
        'hobbies': ['Photography', 'Hiking', 'Playing Guitar']
    },
    {
        'id': 2,
        'uuid': '9ae7f41c-5490-4d08-9a74-7df12bc2640e',
        'full_name': 'Emma Johnson',
        'email': 'emma.johnson@example.com',
        'location': 'London, UK',
        'education': 'XYZ University',
        'skills': ['Java', 'SQL', 'Machine Learning'],
        'work_experience': [
            {
                'job_title': 'Software Developer',
                'company': '123 Systems',
                'duration': '2017-2020',
            },
            {
                'job_title': 'Data Scientist',
                'company': 'Data Insights Ltd.',
                'duration': '2014-2017',
            }
        ],
        'hobbies': ['Traveling', 'Painting', 'Cooking']
    },
    {
        'id': 3,
        'uuid': '6054fd7d-69cc-4c9f-8e5a-1671b742f17a',
        'full_name': 'Michael Brown',
        'email': 'michael.brown@example.com',
        'location': 'San Francisco, USA',
        'education': 'PQR University',
        'skills': ['C++', 'Python', 'Web Development'],
        'work_experience': [
            {
                'job_title': 'Full Stack Developer',
                'company': 'Tech Solutions Inc.',
                'duration': '2019-2022',
            },
            {
                'job_title': 'Software Engineer',
                'company': 'Innovative Technologies',
                'duration': '2016-2019',
            }
        ],
        'hobbies': ['Gaming', 'Reading', 'Playing Piano']
    },
    {
        'id': 4,
        'uuid': '1f7c97d0-6e67-41ef-b313-791eae31d7fb',
        'full_name': 'Sophia Wilson',
        'email': 'sophia.wilson@example.com',
        'location': 'Sydney, Australia',
        'education': 'LMN University',
        'skills': ['JavaScript', 'React', 'UI/UX Design'],
        'work_experience': [
            {
                'job_title': 'Frontend Developer',
                'company': 'Web Solutions Ltd.',
                'duration': '2017-2021',
            },
            {
                'job_title': 'UI/UX Designer',
                'company': 'Creative Design Agency',
                'duration': '2014-2017',
            }
        ],
        'hobbies': ['Traveling', 'Photography', 'Yoga']
    },
    {
        'id': 5,
        'uuid': '8d4e63a9-063a-4500-8220-d2bc3cc4e1de',
        'full_name': 'Liam Davis',
        'email': 'liam.davis@example.com',
        'location': 'Toronto, Canada',
        'education': 'EFG University',
        'skills': ['Java', 'Python', 'Data Science'],
        'work_experience': [
            {
                'job_title': 'Data Analyst',
                'company': 'Data Insights Inc.',
                'duration': '2018-2021',
            },
            {
                'job_title': 'Software Developer',
                'company': 'Tech Solutions Ltd.',
                'duration': '2015-2018',
            }
        ],
        'hobbies': ['Playing Sports', 'Cooking', 'Listening to Music']
    }
]
