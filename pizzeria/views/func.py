from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
import os

from django.http import FileResponse, HttpResponse
from PyPDF2 import PdfFileWriter, PdfFileReader
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from csv import reader
import io
from datetime import datetime
import cv2


import pyqrcode
import png
from pyqrcode import QRCode
import random


path = f"{settings.STATICFILES_DIRS[0]}"


def sendmail(request, username, usermail):
    host = request.META.get('HTTP_HOST')
    info = {
        'username' : username,
        'protocol' : 'http://',
        'host' : host,
    }

    template_email = render_to_string('pizzeria/email.html', info)

    email = EmailMessage("Confirmation de votre commande", template_email, settings.EMAIL_HOST_USER, [usermail])
    email.content_subtype = "html"
    email.fail_silently = False
    try:
        email.send()
        return "OK mail sent success"
    except Exception as e:
        return "Fail to send mail"
    


def genpdf(request, token):

        packet = io.BytesIO()
        can = canvas.Canvas(packet, pagesize=letter)
        can.setFont('Helvetica', 12)

        today = datetime.now().date()

        can.drawString(22, 20, f"Ce document est généré à cette date et est uniquement valable au même date: {today}")
        can.drawString(80, 590, f"Ce document est valable jusqu'à {today}")

        can.setFont('Helvetica', 20)
        can.drawString(80, 520, f"N° de la commande> {token}")

        # can.setFont('Helvetica', 14)
        # can.drawString(95, 475, "1 - Pizza kebab")
        # can.drawString(95, 460, "2 - Pizza chèvre de miel")

        can.drawImage(f'{path}/qrcode/qrcode.png', 200, 250, 200, 200, mask='auto')
        can.save()

        # move to the beginning of the StringIO buffer
        packet.seek(0)

        # create a new PDF with Reportlab
        new_pdf = PdfFileReader(packet) 

        # read your existing PDF
        existing_pdf = PdfFileReader(open(f"{path}/recu/boul.ange.pdf", "rb"))
        output = PdfFileWriter()

        # add the "watermark" (which is the new pdf) on the existing page
        page = existing_pdf.getPage(0)
        page.mergePage(new_pdf.getPage(0))
        output.addPage(page)

        # finally, write "output" to a real file
        outputStream = open(f"{path}/recu/commandes/{today}-{token}.pdf", "wb")
        output.write(outputStream)
        outputStream.close()

        # touch pdf file to render view
        # pdf_file = open(f"{path}/makan_dev.jpg", 'rb')  
        # return FileResponse(pdf_file, as_attachment=True, content_type="application/pdf")


def gentoken(char=10):
    """ Generate token char: len token """

    token = "" 
    alphanum = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
        '!', '?'
    ]
    for _ in range(char):
        random_alphanum = random.choice(alphanum)
        token += random_alphanum

    return token


def qrcode(request, token):
    qr = pyqrcode.create(token)
    qr.png(f"{path}/qrcode/qrcode.png", scale=6)