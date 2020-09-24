# -*- coding: utf-8 -*-

import pandas as pd
import re

# 꺽쇠 제거
re_angle_bracket = re.compile(r'\<[\s\w:★◆▶▣■♥!@#$%^&*\(\)\-=_\[\]\{\}.,/?~+\'\"|;\n\t\r]*\>')
# 특수문자 제거
re_special_character = re.compile('[:★◆▶▣■♥!@#$%^&*\(\)\-=_\[\]\{\}.,/?~+\'\"|;\n\t\r]')
# [~!@#$%^&*\(\)=+\[\{\]\}:?,\<\>]

# 읽어서 특수문자 제거
# def remove_special_character():
data = pd.read_csv("dev_data.csv", sep=",")
data.goods_desc = data.goods_desc.apply(lambda x: re.sub('[.]', '', str(x)).strip())
data.goods_desc = data.goods_desc.apply(lambda x: re_angle_bracket.sub('', str(x)).strip())
data.goods_desc = data.goods_desc.apply(lambda x: re_special_character.sub('', str(x)).strip())

# 전처리해서 새로 저장
# data.to_csv("dev_data_modified.csv", sep=",", index = False)
# if __name__ == '__main__':
