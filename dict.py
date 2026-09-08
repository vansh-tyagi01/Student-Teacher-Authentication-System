students = {
    'pbka123' : {
        'Name' : 'Vansh Tyagi',
        'ID' : 101,
        'Course' : 'B.Tech AI & ML' 
    },

    'payal123' : {
        'Name :' : 'Payal Tyagi',
        'ID :' : 102,
        'Course :' : 'MCA'
    }
}

password = input("Enter your password :")

if password in students:
    stdent = students[password]

    print(stdent['Name'])

