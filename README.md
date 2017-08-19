# atcommands.py
Apply AT commands on Android smartphones using Python (tested only on LG devices using Windows).

## How to use   
First, import **atcommands.py** library
```python
import atcommands
```

Then, use it to apply at commands.

### Examples
Get device's IMEI:
```python
print atcommands.getCurrentValue("IMEI")
```

Set a valid MAC Address:
```python
print atcommands.setNewValue("MAC", getValidMacAddress())
```
