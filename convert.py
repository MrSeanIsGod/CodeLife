import subprocess

def mkv_to_mp4(input_file, output_file):
    """將 MKV 轉換為 MP4，不重新編碼，只更換封裝格式。"""
    command = [
        r"C:\ffmpeg\ffmpeg-2025-03-27-git-114fccc4a5-full_build\bin\ffmpeg.exe", "-i", input_file, "-c:v", "copy", "-c:a", "copy", output_file
    ]
    
    try:
        subprocess.run(command, check=True)
        print(f"轉換成功: {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"轉換失敗: {e}")

# 測試範例
if __name__ == "__main__":
    input_mkv = "input.mkv"
    output_mp4 = "output.mp4"
    mkv_to_mp4(input_mkv, output_mp4)


