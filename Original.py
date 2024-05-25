import argparse
from datetime import time
from src.detection import detect


if __name__ == '__main__':
    t1 = time.localtime()
    start_time = time.strftime("%H:%M:%S", t1)
    parser = argparse.ArgumentParser()

    parser.add_argument('--source', type=str, default="data/movie_test.mp4", help='source')
    
    parser.add_argument('--output', type=str, default="output/test.mp4", help='outputpath')  # output folder  # output folder
    parser.add_argument('--img-size', type=int, default=640, help='inference size (pixels)')
    parser.add_argument('--confthres', type=float, default=0.15, help='object confidence threshold')
    parser.add_argument('--iouthres', type=float, default=0.6, help='IOU threshold for NMS')
    #parser.add_argument('--device', default='', help='cuda device, i.e. 0 or 0,1,2,3 or cpu')
    # parser.add_argument('--yolo_weights', type=str, default='yolov5/weights/yolov5s.pt', help='model.pt path')
    
    # gaze-------------------------------------
    parser.add_argument('--model_weights', type=str, help='model weights', default='mymodel/gaze/model_demo.pt')

    # db---------------------------------------
    parser.add_argument('--output_db_csv', type=str, default="output/db.csv", help='outputpath')  # output folder
    parser.add_argument('--output_emotion_csv', type=str, default="output/emotion.csv", help='outputpath')  # output folder
    parser.add_argument('--output_db_png', type=str, default="output/db.png", help='outputpath')  # output folder
    parser.add_argument('--output_audio_result', type=str, default="output/audio_result.mp4", help='outputpath')  # output folder
    # tocsv-------------------------------------
    parser.add_argument('--output_personid_csv', type=str, default="output/person_id.csv", help='outputpath')  # output folder
    parser.add_argument('--output_attentionid_csv', type=str, default="output/attention_id.csv", help='outputpath')  # output folder
    parser.add_argument('--output_personcount_csv', type=str, default="output/personcount.csv", help='outputpath')  # output folder
    
    # mode-------------------------------------
    parser.add_argument('--gaze', type=str, help='do you need gaze information?', default='True')
    parser.add_argument('--person_count', type=str, help='do you need person-count information?', default='True')
    parser.add_argument('--to_csv', type=str, help='do you need csv information?', default='True')
    # 
    parser.add_argument('--db', type=str, help='do you need db csv and db graph?', default='False')
    parser.add_argument("--device", default="gpu", help="Device to inference on")


    

    args = parser.parse_args()
    detect(args)
    t2 = time.localtime()
    end_time = time.strftime("%H:%M:%S", t2)
    print(start_time)
    print(end_time)