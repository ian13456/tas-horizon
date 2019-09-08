from wand.image import Image as wi
from halo import Halo

import sys
import os
import shutil


# DUMMY CHECKS
if len(sys.argv) == 1:
  print("Please enter a file name.")
  sys.exit()
  

# OBTAINING BASIC FILE INFO 
filepath = sys.argv[1]
basename, file = os.path.split(filepath)
filename, _ = os.path.splitext(file)
img_basename = f"{basename}/{filename}"


# CONVERTING PDF TO JPEG 
def convert_pdf():
  with Halo(text='Converting... This may take a while.', spinner='dots') as spinner:
    # Create or clear image directory
    try:
      os.mkdir(img_basename)
    except:
      spinner.warn(text=f"Directory {img_basename} already exists. Overwritting...")
      shutil.rmtree(img_basename)
      os.mkdir(img_basename)
      
    # Generate PDF
    pdf = wi(filename=filepath, resolution=300)
    pdfimage = pdf.convert("jpeg")
    spinner.succeed('Conversion succeeded!')

  # SAVING IMAGES
  i=0
  for img in pdfimage.sequence:
      imgname = str(i)+".jpg"
      img_filename = f"{img_basename}/{imgname}"

      page = wi(image=img)
      page.save(filename=imgname)
      os.rename(imgname, img_filename)
      i +=1


# GENERATING HTML 
def generate_html():
  imglist = []
  directory = os.fsencode(img_basename)
  imgs_dir = os.listdir(directory)
  imgs_dir.sort()

  for file in imgs_dir: 
    img_name = os.fsdecode(file)
    if img_name.endswith(".jpg"): 
      imglist.append(img_name)

  html_filename = f"{basename}/{filename}.html"

  with open(html_filename, 'w') as htmlfile:

    main_imgs = ""
    cssfile = "../../css/test.css"
    
    for img_filename in imglist:
      main_imgs += f"<div style=\"background-image:url({filename}/{img_filename})\"></div>"

    htmlfile.write(f"""
      <html>
        <head>
          <meta name="viewport" content="width = 1050, user-scalable = no" />
          <script src="https://code.jquery.com/jquery-3.2.1.min.js" integrity="sha256-hwg4gsxgFZhOsEEamdOYGBf13FyQuiTwlAQgxVSNgt4=" crossorigin="anonymous"></script>
          <script src="../../lib/turn.js"></script>
          <link rel="stylesheet" href="{cssfile}" />
        </head>

        <body>
          <div class="flipbook-viewport">
            <div class="container">
              <div class="flipbook">
                {main_imgs}
              </div>
            </div>
          </div>
          
          <script src="../../js/flipbook.js"></script>
        </body>
      </html>
    """)

if __name__ == '__main__':
  # convert_pdf()
  generate_html()

