import sys
sys.path.append(r"C:\Users\gians\Desktop\CS\pythons\randomstuff")
import passwords 

from canvasapi import Canvas
API_URL = "https://njit.instructure.com"
API_KEY = passwords.CANVAS_API_KEY

# Initialize a new Canvas object
canvas = Canvas(API_URL, API_KEY)

# https://njit.instructure.com/files/folder/users_24881/
user = canvas.get_user(24881)
print(user)
# crs = user.get_courses()
courses = user.get_courses(enrollment_status='active')

for course in courses:
    try:
        # print(course,course.start_at)
        print(course)
        assignments = course.get_assignments()
        for assignment in assignments:
            # print(assignment)
            submisssions=assignment.get_submissions()
            for submisssion in submisssions:
                print(submisssion)
    except Exception as e:
        print(e)
    # break



print("-----------------------------------------------")