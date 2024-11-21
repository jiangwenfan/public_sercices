import logging
import os

import requests


def convert_mp4_to_mp3(mp4_file_full_path: str):
    # ffmpeg -i input.mp4 -vn -acodec copy output.mp3
    mp4_file_name = os.path.basename(mp4_file_full_path)

    mp3_dirs = "/whisper/data/mp3_files"
    mp3_file_full_path = os.path.join(
        mp3_dirs, mp4_file_name.replace("mp4", "mp3")
    )

    cmd = (
        f"ffmpeg -i {mp4_file_full_path} -vn -acodec copy {mp3_file_full_path}"
    )
    logging.debug(f"handle cmd: {cmd}")
    logging.info(f"handing {mp4_file_name}")
    try:
        os.system(cmd)
    except Exception:
        logging.error(f"Command execution failed.{mp4_file_name}")
        return False
    else:
        logging.info(f"Command executed successfully.{mp4_file_name}")
        return True


def convert_audio_to_srt(audio_file_full_path: str):
    srt_dirs = "/whisper/data/srt_files"
    audio_file_name = os.path.basename(audio_file_full_path)
    # whisper sample.mp3 --language English --model medium --output_format\
    #  srt --output_dir ./aaa
    cmd = f"whisper {audio_file_full_path} --language English --model medium\
          --output_format srt --output_dir {srt_dirs}"
    logging.debug(f"handle cmd: {cmd}")
    logging.info(f"handing {audio_file_name}")
    try:
        os.system(cmd)
    except Exception:
        logging.error(f"Command execution failed.{audio_file_name}")
        return False
    else:
        logging.info(f"Command executed successfully.{audio_file_name}")
        return True


def upload_srt_file_backend(srt_file_full_path: str):
    srt_file_name = os.path.basename(srt_file_full_path)
    logging.info(f"uploading {srt_file_name} to backend")
    # TODO upload srt file to backend
    _ = requests.post("")
    return True


def split_small_video_from_video(
    video_file_full_path: str, srt_file_full_path: str
):
    video_file_name = os.path.basename(video_file_full_path)
    logging.info(
        f"splitting {video_file_name} to small videos,use {srt_file_full_path}\
              as subtitle file"
    )
    # TODO split video to small videos
    # ffmpeg -i input.mp4 -vf scale=320:240 output_320x240.mp4
    return True
