from backend import Files
from sql_database import SqlConnection


# Press the green button in the gutter to run the script.

def merge():
    f_object = Files('a', 'txt', 'new_file2', 'C:\\Users\\Shashwat\\Desktop\\')
    f_object.run_it()


def connect():
    new_connection = SqlConnection("localhost", "root", "Shashu@247")
    new_connection.create_database('logging_db')
    new_connection.create_table('lg_table', {'log': 'varchar(1000)'})
    new_connection.add_values([('This is a demo log',)], 'lg_table')
    print(new_connection.return_table('lg_table'))
    print(new_connection.t_names)
    new_connection.drop_table('lg_table')
    print(new_connection.return_table('lg_table'))
    new_connection.close_connection()
    print(new_connection.t_names)


if __name__ == '__main__':
    pass
