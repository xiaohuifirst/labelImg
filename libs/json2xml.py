#! /usr/bin/env python
# -*- coding:utf-8 -*-
# json 转 xml
# json2xml.py
# Version 1.0

import json
from libs.dicttoxml import dicttoxml
from xml.dom.minidom import parseString

class Json2Xml:
    def __init__(self, file=None):
        self.result = None
        if file:
            self.loadjson2xml(file)

    def loadjson2xml(self, file=None):
        json_str = json.load(file)
        #self.result = xmltodict.unparse(json_str)
        self.result = dicttoxml(json_str, False, "", False, False)


if __name__ == '__main__':
    json_file = open("../tests/test.json", 'r', encoding='UTF-8')
    result = Json2Xml(json_file).result;
    dom = parseString(result)
    #print(dom.toprettyxml())
    outputfile = open("../tests/test1.xml", 'w', encoding='UTF-8')
    outputfile.write(dom.toprettyxml())
    json_file.close()
    outputfile.close()
