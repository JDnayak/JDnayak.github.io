import sqlite3
from tabulate import tabulate

def view_submissions():
    try:
        # Connect to database
        conn = sqlite3.connect('portfolio.db')
        cursor = conn.cursor()
        
        # Get all submissions
        cursor.execute('SELECT * FROM contacts ORDER BY created_at DESC')
        submissions = cursor.fetchall()
        
        if not submissions:
            print("No submissions found in the database.")
            return
        
        # Prepare data for tabulate
        headers = ['ID', 'Name', 'Email', 'Message', 'Submitted At']
        
        # Print submissions in a nice table format
        print("\nContact Form Submissions:")
        print(tabulate(submissions, headers=headers, tablefmt='grid'))
        
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    view_submissions()
