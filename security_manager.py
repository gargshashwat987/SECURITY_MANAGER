import subprocess
import asyncio
from winrt.windows.devices import radios
from distutils.core import setup
import py2exe
import winreg


#interacting with windows registery editor

def read_registry_key(key_path, value_name):
    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path) as key:
            value, value_type = winreg.QueryValueEx(key, value_name)
            return value
    except Exception as e:
        return str(e)

def write_registry_key(key_path, value_name, value):
    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path, 0, winreg.KEY_SET_VALUE) as key:
            winreg.SetValueEx(key, value_name, 0, winreg.REG_SZ, value)
            return True
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    key_path = r"SOFTWARE\MyApp"
    value_name = "Setting"

    # Write a value to the registry
    write_success = write_registry_key(key_path, value_name, "NewValue")
    if write_success:
        print("Value written to the registry.")

    # Read a value from the registry
    read_value = read_registry_key(key_path, value_name)
    if read_value:
        print(f"Value read from the registry: {read_value}")
    else:
        print("Failed to read value from the registry.")




#USB port blocking function
def disable_usb(){
    # Fetches the list of all usb devices:
    result = subprocess.run(['devcon', 'hwids', '=usb'], 
    capture_output=True, text=True)

# ... add code to parse the result and get the hwid of the device you want ...

    subprocess.run(['devcon', 'disable', parsed_hwid]) # to disable
    subprocess.run(['devcon', 'enable', parsed_hwid]) # to enable


}


#function for controlling bluetooth 
def disable_bluetooth(){
    async def bluetooth_power(turn_on):
    all_radios = await radios.Radio.get_radios_async()
    for this_radio in all_radios:
        if this_radio.kind == radios.RadioKind.BLUETOOTH:
            if turn_on:
                result = await this_radio.set_state_async(radios.RadioState.ON)
            else:
                result = await this_radio.set_state_async(radios.RadioState.OFF)


    if __name__ == '__main__':
        asyncio.run(bluetooth_power(False))

}



#disabling command prompt

def disable_cmd(){
    setup(window=['Main.py'])  
}

#blocking website access

def disable_website_access(){
    website_to_block = "example.com"

# Open the hosts file in append mode and add an entry to block the website
    with open(r"C:\Windows\System32\drivers\etc\hosts", "a") as hosts_file:
        hosts_file.write(f"127.0.0.1 {website_to_block}\n")

    print(f"{website_to_block} is now blocked.")

}



#THE END

print("THANKYOU FOR PERFORMING TASKS!")
