import os
import subprocess
import json

data = []
with open('conversionList.json', 'r') as f:
     data = json.load(f)


for convert_this in data['toConvert']:
	 print ("converting -- " + convert_this['filename'])
	 if hasattr(convert_this, "outFormat"):
	 	os.system("convert "+convert_this['filename']+" -resize "+convert_this['resize']+" " + convert_this['outFormat'] + ":" + convert_this['saveAs']) 
	 else:
	 	os.system("convert "+convert_this['filename']+" -resize "+convert_this['resize']+" " + convert_this['saveAs']) 

