import operator
data = {'hello': ['doc1'], 'my': ['doc1'], 'name': ['doc1'], 'is': ['doc1', 'doc2'], 'james': ['doc1', 'doc2'],
'a': ['doc2'], 'developer': ['doc2']}
get_list=[]
insert_tup=[]
for i in sorted(data.keys()) :
    get_list=[]
    get_list.append(i)
    get_list.append(data[i])
    insert_tup.append(tuple(get_list))
print(insert_tup)   
#get_val.sort(key = operator.itemgetter(0))
#print(get_val)