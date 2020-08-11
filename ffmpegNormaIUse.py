# -*-coding = utf-8 -*-
import json
import os
import subprocess

if __name__ == "__main__":
	whereFfmpeg = ""
	toDir = ""
	beginPath = ""
	paths = os.listdir(beginPath)
	videoName = "\\video.m4s"
	audioName = "\\audio.m4s"
	for path in paths:
		secondPath = os.path.join(beginPath, path)
		liTaskPath = os.listdir(secondPath)
		dirName = os.path.join(toDir, path)
		if not os.path.exists(dirName):
			os.mkdir(dirName)
		for i in liTaskPath:
			thirdPath = os.path.join(secondPath, i)
			with open(thirdPath + "\\entry.json", encoding="utf-8") as file:
				finalName = json.load(file)["page_data"]["download_subtitle"].replace(" ", "")
				finalPath = ""
			for j in os.listdir(thirdPath):
				finalPath = os.path.join(thirdPath, j)
				if os.path.isdir(finalPath):
					break
			finalString = whereFfmpeg + ' -i %s -i %s -c:v copy -c:a aac -strict experimental %s.mp4' \
						  % (finalPath + videoName, finalPath + audioName, dirName + "\\" + finalName)
			print(finalString)
			p = subprocess.Popen(finalString)
			p.communicate()
