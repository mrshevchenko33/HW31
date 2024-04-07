from student import Student
from group import Group, GroupOverflowError

if __name__ == "__main__":
    try:
        st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
        st2 = Student('Female', 25, 'Emma', 'Stone', 'AN145')
        st3 = Student('Male', 22, 'John', 'Doe', 'AN146')
        st4 = Student('Female', 28, 'Emma', 'Watson', 'AN147')
        st5 = Student('Male', 26, 'Tom', 'Cruise', 'AN148')
        st6 = Student('Female', 23, 'Jennifer', 'Lawrence', 'AN149')
        st7 = Student('Male', 21, 'Michael', 'Jordan', 'AN150')
        st8 = Student('Female', 27, 'Scarlett', 'Johansson', 'AN151')
        st9 = Student('Male', 24, 'Leonardo', 'DiCaprio', 'AN152')
        st10 = Student('Female', 29, 'Angelina', 'Jolie', 'AN153')
        st11 = Student('Male', 31, 'Volodymyr', 'Zelensky', 'AN154')

        gr = Group('PD1')
        gr.add_student(st1)
        gr.add_student(st2)
        gr.add_student(st3)
        gr.add_student(st4)
        gr.add_student(st5)
        gr.add_student(st6)
        gr.add_student(st7)
        gr.add_student(st8)
        gr.add_student(st9)
        gr.add_student(st10)
        gr.add_student(st11)

    except GroupOverflowError:
        print("Error: Group capacity exceeded")

    print(gr)


    assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
    assert gr.find_student('Jobs2') is None, 'Test2'
    assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'

    gr.delete_student('Stone')
    print(gr)

    gr.delete_student('Stone')
