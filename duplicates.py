student_data = {'ID-1': {'Name': "Kwesi", 'Age': 13, 'Grade': "VIII"},
                'ID-2': {'Name': "Kwabena", 'Age': 12, 'Grade': "VIII"},
                'ID-3': {'Name': "Kwesi", 'Age': 13, 'Grade': "VIII"},
                'ID-4': {'Name': "Jaden", 'Age': 13, 'Grade': "VIII"}}

result = {}
for key,value in student_data.items():
    if value not in result.values():
        result[key]= value

print(result)