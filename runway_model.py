import runway
import numpy as np
from cnocr import CnOcr

@runway.setup(options={"network_size":runway.category(choices=['64', '128', '256', '512'])})
def setup(opts):
    model = CnOcr()
    return model

@runway.command('classify', inputs={'image': runway.image}, outputs={'text': runway.text})
def classify(model, inputs):
    image = np.array(inputs['image'])
    res = model.ocr(image)
    return {'text':res}

if __name__ == '__main__':
    runway.run(host='0.0.0.0', port=9000)