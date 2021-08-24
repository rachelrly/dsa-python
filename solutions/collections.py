# max sum in a set
def max_sum(set):
    highest = -1
    sec_highest = -1

    for item in set:
        if item > highest:
            sec_highest = highest
            highest = item

    sum = highest + sec_highest
    print(sum)
    return sum


#input = {4, 6, -3, 5, -2, 1}

#max_sum(input)


# merge two sets
def merge_sets(set_one, set_two):
    merged = set_one | set_two
    print(merged)
    return merged


# set_one = {-4, -6, 3, 5, 2, -1}
# set_two = {9, 8, 2, 11}

#merge_sets(set_one, set_two)

# Remove Characters from a string


def remove_chars_from_str(str, chars):
    def split(word):
        letters = set()
        for l in word:
            letters.add(l)
        return letters

    letters = split(chars)
    new_str = ''
    for l in str:
        if l in letters: continue
        new_str += l
    print(new_str)
    return new_str


# str1 = 'testing'
# str2 = 'alien'
# remove_chars_from_str(str1, str2)

# Products
# 'write an algorithm that outputs an array where each
# index is the product of all the numbers in the input array except for
# the number at each current index.'

# use list data type
# copy original for ref?
# loop through length of list

#
