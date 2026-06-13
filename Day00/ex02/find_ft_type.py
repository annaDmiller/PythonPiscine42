def all_thing_is_obj(object: any) -> int:
    
    obj_type = type(object)
    match object:
        case list():
            print("List :", obj_type)

        case set():
            print("Set :", obj_type)

        case tuple():
            print("Tuple :", obj_type)

        case dict():
            print("Dict :", obj_type)

        case str():
            print(object, "is in the kitchen :", obj_type)
        
        case _:
            print("Type not found")

    return 42