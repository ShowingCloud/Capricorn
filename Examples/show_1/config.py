

from PySide import QtCore, QtGui

#import configdialog_rc

class MainClass(QtGui.QMainWindow):
    
    def __init__(self):
        super(MainClass, self).__init__()
        self.resize(637, 618)
        
        self.menuBar = QtGui.QMenuBar(self)
        
        self.menu_File = QtGui.QMenu(self.menuBar)
        self.menu_File.setTitle('menu file')
        self.menuBar.addMenu(self.menu_File)
        
        self.action_Open = QtGui.QAction(self)
        self.action_Open.setText('abc')
        self.menu_File.addAction(self.action_Open)
        self.action_Open.triggered.connect(self.openPage)
        
    def openPage(self):
        dialog = ConfigDialog(self)
        dialog.exec_()
        
class ConfigurationPage(QtGui.QWidget):
    def __init__(self, parent=None):
        super(ConfigurationPage, self).__init__(parent)

        configGroup = QtGui.QGroupBox("Server configuration")

        serverLabel = QtGui.QLabel("Server:")
        serverCombo = QtGui.QComboBox()
        serverCombo.addItem("Trolltech (Australia)")
        serverCombo.addItem("Trolltech (Germany)")
        serverCombo.addItem("Trolltech (Norway)")
        serverCombo.addItem("Trolltech (People's Republic of China)")
        serverCombo.addItem("Trolltech (USA)")

        serverLayout = QtGui.QHBoxLayout()
        serverLayout.addWidget(serverLabel)
        serverLayout.addWidget(serverCombo)

        configLayout = QtGui.QVBoxLayout()
        configLayout.addLayout(serverLayout)
        configGroup.setLayout(configLayout)

        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(configGroup)
        mainLayout.addStretch(1)

        self.setLayout(mainLayout)
        
        self.setWindowTitle('config')


class UpdatePage(QtGui.QWidget):
    def __init__(self, parent=None):
        super(UpdatePage, self).__init__(parent)

        updateGroup = QtGui.QGroupBox("Package selection")
        systemCheckBox = QtGui.QCheckBox("Update system")
        appsCheckBox = QtGui.QCheckBox("Update applications")
        docsCheckBox = QtGui.QCheckBox("Update documentation")

        packageGroup = QtGui.QGroupBox("Existing packages")

        packageList = QtGui.QListWidget()
        qtItem = QtGui.QListWidgetItem(packageList)
        qtItem.setText("Qt")
        qsaItem = QtGui.QListWidgetItem(packageList)
        qsaItem.setText("QSA")
        teamBuilderItem = QtGui.QListWidgetItem(packageList)
        teamBuilderItem.setText("Teambuilder")

        startUpdateButton = QtGui.QPushButton("Start update")

        updateLayout = QtGui.QVBoxLayout()
        updateLayout.addWidget(systemCheckBox)
        updateLayout.addWidget(appsCheckBox)
        updateLayout.addWidget(docsCheckBox)
        updateGroup.setLayout(updateLayout)

        packageLayout = QtGui.QVBoxLayout()
        packageLayout.addWidget(packageList)
        packageGroup.setLayout(packageLayout)

        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(updateGroup)
        mainLayout.addWidget(packageGroup)
        mainLayout.addSpacing(12)
        mainLayout.addWidget(startUpdateButton)
        mainLayout.addStretch(1)

        self.setLayout(mainLayout)


