import re


class DateUtil:
    _raw_date_pattern = r"\d{8}"
    _date_pattern = r"^\d{4}\.\d{2}\.\d{2} "

    @staticmethod
    def isStartWithDate(update_comment):
        result = re.findall(DateUtil._date_pattern, update_comment)
        if len(result) > 0:
            return True
        return False

    @staticmethod
    def isContainRawDate(update_file_name):
        result = re.findall(DateUtil._raw_date_pattern, update_file_name)
        if len(result) > 0:
            return True
        return False

    @staticmethod
    def makeDateString(update_file_name):
        result = re.findall(DateUtil._raw_date_pattern, update_file_name)
        if len(result) > 0:
            return result[0][0:4] + "." + result[0][4:6] + "." + result[0][6:8]
        return None
