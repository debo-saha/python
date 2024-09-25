
def add_new_employee(employee_records,id,name,age,dept,salary):
    employee_records[id]={
        "name":f"{name}",
        "age":f"{age}",
        "dept":f"{dept}",
        "salary":f"{salary}"
    }
    print(employee_records)



def del_employee(employee_records,id):
   del employee_records["id1"]

   return employee_records



def get_employee_details(employee_records,id):
    print(employee_records[id])

employee_records={
    "id1":{
        "name":"debo",
        "age":55,
        "dept":"cse",
        "salary":500000
    }
}

add_new_employee(employee_records,"id5","raja",55,"ece","1000")
# get_employee_details(employee_records,"id1")
del_employee(employee_records,"id1")
print(employee_records)
