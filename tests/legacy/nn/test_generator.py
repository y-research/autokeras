import numpy as np
import torch

from autokeras.legacy.backend.torch.model import TorchModel
from autokeras.legacy.nn.generator import CnnGenerator, MlpGenerator


def test_default_cnn_generator():
    generator = CnnGenerator(3, (28, 28, 1))
    graph = generator.generate()
    model = graph.produce_model()
    inputs = torch.Tensor(np.ones((100, 1, 28, 28)))
    model(inputs).size()
    assert isinstance(model, TorchModel)


def test_default_mlp_generator():
    generator = MlpGenerator(5, (4,))

    graph = generator.generate(3, 5)
    model = graph.produce_model()
    assert isinstance(model, TorchModel)