office=[
    {'dept no:': 101, 'emp roll:': 'E001', 'Salary:': 500000},
    {'dept no:': 101, 'emp roll:': 'E002', 'Salary:': 400000},
    {'dept no:': 102, 'emp roll:': 'E003', 'Salary:': 350000},
    {'dept no:': 102, 'emp roll:': 'E004', 'Salary:': 450000},
    {'dept no:': 103, 'emp roll:': 'E005', 'Salary:': 700000},
    {'dept no:': 104, 'emp roll:': 'E006', 'Salary:': 900000}
    ]
dict1={}
for record in office:
    dept = record['dept no:']
    salary= record['Salary:']
    if dept not in dict1:
        dict1[dept] = []
        dict1.append(salary)
print(dict1)

    
