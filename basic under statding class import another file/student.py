
class Student:
    records=[]
    @staticmethod
    def repeat():
        while True:
            name=input("Enter student Name :")
            pass_fail=input(f"{name} Pass or Fail :")

            Student.records.append([name,pass_fail])

            ch=input("Do you want to continue?(yes/no) :")
            if ch == "yes":
                continue
            elif ch == "no":
                break
            else:
                print("Invalid choice!")






