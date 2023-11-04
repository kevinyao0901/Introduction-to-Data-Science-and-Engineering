import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

# 读取音频文件
audio_file = r"D:\programing\Dase_intro\lec08\ch14\voice_dialing.wav"
sample_rate, audio_data = wavfile.read(audio_file)

# 执行快速傅里叶变换
fft_result = np.fft.fft(audio_data)
fft_freqs = np.fft.fftfreq(len(fft_result), 1.0 / sample_rate)

# 获取幅度谱（去除复数部分的绝对值）
magnitude = np.abs(fft_result)

# 可视化傅里叶变换结果
plt.figure(figsize=(10, 6))
plt.plot(fft_freqs, magnitude)
plt.xlabel('频率 (Hz)')
plt.ylabel('幅度')
plt.title('傅里叶变换结果')
plt.grid(True)
plt.show()
