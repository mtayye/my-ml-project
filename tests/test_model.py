from model import train_model

def test_model_accuracy():
    model, accuracy = train_model()
    assert accuracy > 0.8, f"Accuracy too low: {accuracy}"
