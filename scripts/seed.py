from gradebook.service import (
    add_course,
    add_student,
    add_grade,
    enroll,
    
)


def seed():
    print("Seeding data...")


    # students
    s1 = add_student("Altina")
    s2 = add_student("Mimoza")
    s3 = add_student("Zgjim")

    # courses
    add_course("CS101" , "Intro to CS")
    add_course("MATH101" , "Basic Math")

    enroll(s1,"CS101")
    enroll(s1,"MATH101")
    enroll(s2,"CS101")
    enroll(s3,"MATH101")

    # grades

    add_grade(s1 , "CS101" , 90)
    add_grade(s1 , "CS101" , 80)
    add_grade(s1 , "MATH101" , 85)

    add_grade(s2, "CS101", 70)
    add_grade(s2, "CS101", 75)

    add_grade(s3, "MATH101", 95)

    print("Data seeded successfully!")



    
if __name__ == "__main__":
    seed()



