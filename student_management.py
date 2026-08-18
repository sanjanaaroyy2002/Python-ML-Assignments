# ==========================================================
# Student Record Management System using Binary Search Tree
# ==========================================================

class Student:
    def __init__(self, student_id, name, age, course):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course


class Node:
    def __init__(self, student):
        self.student = student
        self.left = None
        self.right = None


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, student):
        if self.root is None:
            self.root = Node(student)
        else:
            self._insert(self.root, student)

    def _insert(self, current, student):

        if student.student_id < current.student.student_id:

            if current.left is None:
                current.left = Node(student)
            else:
                self._insert(current.left, student)

        elif student.student_id > current.student.student_id:

            if current.right is None:
                current.right = Node(student)
            else:
                self._insert(current.right, student)

        else:
            print("\nStudent ID already exists.")

    def search(self, student_id):
        return self._search(self.root, student_id)

    def _search(self, current, student_id):

        if current is None:
            return None

        if student_id == current.student.student_id:
            return current.student

        elif student_id < current.student.student_id:
            return self._search(current.left, student_id)

        else:
            return self._search(current.right, student_id)

    def display(self):

        if self.root is None:
            print("\nNo records found.")
            return

        print("\n========== STUDENT RECORDS ==========\n")
        self._display(self.root)

    def _display(self, current):

        if current:

            self._display(current.left)

            print("--------------------------------")
            print("Student ID :", current.student.student_id)
            print("Name       :", current.student.name)
            print("Age        :", current.student.age)
            print("Course     :", current.student.course)

            self._display(current.right)

    def delete(self, student_id):
        self.root = self._delete(self.root, student_id)

    def _delete(self, current, student_id):

        if current is None:
            return current

        if student_id < current.student.student_id:
            current.left = self._delete(current.left, student_id)

        elif student_id > current.student.student_id:
            current.right = self._delete(current.right, student_id)

        else:

            if current.left is None:
                return current.right

            if current.right is None:
                return current.left

            successor = self._minimum(current.right)

            current.student = successor.student

            current.right = self._delete(
                current.right,
                successor.student.student_id
            )

        return current

    def _minimum(self, node):

        while node.left:
            node = node.left

        return node


def main():

    bst = BinarySearchTree()

    while True:

        print("\n=====================================")
        print(" STUDENT RECORD MANAGEMENT SYSTEM")
        print("=====================================")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Delete Student")
        print("4. Display Students")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            student_id = int(input("Enter Student ID : "))
            name = input("Enter Name : ")
            age = int(input("Enter Age : "))
            course = input("Enter Course : ")

            student = Student(student_id, name, age, course)

            bst.insert(student)

            print("\nStudent added successfully!")

        elif choice == "2":

            student_id = int(input("Enter Student ID to Search : "))

            student = bst.search(student_id)

            if student:

                print("\nStudent Found")
                print("---------------------------")
                print("Student ID :", student.student_id)
                print("Name       :", student.name)
                print("Age        :", student.age)
                print("Course     :", student.course)

            else:

                print("\nStudent not found.")
        elif choice == "3":

            student_id = int(input("Enter Student ID to Delete : "))

            if bst.search(student_id):
                bst.delete(student_id)
                print("\nStudent deleted successfully!")
            else:
                print("\nStudent not found.")

        elif choice == "4":

            bst.display()

        elif choice == "5":

            print("\nThank you for using the Student Record Management System.")
            break

        else:

            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()