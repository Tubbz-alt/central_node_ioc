from os import path
from pydm import Display

class DeviceInputListItem(Display):
  def __init__(self, device_name=None, parent=None):
    super(DeviceInputListItem, self).__init__(parent=parent)
    if device_name:
      self.ui.currentStateLabel.channel = "ca://{devname}_MPSC".format(devname=device_name)
      self.ui.latchedStateLabel.channel = "ca://{devname}_MPS".format(devname=device_name)
      self.ui.unlatchButton.channel = "ca://{devname}_UNLH".format(devname=device_name)
      self.ui.bypassValueLabel.channel = "ca://{devname}_BYPV".format(devname=device_name)
      self.ui.bypassStatusLabel.channel = "ca://{devname}_BYPS".format(devname=device_name)
  
  def ui_filename(self):
    return 'device-input-list-item.ui'
    
  def ui_filepath(self):
    return path.join(path.dirname(path.realpath(__file__)), self.ui_filename())

intelclass = DeviceInputListItem
