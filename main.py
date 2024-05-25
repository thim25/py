import argparse
import time  # Make sure to import the time module

from src.detection import detect

if __name__ == "__main__":
    t1 = time.localtime()
    start_time = time.strftime("%H:%M:%S", t1)

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--source", type=str, default="data/movie_test.mp4", help="source"
    )
    parser.add_argument(
        "--output", type=str, default="output/test.mp4", help="output path"
    )
    parser.add_argument(
        "--img-size", type=int, default=640, help="inference size (pixels)"
    )
    parser.add_argument(
        "--confthres", type=float, default=0.15, help="object confidence threshold"
    )
    parser.add_argument(
        "--iouthres", type=float, default=0.6, help="IOU threshold for NMS"
    )
    parser.add_argument(
        "--model_weights",
        type=str,
        default="mymodel/gaze/model_demo.pt",
        help="model weights path",
    )

    parser.add_argument(
        "--output_db_csv", type=str, default="output/db.csv", help="output DB CSV path"
    )
    parser.add_argument(
        "--output_emotion_csv",
        type=str,
        default="output/emotion.csv",
        help="output emotion CSV path",
    )
    parser.add_argument(
        "--output_db_png", type=str, default="output/db.png", help="output DB PNG path"
    )
    parser.add_argument(
        "--output_audio_result",
        type=str,
        default="output/audio_result.mp4",
        help="output audio result path",
    )

    parser.add_argument(
        "--output_personid_csv",
        type=str,
        default="output/person_id.csv",
        help="output person ID CSV path",
    )
    parser.add_argument(
        "--output_attentionid_csv",
        type=str,
        default="output/attention_id.csv",
        help="output attention ID CSV path",
    )
    parser.add_argument(
        "--output_personcount_csv",
        type=str,
        default="output/personcount.csv",
        help="output person count CSV path",
    )

    parser.add_argument(
        "--gaze",
        type=lambda x: (str(x).lower() == "true"),
        default=True,
        help="do you need gaze information?",
    )
    parser.add_argument(
        "--person_count",
        type=lambda x: (str(x).lower() == "true"),
        default=True,
        help="do you need person-count information?",
    )
    parser.add_argument(
        "--to_csv",
        type=lambda x: (str(x).lower() == "true"),
        default=True,
        help="do you need CSV information?",
    )
    parser.add_argument(
        "--db",
        type=lambda x: (str(x).lower() == "true"),
        default=False,
        help="do you need DB CSV and DB graph?",
    )

    parser.add_argument(
        "--device", type=str, default="gpu", help="device to inference on"
    )

    args = parser.parse_args()
    detect(args)

    t2 = time.localtime()
    end_time = time.strftime("%H:%M:%S", t2)
    print(start_time)
    print(end_time)
