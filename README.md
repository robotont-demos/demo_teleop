# demo_teleop

![ROS 2](https://img.shields.io/badge/ROS2%20-Jazzy-blue.svg) ![License](https://img.shields.io/badge/License-Apache_2.0-green.svg)

## **Overview**
Teleoperation demo for Robotont (ROS 2).
## **Table of Contents**
- [Installation](#installation)
- [Dependencies](#dependencies)
- [Building the Package](#building-the-package)
- [Launch Files](#launch-files)
- [License](#license)

---

## **Installation**

### **1. Clone the Repository**
```bash
cd ~/<YOUR_WORKSPACE_NAME_HERE>/src
git clone https://github.com/robotont-demos/demo_teleop.git
```

## **Dependencies**
### **1. List of dependencies**
1.1. joy
### **2. Install dependencies**
```bash
cd ~/<YOUR_WORKSPACE_NAME_HERE>
rosdep install --from-paths src --ignore-src -r -y
```

## **Building the package**
```bash
cd ~/<YOUR_WORKSPACE_NAME_HERE>
colcon build --packages-select demo_teleop
```

## **Launch files**
### **1. Source workspace**
```bash
source ~/<YOUR_WORKSPACE_NAME_HERE>/install/setup.bash
```
## 2. Available Launch Files

### 2.1. `gamepad_navigation.launch.py`
Launches joystick teleoperation (e.g., for controlling the robot with a gamepad).

### Supported Parameters

| Name           | Description                                                      | Options/Default                                                                                                       |
|----------------|------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| `use_sim_time` | Use simulation time (Gazebo/Sim)                                 | `true` (default), `false`                                                                                            |
| `params_file`  | Path to parameter YAML file for navigation nodes                 | `nav2_params.yaml` (default)                                                                                         |
| `gamepad_conf` | Gamepad configuration YAML (for teleop)                          | `dualsense.yaml` (default)                                                                                           |

---

**Example: Launch with Dualsense (default) gamepad configuration**
```bash
ros2 launch demo_teleop gamepad_navigation.launch.py
```

**Example: Launch with custom gamepad configuration**
```bash
ros2 launch demo_teleop gamepad_navigation.launch.py gamepad_conf:=path_to_your_conf_file.yaml
```
## **License**
This project is licensed under the Apache 2.0 license - see the [LICENSE](LICENSE) file for more information.
