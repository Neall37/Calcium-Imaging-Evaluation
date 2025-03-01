import numpy as np
import imageio.v3 as iio
import matplotlib.pyplot as plt

# Read the multi-frame TIFF video
imgs = iio.imread('YourFileName.tif')

num_frames, img_height, img_width = imgs.shape

# Select three equally spaced rows
row_indices = [
    img_height // 4,  # Upper quarter
    img_height // 2,  # Middle
    (3 * img_height) // 4  # Lower quarter
]

# Extract the selected rows from each frame
line_stacks = [np.array([frame[row, :] for frame in imgs]) for row in row_indices]

# Visualize each extracted line stack
fig, axes = plt.subplots(3, 1, figsize=(10, 10), sharex=True)

for ax, line_stack, row in zip(axes, line_stacks, row_indices):
    ax.imshow(line_stack, aspect='auto', cmap='gray')
    ax.set_ylabel(f"Frame Index\n(Row {row})")
    ax.set_title(f"Extracted Line at Row {row}")

axes[-1].set_xlabel("Pixel Position")
plt.tight_layout()
plt.show()
