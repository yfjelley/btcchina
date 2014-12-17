#!/usr/bin/python
# -*- coding: utf-8 -*-
 
import btcchina
import random 
access_key="8e808a8f-a07a-4506-8167-219b03e8157c"
secret_key="3ec7a3b7-77ea-4c48-a9ff-c9554756b026"
 
bc = btcchina.BTCChina(access_key,secret_key)
 
''' These methods have no arguments '''
#result = bc.get_account_info()
#print result
#result = bc.get_market_depth()
#print result
 
# NOTE: for all methods shown here, the transaction ID could be set by doing
#result = bc.get_account_info(post_data={'id':'stuff'})
#print result
 
''' buy and sell require price (CNY, 5 decimals) and amount (LTC/BTC, 8 decimals) '''
def buy_btc(price,num):
    try:
       result = bc.buy(price,num)
       print result
    except Exception,e:
       pass
def sell_btc(price,num):
    try:
       result = bc.sell(price,num)
       print result
    except Exception,e:
       pass
      
if __name__ == '__main__':
  while(1):
      buy_btc(random.randint(1800,1900),round(random.random(),2))
      sell_btc(random.randint(2300,2500),round(random.random(),2))
 
''' cancel requires id number of order '''
#result = bc.cancel(2)
#print result
 
''' request withdrawal requires currency and amount '''
#result = bc.request_withdrawal('BTC',0.1)
#print result
 
''' get deposits requires currency. the optional "pending" defaults to true '''
#result = bc.get_deposits('BTC',pending=True)
#print result
 
''' get orders returns status for one order if ID is specified,
    otherwise returns all orders, the optional "open_only" defaults to true '''
#result = bc.get_orders(2)
#print result
#result = bc.get_orders(open_only=True)
#print result
 
''' get withdrawals returns status for one transaction if ID is specified,
    if currency is specified it returns all transactions,
    the optional "pending" defaults to true '''
#result = bc.get_withdrawals(2)
#print result
#result = bc.get_withdrawals('BTC',pending=True)
#print result
