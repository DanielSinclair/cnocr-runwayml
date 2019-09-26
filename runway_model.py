import runway
import numpy
from cnocr import CnOcr

lineCategory = runway.category(
    description = "Number of lines of characters. Improves accurary.",
    choices = ['single', 'multiple'], 
    default = 'multiple'
)

@runway.setup(options={'lines': lineCategory})
def setup(opts):
    model = CnOcr()
    return model.ocr if opts['lines'] == 'multiple' else model.ocr_for_single_line

classifyInput = {'image': runway.image(description="Image with Chinese characters.")}
classifyOutput = {'characters': runway.array(
    item_type = runway.array(item_type = runway.text), 
    description = "2D character array."
)}

@runway.command('classify', inputs = classifyInput, outputs = classifyOutput)
def classify(model, inputs):
    image = numpy.array(inputs['image'])
    res = model(image)
    return {'characters': res}

if __name__ == '__main__':
    runway.run(host='0.0.0.0', port=9000)