import sys
from pathlib import Path

from fastapi.testclient import TestClient

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))
from app import app, activities


def test_unregister_participant_removes_email_from_activity():
    activities["Chess Club"]["participants"] = ["michael@mergington.edu", "daniel@mergington.edu"]

    with TestClient(app) as client:
        response = client.delete("/activities/Chess Club/signup", params={"email": "daniel@mergington.edu"})

    assert response.status_code == 200
    assert "daniel@mergington.edu" not in activities["Chess Club"]["participants"]
    assert "michael@mergington.edu" in activities["Chess Club"]["participants"]
