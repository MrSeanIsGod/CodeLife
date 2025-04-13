import os
import whisper
from moviepy.editor import VideoFileClip

def format_time(seconds):
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    ms = int((seconds - int(seconds)) * 1000)
    return f"{h:02}:{m:02}:{s:02},{ms:03}"

def audio_to_srt_whisper(audio_path, output_srt_path, model_size="base"):
    print("載入 Whisper 模型...")
    model = whisper.load_model(model_size)
    print("開始辨識音訊（中文）...")
    result = model.transcribe(audio_path, language="zh")

    print("寫入 SRT 字幕檔...")
    with open(output_srt_path, "w", encoding="utf-8") as f:
        for i, seg in enumerate(result["segments"]):
            start = format_time(seg["start"])
            end = format_time(seg["end"])
            text = seg["text"].strip()
            f.write(f"{i+1}\n{start} --> {end}\n{text}\n\n")

    print(f"SRT 字幕檔已儲存至：{output_srt_path}")

def video_to_srt(video_path, output_srt_path, temp_audio_path="temp_audio.wav"):
    print(f"正在處理影片：{video_path}")
    video = VideoFileClip(video_path)
    video.audio.write_audiofile(temp_audio_path)
    print("音訊提取完成。")
    audio_to_srt_whisper(temp_audio_path, output_srt_path)
    os.remove(temp_audio_path)

if __name__ == "__main__":
    video_file = "input.mp4"      # 影片檔案
    srt_file = "output.srt"       # 輸出的字幕檔案
    video_to_srt(video_file, srt_file)


'''
from moviepy.editor import VideoFileClip
import speech_recognition as sr
from pydub import AudioSegment
import os

def video_to_srt(video_path, output_srt_path, language='zh-TW'):
    """
    讀取影片，自動產生 SRT 字幕檔。

    Args:
        video_path (str): 影片檔案的路徑。
        output_srt_path (str): 輸出 SRT 檔案的路徑。
        language (str): 語音辨識的語言代碼 (預設為 'zh-TW'，中文台灣)。
                       你可以參考 SpeechRecognition 支援的語言代碼。
    """
    try:
        print(f"正在處理影片：{video_path}")
        video = VideoFileClip(video_path)
        audio = video.audio
        audio_path = "temp_audio.wav"
        audio.write_audiofile(audio_path)
        print("音訊提取完成。")

        r = sr.Recognizer()
        audio_segment = AudioSegment.from_wav(audio_path)
        total_duration = len(audio_segment) / 1000  # 總時長（秒）
        chunk_size = 60 * 1000  # 每段處理 60 秒的音訊
        start_time = 0
        counter = 1
        subtitles = []

        print("開始進行語音辨識...")
        while start_time < total_duration:
            end_time = min(start_time + chunk_size / 1000, total_duration)
            print(f"處理 {start_time:.2f} - {end_time:.2f} 秒...")
            audio_chunk = audio_segment[int(start_time * 1000):int(end_time * 1000)]
            temp_chunk_path = "temp_chunk.wav"
            audio_chunk.export(temp_chunk_path, format="wav")

            with sr.AudioFile(temp_chunk_path) as source:
                try:
                    audio_data = r.record(source)
                    #text = r.recognize_google(audio_data, language=language)
                    text = r.recognize_google(audio_data, language=language, show_all=False)
                    subtitles.append((counter, start_time, end_time, text))
                    counter += 1
                except sr.UnknownValueError:
                    print("無法辨識此段語音。")
                except sr.RequestError as e:
                    print(f"Google Speech Recognition 服務發生錯誤：{e}")

            os.remove(temp_chunk_path)
            start_time = end_time

        os.remove(audio_path)
        print("語音辨識完成。")

        # 寫入 SRT 檔案
        with open(output_srt_path, 'w', encoding='utf-8') as f:
            for index, start, end, text in subtitles:
                start_h = int(start / 3600)
                start_m = int((start % 3600) / 60)
                start_s = int(start % 60)
                start_ms = int((start - int(start)) * 1000)
                end_h = int(end / 3600)
                end_m = int((end % 3600) / 60)
                end_s = int(end % 60)
                end_ms = int((end - int(end)) * 1000)
                f.write(f"{index}\n")
                f.write(f"{start_h:02d}:{start_m:02d}:{start_s:02d},{start_ms:03d} --> {end_h:02d}:{end_m:02d}:{end_s:02d},{end_ms:03d}\n")
                f.write(f"{text}\n\n")

        print(f"SRT 字幕檔已儲存至：{output_srt_path}")

    except Exception as e:
        print(f"處理過程中發生錯誤：{e}")

if __name__ == "__main__":
    video_file = "input.mp4"  # 將你的影片檔案路徑替換在這裡
    srt_file = "output.srt"  # 設定輸出的 SRT 檔案路徑
    video_to_srt(video_file, srt_file)
'''