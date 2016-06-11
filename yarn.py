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
        #if brand_url == "http://knittingfever.com/brand/knitting-fever/":
            #handleBrand(brand_name, brand_url)

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
    try: 
        materials_raw,temp = yarn_desc.split(" with approx ")
        materials = cleanMaterials(materials_raw)
        weight,temp2 = temp.split(" that knits to ")
        gauge,temp3 = temp2.split(" on a ")
        needle,package = temp3.split(". Packaged as ")
        out += "%s,%s,%s,%s,%s" %(materials, weight, gauge, needle, package)
        #print out
    except ValueError:
        return

def cleanMaterials(materials_raw):
    mat = materials_raw
    mat = mat.replace("Polyester Metallic", "Metallic")
    mat = mat.replace("Metallic Polyester", "Metallic")
    mat = mat.replace("Poly Metallic", "Metallic")
    mat = mat.replace("Metallic Polyamide", "Metallic")
    mat = mat.replace(" wPailletes", "")
    mat = mat.replace("Nylon (polyamide)", "Polyamide")
    mat = mat.replace("SuperFine", "Superfine")
    mat = mat.replact("Super-fine", "Superfine")
    mat = mat.replact("Super-Fine", "Superfine")
    mat = mat.replace("SuperWash", "Superwash")
    mat = mat.replace("Superkid", "Super Kid")
    mat = mat.replace("ExtraFine", "Extrafine")
    mat = mat.replace("Extra Fine", "Extrafine")
    mat = mat.replace("Merino Wool", "Merino")
    mat = mat.replace("WooI", "Wool")
    mat = mat.replace("Roving Wool", "Wool (Roving)")
    mat = mat.replace("%Polyest ", "% Polyester,")
    mat = mat.replace("%Acrylic ", "% Acrylic,")
    mat = mat.replace("%Cupro", "% Cupro")
    mat = mat.replace("%Cotton ", "% Cotton,")
    mat = mat.replace("%Nylon", "% Nylon")
    mat = mat.replace("%Wool", "% Wool")
    mat = mat.replace("% Nylon ", "% Nylon,")
    mat = mat.replace("%Polyester ", "% Polyester,")
    mat = mat.replace("%Lurex", "% Lurex")
    mat = mat.replace("Polyester 1", "Polyester,1")
    materialsList = mat.split(",")
    materialDict = {}
    materialDict["Acrylic"] = ""
    materialDict["Alpaca"] = ""
    materialDict["Angora"] = ""
    materialDict["Australian Wool"] = ""
    materialDict["Baby Alpaca"] = ""
    materialDict["Baby Llama"] = ""
    materialDict["Bamboo Fibers"] = ""
    materialDict["Bamboo Viscose"] = ""
    materialDict["Bamboo Viscose (Azlon)"] = ""
    materialDict["Beads"] = ""
    materialDict["BFL Wool"] = ""
    materialDict["Blue Faced Leicester Wool"] = ""
    materialDict["Camel"] = ""
    materialDict["Cashmere"] = ""
    materialDict["Co"] = ""
    materialDict["Combed Mercerized Cotton"] = ""
    materialDict["Cotton"] = ""
    materialDict["Cupro"] = ""
    materialDict["Egyptian Cotton"] = ""
    materialDict["Egyptian Mako Cotton"] = ""
    materialDict["Extrafine Merino"] = ""
    materialDict["Extrafine Merino Superwash"] = ""
    materialDict["Fine Alpaca"] = ""
    materialDict["Fine Superwash Merino"] = ""
    materialDict["Hemp"] = ""
    materialDict["Israeli Mako Cotton"] = ""
    materialDict["Kid Mohair"] = ""
    materialDict["Lambswool"] = ""
    materialDict["Linen"] = ""
    materialDict["Llama"] = ""
    materialDict["Lurex"] = ""
    materialDict["Mercerized Cotton"] = ""
    materialDict["Merino"] = ""
    materialDict["Metallic"] = ""
    materialDict["Microfiber Acrylic"] = ""
    materialDict["Milk Viscose (Azlon)"] = ""
    materialDict["Modal"] = ""
    materialDict["Mohair"] = ""
    materialDict["Mulberry Silk"] = ""
    materialDict["Nylon"] = ""
    materialDict["Organic Cotton"] = ""
    materialDict["Pailettes"] = ""
    materialDict["Peruvian Alpaca"] = ""
    materialDict["Pima Cotton"] = ""
    materialDict["Polyamide"] = ""
    materialDict["Polyester"] = ""
    materialDict["Pure Virgin Merino"] = ""
    materialDict["Recycled Superfine Merino"] = ""
    materialDict["Royal Llama"] = ""
    materialDict["Silk"] = ""
    materialDict["Sugar Cane Viscose"] = ""
    materialDict["Super Kid Mohair"] = ""
    materialDict["Superfine Alpaca"] = ""
    materialDict["Superwash Extrafine Merino"] = ""
    materialDict["Superwash Merino"] = ""
    materialDict["Superwash Wool"] = ""
    materialDict["Virgin Wool"] = ""
    materialDict["Viscose"] = ""
    materialDict["Wool"] = ""
    materialDict["Wool (Merino blend)"] = ""
    materialDict["Wool (Roving)"] = ""
    materialDict["Yak"] = ""

    for material in materialsList:
        material = material.strip()
        value, material_s = material.split("% ")
        if material_s == "Acrylic":
            materialDict["Acrylic"] = value
        elif material_s == "Alpaca":
            materialDict["Alpaca"] = value
        elif material_s == "Angora":
            materialDict["Angora"] = value
        elif material_s == "Australian Wool":
            materialDict["Australian Wool"] = value
        elif material_s == "Baby Alpaca":
            materialDict["Baby Alpaca"] = value
        elif material_s == "Baby Llama":
            materialDict["Baby Llama"] = value
        elif material_s == "Bamboo Fibers":
            materialDict["Bamboo Fibers"] = value
        elif material_s == "Bamboo Viscose":
            materialDict["Bamboo Viscose"] = value
        elif material_s == "Bamboo Viscose (Azlon)":
            materialDict["Bamboo Viscose (Azlon)"] = value
        elif material_s == "Beads":
            materialDict["Beads"] = value
        elif material_s == "BFL Wool":
            materialDict["BFL Wool"] = value
        elif material_s == "Blue Faced Leicester Wool":
            materialDict["Blue Faced Leicester Wool"] = value
        elif material_s == "Camel":
            materialDict["Camel"] = value
        elif material_s == "Cashmere":
            materialDict["Cashmere"] = value
        elif material_s == "Co":
            materialDict["Co"] = value
        elif material_s == "Combed Mercerized Cotton":
            materialDict["Combed Mercerized Cotton"] = value
        elif material_s == "Cotton":
            materialDict["Cotton"] = value
        elif material_s == "Cupro":
            materialDict["Cupro"] = value
        elif material_s == "Egyptian Cotton":
            materialDict["Egyptian Cotton"] = value
        elif material_s == "Egyptian Mako Cotton":
            materialDict["Egyptian Mako Cotton"] = value
        elif material_s == "Extrafine Merino":
            materialDict["Extrafine Merino"] = value
        elif material_s == "Extrafine Merino Superwash":
            materialDict["Extrafine Merino Superwash"] = value
        elif material_s == "Fine Alpaca":
            materialDict["Fine Alpaca"] = value
        elif material_s == "Fine Superwash Merino":
            materialDict["Fine Superwash Merino"] = value
        elif material_s == "Hemp":
            materialDict["Hemp"] = value
        elif material_s == "Israeli Mako Cotton":
            materialDict["Israeli Mako Cotton"] = value
        elif material_s == "Kid Mohair":
            materialDict["Kid Mohair"] = value
        elif material_s == "Lambswool":
            materialDict["Lambswool"] = value
        elif material_s == "Linen":
            materialDict["Linen"] = value
        elif material_s == "Llama":
            materialDict["Llama"] = value
        elif material_s == "Lurex":
            materialDict["Lurex"] = value
        elif material_s == "Mercerized Cotton":
            materialDict["Mercerized Cotton"] = value
        elif material_s == "Merino":
            materialDict["Merino"] = value
        elif material_s == "Metallic":
            materialDict["Metallic"] = value
        elif material_s == "Microfiber Acrylic":
            materialDict["Microfiber Acrylic"] = value
        elif material_s == "Milk Viscose (Azlon)":
            materialDict["Milk Viscose (Azlon)"] = value
        elif material_s == "Modal":
            materialDict["Modal"] = value
        elif material_s == "Mohair":
            materialDict["Mohair"] = value
        elif material_s == "Mulberry Silk":
            materialDict["Mulberry Silk"] = value
        elif material_s == "Nylon":
            materialDict["Nylon"] = value
        elif material_s == "Organic Cotton":
            materialDict["Organic Cotton"] = value
        elif material_s == "Pailettes":
            materialDict["Pailettes"] = value
        elif material_s == "Peruvian Alpaca":
            materialDict["Peruvian Alpaca"] = value
        elif material_s == "Pima Cotton":
            materialDict["Pima Cotton"] = value
        elif material_s == "Polyamide":
            materialDict["Polyamide"] = value
        elif material_s == "Polyester":
            materialDict["Polyester"] = value
        elif material_s == "Pure Virgin Merino":
            materialDict["Pure Virgin Merino"] = value
        elif material_s == "Recycled Superfine Merino":
            materialDict["Recycled Superfine Merino"] = value
        elif material_s == "Royal Llama":
            materialDict["Royal Llama"] = value
        elif material_s == "Silk":
            materialDict["Silk"] = value
        elif material_s == "Sugar Cane Viscose":
            materialDict["Sugar Cane Viscose"] = value
        elif material_s == "Super Kid Mohair":
            materialDict["Super Kid Mohair"] = value
        elif material_s == "Superfine Alpaca":
            materialDict["Superfine Alpaca"] = value
        elif material_s == "Superwash Extrafine Merino":
            materialDict["Superwash Extrafine Merino"] = value
        elif material_s == "Superwash Merino":
            materialDict["Superwash Merino"] = value
        elif material_s == "Superwash Wool":
            materialDict["Superwash Wool"] = value
        elif material_s == "Virgin Wool":
            materialDict["Virgin Wool"] = value
        elif material_s == "Viscose":
            materialDict["Viscose"] = value
        elif material_s == "Wool":
            materialDict["Wool"] = value
        elif material_s == "Wool (Merino blend)":
            materialDict["Wool (Merino blend)"] = value
        elif material_s == "Wool (Roving)":
            materialDict["Wool (Roving)"] = value
        elif material_s == "Yak":
            materialDict["Yak"] = value
        else:
            print("Not Found: %s" %(mat))

    out = ""
    for material in sorted(materialDict):
        out += "%s," %(materialDict[material])
    return out


if __name__ == "__main__":
    main()

