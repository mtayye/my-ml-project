import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from model import train_model

def test_model_accuracy():
    model, accuracy = train_model()
    assert accuracy > 0.8, f"Accuracy too low: {accuracy}"
