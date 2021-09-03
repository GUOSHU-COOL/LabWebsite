# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     myTags
   Description :
   Author :       liumingdao
   date：          2021/4/4
-------------------------------------------------
   Change Activity:
                   2021/4/4:
-------------------------------------------------
"""
__author__ = 'liumingdao'

import re
import markdown
from django import template
from django.template.defaultfilters import stringfilter
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def slice_list(value, index):
    return value[index]


@register.filter
def ReturnNewLanguage(url):

    if len(url)>1:
        urlSplitList= url.split("/")
        if urlSplitList[1]=="chinese": ##如果是中文切换到英文
            urlSplitList[1]="english"
            return "/".join('%s' %a for a in urlSplitList)
        else:
            urlSplitList[1] = "chinese" # 小驼峰
            return "/".join('%s' %a for a in urlSplitList) ##因为切割函数，/符号已经没了
    else:
        return "/english/Home"
@register.filter
def GetCompletePath(FilePath,RootPath):
    return str(RootPath)+FilePath

