# template-ansible-raspberry-pi
Is a template for setting up raspberry pi's quickly with the features you need/want enabled and for deploying src code to a pi. Please modify to your liking.
**Overclocking is setup here, but is disabled by default. Overclocking may void the warranty of the PI**

## Features:
1. An Ansible playbook to provision a Pi (should be done after you enable ssh and change default password).
1. An Ansible playbook to deploy src, or any other files you may need.
1. **An overclock profile.**
1. A sexier terminal theme.
1. A template for deploying a service to raspberry pi.
1. A default setup for provision and deploy src code.

## Notes;
If you run this out of the box it will: install a few packages, make a src directory, enable GPIO pins, and enable the camera.
