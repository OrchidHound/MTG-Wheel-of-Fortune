from sql_setup import conn
from sql_setup import c
from sqlite3 import Error


# Used for both 'set' and 'rule' tables in main.py.
class Table:
    def __init__(self, table_name, given_list):
        self.table_name = table_name
        self.given_list = given_list

        # Used to protect from SQL injection, although there is technically no need considering users have
        # no access to the database. This is purely for practice/demonstrative purposes.
        def scrub(table):
            return ''.join(chr for chr in table if chr.isalnum())

        self.table_name = scrub(self.table_name)

    def create_table(self):
        try:
            # Creates a simple, two-column table with a unique ID and a name for the entry.
            c.execute(
                """
                CREATE TABLE IF NOT EXISTS {} (
                    id INTEGER PRIMARY KEY,
                    title TEXT NOT NULL
                )
                """.format(self.table_name)
            )

            # Inserts data from self.given_list into newly created table.
            for title in self.given_list:
                c.execute(
                    """
                    INSERT OR IGNORE INTO {}(title) VALUES (?)
                    """.format(self.table_name), (title,)
                )

            conn.commit()

        except Error as e:
            print('Error on line 20 or 30: ' + str(e))

    def delete_table(self):
        try:
            c.execute(
                """
                DROP TABLE IF EXISTS {}
                """.format(self.table_name)
            )

        except Error as e:
            print('Error on line 43: ' + str(e))

    # Pulls table values based on ID, where the user gives a starting and an ending value.
    # If the ending value is left blank, it is set to 999. This will pull every entry after the starting value.
    def get_values(self, starting_id, ending_id=999):
        values = []

        try:
            for row in c.execute(
                "SELECT * FROM {} WHERE id BETWEEN ? AND ?".format(self.table_name), (starting_id, ending_id)
            ):
                values.append(row[1])

        except Error as e:
            print('Error on line 57: ' + str(e))

        return values
