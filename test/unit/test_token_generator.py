from datetime import datetime
from src.domain.token_generator import TokenGenerator


def test_token_generation():
    key = 'supersecret'
    algorithm = 'HS256'
    generator = TokenGenerator(key, algorithm)

    date = datetime(2022, 10, 3, 11, 30)
    access_token = generator.create_access_token('mateo', date)
    print(access_token)
    expected_token = (
        'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.'
        'eyJzdWIiOiJtYXRlbyIsImV4cCI6MTY2NDc5NzUwMH0.'
        '2AJY4JAx-zpEAAGVLOLvkCjflOaBQMHKFmn3ygyqt6g'
    )
    assert access_token == expected_token
