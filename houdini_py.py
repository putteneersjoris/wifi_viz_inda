node = hou.pwd()
geo = node.geometry()

geo.addAttrib(hou.attribType.Point, "ssid_n", 0)
geo.addAttrib(hou.attribType.Point, "rssi_n", 0)
geo.addAttrib(hou.attribType.Point, "rssi_max", 0)
geo.addAttrib(hou.attribType.Point, "rssi_min", 0)
geo.addAttrib(hou.attribType.Point, "ssid_max", "")
geo.addAttrib(hou.attribType.Point, "ssid_min", "")

data = """ILYSBAM_2.4G,-50,37,3
CCL-wifi,-69,38,3
CCL-guest,-73,39,3
The_Burrow_2.4G,-78,40,3
pbcourt,-79,41,3
pbc-bms,-80,42,3
pbcourt,-83,43,3
pbc-bms,-83,44,3
CCL-guest,-91,66,4
pbc-bms,-92,67,4
pbcourt,-92,68,4
pbcourt,-92,69,4
la213_2.4G,-92,70,4"""

scans = {}
for line in data.strip().split('\n'):
    parts = line.split(','); 
    ssid, rssi, detection_id, scan_id = parts[0], int(parts[1]), int(parts[2]), int(parts[3])
    
    if scan_id not in scans:
        scans[scan_id] = {'ssids': [], 'rssis': []}
    
    scans[scan_id]['ssids'].append(ssid)
    scans[scan_id]['rssis'].append(rssi)

for scan_id, scan_data in scans.items():
    pt = geo.createPoint()
    position = hou.evalParmTuple("position")
    pt.setPosition((position[0], scan_id, position[2]))
    pt.setAttribValue("ssid_n", len(scan_data['ssids']))
    pt.setAttribValue("rssi_n", sum(scan_data['rssis']))
    pt.setAttribValue("rssi_max", max(scan_data['rssis']))
    pt.setAttribValue("rssi_min", min(scan_data['rssis']))
    max_idx = scan_data['rssis'].index(max(scan_data['rssis']))
    min_idx = scan_data['rssis'].index(min(scan_data['rssis']))
    pt.setAttribValue("ssid_max", scan_data['ssids'][max_idx])
    pt.setAttribValue("ssid_min", scan_data['ssids'][min_idx])
