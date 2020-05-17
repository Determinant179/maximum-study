import json 

str = '{"key" : ["python", "py", 2]}'

jsonData = json.loads(str)

#print(jsonData)
#print(jsonData['key'])

arr = {"key" : 
    {'lang' : "python", 
    "name" : "test", 
    "array" : [1,2,3,4,5]}
}

str2 = json.dumps(arr)

print(str2)
print(arr["key"]['lang'])