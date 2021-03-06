from keras.models import Model
from keras.utils.all_utils import plot_model
from .utils import checkdir

class Base(Model):
    def build_graph(self, inputs):
        return Model(inputs=inputs, outputs=self.call(inputs))

    def summary(self, inputs, line_length=None, positions=None, print_fn=None, expand_nested=False):
        return self.build_graph(inputs).summary(expand_nested=expand_nested)

    def plot_model(self, inputs, expand_nested=True):
        checkdir()
        plot_model(self.build_graph(inputs), expand_nested=expand_nested, to_file="image/model.png")