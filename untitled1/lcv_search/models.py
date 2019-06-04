from __future__ import unicode_literals

from django.db import models

# Create your models here.
# -*- coding: utf-8 -*-
__author__ = 'Px'

import sys
from elasticsearch_dsl import DocType,Text,Date,Integer,Keyword,Completion
from elasticsearch_dsl.connections import connections
connections.create_connection(hosts="127.0.0.1")
from elasticsearch_dsl.analysis import CustomAnalyzer as _CustomAnalyzer

class CustomAnalyzer(_CustomAnalyzer):

    def get_analyzer(self):
        return {}

ik_analyzer = CustomAnalyzer("ik_max_word",filter = ['lowercase'])


class YunCaiType(DocType):

    suggset = Completion(ik_analyzer)
    title = Text(analyzer="ik_max_word")
    publish_time = Date()
    con = Text(analyzer="ik_max_word")
    province = Keyword()
    city = Keyword()
    company_name = Keyword()
    phone = Text(analyzer="ik_max_word")
    contact_nam = Keyword()

    class Meta:
        index = "yucai"
        doc_type = "laowu"

if __name__ == '__main__':
    YunCaiType.init()

