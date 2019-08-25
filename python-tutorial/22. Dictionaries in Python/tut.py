# dict={'key1':'value1', 'key2':'value2'}
# print(dict)
# print(dict['key1'])
# dict={'apl':10, 'tandz':20, 'elak':7}
# print(dict['tandz'])
d={'apl':10, 'tandz':[1,2,3], 'elak':{'elakik':3,'elakikner':4, 'malina':{'d':1,'d2':2}}}
print(d['elak']['malina']['d'])
d={'apl':10, 'tandz':['a','b','c']}
print(d['tandz'][1].upper())
d['morozh']='vanil'
print(d)
print(d.keys())
print(d.values())
print(d.items())
print(d.values())
