import xml.etree.ElementTree as et
from xml.etree.ElementTree import Element, SubElement, Comment, tostring
from xml.dom import minidom
from numpy import float64

tree = et.parse('cam_data.xml')
root = tree.getroot()

def update_cam():
    node = root.find('cam[@id="'+cam_id+'"]')
    val = et.Element("value", {'timestamp':str(float64(timestamp))})
    node.append(val)
    tree.write('cam_data.xml')
    return str(node.attrib), 201


def get_cams():
    rough_string = et.tostring(root, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

def get_cam(cam_id):
    node = root.find('cam[@id="'+str(cam_id)+'"]')
    rough_string = et.tostring(node, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

def get_avg(start, end):
    avg = 0
    print start, end
    a = et.Element('cams')
    for cam in root:
        for value in cam:
            if float(value.attrib.values()[0]) > start and float(value.attrib.values()[0]) < end:
                print cam.attrib['name'], value.text
                if avg == 0:
                    avg = float(value.text)
                else:
                    avg = (avg + float(value.text))/float(2)
    
        b = et.SubElement(a, 'cam')
        b.set('id', cam.attrib['id'])
        b.set('name', cam.attrib['name'])
        c = et.SubElement(a, 'avg_value')
        c.set('start_timestamp', str(start))
        c.set('end_timestamp', str(end))
        c.text = str(int(avg))
    return et.dump(a)

print '\navg: ' + str(get_avg(1496869680, 1496869750.68))
