# demo_teleop
ROS package for teleoperating robotont from a keyboard or a gamepad.

## Teleoperating robotont from a keyboard

```bash
roslaunch demo_teleop teleop_keyboard.launch
```
   

## Teleoperating robotont from a gamepad.

```bash
roslaunch demo_teleop teleop_keyboard.launch
```

See the `ipega.congig.yaml` file in the `config` directory to edit the speed limits as well as mapping of the controller's axes/buttons.

### Parameters

`~joy_dev` (string, default: /dev/input/js0) - Path to the joystick device.

`~joy_config` (string, default: ipega) - Name of the joystick configuration file.

`~config_filepath` (string, default: config/ipega.config.yaml) Path to the joystick configuration file.

For example to use the xbox controller and the second joystick device:

```bash
roslaunch demo_teleop teleop_gamepad.launch joy_dev:=/dev/input/js1 joy_config:=xbox
```

## For more information
See robotont tutorials at [robotont.github.io](https://robotont.github.io/html/files/teleop_robot.html)