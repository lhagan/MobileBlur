newsblur = local_import("newsblur")

threshold = 0
thresholds = ["nt", "ps", "ng"]  # indices -1, 0, 1 for negative, neutral, and positive intelligence filters

#import ipdb
#ipdb.set_trace()
print request.env.path_info
if "nb_cookie" not in request.cookies.keys():
    if [request.application, request.controller, request.function] != [request.application, "default", "login"]:
        redirect(URL("default", "login", vars=dict(redirect=request.folder)))
#else:
#    newsblur.cookies = request.cookies["nb_cookie"]
