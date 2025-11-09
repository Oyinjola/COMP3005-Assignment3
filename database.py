import os
import psycopg2
from psycopg2.extras import RealDictCursor

def get_connection():
    return psycopg2.connect(
        host=os.getenv("PGHOST", "localhost"),
        port=int(os.getenv("PGPORT", "5432")),
        dbname=os.getenv("PGDATABASE", "postgres"),
        user=os.getenv("PGUSER", "postgres"),
        password=os.getenv("PGPASSWORD", "")
    )

def getStudents():
    """READ: print and return all students."""
    with get_connection() as conn, conn.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute("""
            SELECT student_id, first_name, last_name, email, enrollment_date
            FROM students
            ORDER BY student_id;
        """)
        rows = cur.fetchall()
        print("\n[getStudents]")
        for r in rows:
            print(f"  {r['student_id']}: {r['first_name']} {r['last_name']} <{r['email']}> on {r['enrollment_date']}")
        return rows
    
def addStudent(first_name, last_name, email, enrollment_date):
    """CREATE: insert a student; return new student_id."""
    with get_connection() as conn, conn.cursor() as cur:
        cur.execute("""
            INSERT INTO students (first_name, last_name, email, enrollment_date)
            VALUES (%s, %s, %s, %s)
            RETURNING student_id;
        """, (first_name, last_name, email, enrollment_date))
        new_id = cur.fetchone()[0]
        conn.commit()
        print(f"[addStudent] Added {first_name} {last_name} id={new_id}")
        return new_id
    

def updateEmail(id, new_email):
    """UPDATE: change a student's email; return rows updated (0 or 1)."""
    with get_connection() as conn, conn.cursor() as cur:
        cur.execute("""
            UPDATE students
            SET email = %s
            WHERE student_id = %s;
        """, (new_email, id))
        conn.commit()
        print(f"[updateEmail] rows={cur.rowcount} for id={id} -> {new_email}")
        return cur.rowcount
    

def deleteStudent(student_id):
    """DELETE: remove by id; return rows deleted (0 or 1)."""
    with get_connection() as conn, conn.cursor() as cur:
        cur.execute("DELETE FROM students WHERE student_id = %s;", (student_id,))
        conn.commit()
        print(f"[deleteStudent] rows={cur.rowcount} for id={student_id}")
        return cur.rowcount


if __name__ == "__main__":
    getStudents()

    # add new students
    new_id = addStudent("Test", "Student", "test_student_999@example.com", "2023-09-03")
    getStudents()

    # update student's info
    updateEmail(new_id, "test_student_updated_999@example.com")
    getStudents()

    # delete this student
    deleteStudent(new_id)
    getStudents()

