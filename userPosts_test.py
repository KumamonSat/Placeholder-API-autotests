import requests
import random

def test_posts():
    rand_int = random.randint(1, 10)
    resp = requests.get("https://jsonplaceholder.typicode.com/posts?userId=" + str(rand_int))
    assert resp.headers['Content-Type'] == "application/json; charset=utf-8"
    assert resp.status_code == 200
    resp_body = resp.json()
    for i in range(len(resp_body)):
        assert resp_body[i]["userId"] == rand_int
        assert type(resp_body[i]["id"]) == int
        assert resp_body[i]["title"] != None
        assert resp_body[i]["body"] != None
        
