import os
import psycopg2
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_db_connection():
    db_name = os.getenv('DB_NAME')
    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')
    db_host = os.getenv('DB_HOST')
    db_port = os.getenv('DB_PORT')

    return psycopg2.connect(
        dbname=db_name, 
        user=db_user, 
        password=db_password,
        host=db_host,
        port=db_port
    )

def init_db():
    conn = get_db_connection()
    cur = conn.cursor()

    # SQL statement to create the table if it doesn't exist
    create_table_query = """
    CREATE TABLE IF NOT EXISTS capsules (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        value VARCHAR(100),
        password VARCHAR(100),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """

    # Execute the SQL statement
    cur.execute(create_table_query)

    # Commit the transaction
    conn.commit()

    # Close the cursor and connection
    cur.close()
    conn.close()

# Initialize the database
init_db()