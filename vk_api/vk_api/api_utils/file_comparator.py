from PIL import Image
import imagehash


class FileComparator:
    MIN_ACCEPTABLE_DIFF = 70
    MAX_ACCEPTABLE_DIFF = 100

    def compare_images(self, image1, image2):
        hash1 = imagehash.phash(Image.open(image1))
        hash2 = imagehash.phash(Image.open(image2))
        difference = hash1 - hash2
        similarity = (1 - (difference / self.MIN_ACCEPTABLE_DIFF)) * self.MAX_ACCEPTABLE_DIFF
        return similarity >= self.MIN_ACCEPTABLE_DIFF
