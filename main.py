from gif_steganography import gif_steganography

def decode_steganography_gif(gif_filename):
    # Open the encrypted GIF image
    encrypted_image = gif_steganography.open(gif_filename)
    
    # Decode the hidden message
    decoded_message = encrypted_image.decode()
    
    return decoded_message

# Example usage
if __name__ == "__main__":
    gif_filename = 'encrypted_image.gif'  # Replace with your encrypted GIF filename
    decoded_message = decode_steganography_gif(gif_filename)
    print("Decoded Message:", decoded_message)
