from enum import Enum

class AllureStory(str, Enum):
    COURSES = "Courses"
    DASHBOARD = "Dashboard"
    REGISTRATION = "REGISTRATION"
    AUTHORIZATION = "Authorization"