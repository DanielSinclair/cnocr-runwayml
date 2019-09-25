import runway
from cnocr import CnOcr

@runway.setup(options={"network_size":category(choices=[64, 128, 256, 512])})
def setup(opts):
    model = CnOcr()
    return model

@runway.command('classify', inputs={'image':runway.file(description='File path')}, outputs={'text':runway.text(description='Text')})
def classify(model, inputs):
    res = model.ocr(inputs['image'])
    print(res)
    return {'text':res}

if __name__ == '__main__':
    runway.run(host='0.0.0.0', port=9000)