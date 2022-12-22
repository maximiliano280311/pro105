import os
import cv2


path = "Images"

images = []


for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        images.append(file_name)
        
print(len(images))
count = len(images)

frame = cv2.imread(images[0])
height, width, channels = frame.shape
size = (width,height)
print(size)

out = cv2.VideoWriter('Project4.mp4',cv2.VideoWriter_fourcc(*'DIVX'), 30, size)

#para atardecer
for i in range(0,count-1):

#para amanecer
#for i in range(count-1,0,-1):
    frame = cv2.imread(images[i])
    out.write(frame)

out.release()#libereando el video generado
print("para atardecer")