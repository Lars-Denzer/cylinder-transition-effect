# Cylinder Transition Effect

A Python script that creates a smooth cylindrical transition effect between two PDF pages. It generates a series of frame-by-frame PDF images that simulate a sliding wipe from one image to another and back — useful for animations, educational content, or visual storytelling.

## 🎯 Features

- Converts two PDF pages into a dynamic transition sequence
- Cylinder-like slide effect between images
- Optional image scaling for reduced file size
- Includes pause frames before reversing the animation
- Saves output as individual PDF frames

## 🖼️ Example Output

See animate.pdf. Use Adobe or similar for display.

## 🔧 Requirements

- Python 3.8 or newer
- [pdf2image](https://pypi.org/project/pdf2image/)
- [Pillow (PIL)](https://pypi.org/project/Pillow/)
- Poppler (required by pdf2image for PDF rendering)

### 📥 Install dependencies

bash
pip install pdf2image Pillow



## 🚀 Usage

bash
from your_script_file import cylinder_transition_effect

cylinder_transition_effect(
    input_image_path1="first.pdf",
    input_image_path2="second.pdf",
    output_folder="output_frames",
    num_frames=31,
    pause_frames=12,
    scale_factor=0.5
)


This will create a series of PDF files (frames) in the output directory, visually transitioning from first.pdf to second.pdf and back again.

Example:

bash
cylinder_transition_effect("best-min.pdf", "IQ.pdf", "frames_cylinder_new", num_frames=31, pause_frames=12, scale_factor=0.5)


Example usage in latex:

bash
\documentclass[a4paper,10pt]{article}
\usepackage[utf8]{inputenc}
\usepackage{graphicx}
\usepackage{animate}
\usepackage[margin=0cm, top=0cm, bottom=0cm, noheadfoot]{geometry}
\usepackage{hyperref}

\begin{document}
\begin{animateinline}[autoplay,loop,controls=false,poster=first]{15}
\multiframe{88}{i=1+1}{%
    \includegraphics[width=\paperwidth,height=0.99\paperheight]{frames_cylinder_new/frame\i.pdf}}
\end{animateinline}

\end{document}



## 📂 Output Structure

bash
output_frames/
├── frame1.pdf
├── frame2.pdf
├── ...
└── frameN.pdf



## 🧪 Function Parameters

bash
| Parameter           | Type  | Description                                                 |
| ------------------- | ----- | ----------------------------------------------------------- |
| `input_image_path1` | str   | Path to the first PDF file                                  |
| `input_image_path2` | str   | Path to the second PDF file                                 |
| `output_folder`     | str   | Folder to save output frames                                |
| `num_frames`        | int   | Number of transition steps (default: 10)                    |
| `pause_frames`      | int   | Number of still frames before/after transition (default: 5) |
| `scale_factor`      | float | Resize factor for both images (default: 0.5)                |



## 🪪 License

This project is licensed under the MIT License.
Feel free to use, modify, and distribute this code with attribution.

## 🤝 Contributions
Pull requests are welcome! Feel free to open an issue if you find bugs or want to request a feature.
