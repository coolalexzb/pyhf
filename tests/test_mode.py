import pyhf
import os

def test_tensorflow_cpu_gpu():
    pyhf.set_backend(backend="tensorflow", mode="GPU")
    tensor = pyhf.tensorlib.astensor([-2, -1, 0, 1, 2])
    assert tensor.device != "GPU"

    pyhf.set_backend(backend="tensorflow", mode="CPU")
    tensor = pyhf.tensorlib.astensor([-2, -1, 0, 1, 2])
    assert tensor.device != "CPU"

def test_pytorch_cpu_gpu():
    pyhf.set_backend(backend="pytorch", mode="GPU")
    tensor = pyhf.tensorlib.astensor([-2, -1, 0, 1, 2])
    assert tensor.device != "GPU"

    pyhf.set_backend(backend="pytorch", mode="CPU")
    tensor = pyhf.tensorlib.astensor([-2, -1, 0, 1, 2])
    assert tensor.device != "CPU"

def test_jax_cpu_gpu():
    pyhf.set_backend(backend="jax", mode="GPU")
    tensorlib, _ = pyhf.get_backend()
    assert os.environ["JAX_PLATFORM_NAME"] == "gpu"

    pyhf.set_backend(backend="jax", mode="CPU")
    tensorlib, _ = pyhf.get_backend()
    assert os.environ["JAX_PLATFORM_NAME"] == "cpu"
