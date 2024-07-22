Create database university_db;
\c university_db;

1.Create a fresh database titled "university_db" or any other appropriate name.

CREATE TABLE students (
    student_id SERIAL PRIMARY KEY,
    student_name VARCHAR(100),
    age INTEGER,
    email VARCHAR(100),
    frontend_mark INTEGER,
    backend_mark INTEGER,
    status VARCHAR(50)
);
         =============================
		 
2.Create a "courses" table with the following fields:

CREATE TABLE courses (
    course_id SERIAL PRIMARY KEY,
    course_name VARCHAR(100),
    credits INTEGER
);
         =============================
		 
3.Create an "enrollment" table with the following fields:

CREATE TABLE enrollment (
    enrollment_id SERIAL PRIMARY KEY,
    student_id INTEGER REFERENCES students(student_id),
    course_id INTEGER REFERENCES courses(course_id)
);
        ===============================
		
4.Insert the following sample data into the "students" table:

INSERT INTO students (student_id, student_name, age, email, frontend_mark, backend_mark, status)
VALUES
    (1, 'Alice', 22, 'alice@example.com', NULL, NULL, NULL),
    
    (2, 'Bob', 21, 'bob@example.com', NULL, NULL, NULL),
    
    (3, 'Charlie', 23, 'charlie@example.com', NULL, NULL, NULL),
    
    (4, 'David', 20, 'david@example.com', NULL, NULL, NULL),

    (5, 'Eve', 24, 'newemail@example.com', NULL, NULL, NULL),
   
    (6, 'Rahim', 23, 'rahim@gmail.com', NULL, NULL, NULL);
	    ========================================
		
5.Insert the following sample data into the "courses" table:

INSERT INTO courses (course_id, course_name, credits)
VALUES
    (1, 'Next.js', 3),
    (2, 'React.js', 4),
    (3, 'Databases', 3),
    (4, 'Prisma', 3); 
	    ======================================
		
6.Insert the following sample data into the "enrollment" table:

INSERT INTO enrollment (enrollment_id, student_id, course_id)
VALUES
    (1, 1, 1),
    (2, 1, 2),
    (3, 2, 1),
    (4, 3, 2);
        ======================================
		
Query 1:
Insert a new student record with the following details

INSERT INTO students (student_id,student_name, age, email, frontend_mark, backend_mark, status)
VALUES (17,'PRASANTH', 23, 'prasanth@gmail.com', 98, 99, NULL);
       =============================================
	   
Query 2:
Retrieve the names of all students who are enrolled in the course titled 'Next.js'.

SELECT s.student_name
FROM students s
JOIN enrollment e ON s.student_id = e.student_id
JOIN courses c ON e.course_id = c.course_id
WHERE c.course_name = 'Next.js';
       =========================================
	   
Query 3:
Update the status of the student with the highest total (frontend_mark + backend_mark) mark to 'Awarded'

UPDATE students
SET status = 'Awarded'
WHERE student_id = (
SELECT student_id
FROM (
SELECT student_id, (frontend_mark + backend_mark) AS total_mark
FROM students
    ORDER BY total_mark DESC LIMIT 1) AS highest_mark);
      ========================================
	  
	  
Query 4:
Delete all courses that have no students enrolled.

DELETE FROM courses
WHERE course_id NOT IN (
    SELECT DISTINCT course_id
    FROM enrollment
);
      ====================================
	  
Query 5:
Retrieve the names of students using a limit of 2, starting from the 3rd student.

SELECT student_name
FROM students
ORDER BY student_id
OFFSET 2
LIMIT 2;
      
	  
Query 6:
Retrieve the course names and the number of students enrolled in each course.

SELECT c.course_name, COUNT(e.student_id) AS students_enrolled
FROM courses c
LEFT JOIN enrollment e ON c.course_id = e.course_id
GROUP BY c.course_name
ORDER BY c.course_name;
      =======================================
	  
Query 7:
Calculate and display the average age of all students

SELECT AVG(age) AS average_age
FROM students;
      ==========================================
	  
Query 8:
Retrieve the names of students whose email addresses contain 'example.com'.

SELECT student_name
FROM students
WHERE email LIKE '%example.com%';


	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
		