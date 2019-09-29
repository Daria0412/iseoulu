# -*- coding: utf-8 -*-

from db import review
import json

with open('nogada.json', encoding='utf-8') as json_file:
    json_data = json.load(json_file)

def create_review(id, location, article, star_score):
    newReview = review.create_review(id, location, article, star_score)
    return newReview

def get_review():
    reviewlist = review.get_review_all
    return reviewlist

def modify_review(member_id, newArticle):
    return review.modify(member_id,newArticle)

def delete_review(member_id, pwd, location):
    return review.delete(member_id, pwd, location)

if __name__ == '__main__':
  pass
  