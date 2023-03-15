# File for test convergence
from Imagekit.lib import Image
from Imagekit.processors.resize import ResizeToFit
import requests
from io import BytesIO

def test_resizetofit():
    # First create an image with aspect ratio 2:1...
    #img = Image.new('RGB', (200, 100))
    r = requests.get('https://images-na.ssl-images-amazon.com/images/S/pv-target-images/aab65914790c42178adb882aee410703ca305bdd974a00a110b8670258e22095._RI_V_TTW_.jpg')
    img = Image.open(BytesIO(r.content))
    img.show()
    # DP Small then resize it to fit within a 58x100 canvas.
    dp_small = ResizeToFit(200, 100).process(img)
    dp_small.show()
    # Assert that the image has maintained the aspect ratio.
    #assert img.size == (100, 50)

if __name__ == '__main__':
    test_resizetofit()


