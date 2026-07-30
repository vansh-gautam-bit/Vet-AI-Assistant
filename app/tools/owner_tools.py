from langchain_core.tools import tool
from app.services.api_client import api_client

@tool 
def get_all_owners():
    """
    Retrieve all owners from the Vetrinary Management System.
    """
    return api_client.get("/owners/")

@tool
def get_owner_by_id(owner_id: int):
    """
    Retrieve an owner using their unique ID.
    """
    return api_client.get(f"/owners/{owner_id}")

@tool
def find_owner_by_name(name: str):
    """
    Find an owner by name.
    Returns the matching owner if found.
    """

    owners = api_client.get("/owners/")

    matches = []

    for owner in owners:
        if name.strip().lower() in owner["name"].strip().lower():
            matches.append(owner)

    if matches:
        return matches        

    return {
        "message": f"No owner found with name '{name}'."
    }    

@tool
def create_owner(
    name: str,
    phone: str,
    email: str,
):
    """
    Create a new owner.
    """ 

    return api_client.post(
        "/owners/",
        json={
            "name": name,
            "phone": phone,
            "email": email,
        },
    )

@tool
def update_owner(
    owner_id: int,
    name: str,
    phone: str,
    email: str,
):
    """
    Update an existing owner.
    """

    return api_client.put(
        f"/owners/{owner_id}",
        json={
            "name": name,
            "phone": phone,
            "email": email,
        },
    )

@tool
def delete_owner(owner_id: int):
    """
    delete an owner.
    """

    return api_client.delete(f"/owners/{owner_id}")