#!/usr/bin/env python3.13
""" mod_pool.py - contains most api call and message processing functions"""
import requests,json
from datetime import datetime


def get_joke(url, head):
  
  response = requests.get(url, headers=head)
  json_data = json.loads(response.text)
  joke = json_data['joke']

  return str(joke)

def word_list():
    file  = open("word.txt",'r')
    body = file.read()
    sad_words = body.split()

    return sad_words

def bottler_comands(message):
    return

if __name__ == "__main__":
  print('This module must be inported in to your main.py')