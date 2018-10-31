from list import list

class union_find_member:
## class representing the member of a disjoint set  
## Val represent the value this member holds
## rep represents the set representative. all members of a set
## point to same rep

    def __init__(self, val):
        self.val = val
        self.rep = None


## make a set element, Value can be of any type / generally an integer
def make_set(val): 
    mem = union_find_member(val)
    tmpl = [] 
    tmpl.append(mem)
    mem.rep = tmpl
    return tmpl

##  Returns the pointer to the set containing the given element. 
##  elem1 is of type union_find_member
def find_set(elem1): 
    return elem1.rep

## modify the representative for each set element to the 
## given representative. in_set is of list type
def modify_rep(in_set, new_rep):
    for entry in in_set:
        entry.rep = new_rep


def union(set1, set2):
    if ( set1 == set2):
        return
    else :
        if (len(set1) > len(set2)):
            modify_rep(set2, set1)
            set1.append(set2)
            return set1
        else:
            modify_rep(set1, set2)
            set2.append(set1)
            return set2


if __name__ == '__main__':
    pass
