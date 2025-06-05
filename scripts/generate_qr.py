#!/usr/bin/env python3

import argparse
import qrcode
from pathlib import Path
import os

def generate_qr_code(url, output_path=None):
    """
    Generate a QR code from a URL and save it to a file.
    
    Args:
        url (str): The URL to encode in the QR code
        output_path (str, optional): Path where to save the QR code image. 
                                   If not provided, will use the current directory.
    """
    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    # Add data
    qr.add_data(url)
    qr.make(fit=True)
    
    # Create an image from the QR Code
    qr_image = qr.make_image(fill_color="black", back_color="white")
    
    # Generate output filename if not provided
    if output_path is None:
        # Create 'output' directory if it doesn't exist
        output_dir = Path('output')
        output_dir.mkdir(exist_ok=True)
        
        # Generate filename based on URL
        from urllib.parse import urlparse
        parsed_url = urlparse(url)
        filename = f"{parsed_url.netloc}_{parsed_url.path.replace('/', '_')}.png"
        if filename == "_.png":  # Handle empty URL parts
            filename = "qr_code.png"
        output_path = output_dir / filename
    
    # Save the image
    qr_image.save(str(output_path))
    print(f"QR code has been generated and saved to: {output_path}")

def main():
    parser = argparse.ArgumentParser(description='Generate QR code from a URL')
    parser.add_argument('--url', required=True, help='URL to encode in QR code')
    parser.add_argument('--output', help='Output file path (optional)')
    
    args = parser.parse_args()
    
    generate_qr_code(args.url, args.output)

if __name__ == '__main__':
    main()
