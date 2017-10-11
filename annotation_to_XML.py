import xml.etree.ElementTree as ET
from xml.dom import  minidom
import os


f = open(input("INPUT FULL PATH FOR LABEL FILE\n>>"))#label file from object maker style
lines = f.readlines()


for n in lines:
    line = n.split()
    filename = line[0].split("\\")
    filename = filename[1]
    anno = ET.Element("annotation")

    fname = ET.SubElement(anno, "filename")
    fname.text = filename

    size = ET.SubElement(anno, "size")
    width = ET.SubElement(size, "width")
    width.text = "2592"  # width of input image
    height = ET.SubElement(size, "height")
    height.text = "1944"  # height of input image
    depth = ET.SubElement(size, "depth")
    depth.text = "3"  # 3:color image 1:gray image

    count = 0
    limit = (len(line) - 2) // 4
    while True:
        obj = ET.SubElement(anno,"object")

        name = ET.SubElement(obj, "name")
        name.text = "beans"#class name

        bnd = ET.SubElement(obj, "bndbox")
        xmin = ET.SubElement(bnd, "xmin")
        xmin.text = line[2 + count * 4]
        ymin = ET.SubElement(bnd, "ymin")
        ymin.text = line[3 + count * 4]
        xmax = ET.SubElement(bnd, "xmax")
        xmax.text = str(int(line[2 + count * 4]) + int(line[4 + count * 4]))
        ymax = ET.SubElement(bnd, "ymax")
        ymax.text = str(int(line[3 + count * 4]) + int(line[5 + count * 4]))

        count += 1
        limit -= 1
        if limit == 0:
            string = ET.tostring(anno, "utf-8")
            pretty_string = minidom.parseString(string).toprettyxml(indent=' ')
            if not os.path.isdir("output_dir"):
                os.makedirs("output_dir")
            with open("output_dir"+filename[:-3]+'xml', 'w') as f:
                f.write(pretty_string)
            print("Outputted {0}".format(filename))
            break

