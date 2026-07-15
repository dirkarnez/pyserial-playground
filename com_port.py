import re
import wmi


def get_com_port(instance_id):
    # Connect to the local Windows Management Instrumentation service
    c = wmi.WMI()

    # Query for the specific Plug and Play device using its Device ID
    devices = c.Win32_PnPEntity(DeviceID=instance_id)

    if not devices:
        return "Device Instance ID not found."

    # Retrieve the FriendlyName (e.g., "USB Serial Device (COM3)")
    friendly_name = devices[0].Caption

    if friendly_name:
        match = re.search(r"COM\d+", friendly_name)
        if match:
            return match.group(0)

    return "COM port not found in device properties."


# Your specific Device Instance ID
instance_id = r"USB\VID_303A&PID_1001&MI_00\6&21011EDD&0&0000"
print(f"Detected Port: {get_com_port(instance_id)}")
