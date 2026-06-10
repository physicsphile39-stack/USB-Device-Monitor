import pyudev
from datetime import datetime

log_file = "device_log.txt"

context = pyudev.Context()
monitor = pyudev.Monitor.from_netlink(context)
monitor.filter_by(subsystem="usb")

print("USB Monitor Started")
print("Waiting for USB devices...")

for device in iter(monitor.poll, None):

    # Sirf add aur remove events dikhayega
    if device.action not in ["add", "remove"]:
        continue

    time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    vendor = device.get("ID_VENDOR", "Unknown")
    model = device.get("ID_MODEL", "Unknown")
    vendor_id = device.get("ID_VENDOR_ID", "Unknown")
    product_id = device.get("ID_MODEL_ID", "Unknown")

    output = f"""
==============================
Time: {time_now}
Action: {device.action}
Vendor: {vendor}
Model: {model}
Vendor ID: {vendor_id}
Product ID: {product_id}
==============================
"""

    print(output)

    with open(log_file, "a") as file:
        file.write(output + "\n")











































import pyudev
from datetime import datetime

context = pyudev.Context()
monitor = pyudev.Monitor.from_netlink(context)
monitor.filter_by(subsystem="usb")

print("USB Monitor Started")

for device in iter(monitor.poll, None):





    print("\n====================")

    print("Time:",
          datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    print("Action:",
          device.action)

    print("Vendor:",
          device.get("ID_VENDOR", "Unknown"))

    print("Model:",
          device.get("ID_MODEL", "Unknown"))

    print("Vendor ID:",
          device.get("ID_VENDOR_ID", "Unknown"))

    print("Product ID:",
          device.get("ID_MODEL_ID", "Unknown"))

    print("====================")

