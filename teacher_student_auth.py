authentication = input("Enter your Role :").lower()
unique_ID = int(input("Enter your ID :"))
password = input("Enter your Password :")

teacher_id = [201,487]
teacher_pass = ['priya0126','payal1026']
student_id = [47,32]
student_pass = ['pbkalife','yash502']




# Teacher Section


if authentication=="teacher":
    if unique_ID == teacher_id[0] and password == teacher_pass[0]:
        detail = {
            'name':'Priya Thakur',
            'ID':unique_ID,
            'dept':'Data Science',
            'Sallery':27000
        }

        for key,value in detail.items():
            print(f"{key} : {value}")

    elif unique_ID == teacher_id[1] and password == teacher_pass[1]:
        detail = {
                    'name':'Payal Tyagi',
                    'ID':unique_ID,
                    'dept':'AI & ML',
                    'Sallery':47000
                }

        for key,value in detail.items():
                    print(f"{key} : {value}")
         
    else:
        print('Invalid Crediantials')





#  Student Section


if authentication=="student":
    if unique_ID == student_id[0] and password == student_pass[0]:
        detail_stu = {
            'name':'Kanhaiya Tyagi',
            'Father name':'Arun Kumar',
            'DOB':'01/01/2009',
            'ID':unique_ID,
            'dept':'B.Tech [AI & ML]',
            'Fees':'Submit',
            'Fail/Pass':'Passed',
            'Performance':'Very Good'
        }

        for key,value in detail_stu.items():
            print(f"{key} : {value}")

    elif unique_ID == student_id[1] and password == student_pass[1]:
        detail_stu = {
                    'name':'Yash Kumar',
                    'Father name':'Vinit Kumar',
                    'DOB':'11/07/2008',
                    'ID':unique_ID,
                    'dept':'BCA',
                    'Fees':'Pending',
                    'Fail/Pass':'Failed',
                    'Performance':'Very Bad'
                }

        for key,value in detail_stu.items():
                    print(f"{key} : {value}")
         
    else:
        print('Invalid Crediantials')

