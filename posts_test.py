import requests
import random

def test_posts():
    rand_int = random.randint(1, 100)
    resp = requests.get("https://jsonplaceholder.typicode.com/posts/" + str(rand_int))
    assert resp.headers['Content-Type'] == "application/json; charset=utf-8"
    assert resp.status_code == 200
    resp_body = resp.json()
    assert resp_body["id"] == rand_int