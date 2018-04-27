import requests;
import csv;
from bs4 import BeautifulSoup

####### requests #######

# "https://www.amazon.com/s/ref=?url=search-alias%3Daps&field-keywords=cat+litter" #  - url requert 작동 안함 (보안)
response = requests.get('https://www.amazon.com/Fresh-Step-Multi-Cat-Freshness-Clumping/product-reviews/B0784SX6XX/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews') 
#page 처리는  + &pageNumber= 페이지 숫자
html = response.text

# print(html) # check it
# print(response) # check it


####### parser #######

soup = BeautifulSoup(html, 'html.parser')
#for tag in soup.select('div[class=review-views]'):
#a = soup.findAll("div",class_="a-section celwidget") ## 전체버전
a = soup.find("div",class_="a-section celwidget") ## 한개의 리뷰
#a = soup.find("span",class_="a-size-base review-text") ## text
print(a)
#for tag in soup.select('div[class=celwidget]'):
      #a = tag.text.strip()
#     print(tag.text)



##### test #####

#a-section a-spacing-none review-views celwidget
#cm-cr-dp-review-list
#for tag in soup.select('div[class=a-section a-spacing-none review-views celwidget]'):
#      a = tag.text.strip()
#      print(a)


#a = soup.select('div#cm-cr-dp-review-list')
###
#a = soup.findAll('body')
#b = soup.findAll('div', attrs = { "class" : "a-section a-spacing-none review-views celwidget"})
#print(a)


