import nuke
import msgBox
from PyQt4.QtGui import QApplication, QMessageBox
import appUsageApp

def change():
    nodes = nuke.selectedNodes('Read')
    if not nodes:
        msgBox.showMessage(QApplication.activeWindow(), title='Red To Default',
                           msg='No Read node selected',
                           icon=QMessageBox.Information)
        return
    for node in nodes:
        node.knob('tile_color').setValue(0)
    
    appUsageApp.updateDatabase('RedToDefault')
    
    return True