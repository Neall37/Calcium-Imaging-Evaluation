# Calcium-Imaging-Evaluation
An quick approach to evaluate your calcium imaging result

By extracting and visualizing the pixel intensity values from lines across all frames, we are able to evaluate the video quality by looking at an image.

## Example:
An example single frame from a calcium imaging video:

<p align="center">
  <img src="images/first_frame.png" style="max-width: 300px; width: 50%;" alt="Extracted Line Image">
</p>


Extracting a single line across frames allows for easy observation of temporal variations in the video, such as drift, contrast changes, neuron firing, and overall image quality:

<p align="center">
  <img src="images/extracted_line.png" style="max-width: 1000px; width: 100%;" alt="Extracted Line Image">
</p>

## How To Use

1. **Edit the file path:** Download `eval.py` and replace `[YourFileName]` in it with the path to your own file.  
2. **Run the script:** Execute the following command in your terminal:  

   ```bash
   python eval.py
   ``` 

