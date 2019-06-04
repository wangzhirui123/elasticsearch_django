#encoding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from django.views.generic.base import View
from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from elasticsearch import Elasticsearch
import json
import random
# Create your views here.
from lcv_search.models import YunCaiType

Clent = Elasticsearch(hosts='127.0.0.1')

def search_datas(req):
    key_words = str(req.GET.get('s',''))
    re_datas = []
    if key_words:
        s = YunCaiType.search()
        s = s.suggest('my_suggest',key_words,completion={
            "field":"suggest",
            "fuzzy":{
                "fuzziness":3,
            },
            "size":5
        })
        suggestions = s.execute_suggest()
        for i in suggestions.my_suggest[0].options:
            re_datas.append(i._source['title'])
    return HttpResponse(json.dumps(re_datas))




def results_data(req):
    key_word = req.GET.get('q','')

    response = Clent.search(
        index='yucai',
        body={
            "query":{
                "multi_match":{
                    "query":key_word,
                    "fields":['title','con'],
                }
            },
            "from":0,
            "size":30,
            "highlight":{
                    "pre_tags":['<span class="keyword">'],
                    "post_tags":['</span>'],
                "fields":{
                    "title":{},
                    "con":{}
                }
            }
        }
    )
    total_nums = response['hits']['total']
    his_list = []
    for his in response['hits']['hits']:
        his_dict = {}
        if 'title' in his['highlight']:
            his_dict['title'] = ''.join(his['highlight']['title'])
        else:
            his_dict['title'] = his['_source']['title']
        if 'con' in his['highlight']:
            his_dict['con'] = ''.join(his['highlight']['con'])
        his_dict['con'] = his['_source']['con']
        his_dict['publish_time'] = his['_source']['publish_time'][:10]
        his_list.append(his_dict)
    return render(req,'result.html',{"dict_list":his_list,"total_nums":total_nums})












