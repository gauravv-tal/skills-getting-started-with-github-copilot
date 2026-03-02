"""
Tests for the activities endpoint (GET /activities)
"""

import pytest


def test_get_all_activities(client, sample_activities):
    """Test fetching all activities returns correct data."""
    # Arrange
    expected_activities = sample_activities

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert data == expected_activities


def test_get_activities_structure(client):
    """Test that activities response has correct structure."""
    # Arrange
    # No additional setup needed

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    data = response.json()
    
    # Verify it's a dictionary
    assert isinstance(data, dict)
    
    # Verify each activity has required fields
    for activity_name, activity_data in data.items():
        assert isinstance(activity_name, str)
        assert "description" in activity_data
        assert "schedule" in activity_data
        assert "max_participants" in activity_data
        assert "participants" in activity_data
        assert isinstance(activity_data["participants"], list)


def test_get_activities_includes_sample_data(client):
    """Test that activities response includes sample activities."""
    # Arrange
    expected_activities = ["Chess Club", "Programming Class", "Tennis Club"]

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    data = response.json()
    
    for activity in expected_activities:
        assert activity in data
