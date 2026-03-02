"""
Tests for the unregister endpoint (DELETE /activities/{activity_name}/unregister)
"""

import pytest


def test_successful_unregister(client):
    """Test successfully unregistering from an activity."""
    # Arrange
    activity = "Chess Club"
    email = "michael@mergington.edu"  # This participant exists in sample data

    # Act
    response = client.delete(
        f"/activities/{activity}/unregister",
        params={"email": email}
    )

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert email in data["message"]
    assert activity in data["message"]


def test_unregister_removes_participant(client):
    """Test that unregister actually removes the participant from the activity."""
    # Arrange
    activity = "Chess Club"
    email = "michael@mergington.edu"

    # Act
    client.delete(
        f"/activities/{activity}/unregister",
        params={"email": email}
    )
    response = client.get("/activities")

    # Assert
    activities = response.json()
    assert email not in activities[activity]["participants"]


def test_unregister_decreases_participant_count(client):
    """Test that unregister decreases the participant count."""
    # Arrange
    activity = "Programming Class"
    email = "emma@mergington.edu"  # This participant exists in sample data
    
    # Verify initial state
    response_before = client.get("/activities")
    initial_count = len(response_before.json()[activity]["participants"])

    # Act
    client.delete(
        f"/activities/{activity}/unregister",
        params={"email": email}
    )
    
    # Verify after unregister
    response_after = client.get("/activities")
    final_count = len(response_after.json()[activity]["participants"])

    # Assert
    assert final_count == initial_count - 1
