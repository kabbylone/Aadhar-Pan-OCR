# IMPORTING REQUIRED PACKAGES
import tkinter
import tkinter.ttk
from tkinter import messagebox
from tkinter.filedialog import askopenfile
from PAN_OCR import PAN_OCR
from Aadhar_OCR import Aadhar_OCR
from PIL import ImageTk,Image, ExifTags

####################################################################################################################################################################################################
####################################################################################################################################################################################################
####################################################################################################################################################################################################

# INITIALIZING WINDOW AND SETTING TITLE
window = tkinter.Tk()
window.title('Choose Card to Upload')

####################################################################################################################################################################################################
####################################################################################################################################################################################################

# SPLITTING WINDOW INTO 3 FRAMES - TOP, MIDDLE, BOTTOM
# TOP - used for holding the upload buttons
# MID - used for displaying the image path and the image
# BOT - used for displaying the extracted details and the submit button
top_frame = tkinter.Frame(window)
top_frame.grid(column=0, row=0)
    
mid_frame = tkinter.Frame(window)
mid_frame.grid(column=0, row=1)
    
bot_frame = tkinter.Frame(window)
bot_frame.grid(column=0, row=2)

####################################################################################################################################################################################################
####################################################################################################################################################################################################

# COMMIT THE DETAILS EXTRACTED AND VERIFIED FROM THE AADHAR CARD INTO A SQL DATABASE FOR VERIFICATION
def commit_aadhar_changes(img_path, aadhar_no, gender, dob, name):
    aadhar_ocr = Aadhar_OCR(img_path)
    aadhar_ocr.commit_changes(aadhar_no, gender, dob, name)
    
    tkinter.messagebox.showinfo("Changes Saved", "Your Details are saved in our Database and will be validated shortly.")
    
    window.destroy()

####################################################################################################################################################################################################
    
# OPEN THE AADHAR CARD IMAGE FROM WHICH DETAILS ARE TO BE EXTRACTED
def aadhar_card():
    file = askopenfile(mode ='r', filetypes=[('JPG file (*.jpg)', '*.jpg'), 
                                             ('JPEG file (*.jpeg)', '*.jpeg'), 
                                             ('PNG file (*.png)', '*.png')])
    
    ##################################################################################################
    
    if file is not None: 
        # DISPLAY THE PATH OF THE IMAGE AT THE TOP OF THE MID FRAME
        img_path = str(file.name)
        label = tkinter.Label(mid_frame, text=img_path)
        label.grid(column=0, row=0, sticky="W", columnspan=1000)
        
        # DISPLAY THE AADHAR CARD IMAGE AT THE BOTTOM OF THE MID FRAME
        aadhar_img = ImageTk.PhotoImage(Image.open(img_path).resize((300, 500)))
        aadhar_label = tkinter.Label(mid_frame, image=aadhar_img)
        aadhar_label.image = aadhar_img # keep a reference!
        aadhar_label.grid(column=0, row=1, columnspan=1000)
        
        ##################################################################################################
        
        # CALL THE Aadhar_OCR PACKAGE WITH THE IMAGE PATH.
        aadhar_ocr = Aadhar_OCR(img_path)
        # EXTRACT DATA FROM THE IMAGE
        user_aadhar_no, user_gender, user_dob, user_name = aadhar_ocr.extract_data()

        ##################################################################################################
        
        # DISPLAY THE DETAILS AT THE TOP OF THE BOT FRAME - 
        # 1) AADHAR NO
        aadhar_no_label = tkinter.Label(bot_frame, text="Aadhar Card No - ")
        aadhar_no_label.grid(column=0, row=0, sticky="W")

        aadhar_no_entry = tkinter.Entry(bot_frame, width=20)
        aadhar_no_entry.grid(column=1, row=0, sticky="W")
        aadhar_no_entry.insert(0, user_aadhar_no)

        # 2) GENDER
        gender_label = tkinter.Label(bot_frame, text="Gender - ")
        gender_label.grid(column=0, row=1, sticky="W")

        gender_entry = tkinter.Entry(bot_frame, width=20)
        gender_entry.grid(column=1, row=1, sticky="W")
        gender_entry.insert(0, user_gender)

        # 3) DATE OF BIRTH
        dob_label = tkinter.Label(bot_frame, text="Date of Birth - ")
        dob_label.grid(column=0, row=2, sticky="W")

        dob_entry = tkinter.Entry(bot_frame, width=20)
        dob_entry.grid(column=1, row=2, sticky="W")
        dob_entry.insert(0, user_dob)

        # 4) NAME
        name_label = tkinter.Label(bot_frame, text="Name - ")
        name_label.grid(column=0, row=3, sticky="W")

        name_entry = tkinter.Entry(bot_frame, width=20)
        name_entry.grid(column=1, row=3, sticky="W")
        name_entry.insert(0, user_name)
        
        ##################################################################################################
        
        # SUBMIT BUTTON AT THE BOTTOM OF BOT FRAME USED TO COMMIT CHANGES TO A SQL DATABASE ONCE THE USER HAS VERIFIED DETAILS EXTRACTED FROM THE IMAGE
        submit_btn = tkinter.Button(
            bot_frame, 
            text="Submit", 
            fg="red", 
            command = lambda:commit_aadhar_changes(
                img_path,
                aadhar_no_entry.get(), 
                gender_entry.get(), 
                dob_entry.get(), 
                name_entry.get()
            )
        )
        submit_btn.grid(column=0, row=4)

