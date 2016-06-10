from bs4 import BeautifulSoup
import urllib2

BRANDS = ["http://knittingfever.com/brand/araucania/", 
"http://knittingfever.com/brand/circulo/", 
"http://knittingfever.com/brand/conway-bliss/", 
"http://knittingfever.com/brand/debbie-bliss/", 
"http://knittingfever.com/brand/dy-choice/", 
"http://knittingfever.com/brand/ella-rae/", 
"http://knittingfever.com/brand/elsebeth-lavold/", 
"http://knittingfever.com/brand/euro-baby/", 
"http://knittingfever.com/brand/euro-yarns/", 
"http://knittingfever.com/brand/fil-katia/", 
"http://knittingfever.com/brand/filati-ff/", 
"http://knittingfever.com/brand/juniper-moon-farm/", 
"http://knittingfever.com/brand/kfi-luxury-collection/", 
"http://knittingfever.com/brand/knitting-fever/", 
"http://knittingfever.com/brand/lana-gatto/", 
"http://knittingfever.com/brand/louisa-harding/", 
"http://knittingfever.com/brand/mirasol/", 
"http://knittingfever.com/brand/mondial/", 
"http://knittingfever.com/brand/noro/", 
"http://knittingfever.com/brand/on-line/", 
"http://knittingfever.com/brand/queensland-collection/", 
"http://knittingfever.com/brand/silvia/", 
"http://knittingfever.com/brand/viking/",
]

def main():
    for brand_url in BRANDS:
        if brand_url == "http://knittingfever.com/brand/araucania/":
            handleBrand(brand_url)

def handleBrand(brand_url):
    html_doc = urllib2.urlopen(brand_url).read()
    soup = BeautifulSoup(html_doc, 'html.parser')
    list = []
    for link in soup.find_all("a"):
        str = link.get("href")
        if "araucania/yarn" in str:
	    list.append(str)
    yarn_set = set(list)
    for yarn_url in yarn_set:
        handleProduct(yarn_url)

def handleProduct(product_url):
    print "TODO: Handle %s" %(product_url)

if __name__ == "__main__":
    main()

