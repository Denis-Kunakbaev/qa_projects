import base64


class ImageCoder:
    @staticmethod
    def encode_image(image_path):
        with open(image_path, 'rb') as image_file:
            encoded_string = base64.b64encode(image_file.read())
        return encoded_string.decode('utf-8')
