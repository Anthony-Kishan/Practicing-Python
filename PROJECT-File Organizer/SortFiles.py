import os
import shutil

# Define paths
dataset_path = input("Enter Data-set folder path: ") # 'C:/Users/WALTON/Downloads/Dataset'

zip_path = os.path.join(dataset_path, 'ZIP')
font_path = os.path.join(dataset_path, 'FONTS')
program_path = os.path.join(dataset_path, 'PROGRAMS1')
graphics_path = os.path.join(dataset_path, 'GRAPHICS')
video_path = os.path.join(dataset_path, 'VIDEO')
audio_path = os.path.join(dataset_path, 'AUDIO')
picture_path = os.path.join(dataset_path, 'PICTURE')
doc_path = os.path.join(dataset_path, 'DOCUMENTS')

# Create directories if they do not exist
os.makedirs(zip_path, exist_ok=True)
os.makedirs(font_path, exist_ok=True)
os.makedirs(program_path, exist_ok=True)
os.makedirs(graphics_path, exist_ok=True)
os.makedirs(video_path, exist_ok=True)
os.makedirs(audio_path, exist_ok=True)
os.makedirs(picture_path, exist_ok=True)
os.makedirs(doc_path, exist_ok=True)

# Define file extensions for categorization
zip_extensions = ['.zip', '.rar']
font_extensions = ['.ttf', '.otf']
program_extensions = ['.exe', '.py', '.ino']
graphics_extensions = ['.psd', '.ai', '.eps']
video_extensions = ['.mp4', '.avi', '.mov', '.mkv', '.wmv']
audio_extensions = ['.mp3', '.wav', '.aac', '.flac', '.ogg']
picture_extensions = ['.jpg', '.png', '.jpeg', '.gif', '.webm', '.svg', '.webp']
doc_extensions = ['.pdf', '.docx', '.xlsx', '.html', '.txt', '.xls', '.csv', '.doc', '.ppt']

# Function to categorize and rename files
def categorize_and_rename_files():
    for filename in os.listdir(dataset_path):
        file_path = os.path.join(dataset_path, filename)
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(filename)[1].lower()

            if file_extension in zip_extensions:
                shutil.move(file_path, zip_path)

            elif file_extension in font_extensions:
                shutil.move(file_path, font_path)

            elif file_extension in program_extensions:
                shutil.move(file_path, program_path)

            elif file_extension in graphics_extensions:
                shutil.move(file_path, graphics_path)
            
            elif file_extension in video_extensions:
                shutil.move(file_path, video_path)
            
            elif file_extension in audio_extensions:
                shutil.move(file_path, audio_path)

            elif file_extension in picture_extensions:
                shutil.move(file_path, picture_path)

            elif file_extension in doc_extensions:
                shutil.move(file_path, doc_path)


# Main execution
categorize_and_rename_files()

print("Files have been categorized successfully.")
