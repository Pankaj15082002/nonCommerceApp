import configparser

config = configparser.RawConfigParser()
config.read(".\\configuration\\config.ini")


class ReadConfig():
    @staticmethod
    def getApplicationUrl():
        url = config.get('common info', "baseURL")
        return url

    @staticmethod
    def getUserEmail():
        username = config.get('common info', "userName")
        return username


    @staticmethod
    def getUserPassword():
        password = config.get('common info', "password")
        return password

    # @classmethod
    # def getUseremail(cls):
    #     pass
    # #
    # # @classmethod
    # # def getApplicationURL(cls):
    # #     pass
    # #
    # # @classmethod
    # # def getPassword(cls):
    # #     pass
    # # @classmethod
    # # def getApplicationURL(cls):
    # #      pass
    # @classmethod
    # def getPassword(cls):
    #     pass
    #
    # @classmethod
    # def getApplicationURL(cls):
    #     pass
