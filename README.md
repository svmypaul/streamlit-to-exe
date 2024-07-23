# Streamlit To EXE

## Overview

This project is a Python application that uses Streamlit for its frontend. The following guide provides instructions for setting up the development environment and creating an executable file from the Python script.

## Installation Guide

### Prerequisites

Ensure you have Python installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

### Setting Up the Environment

1. **Clone the Repository**

   ```bash
   git clone git@github.com:svmypaul/streamlit-to-exe.git
   cd streamlit-to-exe
   ```

2. **Create and Activate a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Required Packages**

   Create a `requirements.txt` file in your project directory with the necessary packages listed. To install them, run:

   ```bash
   pip install -r requirements.txt
   ```

## Creating the Executable

1. **Prepare the Application**

   Ensure that you have the following files in your project directory:
   - `app.py`: The main Python script for your application.
   - `app_new.py`: The Streamlit script.
   - `streamlit.exe`: This file is located in `env\Scripts\streamlit.exe`.

2. **Install PyInstaller**

   If you haven't installed PyInstaller yet, you can do so using pip:

   ```bash
   pip install pyinstaller
   ```

3. **Generate the Executable**

   Use the following PyInstaller command to create a standalone executable file. This command will bundle your Python script and any additional data files into a single executable:

   ```bash
   pyinstaller --onefile --noconsole --add-data "app_new.py;." --add-data "streamlit.exe;." app.py
   ```

   - `--onefile`: Packages everything into a single executable file.
   - `--noconsole`: Hides the console window (useful for GUI applications).
   - `--add-data "app_new.py;."`: Includes the `app_new.py` script in the executable.
   - `--add-data "streamlit.exe;."`: Includes the `streamlit.exe` file in the executable.
   - `app.py`: Your main Python script.

4. **Locate the Executable**

   After running the PyInstaller command, the executable will be created in the `dist` directory within your project folder.

## Running the Executable

Navigate to the `dist` directory and run the executable file. This will launch your application without needing to run Python or Streamlit separately.

## Troubleshooting

- **If you encounter any issues with missing files**, ensure that all required files are correctly specified in the `--add-data` arguments of the PyInstaller command.
- **If the executable does not run as expected**, check the logs in the `build` directory for any errors that occurred during the packaging process.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or support, please contact [your-email@example.com](mailto:svmypaul.cob@gamil.com).
```

Make sure to replace placeholders like `git@github.com:svmypaul/streamlit-to-exe.git` and `streamlit-to-exe` with your actual repository URL and directory name.
