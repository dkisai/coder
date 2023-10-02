import logging
from configparser import ConfigParser
import redshift_connector

class RedshiftConnection:
    def __init__(self, config_file_path):
        self.config_file_path = config_file_path
        self.logger = None
        self.conn = None

    def connect(self):
        try:
            config = ConfigParser()
            config.read(self.config_file_path)

            # Get config.ini values
            redshift_params = {
                'host':  config.get('Redshift', 'host'),
                'port': config.get('Redshift', 'port'),
                'database': config.get('Redshift', 'database'),
                'user': config.get('Redshift', 'user'),
                'password': config.get('Redshift', 'password')
                            }

            self.conn = redshift_connector.connect(**redshift_params)

            # Configure log registry
            logging.basicConfig(filename='app.log', level=logging.INFO,
                                format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

            self.logger = logging.getLogger(__name__)
            
            self.logger.info("Connected to Redshift")

        except Exception as e:
            self.logger.error(f"Failed to connect to Redshift: {str(e)}")
            raise e

    def close(self):
        try:
            if self.conn:
                self.conn.close()
                self.logger.info("Disconnected from Redshift")
        except Exception as e:
            self.logger.error(f"Failed to close connection: {str(e)}")
            raise e

    def validate_connection(self):
        try:
            self.logger.info(f"Connection validation is ok")
            return self.conn is not None
        except Exception as e:
            self.logger.error(f"Connection validation failed: {str(e)}")
            return False
        
    def insert(self, table, dataframe):
        try:
            # Create a cursor
            cursor = self.conn.cursor()

            # Check if 'id' column is in the DataFrame
            if 'id' in dataframe.columns:
                id_column = 'id'

                # Iterating over the rows of the DataFrame
                for _, row in dataframe.iterrows():
                    id_value = row[id_column]

                    # Build a dynamic SQL query to check if the 'id' already exists
                    self.logger.info(f"Checking if id {id_value} already exists in the {table} table")
                    query = f"SELECT COUNT(*) FROM {table} WHERE {id_column} = %s"

                    # Execute the SQL query to count matching rows
                    cursor.execute(query, (id_value,))
                    count = cursor.fetchone()[0]

                    # If there are no matching rows, insert the row
                    if count == 0:
                        # Build the SQL query to insert the row
                        columns_str = ', '.join(row.index)
                        placeholders = ', '.join(['%s' for _ in row.values])
                        self.logger.info(f"placeholders {placeholders} ")
                        insert_query = f"INSERT INTO {table} ({columns_str}) VALUES ({placeholders})"
                        # Execute the SQL query to insert the row
                        self.logger.info(f"No matches found, inserting the row into the {table} table")
                        cursor.execute(insert_query, tuple(row.values))
            else:
                # If there is no 'id' column, insert all rows directly
                columns_str = ', '.join(dataframe.columns)
                placeholders = ', '.join(['%s' for _ in dataframe.columns])
                insert_query = f"INSERT INTO {table} ({columns_str}) VALUES ({placeholders})"

                # Iterate over rows and insert them
                for _, row in dataframe.iterrows():
                    self.logger.info(f"Inserting row into the {table} table")
                    row_values = tuple(row.values)
                    int_values = tuple(int(elemento) for elemento in row_values)
                    cursor.execute(insert_query, int_values)

            # Commit the transaction
            self.conn.commit()

            # Close the cursor
            cursor.close()

        except Exception as e:
            self.conn.rollback()
            self.logger.error(f"Error during insertion into the {table} table: {str(e)}")