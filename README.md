# demo_teleop
ROS package for teleoperating robotont from a keyboard or a gamepad.

## Installation
You need to use screen in order to run teleop_twist_keyboard by launch file in non-interactive environment. 
```bash
sudo apt-get install screen
```

## Teleoperating robotont from a keyboard

```bash
ros2 launch demo_teleop teleop_keyboard.launch
screen -r teleop_twist_keyboard
```
   

## Teleoperating robotont from a gamepad.

```bash
ros2 launch demo_teleop teleop_joy.launch
screen -r teleop_twist_joy
```

The screen sesssion and node will be both killed if you do CTRL+C in screen session. See the `ipega.congig.yaml` file in the `config` directory to edit the speed limits as well as mapping of the controller's axes/buttons.

### Parameters

`~joy_dev` (string, default: /dev/input/js0) - Path to the joystick device.

`~joy_config` (string, default: ipega) - Name of the joystick configuration file.

`~config_filepath` (string, default: config/ipega.config.yaml) Path to the joystick configuration file.

For example to use the xbox controller and the second joystick device:

```bash
roslaunch demo_teleop teleop_gamepad.launch joy_dev:=/dev/input/js1 joy_config:=xbox
```

## For more information
See robotont tutorials at [robotont.github.io](https://robotont.github.io/humble/teleop.html)
