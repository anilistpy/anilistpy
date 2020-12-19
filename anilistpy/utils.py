def videoLink(site, id):
    if site == "youtube":
        url = "youtu.be/" + str(id)
    else:
        return "no wrapper for"+ site + "yet" 
    return url