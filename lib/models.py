from sqlalchemy import ForeignKey, Column, Integer, String, MetaData
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    # One-to-Many relationship with Course
    courses = relationship("Course", back_populates="teacher")

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    teacher_id = Column(Integer, ForeignKey('teachers.id'))

    # Many-to-One relationship with Teacher
    teacher = relationship("Teacher", back_populates="courses")

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    # Many-to-Many relationship with Course through Enrollment
    enrollments = relationship("Enrollment", back_populates="student")

class Enrollment(Base):
    __tablename__ = 'enrollments'

    id = Column(Integer, primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'))
    student_id = Column(Integer, ForeignKey('students.id'))

    # Define backrefs for convenience
    course = relationship("Course", back_populates="enrollments")
    student = relationship("Student", back_populates="enrollments")
