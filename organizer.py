import os
import shutil

downloadFolder = "/Users/mario/Downloads/"

if __name__ == '__main__':
	for filename in os.listdir(downloadFolder):
		name, extension = os.path.splitext(downloadFolder + filename)

		#MOVER IMAGENES
		if extension.lower() in [".jpg", ".JPEG", ".jpeg", ".png", ".gif", ".jfif"]:
			#print(len(extension))
			#print(downloadFolder+filename)
			picturesFolder = "/Users/mario/Downloads/Imagenes"
			#os.rename(downloadFolder + filename, picturesFolder + filename)
			#print(name+extension)
			shutil.move(downloadFolder+filename, picturesFolder)
			print("Moved: {} to {}".format(filename, picturesFolder))

		#MOVER ZIP
		if extension in [".zip", ".ZIP", ".rar", ".RAR", ".7zip", ".7ZIP"]:
			#print(len(extension))
			zipFolder = "/Users/mario/Downloads/ZIP"
			shutil.move(downloadFolder+filename, zipFolder)
			print("Moved: {} to {}".format(filename, zipFolder))

		#MOVER PDF
		if extension in [".PDF", ".pdf"]:
			#print(len(extension))
			pdfFolder = "/Users/mario/Downloads/PDF"
			shutil.move(downloadFolder+filename, pdfFolder)
			print("Moved: {} to {}".format(filename, pdfFolder))

		#MOVER TXT
		if extension in [".TXT", ".txt"]:
			#print(len(extension))
			txtFolder = "/Users/mario/Downloads/TXT"
			shutil.move(downloadFolder+filename, txtFolder)
			print("Moved: {} to {}".format(filename, txtFolder))

		#MOVER WORD
		if extension in [".doc", ".docx", ".dot", ".dotm", ".dotx"]:
			#print(len(extension))
			wordFolder = "/Users/mario/Downloads/WORD"
			shutil.move(downloadFolder+filename, wordFolder)
			print("Moved: {} to {}".format(filename, wordFolder))

		#MOVER PPT
		if extension.lower() in [".pptx"]:
			#print(len(extension))
			pptFolder = "/Users/mario/Downloads/PPT"
			shutil.move(downloadFolder+filename, pptFolder)
			print("Moved: {} to {}".format(filename, pptFolder))

		#MOVER EXCEL
		if extension.lower() in [".xls", ".xlsx"]:
			#print(len(extension))
			excelFolder = "/Users/mario/Downloads/EXCEL"
			shutil.move(downloadFolder+filename, excelFolder)
			print("Moved: {} to {}".format(filename, excelFolder))

		#MOVER XML
		if extension.lower() in [".xml", ".xsd"]:
			#print(len(extension))
			xmlFolder = "/Users/mario/Downloads/XML"
			shutil.move(downloadFolder+filename, xmlFolder)
			print("Moved: {} to {}".format(filename, xmlFolder))

		#MOVER JSON
		if extension.lower() in [".json"]:
			#print(len(extension))
			jsonFolder = "/Users/mario/Downloads/JSON"
			shutil.move(downloadFolder+filename, jsonFolder)
			print("Moved: {} to {}".format(filename, jsonFolder))

		#MOVER EMAILS
		if extension.lower() in [".eml", ".msg"]:
			#print(len(extension))
			emailFolder = "/Users/mario/Downloads/EMAILS"
			shutil.move(downloadFolder+filename, emailFolder)
			print("Moved: {} to {}".format(filename, emailFolder))

		#MOVER VIDEO
		if extension.lower() in [".mp4"]:
			#print(len(extension))
			videoFolder = "/Users/mario/Downloads/Video_Recordings"
			shutil.move(downloadFolder+filename, videoFolder)
			print("Moved: {} to {}".format(filename, videoFolder))