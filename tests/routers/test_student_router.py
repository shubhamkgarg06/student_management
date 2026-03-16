"""
This module contains unit tests for the student router in the FastAPI application. 
It uses pytest and httpx to test the various endpoints related to student management, including retrieving students, adding a new student, updating an existing student, and deleting a student. Each test checks the response status code to ensure that the endpoints are functioning correctly.
"""
import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app

@pytest.mark.anyio
async def test_get_students():
    transport = ASGITransport(app=app)


    async with AsyncClient(transport=transport, base_url="http://testserver") as client:
        response = await client.get("/students/")
        assert response.status_code == 200


@pytest.mark.anyio
async def test_get_student_by_id():
    transport = ASGITransport(app=app)

    async with AsyncClient(transport=transport, base_url="http://testserver") as client:
        response = await client.get("/students/1")
        assert response.status_code == 200


@pytest.mark.anyio
async def test_get_students_by_section_id():
    transport = ASGITransport(app=app)

    async with AsyncClient(transport=transport, base_url="http://testserver") as client:
        response = await client.get("/students/section/1")
        assert response.status_code == 200


@pytest.mark.anyio
async def test_add_student():
    transport = ASGITransport(app = app)

    async with AsyncClient(transport = transport , base_url = "http://testserver") as client:
        student_data = {
            "id" : 10,
            "name": "John",
            "father_name":"Mark",
            "age":5,
            "section_id": 101
        }

        response = await client.post(
            "/students/",
            json=student_data
        )

        assert response.status_code == 200



@pytest.mark.anyio
async def test_update_student():
    transport = ASGITransport(app = app)

    async with AsyncClient(transport = transport , base_url = "http://testserver") as client:
        student_data = {
            "id" : 10,
            "name": "John Updated",
            "father_name":"Mark Updated",
            "age":6,
            "section_id": 101
        }

        response = await client.put(
            "/students/10/101",
            json=student_data
        )

        assert response.status_code == 200


@pytest.mark.anyio
async def test_delete_student():
    transport = ASGITransport(app = app)

    async with AsyncClient(transport = transport , base_url = "http://testserver") as client:
        response = await client.delete("/students/10/101")
        assert response.status_code == 200


@pytest.mark.anyio
async def test_get_non_existent_student():
    transport = ASGITransport(app = app)

    async with AsyncClient(transport = transport , base_url = "http://testserver") as client:
        response = await client.get("/students/999")
        assert response.status_code == 200

