import pytest
import mujoco
import os


def test_load_g1_model():
    """
    Tests that the Unitree G1 model XML file can be loaded by MuJoCo.
    """
    # Construct the absolute path to the XML file relative to this test file.
    # The test file is in /tests, the model is in /docs/chapter-01-intro/code/
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    model_path = os.path.join(
        base_dir, "docs", "chapter-01-intro", "code", "unitree_g1.xml"
    )

    assert os.path.exists(model_path), f"Model file not found at {model_path}"

    try:
        model = mujoco.MjModel.from_xml_path(model_path)
        assert model is not None
        # Check for a few basic properties
        assert model.nbody > 1  # Should have more than just the world body
        assert model.njnt > 0  # Should have joints
    except Exception as e:
        pytest.fail(f"Failed to load MuJoCo model from {model_path}: {e}")
