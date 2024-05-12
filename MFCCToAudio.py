import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt

# Assume mfccs is your flattened MFCCs
# Shape of mfccs should be (num_frames, num_coefficients)

# Inverse Flatten (reshape back to original shape)
num_frames = test.shape[0]
num_coefficients = 1
mfccs_original_shape = test.reshape((num_frames, -1, num_coefficients))

# Inverse MFCC Transformation
audio_reconstructed = []
for mfcc_frame in mfccs_original_shape:
    audio_frame = librosa.feature.inverse.mfcc_to_audio(mfcc_frame.T)
    audio_reconstructed.extend(audio_frame)

audio_reconstructed = np.array(audio_reconstructed)

# Visualize the waveform of the reconstructed audio
plt.figure(figsize=(10, 4))
librosa.display.waveshow(audio_reconstructed, sr=sr)
plt.title('Reconstructed Waveform from MFCCs')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.show()
