from PIL import Image
from cnocr import CnOcr
import runway
from runway.data_types import file, array, text

char_type = array(item_type=text)

@runway.setup()
def setup():
    ocr = CnOcr()
    return ocr

@runway.command(name='classify', inputs={ 'image': file() }, outputs={ 'chars': array(item_type=char_type) })
def classify(model, input):
    res = model.ocr(input['image'])
    return { 'chars': res }

if __name__ == '__main__':
    runway.run()