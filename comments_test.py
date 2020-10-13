import requests
import random

def test_posts():
    rand_int = random.randint(1, 100)
    resp = requests.get("https://jsonplaceholder.typicode.com/comments?postId=" + str(rand_int))
    assert resp.headers['Content-Type'] == "application/json; charset=utf-8"
    assert resp.status_code == 200
    resp_body = resp.json()
    for i in range(len(resp_body)):
        assert resp_body[i]["postId"] == rand_int
        assert type(resp_body[i]["id"]) == int
        assert resp_body[i]["name"] != None
        assert resp_body[i]["email"] != None
        assert resp_body[i]["body"] != None
        
