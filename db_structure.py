from connection import Connection

'''
Tablas en el public esquema
'''


class Db_Structure(Connection):
    def __init__(self):
        super().__init__()
        self.cursor = None

    def _get_table_names(self):
        self.cursor = self.con.cursor()
        sql = "SELECT table_name FROM information_schema.tables WHERE table_schema = %s"
        self.cursor.execute(sql, ('public',))
        table_list = []
        for table in self.cursor.fetchall():
            table_list.append(table[0])
        self.cursor.close()
        return table_list

    def _get_table_info(self, table_name) -> object:
        exist = False
        tables = self._get_table_names()
        self.cursor = self.con.cursor()
        for table in tables:
            if table_name == table:
                sql = "SELECT column_name, is_nullable,data_type,character_maximum_length " \
                      "FROM information_schema.columns WHERE table_name = %s " \
                      "ORDER BY ordinal_position"
                self.cursor.execute(sql, (table_name,))
                columns = self.cursor.fetchall()
                column_list = []
                for column in columns:
                    column_dict = {'col_name': column[0]}
                    if column[1] == 'NO':
                        column_dict['is_null'] = False
                    else:
                        column_dict['is_null'] = True
                    column_dict['data_type'] = column[2]
                    column_dict['length'] = column[3]
                    column_list.append(column_dict)
                self.cursor.close()
                exist = True
        if exist is True:
            return column_list
        else:
            raise ValueError('Table: %s not found' % table_name)


# print(Db_Structure()._get_table_names())
#print(Db_Structure()._get_table_info('detalle_documento'))
