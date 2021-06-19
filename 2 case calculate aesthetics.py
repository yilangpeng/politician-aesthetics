import os, sys
athec_path = os.path.expanduser("~/Documents/Workspace/Computer vision/Athec/")
sys.path.append(athec_path)
from athec import misc, color, colordict, edge, sharp

cwd = os.path.expanduser("~/Dropbox/Research/Visual aesthetics/Politician/")
users = ["hillaryclinton","realdonaldtrump"]

cd = colordict.color_dict()
first_file = True
filesavepath = os.path.join(cwd, "img attr", "img aesthetics.txt")

for user in users[:]:
    imgfile = os.path.join(cwd, 'img filename', user + '.txt')
    img_folder = os.path.join(cwd, "img all", user)
    resize_folder = os.path.join(cwd, "img resize", user)
    tf_folder = os.path.join(cwd, "img transform", user)
    
    imgfile = open(imgfile, 'r')
    imglines = imgfile.readlines()[:]

    for i, imgline in enumerate(imglines[:]):
        imgname = imgline.rstrip('\r\n')
        print('*'*20)
        print(user, i, imgname, '*'*20)

        img = os.path.join(cwd, "img resize", user, imgname)

        d = {"user":user, "imgname":imgname}

        # file size and image size
        d.update( misc.attr_size(img) )

        # color model statistics
        d.update( color.attr_grayscale(img) )
        d.update( color.attr_HSV(img) )

        # contrast
        d.update( color.attr_contrast_range(img) )

        # colorfulness
        d.update( color.attr_colorful(img) )

        # color variety
        d.update( color.attr_hue_count(img) )

        # visual complexity
        edges = edge.tf_edge_canny(img, 
                                   save_path = os.path.join(tf_folder, "edge canny", imgname),
                                   gaussian_blur_kernel = (3,3))
        d.update( edge.attr_complexity_edge(edges) )

        result = edge.attr_complexity_edge_box(edges,
                                               save_path = os.path.join(tf_folder, "bounding box edge canny", imgname))
        d.update(result)

        # sharpness
        d.update( sharp.attr_sharp_laplacian(img) )

        result = sharp.attr_dof_block(img, sharp_method = "laplacian") 
        d.update(result)

        misc.printd(d)
        misc.save_dict_to_txt(d, filesavepath, save_keys = first_file)
        first_file = False # only save dictionary keys for the first file

print("DONE"*10)

