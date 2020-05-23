import cv2
import os
import random
import string

#Generate a random string of numbers to use as a part of our output file names
def rand_string(length):
    rand_str = ''.join(random.choice(
        string.ascii_lowercase
        + string.ascii_uppercase
        +string.digits)
        for i in range(length))
    return rand_str

#calculating the length of the video / frame count
def length_of_video(video_path):
    cap = cv2.VideoCapture(video_path)
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    #print(length)
    return length

#extraction of video to images
def extracting_frames(video_path, save_path, till = 50):
    print('Extracting frames')
        #param 1: path of the source (video)
        #param 2: where the output images saved
        #param 3: when the extraction should stop 
    
    #split the path to directory and the file name itself
    _, file_name = os.path.split(video_path)
    #getting the file_name without the extention
    file_name = os.path.splitext(file_name)[0]

    length = length_of_video(video_path)
    if length == 0:
        print('Video length is zero')
        return 0

    cap = cv2.VideoCapture(video_path)
    count = 0           #counting frames
    random_string = rand_string(5)              #for naming each frame

    #check if it is working by checking the very first frame of the video
    ret, frame = cap.read()
    test_file_path = os.path.join(
        save_path,
        file_name[:6] +\
        '{}_{}.jpg'.format(random_string, count))

    cv2.imwrite(test_file_path, frame)
    if os.path.isfile(test_file_path):
        print('Test frame saved,' + 'Continuing Extraction')

        #continuing the extraction 
        count = 1
        while ret:
            ret, frame = cap.read()
            #if frame is available and count is less than till, continue extraction
            if ret and count < till:
                file_path = os.path.join(
                    save_path,
                    file_name[:6]+
                    '{}_{}.jpg'.format(random_string, count))

                cv2.imwrite(file_path, frame)
                count +=1
                print(count)
            else:
                count +=1
    else:
        print('Problem with saving the file!')
        return 0
    cap.release()
    print('Extraction completed!')

#main function
if __name__ == '__main__':
    video_frame = ["../data/vtest.avi"]
    save_path = "../data/vtest_frames"
    for video in video_frame:
        print(video)
        extracting_frames(video, save_path, till=30)

    #length_of_video(video_frame)
    