def get_most_likely_ancestor(str1,str2):
    collection = []
    indx = 0
    while indx < (len(str1)-3):
        
        if str2 == str1[indx:indx+4]:
            position = (indx +1)
            collection.append(position)
        indx += 1
    return tuple(collection)
