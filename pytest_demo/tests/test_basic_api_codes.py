import pytest
import requests
from tests.src.app import ENDPOINT


def test_list_tasks():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200
    data = response.json()
    print(data)

def test_update_create_task():
    payload = {
        "content": "test content",
        "user_id": "archana",
        "task_id": "task1",
        "is_done": False
        }
    response = requests.put(ENDPOINT+"/create-task", json=payload)
    data = response.json()
    assert response.status_code == 200
    assert data["task"]["content"] == payload["content"]
    assert data["task"]["user_id"] == payload["user_id"]

    task_id = data["task"]["task_id"]
    list_by_task_id=requests.get(ENDPOINT+f"/get-task/{task_id}")
    assert list_by_task_id.status_code == 200
    data_task_id=list_by_task_id.json()
    assert data_task_id["task_id"] == task_id

    user_id=data["task"]["user_id"]
    list_task_by_user_id=requests.get(ENDPOINT+f"/list-tasks/{user_id}")
    assert list_task_by_user_id.status_code == 200
    data_user_id=list_task_by_user_id.json()
    print(data_user_id)
    for tasks in data_user_id["tasks"]:
        if tasks["user_id"] == user_id:
            assert True
            break