####################################################################################################################################################################################################
        
# BUTTON TO UPLOAD THE AADHAR CARD IMAGE FOR EXTRACTING DATA
aadhar_btn = tkinter.Button(top_frame, text="Aadhar Card", fg="red", command = lambda:aadhar_card())
aadhar_btn.grid(column=0, row=0)

####################################################################################################################################################################################################
####################################################################################################################################################################################################

# COMMIT THE DETAILS EXTRACTED AND VERIFIED FROM THE PAN CARD INTO A SQL DATABASE FOR VERIFICATION
def commit_pan_changes(img_path, pan_no):
    pan_ocr = PAN_OCR(img_path)
    pan_ocr.commit_changes(pan_no)
    
    tkinter.messagebox.showinfo("Changes Saved", "Your Details are saved in our Database and will be validated shortly.")
    
    window.destroy()

####################################################################################################################################################################################################

# OPEN THE PAN CARD IMAGE FROM WHICH DETAILS ARE TO BE EXTRACTED    
def pan_card():
    file = askopenfile(mode ='r', filetypes=[('JPG file (*.jpg)', '*.jpg'), 
                                             ('JPEG file (*.jpeg)', '*.jpeg'), 
                                             ('PNG file (*.png)', '*.png')])
    
    ##################################################################################################
    
    if file is not None: 
        # DISPLAY THE PATH OF THE IMAGE AT THE TOP OF THE MID FRAME
        img_path = str(file.name)
        label = tkinter.Label(mid_frame, text=img_path)
        label.grid(column=0, row=0, sticky="W", columnspan=1000)
        
        # CHECK THE ORIENTATION OF THE IMAGE
        try:
            pan_img=Image.open(img_path)
            for orientation in ExifTags.TAGS.keys():
                if ExifTags.TAGS[orientation]=='Orientation':
                    break
            exif=dict(pan_img._getexif().items())

            if exif[orientation] == 3:
                pan_img=pan_img.rotate(180, expand=True)
            elif exif[orientation] == 6:
                pan_img=pan_img.rotate(270, expand=True)
            elif exif[orientation] == 8:
                pan_img=pan_img.rotate(90, expand=True)
            pan_img.save(img_path)
            pan_img.close()

        except (AttributeError, KeyError, IndexError):
            # cases: image don't have getexif
            pass
        
        # DISPLAY THE PAN CARD IMAGE AT THE BOTTOM OF THE MID FRAME
        pan_img = ImageTk.PhotoImage(Image.open(img_path).resize((500, 300)))
        pan_label = tkinter.Label(mid_frame, image=pan_img)
        pan_label.image = pan_img # keep a reference!
        pan_label.grid(column=0, row=1)
        
        ##################################################################################################
        
        # CALL THE PAN_OCR PACKAGE WITH THE IMAGE PATH.
        pan_ocr = PAN_OCR(str(file.name))
        # EXTRACT DATA FROM THE IMAGE
        user_pan_no = pan_ocr.extract_data()

        ##################################################################################################
        
        # DISPLAY THE DETAILS AT THE TOP OF THE BOT FRAME - 
        # 1) PAN CARD NO
        pan_no_label = tkinter.Label(bot_frame, text="PAN Card No - ")
        pan_no_label.grid(column=0, row=0, sticky="W")

        pan_no_entry = tkinter.Entry(bot_frame, width=20)
        pan_no_entry.grid(column=1, row=0, sticky="W")
        pan_no_entry.insert(0, user_pan_no)
        
        ##################################################################################################
        
        # SUBMIT BUTTON AT THE BOTTOM OF BOT FRAME USED TO COMMIT CHANGES TO A SQL DATABASE ONCE THE USER HAS VERIFIED DETAILS EXTRACTED FROM THE IMAGE
        submit_btn = tkinter.Button(
            bot_frame, 
            text="Submit", 
            fg="red", 
            command = lambda:commit_pan_changes(
                img_path,
                pan_no_entry.get()
            )
        )
        submit_btn.grid(column=0, row=1)

####################################################################################################################################################################################################

# BUTTON TO UPLOAD THE PAN CARD IMAGE FOR EXTRACTING DATA
pan_btn = tkinter.Button(top_frame, text="PAN Card", fg="green", command = lambda:pan_card())
pan_btn.grid(column=1, row=0)

####################################################################################################################################################################################################
####################################################################################################################################################################################################

# SETTING WINDOW TO CLOSE WITH USER'S MOUSE CLICK
window.mainloop()
