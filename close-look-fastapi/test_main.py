#!/usr/bin/env python3

import json


from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_read_home():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {'message': 'Welcome to the Randomizer API'}



def test_read_parameters():
    max_value = 7
    response = client.get(f'/random/{max_value}')
    assert response.status_code == 200
    json_response = response.json()
    assert 'max' in json_response
    assert json_response['max'] == max_value
    assert 'random_number' in json_response.keys()
    assert 1 <= json_response['random_number'] <= 7


def test_read_parameters_error():
    max_value = 'ten'
    response = client.get(f'/random/{max_value}')
    assert response.status_code == 422
    json_response = response.json()
    assert len(json_response) == 1
    assert len(json_response['detail']) == 1
    detail = json_response['detail'][0]
    assert detail['type'] == 'int_parsing'
    assert detail['loc'] == ['path', 'max_value']
    assert detail['msg'].startswith('Input should be a valid integer')
    assert detail['input'] == 'ten'


def test_no_query_parameters():
    response = client.get(f'/random-between')
    assert response.status_code == 200
    json_response = response.json()
    assert 'min' in json_response
    assert json_response['min'] == 1
    assert 'max' in json_response
    assert json_response['max'] == 99
    assert 'random_number' in json_response.keys()
    assert 1 <= json_response['random_number'] <= 99


def test_min_only_query_parameters():
    min_value = 38
    response = client.get(f'/random-between?min_value={min_value}')
    assert response.status_code == 200
    json_response = response.json()
    assert 'min' in json_response
    assert json_response['min'] == min_value
    assert 'max' in json_response
    assert json_response['max'] == 99
    assert 'random_number' in json_response.keys()
    assert min_value <= json_response['random_number'] <= 99


def test_max_only_query_parameters():
    max_value = 75
    response = client.get(f'/random-between?max_value={max_value}')
    assert response.status_code == 200
    json_response = response.json()
    assert 'min' in json_response
    assert json_response['min'] == 1
    assert 'max' in json_response
    assert json_response['max'] == max_value
    assert 'random_number' in json_response.keys()
    assert 1 <= json_response['random_number'] <= max_value


def test_all_query_parameters():
    min_value = 580
    max_value = 673
    response = client.get(f'/random-between?min_value={min_value}&max_value={max_value}')
    assert response.status_code == 200
    json_response = response.json()
    assert 'min' in json_response
    assert json_response['min'] == min_value
    assert 'max' in json_response
    assert json_response['max'] == max_value
    assert 'random_number' in json_response.keys()
    assert min_value <= json_response['random_number'] <= max_value
