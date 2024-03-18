#!/usr/bin/python3

def element_at(my_list, idx):
    my_lenght=len(my_list)-1

    if(idx < 0 or idx > my_lenght):
        return (None)

    else:

        return (my_list[idx])
