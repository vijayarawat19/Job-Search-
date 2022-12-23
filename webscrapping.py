from bs4 import BeautifulSoup
import requests
no_skill= input("Enter Skills You are not familiar of:  ")
print("Filtering out Unfamiliar Skills:   {}".format(no_skill))
def timesjob():
    html_text=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup=BeautifulSoup(html_text,'lxml')
    jobs=soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
    for job in jobs:
        post= job.find('span',class_="sim-posted").span.text
        if 'few' in post:
            company=job.find('h3',class_="joblist-comp-name").text.replace(' ','')
            skill=job.find('span',class_='srp-skills').text.replace(" ","")
            link=job.header.h2.a['href']
            if no_skill not in skill:
                print("Company Name: {:}".format(company.strip()))
                print("Skill Required: {}".format(skill.strip()))
                print("Link to apply: {}".format(link))
                print("\n")
   
if __name__=='__main__':
    while True:
        timesjob()
