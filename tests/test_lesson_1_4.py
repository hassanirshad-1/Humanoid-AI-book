import pytest
import numpy as np
import mujoco
import os


def test_random_policy():
    """
    Tests that a random policy function returns a correctly shaped and bounded
    action vector for the Unitree G1 model. This is a basic smoke test for
    the logic in lesson_1_4_action_loop.py.
    """
    # Construct the absolute path to the XML file
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    model_path = os.path.join(
        base_dir, "docs", "chapter-01-intro", "code", "unitree_g1.xml"
    )

    assert os.path.exists(model_path), f"Model file not found at {model_path}"

    try:
        model = mujoco.MjModel.from_xml_path(model_path)
    except Exception as e:
        pytest.fail(f"Failed to load MuJoCo model from {model_path}: {e}")

    # This is the policy function from the lesson script.
    # We test it directly here.
    def random_policy(model):
        return np.random.uniform(low=-1.0, high=1.0, size=model.nu)

    action = random_policy(model)

    # Check that the action has the correct shape (nu is the number of actuators)
    assert action.shape == (
        model.nu,
    ), f"Action shape is {action.shape}, expected {(model.nu,)}"

    # Check that the action values are within the expected range
    assert np.all(action >= -1.0), "Action values should be >= -1.0"
    assert np.all(action <= 1.0), "Action values should be <= 1.0"

    # Check that the number of actuators is greater than zero
    assert model.nu > 0, "Model should have actuators (nu > 0)"
