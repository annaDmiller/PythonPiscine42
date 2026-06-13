def NULL_not_found(object: any) -> int:

    obj_type = type(object)

    if object != object: #-> to define NaN value, the easiest way
        print("Cheese:", object, obj_type)
        return 0

    match object:
        case None:
            print("Nothing:", object, obj_type)
        
        case False:
            print("Fake:", object, obj_type)
        
        case 0:
            print("Zero:", object, obj_type)

        case "":
            print("Empty:", obj_type)

        case _:
            print("Type not found")
            return 1
        
    return 0