from app import app

def test_api_distance():
    client = app.test_client()

    response = client.post("/api/distance", json={
        "start_point": "0,0",
        "end_point": "3,4"
    })

    assert response.status_code == 200