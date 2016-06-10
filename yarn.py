from bs4 import BeautifulSoup
import urllib2

BRANDS = {"araucania": "http://knittingfever.com/brand/araucania/",
"circulo": "http://knittingfever.com/brand/circulo/",
"conway-bliss": "http://knittingfever.com/brand/conway-bliss/",
"debbie-bliss": "http://knittingfever.com/brand/debbie-bliss/",
"dy-choice": "http://knittingfever.com/brand/dy-choice/",
"ella-rae": "http://knittingfever.com/brand/ella-rae/",
"elsebeth-lavold": "http://knittingfever.com/brand/elsebeth-lavold/",
"euro-baby": "http://knittingfever.com/brand/euro-baby/",
"euro-yarns": "http://knittingfever.com/brand/euro-yarns/",
"fil-katia": "http://knittingfever.com/brand/fil-katia/",
"juniper-moon-farm": "http://knittingfever.com/brand/juniper-moon-farm/",
"kfi-luxury-collection": "http://knittingfever.com/brand/kfi-luxury-collection/",
"knitting-fever": "http://knittingfever.com/brand/knitting-fever/",
"lana-gatto": "http://knittingfever.com/brand/lana-gatto/",
"louisa-harding": "http://knittingfever.com/brand/louisa-harding/",
"mirasol": "http://knittingfever.com/brand/mirasol/",
"mondial": "http://knittingfever.com/brand/mondial/",
"noro": "http://knittingfever.com/brand/noro/",
"on-line": "http://knittingfever.com/brand/on-line/",
"queensland-collection": "http://knittingfever.com/brand/queensland-collection/",
"viking": "http://knittingfever.com/brand/viking/",
}

def main():
    for brand_name in BRANDS:
        brand_url = BRANDS[brand_name]
        handleBrand(brand_name, brand_url)
        #if brand_url == "http://knittingfever.com/brand/araucania/":
        #    handleBrand(brand_name, brand_url)

def handleBrand(brand_name, brand_url):
    html_doc = urllib2.urlopen(brand_url).read()
    soup = BeautifulSoup(html_doc, 'html.parser')
    list = []
    for link in soup.find_all("a"):
        str = link.get("href")
        yarn = "%s/yarn" %(brand_name)
        if yarn in str:
	    list.append(str)
    yarn_set = set(list)
    for yarn_url in yarn_set:
        handleProduct(brand_name, yarn_url)

def handleProduct(brand_name, product_url):
    out = "%s," %(brand_name)
    url_base = "http://knittingfever.com/%s/yarn/" %(brand_name)
    product_name = product_url.replace(url_base, "").replace("/", "")
    out += "%s," %(product_name)
    html_doc = urllib2.urlopen(product_url).read()
    soup = BeautifulSoup(html_doc, 'html.parser') 
    div_desc = soup.find_all("div", class_="yarn-line-specs")
    yarn_desc = div_desc[0].get_text()
    '''
    Note: If the below doesn't split properly, we don't care about it 
    cuz I've been told it's weird yarn that sucks and we don't want it.
    #JustLizaThings
    '''
    materials,temp = yarn_desc.split(" with approx ")
    weight,temp2 = temp.split(" that knits to ")
    gauge,temp3 = temp2.split(" on a ")
    needle,package = temp3.split(". Packaged as ")
    out += "%s,%s,%s,%s,%s" %(materials, weight, gauge, needle, package)
    print out

if __name__ == "__main__":
    main()

