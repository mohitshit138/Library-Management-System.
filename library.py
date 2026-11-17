import json

book={}
#dump json code
def add_json_book():
    with open("book.json","w") as file:
        json.dump(book, file, indent=5)
def load_data():
    with open("book.json","r")as file:
       return json.load(file)
#code for add a book
def add_book():
    book.update(load_data())
    bk_id=input("enter book id: ")

    if bk_id in book:
        print("book is already  present")
        return
    bk_name=input("enter name of the book: ")
    author=input("enter the author of the book: ")
    bk_ctgr=input("enter the category of the book: ")
    copy=int(input("enter the number of available copies: "))
    if copy < 0:
            print("invalid number of copies")
            return
    book[bk_id]={
        "name_of_book": bk_name,
        "author_of_book": author,
        "category_of_book": bk_ctgr,
        "number_of_copies": copy
    }
    add_json_book()

#code for display all books
def display_book():
   book.update(load_data())
   if not book:
     print("books are not available")
     return
   for bk_id,details in book.items():
        print("book id: ",bk_id)
        print("book name:",details['name_of_book'])
        print("author of the book:", details["author_of_book"])
        print("category the book ", details["category_of_book"])
        print("available copies:", details["number_of_copies"])
#code for searching book
def search_book():
    book.update(load_data())
    bk_id=input("enter book id for search: ")
    if bk_id in book:
        print("book is available")
        print("here is the details: ")
        print("name of the book is: ",book[bk_id]["name_of_book"])
        print("name of the author is: ", book[bk_id]["author_of_book"])
        print("number of copies  available: ", book[bk_id]["number_of_copies"])
    else:
        print("sorry book is not available yet")
#code for student registration
student={}
#json code
def add_student():
    with open("students.json","w")as file:
        json.dump(student, file, indent=5)
def load_data2():
    with open("students.json","r")as file:
       return json.load(file)

def std_register():
    student.update(load_data2())
    id=input("enter your id: ")
    if id in student:
        print("student is already registered")
        return
    name=input("enter your name: ")
    branch=input("enter your department: ")
    phone_no=int(input("inter your contact number: "))
    student[id]={
        "Name":name,
        "Department":branch,
        "phone_number":phone_no
    }
    print("student registered successfully")
    add_student()
 #code for issue
issue={}
#json code
def issue2():
    with open("issue.json","w")as file:
        json.dump(issue, file, indent=5)
def load_data3():
    with open("issue.json","r")as file:
       return json.load(file)

def issue_book():
  book.update(load_data())
  student.update(load_data2())
  issue.update(load_data3())
  id=input("enter your id: ")

  if id not in student:
    print("id not found")
    return
  bk_id=input("enter the Id of the book which you want to issue: ")
  if bk_id in book:
    print("book is found")
    if book[bk_id]["number_of_copies"]>0:
      book[bk_id]["number_of_copies"]=book[bk_id]["number_of_copies"]-1
      add_json_book()
      date=input("enter the book issue date: ")
      rtn=input("enter the last date of book return: ")
      iss_id=input("enter the issue Id: ")
      issue[iss_id]={
        "student_id":id,
        "book_id":bk_id,
        "book_name":book[bk_id]["name_of_book"],
        "date of issue":date,
        "last date":rtn
      }
      print("your book is successfully issued: ")
    for iss_id,details in issue.items():
     print("issue Id: ", iss_id)
     print("book Id: ", details["book_id"])
     print("book name: ",details["book_name"])
     print("date of issue: ", details["date of issue"])
     print("last of book return: ", details["last date"])
  else:
        print("book is not available")


  issue2()
#code for return
back={}
def back_book():
  book.update(load_data())
  student.update(load_data2())
  issue.update(load_data3())

  iss_id=input("enter the issue id: ")
  if iss_id not in issue:
      print("wrong issue id")
      return
  id=input("enter student id: ")
  if id==issue[iss_id]["student_id"] :
    bk_id=input("enter the book id: ")
    if bk_id==issue[iss_id]["book_id"]:
     print("your book is returned")
     book[bk_id]["number_of_copies"]=book[bk_id]["number_of_copies"] + 1
     issue.pop(iss_id)
     add_json_book()
     issue2()
    else:
     print("wrong book id")

  else:
     print("wrong id")

#code for delete a book
def delete():
    book.update(load_data())
    issue.update(load_data3())
    bk_id=input("enter book id: ")
    if bk_id not in book:
        print("book id is not exist")
        return
    if bk_id in issue:
        print("book is issued")
        return
    book.pop(bk_id)
    add_json_book()

    print("book is deleted")

















