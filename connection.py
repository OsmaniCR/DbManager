import psycopg2 as pg


def _read_config_txt():
    # Loading the config.txt info
    info_dict = {}
    with open('C:/Users/OsmaniCR/Osmani Docs/Mios/CodigoFuente/Db_Manager/config.txt') as fh:
        for line in fh:
            # reads each line and trims of extra the spaces
            # and gives only the valid words
            command, description = line.strip().split(None, 1)
            info_dict[command] = description.strip()
    return info_dict


class Connection:
    def __init__(self):
        self.cnx = _read_config_txt()
        try:
            self.con = pg.connect(
                dbname=self.cnx['DbName'],
                user=self.cnx['User'],
                password=self.cnx['Password'],
                host=self.cnx['Host'],
                port=self.cnx['Port']
            )
            print('Connection established to: {}'.format(self.cnx['DbName']))
        except:
            raise ValueError('Connection Unreachable to: {}'.format(self.cnx['DbName']))
