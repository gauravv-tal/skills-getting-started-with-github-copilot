"""
Tests for the signup endpoint (POST /activities/{activity_name}/signup)
"""

import pytest


def test_successful_signup(client):
    """Test successfully signing up for an activity."""
    # Arrange
    activity = "Tennis Club"
    email = "john@mergington.edu"

    # Act
    response = client.post(
        f"/activities/{activity}/signup",
        params={"email": email}
    )

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert email in data["message"]
    assert activity in data["message"]


def test_signup_adds_participant(client):
    """Test that signup actually adds the participant to the activity."""
    # Arrange
    activity = "Tennis Club"
    email = "john@mergington.edu"

    # Act
    client.post(
        f"/activities/{activity}/signup",
        params={"email": email}
    )
    response = client.get("/activities")

    # Assert
    activities = response.json()
    assert email in activities[activity]["participants"]


def test_signup_increases_participant_count(client):
    """Test that signup increases the participant count."""
    # Arrange
    activity = "Programming Class"
    email = "newstudent@mergington.edu"
    
    # Verify initial state
    response_before = client.get("/activities")
    initial_count = len(response_before.json()[activity]["participants"])

    # Act
    client.post(
        f"/activities/{activity}/signup",
        params={"email": email}
    )
    
    # Verify after signup
    response_after = client.get("/activities")
    final_count = len(response_after.json()[activity]["participants"])

    # Assert
    assert final_count == initial_count + 1