class QueryPage(QtGui.QWidget):
    def __init__(self, parent=None):
        super(QueryPage, self).__init__(parent)

        packagesGroup = QtGui.QGroupBox("Look for packages")

        nameLabel = QtGui.QLabel("Name:")
        nameEdit = QtGui.QLineEdit()

        dateLabel = QtGui.QLabel("Released after:")
        dateEdit = QtGui.QDateTimeEdit(QtCore.QDate.currentDate())

        releasesCheckBox = QtGui.QCheckBox("Releases")
        upgradesCheckBox = QtGui.QCheckBox("Upgrades")

        hitsSpinBox = QtGui.QSpinBox()
        hitsSpinBox.setPrefix("Return up to ")
        hitsSpinBox.setSuffix(" results")
        hitsSpinBox.setSpecialValueText("Return only the first result")
        hitsSpinBox.setMinimum(1)
        hitsSpinBox.setMaximum(100)
        hitsSpinBox.setSingleStep(10)

        startQueryButton = QtGui.QPushButton("Start query")

        packagesLayout = QtGui.QGridLayout()
        packagesLayout.addWidget(nameLabel, 0, 0)
        packagesLayout.addWidget(nameEdit, 0, 1)
        packagesLayout.addWidget(dateLabel, 1, 0)
        packagesLayout.addWidget(dateEdit, 1, 1)
        packagesLayout.addWidget(releasesCheckBox, 2, 0)
        packagesLayout.addWidget(upgradesCheckBox, 3, 0)
        packagesLayout.addWidget(hitsSpinBox, 4, 0, 1, 2)
        packagesGroup.setLayout(packagesLayout)

        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(packagesGroup)
        mainLayout.addSpacing(12)
        mainLayout.addWidget(startQueryButton)
        mainLayout.addStretch(1)

        self.setLayout(mainLayout)


class ConfigDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        super(ConfigDialog, self).__init__(parent)

        self.contentsWidget = QtGui.QListWidget()
        self.contentsWidget.setViewMode(QtGui.QListView.IconMode)
        self.contentsWidget.setIconSize(QtCore.QSize(96, 84))
        self.contentsWidget.setMovement(QtGui.QListView.Static)
        self.contentsWidget.setMaximumWidth(128)
        self.contentsWidget.setSpacing(12)

        self.pagesWidget = QtGui.QStackedWidget()
        self.pagesWidget.addWidget(ConfigurationPage())
        self.pagesWidget.addWidget(UpdatePage())
        self.pagesWidget.addWidget(QueryPage())

        closeButton = QtGui.QPushButton("Close")

        self.createIcons()
        self.contentsWidget.setCurrentRow(0)

        closeButton.clicked.connect(self.close)

        horizontalLayout = QtGui.QHBoxLayout()
        horizontalLayout.addWidget(self.contentsWidget)
        horizontalLayout.addWidget(self.pagesWidget, 1)

        buttonsLayout = QtGui.QHBoxLayout()
        buttonsLayout.addStretch(1)
        buttonsLayout.addWidget(closeButton)

        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addLayout(horizontalLayout)
        mainLayout.addStretch(1)
        mainLayout.addSpacing(12)
        mainLayout.addLayout(buttonsLayout)

        self.setLayout(mainLayout)

        self.setWindowTitle("Config Dialog")

    def changePage(self, current, previous):
        if not current:
            current = previous

        self.pagesWidget.setCurrentIndex(self.contentsWidget.row(current))

    def createIcons(self):
        configButton = QtGui.QListWidgetItem(self.contentsWidget)
        configButton.setIcon(QtGui.QIcon('images/config.png'))
        configButton.setText("Configuration")
        configButton.setTextAlignment(QtCore.Qt.AlignHCenter)
        configButton.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

        updateButton = QtGui.QListWidgetItem(self.contentsWidget)
        updateButton.setIcon(QtGui.QIcon('images/update.png'))
        updateButton.setText("Update")
        updateButton.setTextAlignment(QtCore.Qt.AlignHCenter)
        updateButton.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

        queryButton = QtGui.QListWidgetItem(self.contentsWidget)
        queryButton.setIcon(QtGui.QIcon('images/query.png'))
        queryButton.setText("Query")
        queryButton.setTextAlignment(QtCore.Qt.AlignHCenter)
        queryButton.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

        self.contentsWidget.currentItemChanged.connect(self.changePage)


if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)
    
    window = MainClass()
    window.show()
    
    sys.exit(app.exec_())
