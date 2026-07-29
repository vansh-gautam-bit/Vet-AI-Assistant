from langchain_core.tools import tool
from app.services.api_client import api_client

@tool
def get_all_pets(
    species: str = None,
    breed: str = None,
    min_age: int = None,
    max_age: int = None,
    search: str = None,
    sort_by: str = None,
    sort_order: str = None,
    limit: int = 10,
    page: int = 1,
):
    """
    Retrieve pets with optional filtering, searching, sorting, and pagination.
    """

    params = {
        "species": species,
        "breed": breed,
        "min_age": min_age,
        "max_age": max_age,
        "search": search,
        "sort_by": sort_by,
        "sort_order": sort_order,
        "limit": limit,
        "page": page,
    }

    params = {k: v for k, v in params.items() if v is not None}

    return api_client.get("/pets/", params=params)


@tool
def get_pet_by_id(pet_id: int):
    """
    Retrieve a pet using its ID.
    """

    return api_client.get(f"/pets/{pet_id}")


@tool
def find_pet_by_name(name: str):
    """
    Find a pet by name.
    """

    return api_client.get(
        "/pets/",
        params={
            "search": name,
            "limit": 10,
            "page": 1,
        },
    )


@tool
def create_pet(
    name: str,
    species: str,
    breed: str,
    age: int,
    owner_id: int,
):
    """
    Create a new pet.
    """

    return api_client.post(
        "/pets/",
        json={
            "name": name,
            "species": species,
            "breed": breed,
            "age": age,
            "owner_id": owner_id,
        },
    )


@tool
def update_pet(
    pet_id: int,
    name: str,
    species: str,
    breed: str,
    age: int,
    owner_id: int,
):
    """
    Update an existing pet.
    """

    return api_client.put(
        f"/pets/{pet_id}",
        json={
            "name": name,
            "species": species,
            "breed": breed,
            "age": age,
            "owner_id": owner_id,
        },
    )


@tool
def delete_pet(pet_id: int):
    """
    Delete a pet.
    """

    return api_client.delete(f"/pets/{pet_id}")
