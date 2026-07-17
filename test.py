from axion.devices import AndroidDevice

device = AndroidDevice()

print(device.is_connected())

print(device.screen_size().stdout)

print(device.battery().stdout)