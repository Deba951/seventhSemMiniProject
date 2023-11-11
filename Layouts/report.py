# from reportlab.lib.pagesizes import letter
# from reportlab.lib import colors
# from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
# import os

# def generate_report(patient_name, doctor_name, pathology_name, user_data, prediction):
#     # Create a PDF report
#     doc = SimpleDocTemplate("diabetes_report.pdf", pagesize=letter)
#     elements = []

#     # Create a list of data to display in the report
#     data = [
#         ["Patient's Name:", patient_name],
#         ["Referred Doctor:", doctor_name],
#         ["Pathology Name:", pathology_name],
#     ]

#     # Add user input data and prediction result to the report
#     for key, value in user_data.items():
#         data.append([key, str(value)])

#     data.append(["Prediction Result:", prediction])  # Use the variable 'prediction'


#     # data.append(["Prediction Result:", prediction_result])

#     # Create a table to display the data
#     table = Table(data, colWidths=150, rowHeights=30)
#     table.setStyle(TableStyle([
#         ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
#         ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
#         ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
#         ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
#         ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
#         ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
#         ('GRID', (0, 0), (-1, -1), 1, colors.black)
#     ]))

#     elements.append(table)

#     # Build and save the PDF report
#     doc.build(elements)

# if __name__ == "__main__":
#     # Example data, replace with actual user input and prediction result
#     patient_name = "John Doe"
#     doctor_name = "Dr. Smith"
#     pathology_name = "Health Clinic"
#     user_data = {
#         "Fasting Glucose": 100,
#         "Aftermeal Glucose": 150,
#         # Include other user input fields
#     }
#     prediction_result = "Positive"

#     # Output file path
#     output_path = "diabetes_report.pdf"

#     generate_report(patient_name, doctor_name, pathology_name, user_data, prediction_result, output_path)
#     print(f"Report generated and saved as {output_path}")














# from reportlab.lib.pagesizes import letter
# from reportlab.lib import colors
# from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Image
# from io import BytesIO
# import os

# def generate_report(patient_name, doctor_name, pathology_name, user_data, prediction, output_path):
#     # Create a PDF report
#     doc = SimpleDocTemplate(output_path, pagesize=letter)
#     elements = []

#     # Create a list of data to display in the report
#     data = [
#         ["Patient's Name:", patient_name],
#         ["Referred Doctor:", doctor_name],
#         ["Pathology Name:", pathology_name],
#     ]

#     # Add user input data and prediction result to the report
#     for key, value in user_data.items():
#         data.append([key, str(value)])

#     data.append(["Prediction Result:", prediction])

#     # Create a table to display the data
#     table = Table(data, colWidths=150, rowHeights=30)
#     table.setStyle(TableStyle([
#         ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
#         ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
#         ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
#         ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
#         ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
#         ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
#         ('GRID', (0, 0), (-1, -1), 1, colors.black)
#     ]))

#     elements.append(table)

#     # Add an image based on prediction result
#     if prediction == "Positive":
#         image_path = "positive_diabetes_image.png"
#     else:
#         image_path = "negative_diabetes_image.png"

#     if os.path.exists(image_path):
#         img = Image(image_path, width=200, height=200)
#         elements.append(img)

#     # Build and save the PDF report
#     doc.build(elements)








from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Image
from io import BytesIO
import os
import streamlit as st

def generate_report(patient_name, doctor_name, pathology_name, user_data, prediction, output_path):

    doc = SimpleDocTemplate(output_path, pagesize=letter)
    elements = []

    # Create a list of data to display in the report
    data = [
        ["Patient's Name:", patient_name],
        ["Referred Doctor:", doctor_name],
        ["Pathology Name:", pathology_name],
    ]

    # Add user input data and prediction result to the report
    for key, value in user_data.items():
        data.append([key, str(value)])

    data.append(["Prediction Result:", prediction])

    # Create a table to display the data
    table = Table(data, colWidths="60%", rowHeights=30)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.black),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))

    elements.append(table)

    # # Add an image based on prediction result
    # if prediction == "Positive":
    #     image_path = "positive_diabetes_image.png"
    # else:
    #     image_path = "negative_diabetes_image.png"

    # if os.path.exists(image_path):
    #     img = Image(image_path, width=200, height=200)
    #     elements.append(img)

    # Build and save the PDF report
    doc.build(elements)

if __name__ == "__main__":
    # Example data, replace with actual user input and prediction result
    patient_name = "John Doe"
    doctor_name = "Dr. Smith"
    pathology_name = "Health Clinic"
    user_data = {
        "Fasting Glucose": 100,
        "Aftermeal Glucose": 150,
        # Include other user input fields
    }
    prediction_result = "Positive"

    # Output file path
    output_path = "diabetes_report.pdf"

    # Call the generate_report function
    generate_report(patient_name, doctor_name, pathology_name, user_data, prediction_result, output_path)
    st.write(f"Report generated and saved as {output_path}")
