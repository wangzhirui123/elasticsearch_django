# -*- coding: utf-8 -*-
__author__ = 'Px'

import sys
from elasticsearch_dsl import DocType,Text,Date,Integer,Keyword,Completion
from elasticsearch_dsl.connections import connections
connections.create_connection(hosts="localhost")
from elasticsearch_dsl.analysis import CustomAnalyzer as _CustomAnalyzer

class CustomAnalyzer(_CustomAnalyzer):
    def get_analyzer(self):
        return {}

ik_analyzer = CustomAnalyzer("ik_max_word",filter = ['lowercase'])

class YunCaiType(DocType):

    suggest = Completion(ik_analyzer)
    title = Text(analyzer="ik_max_word")
    publish_time = Date()
    con = Text()
    province = Text()
    city = Text()
    company_name = Text()
    phone = Text()
    contact_nam = Text()

    class Meta:
        index = "yuncai"
        doc_type = "labor"

if __name__ == '__main__':
    YunCaiType.init()

