
import math

from PIL import Image

class Unshredder(object):

    def __init__(self, in_, width):

        self.input = Image.open(in_)
        self.shred_width = width
        self.number_of_shreds = self.input.size[0] / self.shred_width

    def _get_shreds(self):

        shreds = []

        for i in range(self.number_of_shreds):
            x1 = self.shred_width * i
            y1 = 0
            x2 = x1 + self.shred_width
            y2 = self.input.size[1]

            shreds.append(self.input.crop((x1, y1, x2, y2)))

        return shreds

    def _get_left_pixel_column(self, shred):

        return shred.crop((0, 0, 1, self.input.size[1]))

    def _get_right_pixel_column(self, shred):

        return shred.crop((self.shred_width - 1, 0, self.shred_width, self.input.size[1]))

    def _compare_pixel_columns(self, left, right):

        score = 0

        for y in range(self.input.size[1]):
            left_pixel = left.getpixel((0, y))
            right_pixel = right.getpixel((0, y))

            score += math.sqrt(
                               math.pow(left_pixel[0] - right_pixel[0], 2) + 
                               math.pow(left_pixel[1] - right_pixel[1], 2) + 
                               math.pow(left_pixel[2] - right_pixel[2], 2)
                              )

        return score

    def unshred(self, out):

        unsorted_shreds = self._get_shreds()
        sorted_shreds = [unsorted_shreds[0]]
        unsorted_shreds[0].used = True

        for candidate_shred in unsorted_shreds[1:]:
            left_pixel_strip = self._get_left_pixel_column(sorted_shreds[0])
            right_pixel_strip = self._get_right_pixel_column(sorted_shreds[-1])

            best_left_match, best_right_match = None, None
            best_left_score, best_right_score = None, None

            for unsorted_shred in unsorted_shreds[1:]:
                if hasattr(unsorted_shred, "used"):
                    if unsorted_shred.used == True:
                        continue

                left = self._get_left_pixel_column(unsorted_shred)
                right = self._get_right_pixel_column(unsorted_shred)

                left_score = self._compare_pixel_columns(left_pixel_strip, right)
                right_score = self._compare_pixel_columns(right_pixel_strip, left)

                if best_left_score is None or left_score < best_left_score:
                    best_left_score = left_score
                    best_left_match = unsorted_shred

                if best_right_score is None or right_score < best_right_score:
                    best_right_score = right_score
                    best_right_match = unsorted_shred

            if best_right_score < best_left_score:
                sorted_shreds.append(best_right_match)
                best_right_match.used = True

            else:
                sorted_shreds.insert(0, best_left_match)
                best_left_match.used = True

        output = Image.new("RGBA", self.input.size)
        for i in range(self.number_of_shreds):
            x1 = self.shred_width * i
            y1 = 0

            output.paste(sorted_shreds[i], (x1, y1))

        output.save(out, "JPEG")

if __name__ == "__main__":

    import argparse

    parser = argparse.ArgumentParser(description="Image Unshredder.")
    parser.add_argument("-i", "--in", required=True, dest="in_", help="Path to the input file.")
    parser.add_argument("-o", "--out", required=True, dest="out", help="Path to the output file.")
    parser.add_argument("-w", "--strip-width", required=True, dest="width", type=int, help="The width in pixels of each strip.")

    args = parser.parse_args()

    unshredder = Unshredder(args.in_, args.width)
    unshredder.unshred(args.out)

