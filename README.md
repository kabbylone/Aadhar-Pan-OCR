# Aadhar_Card_OCR_Python
This is a simple implementation of a OCR reader for the Aadhar and PAN Card. To use this project: 
- Download the python files in the repository.
- Open the python files - **Aadhar_OCR.py** and **PAN_OCR.py** in any IDLE and make the necessary changes in the code to match your system.
- Make sure that the mysql server is running while running the main source file **FYP_OCR.py**. Create a table in a database with columns for Aadhar card number, gender, data of birth, and name for reading the Aadhar Card details. Also create a table in a database with column for PAN card no. for reading the PAN card details.
- Execute the python file - **FYP_OCR.py** and make sure the files **Aadhar_OCR.py** and **PAN_OCR.py** are in the same working directory.

## Implementation Steps
On executing the **FYP_OCR.py** file you should observe this window - <br>
![Start OCR](Images/Start_OCR.PNG) <br>


On selecting **Aadhar Card** or **PAN Card** you should be promted to a new open-file window - <br>
![Open Image](Images/Image_to_upload.PNG) <br>


On uploading an image, you might have to wait for a few seconds (depending on your system) before the window changes and you see your details extracted from the image. <br>
#### Aadhar Card
![Aadhar Card Details Extracted](Images/Aadhar_Card_To_Upload.PNG) <br>
#### PAN Card
![PAN Card Details Extracted](Images/PAN_Card_To_Upload.PNG) <br>


If the details extracted are not correct the user may rectify that in the text box. Once the details are verified the user may click the submit button and expect the following response - <br>
![Changes sent to database](Images/Details_Submitted.PNG) <br>


On clicking **OK** the window closes and the details will be reflected in the mysql database. 

## Dependencies
The project has the following dependencies:
- [opencv](https://pypi.org/project/opencv-python/)
- [PIL](https://pypi.org/project/Pillow/2.2.2/)
- [pytesseract](https://pypi.org/project/pytesseract/)
- [Tkinter](https://docs.python.org/3/library/tkinter.html)
- Regular Expressions - [re](https://pypi.org/project/regex/)
- mysql connector for python - [mysql.connector](https://pypi.org/project/mysql-connector-python/)
