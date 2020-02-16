import cv2
import os
import glob

def bulk_resizer(input_path,output_path,desired_size=32,color = [0,0,0],rename = True):
    img_no = 0
    #   onlyfiles = [f for f in os.listdir(input_path) if os.path.isfile(os.path.join(input_path, f))]

    onlyfiles =  os.listdir(input_path)
    #print(onlyfiles)
    for im_pth in onlyfiles:
        #im_pth = "img1.jpeg"
        try:

            im = cv2.imread(im_pth)
            old_size = im.shape[:2]
        except:

            continue

        # old_size is in (height, width) format

        ratio = float(desired_size)/max(old_size)
        new_size = tuple([int(x*ratio) for x in old_size])

        # new_size should be in (width, height) format

        im = cv2.resize(im, (new_size[1], new_size[0]))

        delta_w = desired_size - new_size[1]
        delta_h = desired_size - new_size[0]
        top, bottom = delta_h//2, delta_h-(delta_h//2)
        left, right = delta_w//2, delta_w-(delta_w//2)

        new_im = cv2.copyMakeBorder(im, top, bottom, left, right, cv2.BORDER_CONSTANT,
            value=color)
        if rename:
            output_path1 = output_path+"/"+str(img_no)+".jpg"
            img_no += 1
        else:
            output_path1 = output_path+"/"+os.path.splitext(os.path.basename(im_pth))[0]+".jpg"

        cv2.imwrite(output_path1, new_im)

def resizer(im_pth,output_path,desired_size=32,color = [0,0,0],rename = True):
    img_no = 0
    try:

        im = cv2.imread(im_pth)
        old_size = im.shape[:2]
    except:
        print("invalid image path")
        return -1
    # old_size is in (height, width) format

    ratio = float(desired_size)/max(old_size)
    new_size = tuple([int(x*ratio) for x in old_size])

    # new_size should be in (width, height) format

    im = cv2.resize(im, (new_size[1], new_size[0]))

    delta_w = desired_size - new_size[1]
    delta_h = desired_size - new_size[0]
    top, bottom = delta_h//2, delta_h-(delta_h//2)
    left, right = delta_w//2, delta_w-(delta_w//2)

    new_im = cv2.copyMakeBorder(im, top, bottom, left, right, cv2.BORDER_CONSTANT,
        value=color)
    if rename:
        output_path1 = output_path+"/"+str(img_no)+".jpg"

    else:
        output_path1 = output_path+"/"+os.path.splitext(os.path.basename(im_pth))[0]+".jpg"

    cv2.imwrite(output_path1, new_im)
