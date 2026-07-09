class DenseLayer:
    def __init__(self, input_dim, output_dim, activation_fn=None):
        self.input_dim = input_dim
        self.output_dim = output_dim
        self.activation_fn = activation_fn
        self.weights = None
        self.bias = None
        self.input_cache = None

    def initialize_parameters(self):
        pass

    def forward(self, input_data):
        pass

    def backward(self, output_gradient, learning_rate):
        pass
