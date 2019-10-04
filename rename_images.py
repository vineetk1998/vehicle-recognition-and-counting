import xml.etree.ElementTree as xml
import os

		
if __name__ == "__main__":
	n=900
	for root,dirs, files in os.walk("C:\\Users\\Shubh\\minor_project2\\images\\"):
		for file in files :
			name='heavy' + str(n)
			os.rename("C:\\Users\\Shubh\\minor_project2\\images\\"+file,"C:\\Users\\Shubh\\minor_project2\\images\\"+name+'.png')
			n=n+1