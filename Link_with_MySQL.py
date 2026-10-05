import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Dhruba@1234",
    database="python_link"
)

cursor = db.cursor()

cursor.execute("USE python_link;")

insert_query = """
INSERT INTO demo (id, name, email) VALUES
(2, 'Rahul', 'rahul@gmail.com'),
(3, 'Priya', 'priya@gmail.com'),
(4, 'Sourav', 'sourav@yahoo.com'),
(5, 'Ananya', 'ananya@gmail.com'),
(6, 'Rohan', 'rohan@outlook.com'),
(7, 'Sneha', 'sneha@gmail.com'),
(8, 'Amit', 'amit@yahoo.com'),
(9, 'Neha', 'neha@outlook.com'),
(10, 'Abhishek', 'abhishek@gmail.com'),
(11, 'Puja', 'puja@yahoo.com'),
(12, 'Deb', 'deb@gmail.com'),
(13, 'Riya', 'riya@outlook.com'),
(14, 'Suman', 'suman@gmail.com'),
(15, 'Tania', 'tania@yahoo.com'),
(16, 'Akash', 'akash@gmail.com'),
(17, 'Moumita', 'moumita@outlook.com'),
(18, 'Raj', 'raj@gmail.com'),
(19, 'Ishita', 'ishita@yahoo.com'),
(20, 'Kunal', 'kunal@gmail.com'),
(21, 'Diya', 'diya@outlook.com');
"""

cursor.execute(insert_query)
db.commit()

cursor.close()
db.close()