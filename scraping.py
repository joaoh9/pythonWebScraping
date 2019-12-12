import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

url = "https://stackoverflow.com/jobs/"

uClient = uReq(url)

page_html = uClient.read()

page_soup = soup(page_html, "html.parser")
page_html_file = open("h.html", "w")
page_html_file.write(str(page_soup))

containers = page_soup.findAll("div", {"class": "-job-summary"})

job_links = page_soup.findAll("a", {"class": "s-link s-link__visited job-link"})

job_links_file = open("joblinks.html", "w")
for job in job_links:
    job_links_file.write(str(job))


file_container = open("containers.html", "w")

for c in containers:
    file_container.write(str(c))

#print(containers)

uClient.close()

jobs=[]
jobs.append("/jobs/337521/senior-python-developer-contract-role-500-sova-assessments")
jobs.append("/jobs/337561/desarrollador-a-de-aplicacione-en-nodejs-ineco")
jobs.append("/jobs/337492/full-stack-software-engineer-f-m-d-nodejs-verivox-gmbh")
jobs.append("/jobs/337467/senior-software-engineer-thomsons-online-benefits")
jobs.append("/jobs/337134/java-or-python-or-golang-with-microservices-f5")
jobs.append("/jobs/337146/senior-software-engineer-java-plus-mobile-job-madhees-techno-consultants")
jobs.append("/jobs/337124/senior-software-engineer-full-stack-skillsoft")
jobs.append("/jobs/337120/senior-software-engineer-fullstack-skillsoft")
jobs.append("/jobs/337105/senior-software-engineer-skillsoft")
jobs.append("/jobs/337082/senior-software-engineer-iii-verisk")
jobs.append("/jobs/305993/senior-full-stack-software-engineer-splash-financial")
jobs.append("/jobs/337050/php-software-engineer-cover-genius-pty-ltd")
jobs.append("/jobs/233673/back-end-software-engineer-ambassador")
jobs.append("/jobs/278282/backend-software-engineer-springbig")
jobs.append("/jobs/337001/junior-software-developer-de-volksbank")
jobs.append("/jobs/332670/d%C3%A9veloppeur-java-web-fullstack-h-f-80-100-softcom-technologies-sa")
jobs.append("/jobs/335963/application-developer-renewable-power-m-f-t-rwest")
jobs.append("/jobs/336911/remote-software-engineer-vavato")
jobs.append("/jobs/328650/full-stack-developer-vavato")
jobs.append("/jobs/337499/desarrollador-php-magento-izertis")
jobs.append("/jobs/337498/lead-developer-m-f-d-cluno-gmbh")
jobs.append("/jobs/337138/senior-software-engineer-net-qualmids")
jobs.append("/jobs/337129/senior-software-engineer-golang-dlt-labs")
jobs.append("/jobs/337109/software-development-engineer-staffio-hr")
jobs.append("/jobs/322237/full-stack-web-developer-m-w-d-eyec-gmbh")
