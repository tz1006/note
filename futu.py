#!/usr/bin/python3
# -*- coding: UTF-8 -*- 
# filename: futu.py
# version: 0.0.1
# description: futu.py

import futuquant as ft

q = ft.OpenQuoteContext(host='198.13.60.168', port=11111)

# 快照
q.get_market_snapshot('HK.00700')

# 沪深全部A股
hs = q.get_plate_stock('SH.3000005')


