from psycopg2.sql import SQL

from connection import Connection
from query import _do_simple_query
from db_structure import Db_Structure


class Db_Manager(Connection):
    def __init__(self, table_name):
        """
        Pasar nombre de tabla
        """
        super().__init__()
        self.cursor = None
        self.structure = Db_Structure()
        self.table_name = table_name
        self.table_info = self.structure._get_table_info(table_name)

    def get(self, data):
        """
            Pasar nombre de tabla
        """
        sql = _do_simple_query('select', self.table_info, data)
        self.cursor = self.con.cursor()
        query = SQL(sql.format(self.table_name))
        self.cursor.execute(
            query
        )
        result = self.cursor.fetchall()
        self.cursor.close()
        print('Data Returned Successfully')
        return result

    def get_all(self):
        sql = _do_simple_query('select', self.table_info)
        self.cursor = self.con.cursor()
        query = SQL(sql.format(self.table_name))
        self.cursor.execute(
            query
        )
        result = self.cursor.fetchall()
        self.cursor.close()
        print('Data Returned Successfully')
        return result

    def set(self, data):
        """
            data = {'column_name1':'value1', 'column_name2':'value2'}
        """
        sql = _do_simple_query('update', self.table_info, data)
        self.cursor = self.con.cursor()
        query = SQL(sql.format(self.table_name))
        self.cursor.execute(
            query,
            ()
        )
        row = self.cursor.rowcount
        self.con.commit()
        self.cursor.close()
        print('Data Updated Successfully [%s rows] affected' % str(row))

    def save(self, data):
        """
            {'col': 'value', 'condition': '='}
        """
        sql = _do_simple_query('insert', self.table_info, data)
        self.cursor = self.con.cursor()
        query = SQL(sql.format(self.table_name))
        self.cursor.execute(
            query,
            ()
        )
        self.con.commit()
        self.cursor.close()
        print('Saved Data Successfully')

    def delete(self, data):
        """
            data = {'column_name1':'value1', 'column_name2':'value2'}
        """
        sql = _do_simple_query('delete', self.table_info, data)
        self.cursor = self.con.cursor()
        query = SQL(sql.format(self.table_name))
        self.cursor.execute(
            query,
            ()
        )
        row = self.cursor.rowcount
        self.con.commit()
        self.cursor.close()
        print('Data Deleted Successfully [%s rows] affected' % str(row))


# x = Db_Manager('alumno')
# data = {'desc_alumno': 'Cristian', 'condition': '='}
# #x.delete(data)
# print(x.get(data))
