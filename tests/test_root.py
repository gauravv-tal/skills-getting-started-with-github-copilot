"""
Tests for the root endpoint (GET /)
"""

import pytest


def test_root_redirect(client):
    """Test that root endpoint redirects to static index page."""
    # Arrange
    # No additional setup needed

    # Act
    response = client.get("/", follow_redirects=False)

    # Assert
    assert response.status_code == 307
    assert response.headers["location"] == "/static/index.html"


def test_root_redirect_follows(client):
    """Test that root endpoint successfully redirects to index.html."""
    # Arrange
    # No additional setup needed

    # Act
    response = client.get("/", follow_redirects=True)

    # Assert
    assert response.status_code == 200
