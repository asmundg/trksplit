from copy import deepcopy
import os
import sys
from lxml import etree

ns = {'g': 'http://www.topografix.com/GPX/1/1'}

def main():
    infile = sys.argv[1]
    name = os.path.splitext(infile)[0]
    root = etree.parse(infile)

    gpx = root.getroot()
    count = 0
    for trk in gpx.xpath('/g:gpx/g:trk', namespaces=ns):
        new_gpx = deepcopy(gpx)
        for old_trk in new_gpx.xpath('./g:trk', namespaces=ns):
            new_gpx.remove(old_trk)

        new_gpx.append(trk)
        with open('{0}-{1}.gpx'.format(name, count), 'w') as f:
            f.write(etree.tostring(new_gpx, xml_declaration=True,
                                   encoding='utf-8', standalone=False))
        count += 1

if __name__ == '__main__':
    main()
