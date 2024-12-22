import gzip
import os.path
import shutil
import urllib.request

from lxml import etree


def _get_region_dump():
    if not os.path.exists("./regions.xml.gz"):
        request = urllib.request.Request("https://www.nationstates.net/pages/regions.xml.gz", headers={"User-Agent": "trigger_find_reference test script by notanam"})
        with urllib.request.urlopen(request) as response, open("regions.xml.gz", 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
    dump = gzip.open('./regions.xml.gz', 'rb').read()
    data = etree.fromstring(dump)
    region_list = data.findall('REGION')
    del dump
    del data
    return region_list


def region_dump_data(target_set: set[str], min_trig: int) -> tuple[list[str], dict[str, int], int, set[str]]:
    dump_regions = _get_region_dump()
    region_names = []
    update_map = {}
    for region in dump_regions:
        region_name = region.find("NAME").text.lower().replace(" ", "_")
        region_names.append(region_name)
        update_map[region_name] = int(region.find("LASTUPDATE").text)
    target_set = {t.lower().replace(" ", "_") for t in target_set}
    return region_names, update_map, min_trig, target_set
