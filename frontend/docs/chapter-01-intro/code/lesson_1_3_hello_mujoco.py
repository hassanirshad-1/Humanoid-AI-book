import mujoco
import mujoco.viewer
import time
import os


def main():
    # Get the directory of the currently executing script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(script_dir, "unitree_g1.xml")

    # Load the model from an XML file
    try:
        model = mujoco.MjModel.from_xml_path(model_path)
    except Exception as e:
        print(f"Error loading model: {e}")
        print(
            f"Please make sure 'unitree_g1.xml' is in the same directory as the script: {script_dir}"
        )
        return

    data = mujoco.MjData(model)

    # Create a viewer
    print("Launching MuJoCo viewer...")
    with mujoco.viewer.launch_passive(model, data) as viewer:
        # Set the camera position
        viewer.cam.azimuth = 90
        viewer.cam.elevation = -15
        viewer.cam.distance = 3.0
        viewer.cam.lookat[:] = [0.0, 0.0, 0.75]

        print("Simulation started. Close the window or press Ctrl+C to exit.")

        try:
            while viewer.is_running():
                step_start = time.time()
                mujoco.mj_step(model, data)
                viewer.sync()
                time_until_next_step = model.opt.timestep - (time.time() - step_start)
                if time_until_next_step > 0:
                    time.sleep(time_until_next_step)
        except KeyboardInterrupt:
            print("Simulation ended by user.")
        except Exception as e:
            print(f"An error occurred during simulation: {e}")

    print("Viewer closed.")


if __name__ == "__main__":
    main()
