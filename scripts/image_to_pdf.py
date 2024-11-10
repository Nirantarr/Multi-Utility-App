import img2pdf
from tkinter import Tk
from tkinter.filedialog import askopenfilenames, asksaveasfilename

def create_pdf_from_images(selected_images, output_pdf_name):
    if not selected_images:
        print("No images selected. Please select some images to proceed.")
        return
    
    image_data_list = []
    for image_path in selected_images:
        with open(image_path, "rb") as img_file:
            image_data_list.append(img_file.read())

    pdf_data = img2pdf.convert(image_data_list)

    with open(output_pdf_name, "wb") as pdf_file:
        pdf_file.write(pdf_data)
    
    print(f"PDF created successfully! You can find it at: '{output_pdf_name}'")


def select_images():
    Tk().withdraw()
    selected_images = askopenfilenames(
        title="Select Images to Convert into PDF",
        filetypes=[("Image Files", "*.jpg *.jpeg *.png *.gif")]
    )
    return selected_images

def choose_pdf_save_location():
    Tk().withdraw()
    output_pdf_name = asksaveasfilename(
        title="Save PDF As",
        defaultextension=".pdf",
        filetypes=[("PDF Files", "*.pdf")]
    )
    return output_pdf_name


selected_images = select_images()
output_pdf_name = choose_pdf_save_location()


if selected_images and output_pdf_name:
    create_pdf_from_images(selected_images, output_pdf_name)
else:
    print("Operation cancelled. Please ensure you select images and specify a file name.")