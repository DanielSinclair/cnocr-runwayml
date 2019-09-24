import runway
from cnocr import CnOcr


@runway.setup(options={'lines': runway.category(choices=['single', 'multiple'])})
def setup(opts):
    ocr = CnOcr()
    return ocr.ocr if opts['lines'] == 'multiple' else ocr.ocr_for_single_line


@runway.command('classify', inputs={'image': runway.file(description='File path')}, outputs={'text': runway.text(description='Text')})
def classify(model, inputs):
    res = model(inputs['image'])
    print(res)
    return {'text': res}


if __name__ == '__main__':
    runway.run(host='0.0.0.0', port=9000)
