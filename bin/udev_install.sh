#!/usr/bin/env bash

cp ./99_usbdevices.rules /etc/udev/rules.d/
udevadm trigger

mv ./99_usbdevices.rules ./.99_usbdevices.rules