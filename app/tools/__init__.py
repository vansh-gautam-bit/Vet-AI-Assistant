from app.tools.owner_tools import *
from app.tools.pet_tools import *
from app.tools.visit_tools import *

TOOLS = [
   
    get_all_owners,
    get_owner_by_id,
    find_owner_by_name,
    create_owner,
    update_owner,
    delete_owner,

    get_all_pets,
    get_pet_by_id,
    find_pet_by_name,
    create_pet,
    update_pet,
    delete_pet,
    
    create_visit,
    get_pet_visits,
    update_visit,
    delete_visit,
]