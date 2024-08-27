# File Organizer

This project is a simple Python-based file organizer that categorizes files into different folders based on their extensions. The script helps you manage and organize a large dataset by automatically moving files into designated directories like ZIP, FONTS, PROGRAMS, GRAPHICS, VIDEO, AUDIO, PICTURES, and DOCUMENTS.

## Features

- **Automatic Categorization**: Organizes files into folders based on their file extensions.
- **Extensible**: Easily add more file extensions to customize categorization.
- **Cross-Platform**: Works on Windows, macOS, and Linux.

## Requirements

- Python 3.x

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Anthony-Kishan/file-organizer.git
   cd file-organizer
   ```

2. **Install Dependencies:**
   This project does not require any external dependencies, so you can run the Python script directly.

## Usage

1. **Run the Script:**
   Execute the script using Python:
   ```bash
   python file_organizer.py
   ```

2. **Input the Dataset Path:**
   When prompted, enter the path to the folder containing your files to be organized. Example:
   ```bash
   Enter Data-set folder path: C:/Users/WALTON/Downloads/Dataset
   ```

3. **Categorization:**
   The script will automatically move files into their respective folders based on the following extensions:

   - **ZIP Files:** `.zip`, `.rar`
   - **Fonts:** `.ttf`, `.otf`
   - **Programs:** `.exe`, `.py`, `.ino`
   - **Graphics:** `.psd`, `.ai`, `.eps`
   - **Videos:** `.mp4`, `.avi`, `.mov`, `.mkv`, `.wmv`
   - **Audio:** `.mp3`, `.wav`, `.aac`, `.flac`, `.ogg`
   - **Pictures:** `.jpg`, `.png`, `.jpeg`, `.gif`, `.webm`, `.svg`, `.webp`
   - **Documents:** `.pdf`, `.docx`, `.xlsx`, `.html`, `.txt`, `.xls`, `.csv`, `.doc`, `.ppt`

4. **Completion:**
   After execution, a message will confirm that the files have been categorized successfully.

## Contributing

If you would like to contribute to this project, feel free to fork the repository and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the open-source community for inspiration and code snippets.