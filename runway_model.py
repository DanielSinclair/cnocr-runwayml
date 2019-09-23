from PIL import Image
from cnocr import CnOcr
import runway
from runway.data_types import file, array, text

char_type = array(item_type=text)
ocr = CnOcr()

@runway.setup
def setup():
    return ocr

@runway.command('classify', inputs={ 'image': file() }, outputs={ 'chars': array(item_type=char_type) })
def classify(model, input):
    img = input['image']
    res = ocr.ocr(img)
    return { 'chars': res }

if __name__ == '__main__':
    runway.run()