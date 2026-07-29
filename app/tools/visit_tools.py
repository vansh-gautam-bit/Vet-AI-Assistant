from langchain_core.tools import tool

from app.services.api_client import api_client


@tool
def create_visit(
    pet_id: int,
    reason: str,
    notes: str,
):
    """
    Create a visit for a pet.
    """

    return api_client.post(
        f"/visits/{pet_id}/visits",
        json={
            "reason": reason,
            "notes": notes,
        },
    )


@tool
def get_pet_visits(pet_id: int):
    """
    Retrieve all visits for a pet.
    """

    return api_client.get(
        f"/visits/{pet_id}/visits"
    )


@tool
def update_visit(
    visit_id: int,
    reason: str,
    notes: str,
    visit_date: str,
):
    """
    Update an existing visit.
    """

    return api_client.put(
        f"/visits/{visit_id}",
        json={
            "reason": reason,
            "notes": notes,
            "visit_date": visit_date,
        },
    )


@tool
def delete_visit(visit_id: int):
    """
    Delete a visit.
    """

    return api_client.delete(
        f"/visits/{visit_id}"
    )