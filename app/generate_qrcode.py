import random
import qrcode
from datetime import datetime
import os, string


def generate_random_code(length=6):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

def main():
    FORM_URL_BASE = os.getenv('FORM_URL_BASE')
    OUTPUT_DIR = os.getenv('OUTPUT_DIR')
    CODE_LENGTH = int(os.getenv('CODE_LENGTH'))
    
    code = generate_random_code(CODE_LENGTH)
    # add the code to the url, will be implemented later
    # full_url = f"{FORM_URL_BASE}{code}"

    full_url = f"{FORM_URL_BASE}"
    # Generate QR code
    qr = qrcode.make(full_url)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = "qr.png"
    file_path = os.path.join(OUTPUT_DIR, file_name)
    qr.save(file_path)
    return "QR Code generated"
if __name__ == "__main__":
    main()