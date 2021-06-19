import os, sys
athec_path = os.path.expanduser("~/Documents/Workspace/Computer vision/Athec/")
sys.path.append(athec_path)
from athec import misc

cwd = os.path.expanduser("~/Dropbox/Research/Visual aesthetics/Politician/")
users = ["hillaryclinton","realdonaldtrump"]

for user in users:
    imgfile = os.path.join(cwd, 'img filename', user + '.txt')
    img_folder = os.path.join(cwd, "img all", user)
    resize_folder = os.path.join(cwd, "img resize", user)
    tf_folder = os.path.join(cwd, "img transform", user)
    
    imgfile = open(imgfile, 'r')
    imglines = imgfile.readlines()[:]

    for i, imgline in enumerate(imglines[:]):
        imgname = imgline.rstrip('\r\n')
        print(user, i, imgname, '*'*20)

        img_path = os.path.join(cwd, "img all", user, imgname)
        resize_path = os.path.join(cwd, "img resize", user, imgname)

        result = misc.tf_resize(img_path, resize_path, max_side = 400)
        print(result)

