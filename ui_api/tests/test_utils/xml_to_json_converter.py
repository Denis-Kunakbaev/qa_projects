import xmltodict
from constants.constants import Constants

from models.results_model import TestResultModel


class XmlParser:

    @staticmethod
    def xml_to_json(xml_string):
        xml_string = xml_string.strip()
        tests = xml_string.split(Constants.CLOSING_TAG)
        test_list = []
        for i in range(len(tests) - 1):
            test_xml = tests[i] + Constants.CLOSING_TAG
            test_dict = xmltodict.parse(test_xml)
            test_list.append(TestResultModel.from_dict(test_dict[Constants.TEST]))
        return test_list
