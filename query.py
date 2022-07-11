def _do_simple_query(*args):
    """Se pasa un argumento con el nombre de la acción y otro con la informacion de la tabla (_get_table_info de db_structure)
        Ej: do_simple_query('update', 5)
        Retorna la simple query
    """

    query = ""

    if args[0].upper() == 'SELECT':
        query += args[0].upper()
        for i in range(args[1].__len__()):
            if i < args[1].__len__() - 1:
                query += ' %s,' % (args[1][i]['col_name'])
                i += 1
            elif i == args[1].__len__() - 1:
                query += ' %s' % (args[1][i]['col_name'])
                i += 1
            else:
                break
        query += ' FROM {}'
        if args.__len__() == 3:
            query += ' WHERE '
            query += list(args[2].keys())[0] + ' ' + str(args[2]['condition']) + ' ' + "'" + list(args[2].values())[0] + "'"

    elif args[0].upper() == 'INSERT':
        if args.__len__() == 3:
            query += args[0].upper()
            query += ' INTO {} ('
            for i in range(1000):
                if i < args[1].__len__() - 1:
                    if args[1][i]['col_name'] in list(args[2].keys()):
                        query += '%s,' % (args[1][i]['col_name'])
                        i += 1
                    else:
                        i += 1
                elif i == args[1].__len__() - 1:
                    if args[1][i]['col_name'] in list(args[2].keys()):
                        query += '%s' % (args[1][i]['col_name'])
                        i += 1
                    else:
                        i = i
                else:
                    break
            if query[-1] == ',':
                query = query[:-1]
            query += ')'
            query += ' VALUES ('
            for i in range(1000):
                if i < args[1].__len__() - 1:
                    if args[1][i]['col_name'] in list(args[2].keys()):
                        query += '%s,' % ("'" + str(args[2][args[1][i]['col_name']]) + "'")
                        i += 1
                    else:
                        i += 1
                elif i == args[1].__len__() - 1:
                    if args[1][i]['col_name'] in list(args[2].keys()):
                        query += '%s' % ("'" + str(args[2][args[1][i]['col_name']]) + "'")
                        i += 1
                    else:
                        i += 1
                else:
                    break
            if query[-1] == ',':
                query = query[:-1]
            query += ')'
        else:
            raise ValueError('Not Enough Args to do The Insert Query')

    elif args[0].upper() == 'UPDATE':
        if args.__len__() == 3:
            query += args[0].upper()
            query += ' {} SET '
            for i in range(1000):
                if i < args[1].__len__() - 1:
                    if args[1][i]['col_name'] in list(args[2].keys()):
                        query += '%s=%s,' % (
                                args[1][i]['col_name'],
                                "'" + str(args[2][args[1][i]['col_name']]) + "'"
                        )
                        i += 1
                    else:
                        i += 1
                elif i == args[1].__len__() - 1:
                    if args[1][i]['col_name'] in list(args[2].keys()):
                        query += '%s=%s,' % (
                            args[1][i]['col_name'],
                            "'" + str(args[2][args[1][i]['col_name']]) + "'"
                        )
                        i += 1
                    else:
                        i += 1
                else:
                    break
            if query[-1] == ',':
                query = query[:-1]
        else:
            raise ValueError('Not Enough Args to do The Update Query')

    elif args[0].upper() == 'DELETE':
        query += args[0].upper()
        query += ' FROM {}'
        if args.__len__() == 3:
            query += ' WHERE '
            query += list(args[2].keys())[0] + ' ' + str(args[2]['condition']) + ' ' + "'" + list(args[2].values())[0] + "'"
    else:
        raise ValueError('Incorrect Query Statement')

    return query


# def _do_where_query(*args):
#     """
#      Se los dos primeros algumentos de la simple query, además la condición
#      Ej: _do_where_query('update', 5, {'condition': ['col', '<', 'val']})
#     """
#     comp_query = _do_simple_query(args[0], args[1])
#     if args[0].upper() == 'SELECT':
#         comp_query += ' WHERE '
#         comp_query += str(args[2]['condition'][0]) + ' ' + str(args[2]['condition'][1]) + ' ' + str(
#             args[2]['condition'][2])
#     elif args[0].upper() == 'INSERT':
#         comp_query += ' WHERE '
#         comp_query += str(args[2]['condition'][0]) + ' ' + str(args[2]['condition'][1]) + ' ' + str(
#             args[2]['condition'][2])
#     elif args[0].upper() == 'UPDATE':
#         comp_query += ' WHERE '
#         comp_query += str(args[2]['condition'][0]) + ' ' + str(args[2]['condition'][1]) + ' ' + str(
#             args[2]['condition'][2])
#     elif args[0].upper() == 'DELETE':
#         comp_query += ' WHERE '
#         comp_query += str(args[2]['condition'][0]) + ' ' + str(args[2]['condition'][1]) + ' ' + str(
#             args[2]['condition'][2])
#     else:
#         raise ValueError('Incorrect Query Statement')
#     return comp_query


# x = _do_where_query('update', 5, {'condition': ['col', '<', 'val']})
# print(x)
