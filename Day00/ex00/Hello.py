ft_list = ["Hello", "tata!"] #changeable and ordered: items have a defined order and it won't be changed; new item is added to the end; we can change, add or remove items
ft_tuple = ("Hello", "toto!") #unchangeable and ordered: we cannot change, add or remove after creation
ft_set = {"Hello", "tutu!"} #changeable and unordered: we can't predict in which order the elements will be printed
ft_dict = {"Hello" : "titi!"} #changeable and ordered: the dictionary with 'key' = 'value' logic

ft_list[1] = "World!"

temp_tuple = list(ft_tuple)
temp_tuple[1] = "France!"
ft_tuple = tuple(temp_tuple)

ft_set.discard("tutu!")
ft_set.add("Paris!")

ft_dict["Hello"] = "42Paris!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)