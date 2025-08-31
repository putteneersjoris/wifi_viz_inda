geo = hou.pwd().geometry()

geo.addArrayAttrib(hou.attribType.Point, "ssid", hou.attribData.String, 1)
geo.addArrayAttrib(hou.attribType.Point, "rssi", hou.attribData.Int, 1)
geo.addAttrib(hou.attribType.Point, "ssid_n", 0)
geo.addAttrib(hou.attribType.Point, "rssi_n", 0)
geo.addAttrib(hou.attribType.Point, "rssi_max", 0)
geo.addAttrib(hou.attribType.Point, "rssi_min", 0)
geo.addAttrib(hou.attribType.Point, "ssid_max", "")
geo.addAttrib(hou.attribType.Point, "ssid_min", "")
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
pbc-bms,-89,45,3
pbcourt,-91,46,3
pbcourt,-91,47,3
pbc-bms,-91,48,3
pbc-bms,-92,49,3
pbcourt,-92,50,3
ILYSBAM_2.4G,-49,51,4
CCL-wifi,-70,52,4
CCL-guest,-70,53,4
The_Burrow_2.4G,-78,54,4
pbc-bms,-80,55,4
pbcourt,-81,56,4
pbcourt,-81,57,4
pbcourt,-83,58,4
pbc-bms,-84,59,4
Gisela Schneider,-86,60,4
pbcourtmain_2.4G,-88,61,4
Nuch,-88,62,4
pbcourt,-89,63,4
pbcourt,-90,64,4
pbc-bms,-90,65,4
CCL-guest,-91,66,4
pbc-bms,-92,67,4
pbcourt,-92,68,4
pbcourt,-92,69,4
la213_2.4G,-92,70,4"""

scans = {}
for line in data.strip().split('\n'):
    parts = line.split(','); ssid, rssi, detection_id, scan_id = parts[0], int(parts[1]), int(parts[2]), int(parts[3])
    
    if scan_id not in scans:
        scans[scan_id] = {'ssids': [], 'rssis': []}
    
    scans[scan_id]['ssids'].append(ssid)
    scans[scan_id]['rssis'].append(rssi)

for scan_id, scan_data in scans.items():
    pt = geo.createPoint()
    pt.setPosition((scan_id, 0, 0))
    pt.setAttribValue("ssid", scan_data['ssids'])
    pt.setAttribValue("rssi", scan_data['rssis'])
    pt.setAttribValue("ssid_n", len(scan_data['ssids']))
    pt.setAttribValue("rssi_n", sum(scan_data['rssis']))
    pt.setAttribValue("rssi_max", max(scan_data['rssis']))
    pt.setAttribValue("rssi_min", min(scan_data['rssis']))
    max_idx = scan_data['rssis'].index(max(scan_data['rssis']))
    min_idx = scan_data['rssis'].index(min(scan_data['rssis']))
    pt.setAttribValue("ssid_max", scan_data['ssids'][max_idx])
    pt.setAttribValue("ssid_min", scan_data['ssids'][min_idx])
