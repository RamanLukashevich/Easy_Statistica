# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QDoubleSpinBox, QFormLayout, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLayout,
    QMainWindow, QPushButton, QRadioButton, QScrollArea,
    QSizePolicy, QSpacerItem, QSpinBox, QStackedWidget,
    QTableView, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

from mplwidget import MplWidget
import recources

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1344, 811)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setStyleSheet(u"*{\n"
"	border: none;\n"
"	background-color: transparent;\n"
"	background: none;\n"
"	padding: 0;\n"
"	margin: 0;\n"
"}\n"
"\n"
"\n"
"#MainWindow, #centralwidget, #LeftMenuContainer, #LeftMenuContainer_2, #LeftSubMenuContainer, #frame_4{\n"
"	background-color:#B8B8B8\n"
"}\n"
"\n"
"QPushButton{\n"
"	text-align: left;\n"
"	padding: 5px 10px;\n"
"}\n"
"\n"
"#CentralMenuSubContainer{\n"
"	background-color: #F0F0F0 \n"
"}\n"
"\n"
"#HeaderContainer, #horizontalLayout_8{\n"
"	background-color: #F5F5F5 \n"
"}\n"
"\n"
"#frame_4{\n"
"	border-radius: 10px;  \n"
"}\n"
"\n"
"#frame_10{\n"
"	background-color:#F8F8F8;\n"
"	border-radius: 10px;  \n"
"}\n"
"\n"
"#HeaderContainer{\n"
"	border-radius: 10px;  \n"
"\n"
"}\n"
"\n"
"#BaseCalculateBtn, #BaseCancelBtn, #StatisticalCalculateBtn, #StatisticalCancelBtn, #CorrCalculateBtn, #CorrCancelBtn, #SampleCalculateBtn, #SampleCancelBtn, #CoeffCalculateBtn, #CoeffCancelBtn, #NCountCoeffBox, #PLevelSpinBox, #SampleSpinBox_1, #SampleSpinBox_2, #SampleSpinBox_3, #SampleSpinBox_4, #Sam"
                        "pleSpinBox_5, #SampleSpinBox_6, #PLevelSpinBox_2, #SampleResult_1, #SampleResult_2, #ChiResultLebel, #TResultLebel, #NCountCoeffBox_2, #PLevelSpinBox_3, #PLevelSpinBox_4, #ZResultLebel, #PoissonSpinBox, #PResultLebel, #NCountCoeffBox_3 {\n"
"	background-color: #F0F0F0;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"#StatSpinBox, #StatSpinBox_2, #StatSpinBox_3, #StatSpinBox_4, #StatSpinBox_5, #CorrSpinBox, #CorrSpinBox_2, #CorrSpinBox_3, #RegrSpinBox, #RegrSpinBox_2, #RegrSpinBox_3, #RegrSpinBox_4, #RegrSpinBox_5, #RegrSpinBox_6, #BaseSpinBox, #BaseSpinBox_2, #ExMeanSpinBox {\n"
"	background-color: #F0F0F0;\n"
"	border-radius: 3px;\n"
"}\n"
"\n"
"\n"
"#RightMenuSubContainer{\n"
"	background-color: #D3D3D3;\n"
"	border-radius: 10px;  \n"
"}\n"
"\n"
"\n"
"#MainContentContainer, #TableResultView, #graphicsView, #dfTableView{\n"
"	background-color: #F0F0F0;\n"
"}\n"
"\n"
"#RightContentMenuContainer{\n"
"background-color: #E0E0E0;\n"
"border-radius: 10px;  \n"
"}\n"
"\n"
"\n"
"#CreateTableBtn, #OpenTableBtn, #LetsGoBtn, #"
                        "NumberColumnSb, #NumberRowsSb, #OpenCsvBtn, #SavePdfBtn, #SaveExcelBtn, #SaveCsvBtn, #ExportPdfBtn, #PreviewBtn, #PrintBtn, #SaveDfPushButton, #SaveDfPushButton_2, #SaveJpgPushButton, #PNumSpinBox, #PNumSpinBox_2, #FAQButton, #FAQButton_2, #FAQButton_3, #FAQButton_4, #FAQButton_5, #FAQButton_6\n"
"{\n"
"background-color: #E0E0E0;\n"
"border-radius: 10px;  \n"
"\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(0, 0))
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.LeftSubMenuContainer = QWidget(self.centralwidget)
        self.LeftSubMenuContainer.setObjectName(u"LeftSubMenuContainer")
        self.LeftSubMenuContainer.setMinimumSize(QSize(0, 0))
        self.LeftSubMenuContainer.setMaximumSize(QSize(50, 16777215))
        self.horizontalLayout_3 = QHBoxLayout(self.LeftSubMenuContainer)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.LeftMenuContainer_2 = QWidget(self.LeftSubMenuContainer)
        self.LeftMenuContainer_2.setObjectName(u"LeftMenuContainer_2")
        self.LeftMenuContainer_2.setEnabled(True)
        self.LeftMenuContainer_2.setMinimumSize(QSize(0, 0))
        self.LeftMenuContainer_2.setMaximumSize(QSize(55, 16777215))
        self.LeftMenuContainer_2.setBaseSize(QSize(0, 0))
        self.verticalLayout_26 = QVBoxLayout(self.LeftMenuContainer_2)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.LeftMenuContainer_2)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setEnabled(True)
        self.widget_3.setMinimumSize(QSize(55, 600))
        self.widget_3.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_27 = QVBoxLayout(self.widget_3)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.widget_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_7)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(5, -1, -1, -1)
        self.MenuBtn_2 = QPushButton(self.frame_7)
        self.MenuBtn_2.setObjectName(u"MenuBtn_2")
        font = QFont()
        font.setPointSize(10)
        self.MenuBtn_2.setFont(font)
        icon = QIcon()
        icon.addFile(u"H:/Easy Statistica/icons/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.MenuBtn_2.setIcon(icon)
        self.MenuBtn_2.setIconSize(QSize(24, 24))
        self.MenuBtn_2.setCheckable(True)
        self.MenuBtn_2.setChecked(False)
        self.MenuBtn_2.setAutoRepeat(False)

        self.verticalLayout_28.addWidget(self.MenuBtn_2)


        self.verticalLayout_27.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.widget_3)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy)
        self.frame_8.setMinimumSize(QSize(0, 0))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_8)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(6, -1, -1, -1)
        self.DataBtn_2 = QPushButton(self.frame_8)
        self.DataBtn_2.setObjectName(u"DataBtn_2")
        font1 = QFont()
        font1.setPointSize(12)
        self.DataBtn_2.setFont(font1)
        icon1 = QIcon()
        icon1.addFile(u"H:/Easy Statistica/icons/table.png", QSize(), QIcon.Normal, QIcon.Off)
        self.DataBtn_2.setIcon(icon1)
        self.DataBtn_2.setIconSize(QSize(24, 24))
        self.DataBtn_2.setCheckable(True)

        self.verticalLayout_29.addWidget(self.DataBtn_2)

        self.DataAnalysisBtn_2 = QPushButton(self.frame_8)
        self.DataAnalysisBtn_2.setObjectName(u"DataAnalysisBtn_2")
        self.DataAnalysisBtn_2.setFont(font1)
        icon2 = QIcon()
        icon2.addFile(u"H:/Easy Statistica/icons/pie-chart.png", QSize(), QIcon.Normal, QIcon.Off)
        self.DataAnalysisBtn_2.setIcon(icon2)
        self.DataAnalysisBtn_2.setIconSize(QSize(24, 24))
        self.DataAnalysisBtn_2.setCheckable(True)

        self.verticalLayout_29.addWidget(self.DataAnalysisBtn_2)

        self.ReportsBtn_2 = QPushButton(self.frame_8)
        self.ReportsBtn_2.setObjectName(u"ReportsBtn_2")
        self.ReportsBtn_2.setFont(font1)
        icon3 = QIcon()
        icon3.addFile(u"H:/Easy Statistica/icons/save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ReportsBtn_2.setIcon(icon3)
        self.ReportsBtn_2.setIconSize(QSize(24, 24))

        self.verticalLayout_29.addWidget(self.ReportsBtn_2)


        self.verticalLayout_27.addWidget(self.frame_8)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_27.addItem(self.verticalSpacer_6)

        self.frame_13 = QFrame(self.widget_3)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_13)
        self.verticalLayout_30.setSpacing(4)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(5, 6, 4, 6)
        self.SettingsBtn_2 = QPushButton(self.frame_13)
        self.SettingsBtn_2.setObjectName(u"SettingsBtn_2")
        self.SettingsBtn_2.setFont(font1)
        icon4 = QIcon()
        icon4.addFile(u"H:/Easy Statistica/icons/settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.SettingsBtn_2.setIcon(icon4)
        self.SettingsBtn_2.setIconSize(QSize(24, 24))
        self.SettingsBtn_2.setCheckable(True)

        self.verticalLayout_30.addWidget(self.SettingsBtn_2)

        self.HelpBtn_2 = QPushButton(self.frame_13)
        self.HelpBtn_2.setObjectName(u"HelpBtn_2")
        self.HelpBtn_2.setFont(font1)
        icon5 = QIcon()
        icon5.addFile(u"H:/Easy Statistica/icons/help-circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.HelpBtn_2.setIcon(icon5)
        self.HelpBtn_2.setIconSize(QSize(24, 24))
        self.HelpBtn_2.setCheckable(True)

        self.verticalLayout_30.addWidget(self.HelpBtn_2)

        self.InfoBtn_2 = QPushButton(self.frame_13)
        self.InfoBtn_2.setObjectName(u"InfoBtn_2")
        self.InfoBtn_2.setFont(font1)
        icon6 = QIcon()
        icon6.addFile(u"H:/Easy Statistica/icons/github.png", QSize(), QIcon.Normal, QIcon.Off)
        self.InfoBtn_2.setIcon(icon6)
        self.InfoBtn_2.setIconSize(QSize(24, 24))
        self.InfoBtn_2.setCheckable(True)

        self.verticalLayout_30.addWidget(self.InfoBtn_2)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_30.addItem(self.verticalSpacer_7)


        self.verticalLayout_27.addWidget(self.frame_13, 0, Qt.AlignBottom)


        self.verticalLayout_26.addWidget(self.widget_3)


        self.horizontalLayout_3.addWidget(self.LeftMenuContainer_2)


        self.horizontalLayout.addWidget(self.LeftSubMenuContainer)

        self.LeftMenuContainer = QWidget(self.centralwidget)
        self.LeftMenuContainer.setObjectName(u"LeftMenuContainer")
        self.LeftMenuContainer.setEnabled(True)
        self.LeftMenuContainer.setMinimumSize(QSize(0, 0))
        self.LeftMenuContainer.setMaximumSize(QSize(16777215, 16777215))
        self.LeftMenuContainer.setBaseSize(QSize(0, 0))
        self.verticalLayout = QVBoxLayout(self.LeftMenuContainer)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.LeftMenuSubContainer = QWidget(self.LeftMenuContainer)
        self.LeftMenuSubContainer.setObjectName(u"LeftMenuSubContainer")
        self.LeftMenuSubContainer.setEnabled(True)
        self.LeftMenuSubContainer.setMinimumSize(QSize(0, 0))
        self.LeftMenuSubContainer.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.LeftMenuSubContainer)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.LeftMenuSubContainer)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, -1, -1, -1)
        self.MenuBtn = QPushButton(self.frame)
        self.MenuBtn.setObjectName(u"MenuBtn")
        self.MenuBtn.setFont(font)
        icon7 = QIcon()
        icon7.addFile(u"H:/Easy Statistica/icons/chevron-left.png", QSize(), QIcon.Normal, QIcon.Off)
        self.MenuBtn.setIcon(icon7)
        self.MenuBtn.setIconSize(QSize(24, 24))
        self.MenuBtn.setCheckable(True)
        self.MenuBtn.setAutoRepeat(False)

        self.verticalLayout_3.addWidget(self.MenuBtn, 0, Qt.AlignLeft)


        self.verticalLayout_2.addWidget(self.frame, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.frame_2 = QFrame(self.LeftMenuSubContainer)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(6, -1, -1, -1)
        self.DataBtn = QPushButton(self.frame_2)
        self.DataBtn.setObjectName(u"DataBtn")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.DataBtn.setFont(font2)
        self.DataBtn.setIcon(icon1)
        self.DataBtn.setIconSize(QSize(24, 24))
        self.DataBtn.setCheckable(True)

        self.verticalLayout_4.addWidget(self.DataBtn)

        self.DataAnalysisBtn = QPushButton(self.frame_2)
        self.DataAnalysisBtn.setObjectName(u"DataAnalysisBtn")
        self.DataAnalysisBtn.setFont(font2)
        self.DataAnalysisBtn.setIcon(icon2)
        self.DataAnalysisBtn.setIconSize(QSize(24, 24))
        self.DataAnalysisBtn.setCheckable(True)

        self.verticalLayout_4.addWidget(self.DataAnalysisBtn)

        self.ReportsBtn = QPushButton(self.frame_2)
        self.ReportsBtn.setObjectName(u"ReportsBtn")
        self.ReportsBtn.setFont(font2)
        self.ReportsBtn.setAutoFillBackground(False)
        self.ReportsBtn.setIcon(icon3)
        self.ReportsBtn.setIconSize(QSize(24, 24))
        self.ReportsBtn.setCheckable(True)

        self.verticalLayout_4.addWidget(self.ReportsBtn)


        self.verticalLayout_2.addWidget(self.frame_2, 0, Qt.AlignTop)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.frame_3 = QFrame(self.LeftMenuSubContainer)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setSpacing(4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(5, 6, 4, 6)
        self.SettingsBtn = QPushButton(self.frame_3)
        self.SettingsBtn.setObjectName(u"SettingsBtn")
        self.SettingsBtn.setFont(font2)
        self.SettingsBtn.setIcon(icon4)
        self.SettingsBtn.setIconSize(QSize(24, 24))
        self.SettingsBtn.setCheckable(True)

        self.verticalLayout_5.addWidget(self.SettingsBtn)

        self.HelpBtn = QPushButton(self.frame_3)
        self.HelpBtn.setObjectName(u"HelpBtn")
        self.HelpBtn.setFont(font2)
        self.HelpBtn.setIcon(icon5)
        self.HelpBtn.setIconSize(QSize(24, 24))
        self.HelpBtn.setCheckable(True)

        self.verticalLayout_5.addWidget(self.HelpBtn)

        self.InfoBtn = QPushButton(self.frame_3)
        self.InfoBtn.setObjectName(u"InfoBtn")
        self.InfoBtn.setFont(font2)
        self.InfoBtn.setIcon(icon6)
        self.InfoBtn.setIconSize(QSize(24, 24))
        self.InfoBtn.setCheckable(True)

        self.verticalLayout_5.addWidget(self.InfoBtn)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_5)


        self.verticalLayout_2.addWidget(self.frame_3, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.LeftMenuSubContainer)


        self.horizontalLayout.addWidget(self.LeftMenuContainer)

        self.CentralMenuContainer = QWidget(self.centralwidget)
        self.CentralMenuContainer.setObjectName(u"CentralMenuContainer")
        sizePolicy.setHeightForWidth(self.CentralMenuContainer.sizePolicy().hasHeightForWidth())
        self.CentralMenuContainer.setSizePolicy(sizePolicy)
        self.CentralMenuContainer.setMinimumSize(QSize(0, 0))
        self.CentralMenuContainer.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_6 = QVBoxLayout(self.CentralMenuContainer)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.CentralMenuSubContainer = QWidget(self.CentralMenuContainer)
        self.CentralMenuSubContainer.setObjectName(u"CentralMenuSubContainer")
        sizePolicy.setHeightForWidth(self.CentralMenuSubContainer.sizePolicy().hasHeightForWidth())
        self.CentralMenuSubContainer.setSizePolicy(sizePolicy)
        self.CentralMenuSubContainer.setMinimumSize(QSize(0, 0))
        self.CentralMenuSubContainer.setStyleSheet(u"")
        self.verticalLayout_7 = QVBoxLayout(self.CentralMenuSubContainer)
        self.verticalLayout_7.setSpacing(2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(2, 3, 2, 0)
        self.frame_4 = QFrame(self.CentralMenuSubContainer)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 9, -1, 9)
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(20, 28))
        self.label.setMaximumSize(QSize(16777215, 10))
        self.label.setFont(font2)
        self.label.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_2.addWidget(self.label, 0, Qt.AlignRight|Qt.AlignTop)

        self.CloseCentralMenuBtn = QPushButton(self.frame_4)
        self.CloseCentralMenuBtn.setObjectName(u"CloseCentralMenuBtn")
        self.CloseCentralMenuBtn.setLayoutDirection(Qt.RightToLeft)
        icon8 = QIcon()
        icon8.addFile(u"H:/Easy Statistica/icons/x-circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.CloseCentralMenuBtn.setIcon(icon8)
        self.CloseCentralMenuBtn.setIconSize(QSize(18, 18))

        self.horizontalLayout_2.addWidget(self.CloseCentralMenuBtn, 0, Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.frame_4, 0, Qt.AlignTop)

        self.stackedWidget = QStackedWidget(self.CentralMenuSubContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(3)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy1)
        self.stackedWidget.setMinimumSize(QSize(0, 0))
        self.stackedWidget.setMaximumSize(QSize(320, 16777215))
        self.stackedWidget.setSizeIncrement(QSize(0, 0))
        self.DataPg = QWidget()
        self.DataPg.setObjectName(u"DataPg")
        self.DataPg.setMinimumSize(QSize(0, 0))
        self.DataPg.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_13 = QVBoxLayout(self.DataPg)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(5, 5, 5, 5)
        self.frame_15 = QFrame(self.DataPg)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_15)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(5, 5, 5, 5)
        self.frame_17 = QFrame(self.frame_15)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMinimumSize(QSize(0, 0))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_17)
        self.verticalLayout_32.setSpacing(5)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.frame_17)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(0, 0))
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setItalic(False)
        font3.setUnderline(False)
        self.label_9.setFont(font3)

        self.verticalLayout_32.addWidget(self.label_9)

        self.verticalSpacer_12 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_32.addItem(self.verticalSpacer_12)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_8 = QLabel(self.frame_17)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(0, 0))
        self.label_8.setFont(font)

        self.horizontalLayout_9.addWidget(self.label_8)

        self.NumberColumnSb = QSpinBox(self.frame_17)
        self.NumberColumnSb.setObjectName(u"NumberColumnSb")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.NumberColumnSb.sizePolicy().hasHeightForWidth())
        self.NumberColumnSb.setSizePolicy(sizePolicy2)
        self.NumberColumnSb.setMinimumSize(QSize(80, 40))
        self.NumberColumnSb.setMaximumSize(QSize(60, 16777215))
        font4 = QFont()
        font4.setPointSize(10)
        font4.setBold(False)
        self.NumberColumnSb.setFont(font4)
        self.NumberColumnSb.setMouseTracking(False)
        self.NumberColumnSb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.NumberColumnSb.setMinimum(2)
        self.NumberColumnSb.setMaximum(10)
        self.NumberColumnSb.setValue(2)

        self.horizontalLayout_9.addWidget(self.NumberColumnSb)


        self.verticalLayout_32.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_11 = QLabel(self.frame_17)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(0, 0))
        self.label_11.setFont(font)

        self.horizontalLayout_10.addWidget(self.label_11)

        self.NumberRowsSb = QSpinBox(self.frame_17)
        self.NumberRowsSb.setObjectName(u"NumberRowsSb")
        sizePolicy2.setHeightForWidth(self.NumberRowsSb.sizePolicy().hasHeightForWidth())
        self.NumberRowsSb.setSizePolicy(sizePolicy2)
        self.NumberRowsSb.setMinimumSize(QSize(80, 40))
        self.NumberRowsSb.setMaximumSize(QSize(60, 16777215))
        self.NumberRowsSb.setFont(font4)
        self.NumberRowsSb.setMouseTracking(False)
        self.NumberRowsSb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.NumberRowsSb.setMinimum(2)
        self.NumberRowsSb.setMaximum(999)
        self.NumberRowsSb.setValue(2)

        self.horizontalLayout_10.addWidget(self.NumberRowsSb)


        self.verticalLayout_32.addLayout(self.horizontalLayout_10)

        self.verticalSpacer_13 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_32.addItem(self.verticalSpacer_13)

        self.CreateTableBtn = QPushButton(self.frame_17)
        self.CreateTableBtn.setObjectName(u"CreateTableBtn")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.CreateTableBtn.sizePolicy().hasHeightForWidth())
        self.CreateTableBtn.setSizePolicy(sizePolicy3)
        self.CreateTableBtn.setMinimumSize(QSize(0, 30))
        self.CreateTableBtn.setMaximumSize(QSize(16777215, 16777215))
        self.CreateTableBtn.setFont(font4)
        icon9 = QIcon()
        icon9.addFile(u"H:/Easy Statistica/icons/zap.png", QSize(), QIcon.Normal, QIcon.Off)
        self.CreateTableBtn.setIcon(icon9)
        self.CreateTableBtn.setIconSize(QSize(16, 16))

        self.verticalLayout_32.addWidget(self.CreateTableBtn)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_32.addItem(self.verticalSpacer_10)

        self.OpenTableBtn = QPushButton(self.frame_17)
        self.OpenTableBtn.setObjectName(u"OpenTableBtn")
        sizePolicy3.setHeightForWidth(self.OpenTableBtn.sizePolicy().hasHeightForWidth())
        self.OpenTableBtn.setSizePolicy(sizePolicy3)
        self.OpenTableBtn.setMinimumSize(QSize(0, 30))
        self.OpenTableBtn.setFont(font4)
        icon10 = QIcon()
        icon10.addFile(u"H:/Easy Statistica/icons/file.png", QSize(), QIcon.Normal, QIcon.Off)
        self.OpenTableBtn.setIcon(icon10)
        self.OpenTableBtn.setIconSize(QSize(16, 16))

        self.verticalLayout_32.addWidget(self.OpenTableBtn)

        self.verticalSpacer_11 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_32.addItem(self.verticalSpacer_11)

        self.OpenCsvBtn = QPushButton(self.frame_17)
        self.OpenCsvBtn.setObjectName(u"OpenCsvBtn")
        self.OpenCsvBtn.setFont(font4)
        self.OpenCsvBtn.setIcon(icon10)
        self.OpenCsvBtn.setIconSize(QSize(16, 16))

        self.verticalLayout_32.addWidget(self.OpenCsvBtn)

        self.verticalSpacer_35 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_32.addItem(self.verticalSpacer_35)

        self.label_10 = QLabel(self.frame_17)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(0, 20))
        font5 = QFont()
        font5.setPointSize(9)
        font5.setBold(True)
        self.label_10.setFont(font5)

        self.verticalLayout_32.addWidget(self.label_10)

        self.verticalSpacer_14 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_32.addItem(self.verticalSpacer_14)

        self.tableWidget_2 = QTableWidget(self.frame_17)
        if (self.tableWidget_2.columnCount() < 2):
            self.tableWidget_2.setColumnCount(2)
        if (self.tableWidget_2.rowCount() < 2):
            self.tableWidget_2.setRowCount(2)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(2)
        sizePolicy4.setHeightForWidth(self.tableWidget_2.sizePolicy().hasHeightForWidth())
        self.tableWidget_2.setSizePolicy(sizePolicy4)
        self.tableWidget_2.setMinimumSize(QSize(300, 0))
        self.tableWidget_2.setDragEnabled(True)
        self.tableWidget_2.setDragDropMode(QAbstractItemView.DragDrop)
        self.tableWidget_2.setDefaultDropAction(Qt.CopyAction)
        self.tableWidget_2.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.tableWidget_2.setRowCount(2)
        self.tableWidget_2.setColumnCount(2)

        self.verticalLayout_32.addWidget(self.tableWidget_2)

        self.verticalSpacer_8 = QSpacerItem(20, 6, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_32.addItem(self.verticalSpacer_8)

        self.LetsGoBtn = QPushButton(self.frame_17)
        self.LetsGoBtn.setObjectName(u"LetsGoBtn")
        sizePolicy3.setHeightForWidth(self.LetsGoBtn.sizePolicy().hasHeightForWidth())
        self.LetsGoBtn.setSizePolicy(sizePolicy3)
        font6 = QFont()
        font6.setPointSize(10)
        font6.setBold(True)
        font6.setUnderline(False)
        font6.setStrikeOut(False)
        font6.setKerning(True)
        self.LetsGoBtn.setFont(font6)
        self.LetsGoBtn.setIcon(icon9)
        self.LetsGoBtn.setIconSize(QSize(16, 16))

        self.verticalLayout_32.addWidget(self.LetsGoBtn)


        self.verticalLayout_31.addWidget(self.frame_17, 0, Qt.AlignLeft)


        self.verticalLayout_13.addWidget(self.frame_15)

        self.stackedWidget.addWidget(self.DataPg)
        self.ReportsPg = QWidget()
        self.ReportsPg.setObjectName(u"ReportsPg")
        self.ReportsPg.setMinimumSize(QSize(0, 0))
        self.verticalLayout_44 = QVBoxLayout(self.ReportsPg)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalSpacer_64 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_64)

        self.label_7 = QLabel(self.ReportsPg)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font2)

        self.verticalLayout_14.addWidget(self.label_7)

        self.verticalSpacer_44 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_44)

        self.SaveExcelBtn = QPushButton(self.ReportsPg)
        self.SaveExcelBtn.setObjectName(u"SaveExcelBtn")
        self.SaveExcelBtn.setMinimumSize(QSize(0, 30))
        self.SaveExcelBtn.setFont(font4)
        icon11 = QIcon()
        icon11.addFile(u"H:/Easy Statistica/icons/folder.png", QSize(), QIcon.Normal, QIcon.Off)
        self.SaveExcelBtn.setIcon(icon11)
        self.SaveExcelBtn.setIconSize(QSize(16, 16))

        self.verticalLayout_14.addWidget(self.SaveExcelBtn)

        self.SaveCsvBtn = QPushButton(self.ReportsPg)
        self.SaveCsvBtn.setObjectName(u"SaveCsvBtn")
        self.SaveCsvBtn.setMinimumSize(QSize(0, 30))
        self.SaveCsvBtn.setFont(font4)
        self.SaveCsvBtn.setIcon(icon11)
        self.SaveCsvBtn.setIconSize(QSize(16, 16))

        self.verticalLayout_14.addWidget(self.SaveCsvBtn)

        self.verticalSpacer_43 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_43)


        self.verticalLayout_44.addLayout(self.verticalLayout_14)

        self.verticalLayout_43 = QVBoxLayout()
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.label_31 = QLabel(self.ReportsPg)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font2)

        self.verticalLayout_43.addWidget(self.label_31)

        self.verticalSpacer_54 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_43.addItem(self.verticalSpacer_54)

        self.SaveDfPushButton = QPushButton(self.ReportsPg)
        self.SaveDfPushButton.setObjectName(u"SaveDfPushButton")
        self.SaveDfPushButton.setFont(font)
        self.SaveDfPushButton.setIcon(icon11)
        self.SaveDfPushButton.setIconSize(QSize(16, 16))

        self.verticalLayout_43.addWidget(self.SaveDfPushButton)

        self.SaveDfPushButton_2 = QPushButton(self.ReportsPg)
        self.SaveDfPushButton_2.setObjectName(u"SaveDfPushButton_2")
        self.SaveDfPushButton_2.setFont(font)
        self.SaveDfPushButton_2.setIcon(icon11)
        self.SaveDfPushButton_2.setIconSize(QSize(16, 16))

        self.verticalLayout_43.addWidget(self.SaveDfPushButton_2)

        self.ExportPdfBtn = QPushButton(self.ReportsPg)
        self.ExportPdfBtn.setObjectName(u"ExportPdfBtn")
        self.ExportPdfBtn.setFont(font4)
        self.ExportPdfBtn.setIcon(icon11)
        self.ExportPdfBtn.setIconSize(QSize(16, 16))

        self.verticalLayout_43.addWidget(self.ExportPdfBtn)

        self.SaveJpgPushButton = QPushButton(self.ReportsPg)
        self.SaveJpgPushButton.setObjectName(u"SaveJpgPushButton")
        self.SaveJpgPushButton.setFont(font)
        self.SaveJpgPushButton.setIcon(icon11)
        self.SaveJpgPushButton.setIconSize(QSize(16, 16))

        self.verticalLayout_43.addWidget(self.SaveJpgPushButton)

        self.verticalSpacer_57 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_43.addItem(self.verticalSpacer_57)


        self.verticalLayout_44.addLayout(self.verticalLayout_43)

        self.stackedWidget.addWidget(self.ReportsPg)
        self.SettingPg = QWidget()
        self.SettingPg.setObjectName(u"SettingPg")
        self.SettingPg.setMinimumSize(QSize(0, 0))
        self.verticalLayout_37 = QVBoxLayout(self.SettingPg)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalSpacer_67 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_37.addItem(self.verticalSpacer_67)

        self.label_2 = QLabel(self.SettingPg)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font2)
        self.label_2.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_37.addWidget(self.label_2)

        self.verticalSpacer_66 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_37.addItem(self.verticalSpacer_66)

        self.label_58 = QLabel(self.SettingPg)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setFont(font2)

        self.verticalLayout_37.addWidget(self.label_58)

        self.verticalSpacer_68 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_37.addItem(self.verticalSpacer_68)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(15, -1, -1, -1)
        self.SetDataRadioButton = QRadioButton(self.SettingPg)
        self.SetDataRadioButton.setObjectName(u"SetDataRadioButton")
        self.SetDataRadioButton.setFont(font)

        self.verticalLayout_8.addWidget(self.SetDataRadioButton)

        self.SetDataRadioButton_2 = QRadioButton(self.SettingPg)
        self.SetDataRadioButton_2.setObjectName(u"SetDataRadioButton_2")
        font7 = QFont()
        font7.setPointSize(10)
        font7.setItalic(False)
        self.SetDataRadioButton_2.setFont(font7)

        self.verticalLayout_8.addWidget(self.SetDataRadioButton_2)

        self.SetDataRadioButton_3 = QRadioButton(self.SettingPg)
        self.SetDataRadioButton_3.setObjectName(u"SetDataRadioButton_3")
        self.SetDataRadioButton_3.setFont(font)

        self.verticalLayout_8.addWidget(self.SetDataRadioButton_3)

        self.SetDataRadioButton_4 = QRadioButton(self.SettingPg)
        self.SetDataRadioButton_4.setObjectName(u"SetDataRadioButton_4")
        self.SetDataRadioButton_4.setFont(font)

        self.verticalLayout_8.addWidget(self.SetDataRadioButton_4)


        self.verticalLayout_37.addLayout(self.verticalLayout_8)

        self.verticalSpacer_40 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_37.addItem(self.verticalSpacer_40)

        self.label_6 = QLabel(self.SettingPg)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)

        self.verticalLayout_37.addWidget(self.label_6)

        self.verticalSpacer_69 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_37.addItem(self.verticalSpacer_69)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_38 = QLabel(self.SettingPg)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setFont(font)

        self.horizontalLayout_18.addWidget(self.label_38)

        self.PNumSpinBox = QSpinBox(self.SettingPg)
        self.PNumSpinBox.setObjectName(u"PNumSpinBox")
        self.PNumSpinBox.setMinimumSize(QSize(50, 30))
        self.PNumSpinBox.setMaximumSize(QSize(70, 16777215))
        self.PNumSpinBox.setFont(font)
        self.PNumSpinBox.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.PNumSpinBox.setKeyboardTracking(False)
        self.PNumSpinBox.setMinimum(2)
        self.PNumSpinBox.setMaximum(5)
        self.PNumSpinBox.setValue(3)

        self.horizontalLayout_18.addWidget(self.PNumSpinBox)


        self.verticalLayout_37.addLayout(self.horizontalLayout_18)

        self.verticalSpacer_15 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_37.addItem(self.verticalSpacer_15)

        self.label_48 = QLabel(self.SettingPg)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setFont(font2)

        self.verticalLayout_37.addWidget(self.label_48)

        self.verticalSpacer_71 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_37.addItem(self.verticalSpacer_71)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_49 = QLabel(self.SettingPg)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setFont(font)

        self.horizontalLayout_19.addWidget(self.label_49)

        self.PNumSpinBox_2 = QSpinBox(self.SettingPg)
        self.PNumSpinBox_2.setObjectName(u"PNumSpinBox_2")
        self.PNumSpinBox_2.setMinimumSize(QSize(50, 30))
        self.PNumSpinBox_2.setMaximumSize(QSize(70, 16777215))
        self.PNumSpinBox_2.setFont(font)
        self.PNumSpinBox_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.PNumSpinBox_2.setKeyboardTracking(False)
        self.PNumSpinBox_2.setMinimum(0)
        self.PNumSpinBox_2.setMaximum(6)
        self.PNumSpinBox_2.setValue(3)

        self.horizontalLayout_19.addWidget(self.PNumSpinBox_2)


        self.verticalLayout_37.addLayout(self.horizontalLayout_19)

        self.verticalSpacer_70 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_37.addItem(self.verticalSpacer_70)

        self.stackedWidget.addWidget(self.SettingPg)
        self.HelpPg = QWidget()
        self.HelpPg.setObjectName(u"HelpPg")
        self.HelpPg.setMinimumSize(QSize(0, 0))
        self.verticalLayout_10 = QVBoxLayout(self.HelpPg)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_21 = QFrame(self.HelpPg)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_46 = QVBoxLayout(self.frame_21)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalSpacer_74 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_46.addItem(self.verticalSpacer_74)

        self.label_4 = QLabel(self.frame_21)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)

        self.verticalLayout_46.addWidget(self.label_4)

        self.verticalSpacer_73 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_46.addItem(self.verticalSpacer_73)

        self.FAQButton = QPushButton(self.frame_21)
        self.FAQButton.setObjectName(u"FAQButton")
        self.FAQButton.setFont(font)
        icon12 = QIcon()
        icon12.addFile(u"H:/Easy Statistica/icons/book-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.FAQButton.setIcon(icon12)
        self.FAQButton.setIconSize(QSize(16, 16))

        self.verticalLayout_46.addWidget(self.FAQButton)

        self.FAQButton_2 = QPushButton(self.frame_21)
        self.FAQButton_2.setObjectName(u"FAQButton_2")
        self.FAQButton_2.setFont(font)
        self.FAQButton_2.setIcon(icon12)
        self.FAQButton_2.setIconSize(QSize(16, 16))

        self.verticalLayout_46.addWidget(self.FAQButton_2)

        self.FAQButton_3 = QPushButton(self.frame_21)
        self.FAQButton_3.setObjectName(u"FAQButton_3")
        self.FAQButton_3.setFont(font)
        self.FAQButton_3.setIcon(icon12)
        self.FAQButton_3.setIconSize(QSize(16, 16))

        self.verticalLayout_46.addWidget(self.FAQButton_3)

        self.FAQButton_4 = QPushButton(self.frame_21)
        self.FAQButton_4.setObjectName(u"FAQButton_4")
        self.FAQButton_4.setFont(font)
        self.FAQButton_4.setIcon(icon12)
        self.FAQButton_4.setIconSize(QSize(16, 16))

        self.verticalLayout_46.addWidget(self.FAQButton_4)

        self.FAQButton_5 = QPushButton(self.frame_21)
        self.FAQButton_5.setObjectName(u"FAQButton_5")
        self.FAQButton_5.setFont(font)
        self.FAQButton_5.setIcon(icon12)
        self.FAQButton_5.setIconSize(QSize(16, 16))

        self.verticalLayout_46.addWidget(self.FAQButton_5)

        self.FAQButton_6 = QPushButton(self.frame_21)
        self.FAQButton_6.setObjectName(u"FAQButton_6")
        self.FAQButton_6.setFont(font)
        self.FAQButton_6.setIcon(icon12)
        self.FAQButton_6.setIconSize(QSize(16, 16))

        self.verticalLayout_46.addWidget(self.FAQButton_6)

        self.verticalSpacer_72 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_46.addItem(self.verticalSpacer_72)


        self.verticalLayout_10.addWidget(self.frame_21)

        self.stackedWidget.addWidget(self.HelpPg)
        self.InfoPg = QWidget()
        self.InfoPg.setObjectName(u"InfoPg")
        self.InfoPg.setMinimumSize(QSize(0, 0))
        self.verticalLayout_9 = QVBoxLayout(self.InfoPg)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.infoLabel = QLabel(self.InfoPg)
        self.infoLabel.setObjectName(u"infoLabel")
        self.infoLabel.setFont(font)
        self.infoLabel.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_9.addWidget(self.infoLabel)

        self.stackedWidget.addWidget(self.InfoPg)

        self.verticalLayout_7.addWidget(self.stackedWidget)


        self.verticalLayout_6.addWidget(self.CentralMenuSubContainer, 0, Qt.AlignLeft)


        self.horizontalLayout.addWidget(self.CentralMenuContainer)

        self.MainBodyContainer = QWidget(self.centralwidget)
        self.MainBodyContainer.setObjectName(u"MainBodyContainer")
        sizePolicy.setHeightForWidth(self.MainBodyContainer.sizePolicy().hasHeightForWidth())
        self.MainBodyContainer.setSizePolicy(sizePolicy)
        self.MainBodyContainer.setStyleSheet(u"")
        self.verticalLayout_11 = QVBoxLayout(self.MainBodyContainer)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.HeaderContainer = QWidget(self.MainBodyContainer)
        self.HeaderContainer.setObjectName(u"HeaderContainer")
        sizePolicy5 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.HeaderContainer.sizePolicy().hasHeightForWidth())
        self.HeaderContainer.setSizePolicy(sizePolicy5)
        self.HeaderContainer.setLayoutDirection(Qt.LeftToRight)
        self.horizontalLayout_4 = QHBoxLayout(self.HeaderContainer)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(20, 10, 10, 10)
        self.frame_5 = QFrame(self.HeaderContainer)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 0))
        self.frame_5.setMaximumSize(QSize(16777215, 16777215))
        self.frame_5.setLayoutDirection(Qt.RightToLeft)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_5)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(10, 0, 10, 0)
        self.label_19 = QLabel(self.frame_5)
        self.label_19.setObjectName(u"label_19")
        font8 = QFont()
        font8.setPointSize(14)
        font8.setBold(True)
        font8.setItalic(False)
        font8.setUnderline(False)
        font8.setStrikeOut(False)
        font8.setKerning(True)
        self.label_19.setFont(font8)
        self.label_19.setLayoutDirection(Qt.RightToLeft)

        self.verticalLayout_24.addWidget(self.label_19)


        self.horizontalLayout_4.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.HeaderContainer)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_16 = QFrame(self.frame_6)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 2, 0, 2)
        self.MinimizeBtn = QPushButton(self.frame_16)
        self.MinimizeBtn.setObjectName(u"MinimizeBtn")
        icon13 = QIcon()
        icon13.addFile(u"H:/Easy Statistica/icons/minus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.MinimizeBtn.setIcon(icon13)

        self.horizontalLayout_11.addWidget(self.MinimizeBtn)

        self.NormalBtn = QPushButton(self.frame_16)
        self.NormalBtn.setObjectName(u"NormalBtn")
        icon14 = QIcon()
        icon14.addFile(u"H:/Easy Statistica/icons/copy.png", QSize(), QIcon.Normal, QIcon.Off)
        self.NormalBtn.setIcon(icon14)

        self.horizontalLayout_11.addWidget(self.NormalBtn)

        self.RestoreBtn = QPushButton(self.frame_16)
        self.RestoreBtn.setObjectName(u"RestoreBtn")
        icon15 = QIcon()
        icon15.addFile(u"H:/Easy Statistica/icons/square.png", QSize(), QIcon.Normal, QIcon.Off)
        self.RestoreBtn.setIcon(icon15)

        self.horizontalLayout_11.addWidget(self.RestoreBtn)

        self.CloseBtn = QPushButton(self.frame_16)
        self.CloseBtn.setObjectName(u"CloseBtn")
        sizePolicy2.setHeightForWidth(self.CloseBtn.sizePolicy().hasHeightForWidth())
        self.CloseBtn.setSizePolicy(sizePolicy2)
        icon16 = QIcon()
        icon16.addFile(u"H:/Easy Statistica/icons/x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.CloseBtn.setIcon(icon16)

        self.horizontalLayout_11.addWidget(self.CloseBtn)


        self.horizontalLayout_12.addWidget(self.frame_16)


        self.horizontalLayout_4.addWidget(self.frame_6, 0, Qt.AlignRight)


        self.verticalLayout_11.addWidget(self.HeaderContainer)

        self.MainBodyContent = QWidget(self.MainBodyContainer)
        self.MainBodyContent.setObjectName(u"MainBodyContent")
        sizePolicy.setHeightForWidth(self.MainBodyContent.sizePolicy().hasHeightForWidth())
        self.MainBodyContent.setSizePolicy(sizePolicy)
        self.horizontalLayout_5 = QHBoxLayout(self.MainBodyContent)
        self.horizontalLayout_5.setSpacing(3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 5, 0, 0)
        self.MainContentContainer = QWidget(self.MainBodyContent)
        self.MainContentContainer.setObjectName(u"MainContentContainer")
        self.verticalLayout_22 = QVBoxLayout(self.MainContentContainer)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.MainContentSubContainer = QStackedWidget(self.MainContentContainer)
        self.MainContentSubContainer.setObjectName(u"MainContentSubContainer")
        self.MainContentSubContainer.setMaximumSize(QSize(16777215, 16777215))
        self.HelloPg = QWidget()
        self.HelloPg.setObjectName(u"HelloPg")
        self.verticalLayout_25 = QVBoxLayout(self.HelloPg)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(5, 5, 5, 5)
        self.HelloViewPg = QFrame(self.HelloPg)
        self.HelloViewPg.setObjectName(u"HelloViewPg")
        self.HelloViewPg.setFrameShape(QFrame.NoFrame)
        self.HelloViewPg.setFrameShadow(QFrame.Plain)
        self.verticalLayout_49 = QVBoxLayout(self.HelloViewPg)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.verticalLayout_49.setContentsMargins(5, 5, 5, 5)
        self.scrollArea_2 = QScrollArea(self.HelloViewPg)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.scrollArea_2.sizePolicy().hasHeightForWidth())
        self.scrollArea_2.setSizePolicy(sizePolicy6)
        self.scrollArea_2.setMinimumSize(QSize(0, 0))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 87, 71))
        self.scrollAreaWidgetContents_3.setMinimumSize(QSize(0, 0))
        self.verticalLayout_48 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.verticalLayout_48.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_14 = QGridLayout()
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.firstWelcomeLabel = QLabel(self.scrollAreaWidgetContents_3)
        self.firstWelcomeLabel.setObjectName(u"firstWelcomeLabel")
        sizePolicy7 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.firstWelcomeLabel.sizePolicy().hasHeightForWidth())
        self.firstWelcomeLabel.setSizePolicy(sizePolicy7)
        self.firstWelcomeLabel.setMinimumSize(QSize(0, 0))
        self.firstWelcomeLabel.setFont(font2)
        self.firstWelcomeLabel.setTextFormat(Qt.AutoText)
        self.firstWelcomeLabel.setScaledContents(False)

        self.gridLayout_14.addWidget(self.firstWelcomeLabel, 0, 0, 1, 1)

        self.viewWelcomeLabel_1 = QLabel(self.scrollAreaWidgetContents_3)
        self.viewWelcomeLabel_1.setObjectName(u"viewWelcomeLabel_1")
        sizePolicy.setHeightForWidth(self.viewWelcomeLabel_1.sizePolicy().hasHeightForWidth())
        self.viewWelcomeLabel_1.setSizePolicy(sizePolicy)
        self.viewWelcomeLabel_1.setMinimumSize(QSize(0, 0))
        self.viewWelcomeLabel_1.setFont(font4)
        self.viewWelcomeLabel_1.setTextFormat(Qt.AutoText)
        self.viewWelcomeLabel_1.setScaledContents(False)

        self.gridLayout_14.addWidget(self.viewWelcomeLabel_1, 1, 0, 1, 1)

        self.viewWelcomeLabel_2 = QLabel(self.scrollAreaWidgetContents_3)
        self.viewWelcomeLabel_2.setObjectName(u"viewWelcomeLabel_2")
        sizePolicy.setHeightForWidth(self.viewWelcomeLabel_2.sizePolicy().hasHeightForWidth())
        self.viewWelcomeLabel_2.setSizePolicy(sizePolicy)
        self.viewWelcomeLabel_2.setMinimumSize(QSize(0, 0))
        self.viewWelcomeLabel_2.setFont(font)
        self.viewWelcomeLabel_2.setScaledContents(False)

        self.gridLayout_14.addWidget(self.viewWelcomeLabel_2, 2, 0, 1, 1)

        self.viewWelcomeLabel_3 = QLabel(self.scrollAreaWidgetContents_3)
        self.viewWelcomeLabel_3.setObjectName(u"viewWelcomeLabel_3")
        sizePolicy.setHeightForWidth(self.viewWelcomeLabel_3.sizePolicy().hasHeightForWidth())
        self.viewWelcomeLabel_3.setSizePolicy(sizePolicy)
        self.viewWelcomeLabel_3.setMinimumSize(QSize(0, 0))
        font9 = QFont()
        font9.setPointSize(9)
        self.viewWelcomeLabel_3.setFont(font9)
        self.viewWelcomeLabel_3.setScaledContents(False)

        self.gridLayout_14.addWidget(self.viewWelcomeLabel_3, 3, 0, 1, 1)


        self.verticalLayout_48.addLayout(self.gridLayout_14)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_49.addWidget(self.scrollArea_2)


        self.verticalLayout_25.addWidget(self.HelloViewPg)

        self.MainContentSubContainer.addWidget(self.HelloPg)
        self.WorkingPg = QWidget()
        self.WorkingPg.setObjectName(u"WorkingPg")
        self.WorkingPg.setMinimumSize(QSize(0, 0))
        self.verticalLayout_23 = QVBoxLayout(self.WorkingPg)
        self.verticalLayout_23.setSpacing(2)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(6, -1, 6, 6)
        self.ResultViewPg = QFrame(self.WorkingPg)
        self.ResultViewPg.setObjectName(u"ResultViewPg")
        sizePolicy.setHeightForWidth(self.ResultViewPg.sizePolicy().hasHeightForWidth())
        self.ResultViewPg.setSizePolicy(sizePolicy)
        self.ResultViewPg.setMinimumSize(QSize(0, 0))
        self.verticalLayout_45 = QVBoxLayout(self.ResultViewPg)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.ResultScrollArea = QScrollArea(self.ResultViewPg)
        self.ResultScrollArea.setObjectName(u"ResultScrollArea")
        self.ResultScrollArea.setMinimumSize(QSize(0, 0))
        self.ResultScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 316, 1667))
        self.scrollAreaWidgetContents.setMinimumSize(QSize(0, 0))
        self.verticalLayout_33 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.label_13 = QLabel(self.scrollAreaWidgetContents)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font2)
        self.label_13.setText(u"Result of data analysis:")

        self.verticalLayout_33.addWidget(self.label_13)

        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.ResultViewLabel = QLabel(self.scrollAreaWidgetContents)
        self.ResultViewLabel.setObjectName(u"ResultViewLabel")
        sizePolicy.setHeightForWidth(self.ResultViewLabel.sizePolicy().hasHeightForWidth())
        self.ResultViewLabel.setSizePolicy(sizePolicy)
        self.ResultViewLabel.setMinimumSize(QSize(0, 0))
        self.ResultViewLabel.setFont(font)
        self.ResultViewLabel.setTextFormat(Qt.AutoText)
        self.ResultViewLabel.setScaledContents(False)
        self.ResultViewLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_11.addWidget(self.ResultViewLabel, 0, 0, 1, 2)

        self.ResultViewLabel_1 = QLabel(self.scrollAreaWidgetContents)
        self.ResultViewLabel_1.setObjectName(u"ResultViewLabel_1")
        sizePolicy7.setHeightForWidth(self.ResultViewLabel_1.sizePolicy().hasHeightForWidth())
        self.ResultViewLabel_1.setSizePolicy(sizePolicy7)
        self.ResultViewLabel_1.setFont(font2)
        self.ResultViewLabel_1.setTextFormat(Qt.AutoText)

        self.gridLayout_11.addWidget(self.ResultViewLabel_1, 1, 0, 1, 1)

        self.ResultViewLabel_8 = QLabel(self.scrollAreaWidgetContents)
        self.ResultViewLabel_8.setObjectName(u"ResultViewLabel_8")
        sizePolicy7.setHeightForWidth(self.ResultViewLabel_8.sizePolicy().hasHeightForWidth())
        self.ResultViewLabel_8.setSizePolicy(sizePolicy7)
        self.ResultViewLabel_8.setFont(font2)

        self.gridLayout_11.addWidget(self.ResultViewLabel_8, 1, 1, 1, 1)

        self.ResultViewLabel_2 = QLabel(self.scrollAreaWidgetContents)
        self.ResultViewLabel_2.setObjectName(u"ResultViewLabel_2")
        sizePolicy7.setHeightForWidth(self.ResultViewLabel_2.sizePolicy().hasHeightForWidth())
        self.ResultViewLabel_2.setSizePolicy(sizePolicy7)
        self.ResultViewLabel_2.setMinimumSize(QSize(0, 0))
        self.ResultViewLabel_2.setFont(font)
        self.ResultViewLabel_2.setTextFormat(Qt.AutoText)
        self.ResultViewLabel_2.setScaledContents(False)
        self.ResultViewLabel_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_11.addWidget(self.ResultViewLabel_2, 2, 0, 1, 1)

        self.dfTableView = QTableView(self.scrollAreaWidgetContents)
        self.dfTableView.setObjectName(u"dfTableView")

        self.gridLayout_11.addWidget(self.dfTableView, 2, 1, 4, 1)

        self.ResultViewLabel_3 = QLabel(self.scrollAreaWidgetContents)
        self.ResultViewLabel_3.setObjectName(u"ResultViewLabel_3")
        sizePolicy7.setHeightForWidth(self.ResultViewLabel_3.sizePolicy().hasHeightForWidth())
        self.ResultViewLabel_3.setSizePolicy(sizePolicy7)
        self.ResultViewLabel_3.setFont(font)

        self.gridLayout_11.addWidget(self.ResultViewLabel_3, 3, 0, 1, 1)

        self.ResultViewLabel_4 = QLabel(self.scrollAreaWidgetContents)
        self.ResultViewLabel_4.setObjectName(u"ResultViewLabel_4")
        sizePolicy7.setHeightForWidth(self.ResultViewLabel_4.sizePolicy().hasHeightForWidth())
        self.ResultViewLabel_4.setSizePolicy(sizePolicy7)
        self.ResultViewLabel_4.setFont(font)

        self.gridLayout_11.addWidget(self.ResultViewLabel_4, 4, 0, 1, 1)

        self.ResultViewLabel_5 = QLabel(self.scrollAreaWidgetContents)
        self.ResultViewLabel_5.setObjectName(u"ResultViewLabel_5")
        sizePolicy7.setHeightForWidth(self.ResultViewLabel_5.sizePolicy().hasHeightForWidth())
        self.ResultViewLabel_5.setSizePolicy(sizePolicy7)
        self.ResultViewLabel_5.setFont(font)

        self.gridLayout_11.addWidget(self.ResultViewLabel_5, 5, 0, 1, 1)

        self.ResultViewLabel_6 = QLabel(self.scrollAreaWidgetContents)
        self.ResultViewLabel_6.setObjectName(u"ResultViewLabel_6")
        sizePolicy7.setHeightForWidth(self.ResultViewLabel_6.sizePolicy().hasHeightForWidth())
        self.ResultViewLabel_6.setSizePolicy(sizePolicy7)
        font10 = QFont()
        font10.setPointSize(10)
        font10.setItalic(True)
        self.ResultViewLabel_6.setFont(font10)

        self.gridLayout_11.addWidget(self.ResultViewLabel_6, 6, 0, 1, 1)

        self.ResultViewLabel_7 = QLabel(self.scrollAreaWidgetContents)
        self.ResultViewLabel_7.setObjectName(u"ResultViewLabel_7")
        sizePolicy7.setHeightForWidth(self.ResultViewLabel_7.sizePolicy().hasHeightForWidth())
        self.ResultViewLabel_7.setSizePolicy(sizePolicy7)
        self.ResultViewLabel_7.setFont(font2)

        self.gridLayout_11.addWidget(self.ResultViewLabel_7, 7, 0, 1, 1)


        self.verticalLayout_33.addLayout(self.gridLayout_11)

        self.MplWidget = MplWidget(self.scrollAreaWidgetContents)
        self.MplWidget.setObjectName(u"MplWidget")
        self.MplWidget.setMinimumSize(QSize(0, 400))

        self.verticalLayout_33.addWidget(self.MplWidget)

        self.MplWidget_2 = MplWidget(self.scrollAreaWidgetContents)
        self.MplWidget_2.setObjectName(u"MplWidget_2")
        self.MplWidget_2.setMinimumSize(QSize(0, 400))

        self.verticalLayout_33.addWidget(self.MplWidget_2)

        self.MplWidget_3 = MplWidget(self.scrollAreaWidgetContents)
        self.MplWidget_3.setObjectName(u"MplWidget_3")
        self.MplWidget_3.setMinimumSize(QSize(0, 700))

        self.verticalLayout_33.addWidget(self.MplWidget_3)

        self.ResultScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_45.addWidget(self.ResultScrollArea)


        self.verticalLayout_23.addWidget(self.ResultViewPg)

        self.MainContentSubContainer.addWidget(self.WorkingPg)

        self.verticalLayout_22.addWidget(self.MainContentSubContainer)


        self.horizontalLayout_5.addWidget(self.MainContentContainer)

        self.RightContentContainer = QWidget(self.MainBodyContent)
        self.RightContentContainer.setObjectName(u"RightContentContainer")
        self.verticalLayout_15 = QVBoxLayout(self.RightContentContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.RightSubMenuSubContainer = QWidget(self.RightContentContainer)
        self.RightSubMenuSubContainer.setObjectName(u"RightSubMenuSubContainer")
        self.horizontalLayout_6 = QHBoxLayout(self.RightSubMenuSubContainer)
        self.horizontalLayout_6.setSpacing(2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.RightContentMenuContainer = QWidget(self.RightSubMenuSubContainer)
        self.RightContentMenuContainer.setObjectName(u"RightContentMenuContainer")
        self.RightContentMenuContainer.setMinimumSize(QSize(0, 0))
        self.RightContentMenuContainer.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_16 = QVBoxLayout(self.RightContentMenuContainer)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(3, 3, 1, 3)
        self.stackedWidget_2 = QStackedWidget(self.RightContentMenuContainer)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        sizePolicy.setHeightForWidth(self.stackedWidget_2.sizePolicy().hasHeightForWidth())
        self.stackedWidget_2.setSizePolicy(sizePolicy)
        self.stackedWidget_2.setMinimumSize(QSize(0, 0))
        self.stackedWidget_2.setMaximumSize(QSize(16777215, 16777215))
        self.stackedWidget_2.setFont(font)
        self.BaseStatisticsPg = QWidget()
        self.BaseStatisticsPg.setObjectName(u"BaseStatisticsPg")
        self.verticalLayout_19 = QVBoxLayout(self.BaseStatisticsPg)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.frame_14 = QFrame(self.BaseStatisticsPg)
        self.frame_14.setObjectName(u"frame_14")
        sizePolicy.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy)
        self.frame_14.setMinimumSize(QSize(0, 0))
        self.frame_14.setMaximumSize(QSize(16777215, 16777215))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_14)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalSpacer_18 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_17.addItem(self.verticalSpacer_18)

        self.label_12 = QLabel(self.frame_14)
        self.label_12.setObjectName(u"label_12")
        font11 = QFont()
        font11.setPointSize(11)
        font11.setBold(True)
        self.label_12.setFont(font11)

        self.verticalLayout_17.addWidget(self.label_12)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.PLevelCoeffLabel_2 = QLabel(self.frame_14)
        self.PLevelCoeffLabel_2.setObjectName(u"PLevelCoeffLabel_2")
        self.PLevelCoeffLabel_2.setMaximumSize(QSize(16777215, 16777215))
        self.PLevelCoeffLabel_2.setFont(font)
        self.PLevelCoeffLabel_2.setLayoutDirection(Qt.RightToLeft)
        self.PLevelCoeffLabel_2.setScaledContents(False)

        self.horizontalLayout_14.addWidget(self.PLevelCoeffLabel_2)

        self.PLevelSpinBox_2 = QDoubleSpinBox(self.frame_14)
        self.PLevelSpinBox_2.setObjectName(u"PLevelSpinBox_2")
        sizePolicy8 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.PLevelSpinBox_2.sizePolicy().hasHeightForWidth())
        self.PLevelSpinBox_2.setSizePolicy(sizePolicy8)
        self.PLevelSpinBox_2.setMinimumSize(QSize(90, 35))
        self.PLevelSpinBox_2.setMaximumSize(QSize(80, 16777215))
        self.PLevelSpinBox_2.setFont(font4)
        self.PLevelSpinBox_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.PLevelSpinBox_2.setDecimals(3)
        self.PLevelSpinBox_2.setMinimum(0.001000000000000)
        self.PLevelSpinBox_2.setMaximum(1.000000000000000)
        self.PLevelSpinBox_2.setSingleStep(0.001000000000000)
        self.PLevelSpinBox_2.setValue(0.950000000000000)

        self.horizontalLayout_14.addWidget(self.PLevelSpinBox_2)


        self.verticalLayout_17.addLayout(self.horizontalLayout_14)

        self.verticalSpacer_29 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_29)

        self.label_23 = QLabel(self.frame_14)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font2)

        self.verticalLayout_17.addWidget(self.label_23)

        self.widget = QWidget(self.frame_14)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_34 = QVBoxLayout(self.widget)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.PearsonCheckBox = QCheckBox(self.widget)
        self.PearsonCheckBox.setObjectName(u"PearsonCheckBox")
        self.PearsonCheckBox.setFont(font)

        self.verticalLayout_34.addWidget(self.PearsonCheckBox)

        self.ShapiroCheckBox = QCheckBox(self.widget)
        self.ShapiroCheckBox.setObjectName(u"ShapiroCheckBox")
        self.ShapiroCheckBox.setFont(font)

        self.verticalLayout_34.addWidget(self.ShapiroCheckBox)

        self.KolmogorovCheckBox = QCheckBox(self.widget)
        self.KolmogorovCheckBox.setObjectName(u"KolmogorovCheckBox")
        self.KolmogorovCheckBox.setFont(font)

        self.verticalLayout_34.addWidget(self.KolmogorovCheckBox)

        self.ZCheckBox = QCheckBox(self.widget)
        self.ZCheckBox.setObjectName(u"ZCheckBox")
        self.ZCheckBox.setFont(font)

        self.verticalLayout_34.addWidget(self.ZCheckBox)

        self.verticalSpacer_28 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_34.addItem(self.verticalSpacer_28)


        self.verticalLayout_17.addWidget(self.widget)

        self.label_15 = QLabel(self.frame_14)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font2)

        self.verticalLayout_17.addWidget(self.label_15)

        self.verticalSpacer_20 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_20)

        self.BaseCheckBox = QCheckBox(self.frame_14)
        self.BaseCheckBox.setObjectName(u"BaseCheckBox")
        self.BaseCheckBox.setFont(font)

        self.verticalLayout_17.addWidget(self.BaseCheckBox)

        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.label_59 = QLabel(self.frame_14)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setMinimumSize(QSize(0, 0))
        self.label_59.setMaximumSize(QSize(16777215, 16777215))
        self.label_59.setFont(font)

        self.gridLayout_10.addWidget(self.label_59, 0, 0, 1, 1)

        self.BaseSpinBox = QComboBox(self.frame_14)
        self.BaseSpinBox.setObjectName(u"BaseSpinBox")
        self.BaseSpinBox.setMinimumSize(QSize(90, 25))
        self.BaseSpinBox.setFont(font)
        self.BaseSpinBox.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout_10.addWidget(self.BaseSpinBox, 0, 1, 1, 1)


        self.verticalLayout_17.addLayout(self.gridLayout_10)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_9)

        self.BaseCheckBox_2 = QCheckBox(self.frame_14)
        self.BaseCheckBox_2.setObjectName(u"BaseCheckBox_2")
        self.BaseCheckBox_2.setFont(font)

        self.verticalLayout_17.addWidget(self.BaseCheckBox_2)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.BaseSpinBox_2 = QComboBox(self.frame_14)
        self.BaseSpinBox_2.setObjectName(u"BaseSpinBox_2")
        self.BaseSpinBox_2.setMinimumSize(QSize(90, 25))
        self.BaseSpinBox_2.setFont(font)
        self.BaseSpinBox_2.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout_6.addWidget(self.BaseSpinBox_2, 0, 1, 1, 1)

        self.label_45 = QLabel(self.frame_14)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setMinimumSize(QSize(0, 0))
        self.label_45.setMaximumSize(QSize(16777215, 16777215))
        self.label_45.setFont(font)

        self.gridLayout_6.addWidget(self.label_45, 0, 0, 1, 1)


        self.verticalLayout_17.addLayout(self.gridLayout_6)

        self.verticalSpacer_16 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_16)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(-1, -1, 0, -1)
        self.BaseCalculateBtn = QPushButton(self.frame_14)
        self.BaseCalculateBtn.setObjectName(u"BaseCalculateBtn")
        sizePolicy2.setHeightForWidth(self.BaseCalculateBtn.sizePolicy().hasHeightForWidth())
        self.BaseCalculateBtn.setSizePolicy(sizePolicy2)
        self.BaseCalculateBtn.setMinimumSize(QSize(0, 0))
        self.BaseCalculateBtn.setMaximumSize(QSize(16777215, 16777215))
        self.BaseCalculateBtn.setFont(font2)
        self.BaseCalculateBtn.setLayoutDirection(Qt.LeftToRight)
        self.BaseCalculateBtn.setIcon(icon9)
        self.BaseCalculateBtn.setCheckable(True)

        self.horizontalLayout_13.addWidget(self.BaseCalculateBtn)

        self.BaseCancelBtn = QPushButton(self.frame_14)
        self.BaseCancelBtn.setObjectName(u"BaseCancelBtn")
        sizePolicy2.setHeightForWidth(self.BaseCancelBtn.sizePolicy().hasHeightForWidth())
        self.BaseCancelBtn.setSizePolicy(sizePolicy2)
        self.BaseCancelBtn.setMinimumSize(QSize(0, 0))
        self.BaseCancelBtn.setMaximumSize(QSize(16777215, 16777215))
        self.BaseCancelBtn.setFont(font2)
        self.BaseCancelBtn.setLayoutDirection(Qt.LeftToRight)
        self.BaseCancelBtn.setIcon(icon8)
        self.BaseCancelBtn.setCheckable(True)
        self.BaseCancelBtn.setAutoDefault(False)

        self.horizontalLayout_13.addWidget(self.BaseCancelBtn)


        self.verticalLayout_17.addLayout(self.horizontalLayout_13)

        self.verticalSpacer_30 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_17.addItem(self.verticalSpacer_30)


        self.verticalLayout_19.addWidget(self.frame_14)

        self.stackedWidget_2.addWidget(self.BaseStatisticsPg)
        self.StatisticalCriteriaPg = QWidget()
        self.StatisticalCriteriaPg.setObjectName(u"StatisticalCriteriaPg")
        self.verticalLayout_20 = QVBoxLayout(self.StatisticalCriteriaPg)
        self.verticalLayout_20.setSpacing(6)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(3, 0, 3, 0)
        self.frame_18 = QFrame(self.StatisticalCriteriaPg)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMinimumSize(QSize(0, 0))
        self.frame_18.setMaximumSize(QSize(16777215, 16777215))
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.frame_18)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalSpacer_25 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_39.addItem(self.verticalSpacer_25)

        self.label_16 = QLabel(self.frame_18)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font11)

        self.verticalLayout_39.addWidget(self.label_16)

        self.verticalSpacer_26 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_39.addItem(self.verticalSpacer_26)

        self.label_21 = QLabel(self.frame_18)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font2)

        self.verticalLayout_39.addWidget(self.label_21)

        self.verticalSpacer_27 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_39.addItem(self.verticalSpacer_27)

        self.ttestCheckBox = QCheckBox(self.frame_18)
        self.ttestCheckBox.setObjectName(u"ttestCheckBox")
        self.ttestCheckBox.setFont(font)

        self.verticalLayout_39.addWidget(self.ttestCheckBox)

        self.verticalLayout_36 = QVBoxLayout()
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(12, -1, -1, -1)
        self.OneTtestRadioButton = QRadioButton(self.frame_18)
        self.OneTtestRadioButton.setObjectName(u"OneTtestRadioButton")
        self.OneTtestRadioButton.setFont(font)

        self.verticalLayout_36.addWidget(self.OneTtestRadioButton)

        self.gridLayout_12 = QGridLayout()
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.label_34 = QLabel(self.frame_18)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMinimumSize(QSize(90, 0))
        self.label_34.setMaximumSize(QSize(100, 16777215))
        self.label_34.setFont(font)
        self.label_34.setLayoutDirection(Qt.LeftToRight)
        self.label_34.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_12.addWidget(self.label_34, 0, 0, 1, 1)

        self.ExMeanSpinBox = QDoubleSpinBox(self.frame_18)
        self.ExMeanSpinBox.setObjectName(u"ExMeanSpinBox")
        self.ExMeanSpinBox.setMinimumSize(QSize(60, 25))
        self.ExMeanSpinBox.setFont(font)
        self.ExMeanSpinBox.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.ExMeanSpinBox.setDecimals(3)
        self.ExMeanSpinBox.setMaximum(9999.989999999999782)
        self.ExMeanSpinBox.setSingleStep(0.001000000000000)
        self.ExMeanSpinBox.setValue(1.000000000000000)

        self.gridLayout_12.addWidget(self.ExMeanSpinBox, 0, 1, 1, 1)


        self.verticalLayout_36.addLayout(self.gridLayout_12)

        self.TwoTRadioButton = QRadioButton(self.frame_18)
        self.TwoTRadioButton.setObjectName(u"TwoTRadioButton")
        self.TwoTRadioButton.setFont(font)

        self.verticalLayout_36.addWidget(self.TwoTRadioButton)

        self.PairTRadioButton = QRadioButton(self.frame_18)
        self.PairTRadioButton.setObjectName(u"PairTRadioButton")
        self.PairTRadioButton.setFont(font)

        self.verticalLayout_36.addWidget(self.PairTRadioButton)

        self.MultiTRadioButton = QRadioButton(self.frame_18)
        self.MultiTRadioButton.setObjectName(u"MultiTRadioButton")
        self.MultiTRadioButton.setFont(font)

        self.verticalLayout_36.addWidget(self.MultiTRadioButton)


        self.verticalLayout_39.addLayout(self.verticalLayout_36)

        self.FisherCheckBox = QCheckBox(self.frame_18)
        self.FisherCheckBox.setObjectName(u"FisherCheckBox")
        self.FisherCheckBox.setFont(font)

        self.verticalLayout_39.addWidget(self.FisherCheckBox)

        self.AnovaCheckBox = QCheckBox(self.frame_18)
        self.AnovaCheckBox.setObjectName(u"AnovaCheckBox")
        self.AnovaCheckBox.setFont(font)

        self.verticalLayout_39.addWidget(self.AnovaCheckBox)

        self.verticalSpacer_24 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_39.addItem(self.verticalSpacer_24)

        self.label_22 = QLabel(self.frame_18)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font2)

        self.verticalLayout_39.addWidget(self.label_22)

        self.verticalSpacer_23 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_39.addItem(self.verticalSpacer_23)

        self.UtestCheckBox = QCheckBox(self.frame_18)
        self.UtestCheckBox.setObjectName(u"UtestCheckBox")
        self.UtestCheckBox.setFont(font)

        self.verticalLayout_39.addWidget(self.UtestCheckBox)

        self.WilcoxCheckBox = QCheckBox(self.frame_18)
        self.WilcoxCheckBox.setObjectName(u"WilcoxCheckBox")
        self.WilcoxCheckBox.setFont(font)

        self.verticalLayout_39.addWidget(self.WilcoxCheckBox)

        self.KolmCheckBox = QCheckBox(self.frame_18)
        self.KolmCheckBox.setObjectName(u"KolmCheckBox")
        self.KolmCheckBox.setFont(font)

        self.verticalLayout_39.addWidget(self.KolmCheckBox)

        self.KruWallCheckBox = QCheckBox(self.frame_18)
        self.KruWallCheckBox.setObjectName(u"KruWallCheckBox")
        self.KruWallCheckBox.setFont(font)

        self.verticalLayout_39.addWidget(self.KruWallCheckBox)

        self.FriCheckBox = QCheckBox(self.frame_18)
        self.FriCheckBox.setObjectName(u"FriCheckBox")
        self.FriCheckBox.setFont(font)

        self.verticalLayout_39.addWidget(self.FriCheckBox)

        self.verticalSpacer_56 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_39.addItem(self.verticalSpacer_56)

        self.label_40 = QLabel(self.frame_18)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setFont(font5)

        self.verticalLayout_39.addWidget(self.label_40)

        self.verticalSpacer_55 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_39.addItem(self.verticalSpacer_55)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(4)
        self.gridLayout_3.setVerticalSpacing(6)
        self.label_41 = QLabel(self.frame_18)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMinimumSize(QSize(0, 0))
        self.label_41.setMaximumSize(QSize(16777215, 16777215))
        self.label_41.setFont(font)

        self.gridLayout_3.addWidget(self.label_41, 0, 0, 1, 1)

        self.label_42 = QLabel(self.frame_18)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMinimumSize(QSize(0, 0))
        self.label_42.setMaximumSize(QSize(16777215, 16777215))
        self.label_42.setFont(font)

        self.gridLayout_3.addWidget(self.label_42, 1, 0, 1, 1)

        self.label_43 = QLabel(self.frame_18)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setMinimumSize(QSize(0, 0))
        self.label_43.setMaximumSize(QSize(16777215, 16777215))
        self.label_43.setFont(font)

        self.gridLayout_3.addWidget(self.label_43, 2, 0, 1, 1)

        self.label_44 = QLabel(self.frame_18)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setMinimumSize(QSize(0, 0))
        self.label_44.setMaximumSize(QSize(16777215, 16777215))
        self.label_44.setFont(font)

        self.gridLayout_3.addWidget(self.label_44, 3, 0, 1, 1)

        self.StatSpinBox = QComboBox(self.frame_18)
        self.StatSpinBox.setObjectName(u"StatSpinBox")
        self.StatSpinBox.setMinimumSize(QSize(90, 25))
        self.StatSpinBox.setFont(font)
        self.StatSpinBox.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout_3.addWidget(self.StatSpinBox, 0, 1, 1, 1)

        self.StatSpinBox_2 = QComboBox(self.frame_18)
        self.StatSpinBox_2.setObjectName(u"StatSpinBox_2")
        self.StatSpinBox_2.setMinimumSize(QSize(90, 25))
        self.StatSpinBox_2.setFont(font)

        self.gridLayout_3.addWidget(self.StatSpinBox_2, 1, 1, 1, 1)

        self.StatSpinBox_3 = QComboBox(self.frame_18)
        self.StatSpinBox_3.setObjectName(u"StatSpinBox_3")
        self.StatSpinBox_3.setMinimumSize(QSize(90, 25))
        self.StatSpinBox_3.setFont(font)

        self.gridLayout_3.addWidget(self.StatSpinBox_3, 2, 1, 1, 1)

        self.StatSpinBox_4 = QComboBox(self.frame_18)
        self.StatSpinBox_4.setObjectName(u"StatSpinBox_4")
        self.StatSpinBox_4.setMinimumSize(QSize(90, 25))
        self.StatSpinBox_4.setFont(font)

        self.gridLayout_3.addWidget(self.StatSpinBox_4, 3, 1, 1, 1)

        self.label_17 = QLabel(self.frame_18)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font)

        self.gridLayout_3.addWidget(self.label_17, 4, 0, 1, 1)

        self.StatSpinBox_5 = QComboBox(self.frame_18)
        self.StatSpinBox_5.setObjectName(u"StatSpinBox_5")
        self.StatSpinBox_5.setMinimumSize(QSize(90, 25))
        self.StatSpinBox_5.setFont(font)

        self.gridLayout_3.addWidget(self.StatSpinBox_5, 4, 1, 1, 1)


        self.verticalLayout_39.addLayout(self.gridLayout_3)

        self.verticalSpacer_22 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_39.addItem(self.verticalSpacer_22)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(-1, -1, 0, -1)
        self.StatisticalCalculateBtn = QPushButton(self.frame_18)
        self.StatisticalCalculateBtn.setObjectName(u"StatisticalCalculateBtn")
        self.StatisticalCalculateBtn.setFont(font2)
        self.StatisticalCalculateBtn.setIcon(icon9)

        self.horizontalLayout_15.addWidget(self.StatisticalCalculateBtn)

        self.StatisticalCancelBtn = QPushButton(self.frame_18)
        self.StatisticalCancelBtn.setObjectName(u"StatisticalCancelBtn")
        self.StatisticalCancelBtn.setMinimumSize(QSize(0, 0))
        self.StatisticalCancelBtn.setMaximumSize(QSize(16777215, 16777215))
        self.StatisticalCancelBtn.setFont(font2)
        self.StatisticalCancelBtn.setIcon(icon8)

        self.horizontalLayout_15.addWidget(self.StatisticalCancelBtn)


        self.verticalLayout_39.addLayout(self.horizontalLayout_15)

        self.verticalSpacer_31 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_39.addItem(self.verticalSpacer_31)


        self.verticalLayout_20.addWidget(self.frame_18)

        self.stackedWidget_2.addWidget(self.StatisticalCriteriaPg)
        self.CorrelRegrPg = QWidget()
        self.CorrelRegrPg.setObjectName(u"CorrelRegrPg")
        self.verticalLayout_35 = QVBoxLayout(self.CorrelRegrPg)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.widget_4 = QWidget(self.CorrelRegrPg)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_18 = QVBoxLayout(self.widget_4)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalSpacer_41 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_18.addItem(self.verticalSpacer_41)

        self.label_27 = QLabel(self.widget_4)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font11)

        self.verticalLayout_18.addWidget(self.label_27)

        self.verticalSpacer_21 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_18.addItem(self.verticalSpacer_21)

        self.label_28 = QLabel(self.widget_4)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font2)

        self.verticalLayout_18.addWidget(self.label_28)

        self.verticalSpacer_39 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_18.addItem(self.verticalSpacer_39)

        self.verticalLayout_40 = QVBoxLayout()
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.PearsonCorrCheckBox = QCheckBox(self.widget_4)
        self.PearsonCorrCheckBox.setObjectName(u"PearsonCorrCheckBox")
        self.PearsonCorrCheckBox.setFont(font)

        self.verticalLayout_40.addWidget(self.PearsonCorrCheckBox)

        self.SpearCorrCheckBox = QCheckBox(self.widget_4)
        self.SpearCorrCheckBox.setObjectName(u"SpearCorrCheckBox")
        self.SpearCorrCheckBox.setFont(font)

        self.verticalLayout_40.addWidget(self.SpearCorrCheckBox)

        self.KendalCorrCheckBox = QCheckBox(self.widget_4)
        self.KendalCorrCheckBox.setObjectName(u"KendalCorrCheckBox")
        self.KendalCorrCheckBox.setFont(font)

        self.verticalLayout_40.addWidget(self.KendalCorrCheckBox)


        self.verticalLayout_18.addLayout(self.verticalLayout_40)

        self.verticalSpacer_32 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_18.addItem(self.verticalSpacer_32)

        self.gridLayout_13 = QGridLayout()
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setHorizontalSpacing(2)
        self.CorrSpinBox_2 = QComboBox(self.widget_4)
        self.CorrSpinBox_2.setObjectName(u"CorrSpinBox_2")
        self.CorrSpinBox_2.setMinimumSize(QSize(90, 25))
        self.CorrSpinBox_2.setFont(font)

        self.gridLayout_13.addWidget(self.CorrSpinBox_2, 2, 1, 1, 1)

        self.label_47 = QLabel(self.widget_4)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setMinimumSize(QSize(0, 0))
        self.label_47.setMaximumSize(QSize(16777215, 16777215))
        self.label_47.setFont(font)

        self.gridLayout_13.addWidget(self.label_47, 2, 0, 1, 1)

        self.CorrSpinBox = QComboBox(self.widget_4)
        self.CorrSpinBox.setObjectName(u"CorrSpinBox")
        self.CorrSpinBox.setMinimumSize(QSize(90, 25))
        self.CorrSpinBox.setFont(font)

        self.gridLayout_13.addWidget(self.CorrSpinBox, 0, 1, 1, 1)

        self.CorrSpinBox_3 = QComboBox(self.widget_4)
        self.CorrSpinBox_3.setObjectName(u"CorrSpinBox_3")
        self.CorrSpinBox_3.setMinimumSize(QSize(90, 25))
        self.CorrSpinBox_3.setFont(font)

        self.gridLayout_13.addWidget(self.CorrSpinBox_3, 3, 1, 1, 1)

        self.verticalSpacer_65 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_13.addItem(self.verticalSpacer_65, 1, 0, 1, 1)

        self.label_39 = QLabel(self.widget_4)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setMinimumSize(QSize(0, 0))
        self.label_39.setMaximumSize(QSize(16777215, 16777215))
        self.label_39.setFont(font)

        self.gridLayout_13.addWidget(self.label_39, 0, 0, 1, 1)

        self.label_46 = QLabel(self.widget_4)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setMinimumSize(QSize(0, 0))
        self.label_46.setMaximumSize(QSize(16777215, 16777215))
        self.label_46.setFont(font)

        self.gridLayout_13.addWidget(self.label_46, 3, 0, 1, 1)


        self.verticalLayout_18.addLayout(self.gridLayout_13)

        self.verticalSpacer_75 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_18.addItem(self.verticalSpacer_75)

        self.label_29 = QLabel(self.widget_4)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font2)

        self.verticalLayout_18.addWidget(self.label_29)

        self.verticalSpacer_52 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_18.addItem(self.verticalSpacer_52)

        self.LinRegCheckBox = QCheckBox(self.widget_4)
        self.LinRegCheckBox.setObjectName(u"LinRegCheckBox")
        self.LinRegCheckBox.setFont(font)

        self.verticalLayout_18.addWidget(self.LinRegCheckBox)

        self.RoCheckBox = QCheckBox(self.widget_4)
        self.RoCheckBox.setObjectName(u"RoCheckBox")
        self.RoCheckBox.setFont(font)

        self.verticalLayout_18.addWidget(self.RoCheckBox)

        self.verticalSpacer_53 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_18.addItem(self.verticalSpacer_53)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(2)
        self.label_20 = QLabel(self.widget_4)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(0, 0))
        self.label_20.setMaximumSize(QSize(16777215, 16777215))
        self.label_20.setFont(font)

        self.gridLayout.addWidget(self.label_20, 0, 0, 1, 1)

        self.verticalSpacer_51 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_51, 1, 0, 1, 1)

        self.label_33 = QLabel(self.widget_4)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMinimumSize(QSize(0, 0))
        self.label_33.setMaximumSize(QSize(16777215, 16777215))
        self.label_33.setFont(font)

        self.gridLayout.addWidget(self.label_33, 3, 0, 1, 1)

        self.label_32 = QLabel(self.widget_4)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMinimumSize(QSize(0, 0))
        self.label_32.setMaximumSize(QSize(16777215, 16777215))
        self.label_32.setFont(font)

        self.gridLayout.addWidget(self.label_32, 2, 0, 1, 1)

        self.label_37 = QLabel(self.widget_4)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMinimumSize(QSize(0, 0))
        self.label_37.setMaximumSize(QSize(16777215, 16777215))
        self.label_37.setFont(font)

        self.gridLayout.addWidget(self.label_37, 6, 0, 1, 1)

        self.label_36 = QLabel(self.widget_4)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMinimumSize(QSize(0, 0))
        self.label_36.setMaximumSize(QSize(16777215, 16777215))
        self.label_36.setFont(font)

        self.gridLayout.addWidget(self.label_36, 5, 0, 1, 1)

        self.label_35 = QLabel(self.widget_4)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMinimumSize(QSize(0, 0))
        self.label_35.setMaximumSize(QSize(16777215, 16777215))
        self.label_35.setFont(font)

        self.gridLayout.addWidget(self.label_35, 4, 0, 1, 1)

        self.RegrSpinBox = QComboBox(self.widget_4)
        self.RegrSpinBox.setObjectName(u"RegrSpinBox")
        self.RegrSpinBox.setMinimumSize(QSize(90, 25))
        self.RegrSpinBox.setFont(font)

        self.gridLayout.addWidget(self.RegrSpinBox, 0, 1, 1, 1)

        self.RegrSpinBox_2 = QComboBox(self.widget_4)
        self.RegrSpinBox_2.setObjectName(u"RegrSpinBox_2")
        self.RegrSpinBox_2.setMinimumSize(QSize(90, 25))
        self.RegrSpinBox_2.setFont(font)

        self.gridLayout.addWidget(self.RegrSpinBox_2, 2, 1, 1, 1)

        self.RegrSpinBox_3 = QComboBox(self.widget_4)
        self.RegrSpinBox_3.setObjectName(u"RegrSpinBox_3")
        self.RegrSpinBox_3.setMinimumSize(QSize(90, 25))
        self.RegrSpinBox_3.setFont(font)

        self.gridLayout.addWidget(self.RegrSpinBox_3, 3, 1, 1, 1)

        self.RegrSpinBox_4 = QComboBox(self.widget_4)
        self.RegrSpinBox_4.setObjectName(u"RegrSpinBox_4")
        self.RegrSpinBox_4.setMinimumSize(QSize(90, 25))
        self.RegrSpinBox_4.setFont(font)

        self.gridLayout.addWidget(self.RegrSpinBox_4, 4, 1, 1, 1)

        self.RegrSpinBox_5 = QComboBox(self.widget_4)
        self.RegrSpinBox_5.setObjectName(u"RegrSpinBox_5")
        self.RegrSpinBox_5.setMinimumSize(QSize(90, 25))
        self.RegrSpinBox_5.setFont(font)

        self.gridLayout.addWidget(self.RegrSpinBox_5, 5, 1, 1, 1)

        self.RegrSpinBox_6 = QComboBox(self.widget_4)
        self.RegrSpinBox_6.setObjectName(u"RegrSpinBox_6")
        self.RegrSpinBox_6.setMinimumSize(QSize(90, 25))
        self.RegrSpinBox_6.setFont(font)

        self.gridLayout.addWidget(self.RegrSpinBox_6, 6, 1, 1, 1)


        self.verticalLayout_18.addLayout(self.gridLayout)

        self.verticalSpacer_17 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_18.addItem(self.verticalSpacer_17)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.CorrCalculateBtn = QPushButton(self.widget_4)
        self.CorrCalculateBtn.setObjectName(u"CorrCalculateBtn")
        self.CorrCalculateBtn.setFont(font2)
        self.CorrCalculateBtn.setIcon(icon9)

        self.horizontalLayout_16.addWidget(self.CorrCalculateBtn)

        self.CorrCancelBtn = QPushButton(self.widget_4)
        self.CorrCancelBtn.setObjectName(u"CorrCancelBtn")
        self.CorrCancelBtn.setMaximumSize(QSize(16777215, 16777215))
        self.CorrCancelBtn.setFont(font2)
        self.CorrCancelBtn.setIcon(icon8)

        self.horizontalLayout_16.addWidget(self.CorrCancelBtn)


        self.verticalLayout_18.addLayout(self.horizontalLayout_16)

        self.verticalSpacer_42 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_18.addItem(self.verticalSpacer_42)


        self.verticalLayout_35.addWidget(self.widget_4)

        self.stackedWidget_2.addWidget(self.CorrelRegrPg)
        self.SampleSizePg = QWidget()
        self.SampleSizePg.setObjectName(u"SampleSizePg")
        self.SampleSizePg.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_42 = QVBoxLayout(self.SampleSizePg)
        self.verticalLayout_42.setSpacing(6)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(3, 0, 3, 0)
        self.frame_20 = QFrame(self.SampleSizePg)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.frame_20)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_38.setContentsMargins(6, 6, 6, 6)
        self.verticalSpacer_63 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_38.addItem(self.verticalSpacer_63)

        self.label_14 = QLabel(self.frame_20)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font11)

        self.verticalLayout_38.addWidget(self.label_14)

        self.verticalSpacer_62 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_38.addItem(self.verticalSpacer_62)

        self.SampleRadioButton = QRadioButton(self.frame_20)
        self.SampleRadioButton.setObjectName(u"SampleRadioButton")
        self.SampleRadioButton.setFont(font2)

        self.verticalLayout_38.addWidget(self.SampleRadioButton)

        self.verticalSpacer_61 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_38.addItem(self.verticalSpacer_61)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setSpacing(10)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_4.setContentsMargins(3, 3, 3, 3)
        self.label_50 = QLabel(self.frame_20)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setFont(font)

        self.gridLayout_4.addWidget(self.label_50, 0, 0, 1, 1)

        self.SampleSpinBox_2 = QSpinBox(self.frame_20)
        self.SampleSpinBox_2.setObjectName(u"SampleSpinBox_2")
        self.SampleSpinBox_2.setMinimumSize(QSize(90, 30))
        self.SampleSpinBox_2.setMaximumSize(QSize(90, 16777215))
        self.SampleSpinBox_2.setFont(font)
        self.SampleSpinBox_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.SampleSpinBox_2.setSuffix(u"")
        self.SampleSpinBox_2.setMinimum(1)
        self.SampleSpinBox_2.setMaximum(100)
        self.SampleSpinBox_2.setValue(1)
        self.SampleSpinBox_2.setDisplayIntegerBase(10)

        self.gridLayout_4.addWidget(self.SampleSpinBox_2, 1, 1, 1, 1)

        self.label_51 = QLabel(self.frame_20)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setFont(font)

        self.gridLayout_4.addWidget(self.label_51, 2, 0, 1, 1)

        self.label_52 = QLabel(self.frame_20)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setFont(font)

        self.gridLayout_4.addWidget(self.label_52, 1, 0, 1, 1)

        self.SampleSpinBox_3 = QSpinBox(self.frame_20)
        self.SampleSpinBox_3.setObjectName(u"SampleSpinBox_3")
        self.SampleSpinBox_3.setMinimumSize(QSize(90, 30))
        self.SampleSpinBox_3.setMaximumSize(QSize(90, 16777215))
        self.SampleSpinBox_3.setFont(font)
        self.SampleSpinBox_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.SampleSpinBox_3.setSuffix(u"")
        self.SampleSpinBox_3.setMaximum(100)
        self.SampleSpinBox_3.setSingleStep(1)
        self.SampleSpinBox_3.setValue(50)

        self.gridLayout_4.addWidget(self.SampleSpinBox_3, 2, 1, 1, 1)

        self.SampleSpinBox_1 = QDoubleSpinBox(self.frame_20)
        self.SampleSpinBox_1.setObjectName(u"SampleSpinBox_1")
        self.SampleSpinBox_1.setMinimumSize(QSize(90, 30))
        self.SampleSpinBox_1.setMaximumSize(QSize(90, 16777215))
        self.SampleSpinBox_1.setFont(font)
        self.SampleSpinBox_1.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.SampleSpinBox_1.setDecimals(3)
        self.SampleSpinBox_1.setMinimum(0.001000000000000)
        self.SampleSpinBox_1.setMaximum(0.999000000000000)
        self.SampleSpinBox_1.setSingleStep(0.001000000000000)
        self.SampleSpinBox_1.setValue(0.950000000000000)

        self.gridLayout_4.addWidget(self.SampleSpinBox_1, 0, 1, 1, 1)

        self.label_53 = QLabel(self.frame_20)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setFont(font2)

        self.gridLayout_4.addWidget(self.label_53, 3, 0, 1, 1)

        self.SampleResult_1 = QLabel(self.frame_20)
        self.SampleResult_1.setObjectName(u"SampleResult_1")
        self.SampleResult_1.setMinimumSize(QSize(90, 30))
        self.SampleResult_1.setMaximumSize(QSize(90, 16777215))
        self.SampleResult_1.setFont(font)

        self.gridLayout_4.addWidget(self.SampleResult_1, 3, 1, 1, 1)


        self.verticalLayout_38.addLayout(self.gridLayout_4)

        self.verticalSpacer_60 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_38.addItem(self.verticalSpacer_60)

        self.ErrorRadioButton = QRadioButton(self.frame_20)
        self.ErrorRadioButton.setObjectName(u"ErrorRadioButton")
        self.ErrorRadioButton.setFont(font2)

        self.verticalLayout_38.addWidget(self.ErrorRadioButton)

        self.verticalSpacer_59 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_38.addItem(self.verticalSpacer_59)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setSpacing(10)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_5.setContentsMargins(3, 3, 3, 3)
        self.SampleSpinBox_6 = QSpinBox(self.frame_20)
        self.SampleSpinBox_6.setObjectName(u"SampleSpinBox_6")
        self.SampleSpinBox_6.setMinimumSize(QSize(90, 30))
        self.SampleSpinBox_6.setMaximumSize(QSize(90, 16777215))
        self.SampleSpinBox_6.setFont(font)
        self.SampleSpinBox_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.SampleSpinBox_6.setSuffix(u"")
        self.SampleSpinBox_6.setMaximum(100)
        self.SampleSpinBox_6.setValue(50)

        self.gridLayout_5.addWidget(self.SampleSpinBox_6, 2, 1, 1, 1)

        self.SampleSpinBox_4 = QDoubleSpinBox(self.frame_20)
        self.SampleSpinBox_4.setObjectName(u"SampleSpinBox_4")
        self.SampleSpinBox_4.setMinimumSize(QSize(90, 30))
        self.SampleSpinBox_4.setMaximumSize(QSize(90, 16777215))
        self.SampleSpinBox_4.setFont(font)
        self.SampleSpinBox_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.SampleSpinBox_4.setDecimals(3)
        self.SampleSpinBox_4.setMinimum(0.001000000000000)
        self.SampleSpinBox_4.setMaximum(0.999000000000000)
        self.SampleSpinBox_4.setSingleStep(0.001000000000000)
        self.SampleSpinBox_4.setValue(0.950000000000000)

        self.gridLayout_5.addWidget(self.SampleSpinBox_4, 0, 1, 1, 1)

        self.label_54 = QLabel(self.frame_20)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setFont(font)

        self.gridLayout_5.addWidget(self.label_54, 0, 0, 1, 1)

        self.label_55 = QLabel(self.frame_20)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setFont(font)

        self.gridLayout_5.addWidget(self.label_55, 1, 0, 1, 1)

        self.SampleSpinBox_5 = QSpinBox(self.frame_20)
        self.SampleSpinBox_5.setObjectName(u"SampleSpinBox_5")
        self.SampleSpinBox_5.setMinimumSize(QSize(90, 30))
        self.SampleSpinBox_5.setMaximumSize(QSize(90, 16777215))
        self.SampleSpinBox_5.setFont(font)
        self.SampleSpinBox_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.SampleSpinBox_5.setSuffix(u"")
        self.SampleSpinBox_5.setMinimum(1)
        self.SampleSpinBox_5.setMaximum(9000)
        self.SampleSpinBox_5.setValue(1)

        self.gridLayout_5.addWidget(self.SampleSpinBox_5, 1, 1, 1, 1)

        self.label_56 = QLabel(self.frame_20)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setFont(font)

        self.gridLayout_5.addWidget(self.label_56, 2, 0, 1, 1)

        self.label_57 = QLabel(self.frame_20)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setMinimumSize(QSize(0, 30))
        self.label_57.setFont(font2)

        self.gridLayout_5.addWidget(self.label_57, 3, 0, 1, 1)

        self.SampleResult_2 = QLabel(self.frame_20)
        self.SampleResult_2.setObjectName(u"SampleResult_2")
        self.SampleResult_2.setMinimumSize(QSize(90, 25))
        self.SampleResult_2.setMaximumSize(QSize(90, 16777215))
        self.SampleResult_2.setFont(font)

        self.gridLayout_5.addWidget(self.SampleResult_2, 3, 1, 1, 1)


        self.verticalLayout_38.addLayout(self.gridLayout_5)

        self.verticalSpacer_58 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_38.addItem(self.verticalSpacer_58)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.SampleCalculateBtn = QPushButton(self.frame_20)
        self.SampleCalculateBtn.setObjectName(u"SampleCalculateBtn")
        self.SampleCalculateBtn.setMaximumSize(QSize(16777215, 16777215))
        self.SampleCalculateBtn.setFont(font2)
        self.SampleCalculateBtn.setIcon(icon9)

        self.horizontalLayout_17.addWidget(self.SampleCalculateBtn)

        self.SampleCancelBtn = QPushButton(self.frame_20)
        self.SampleCancelBtn.setObjectName(u"SampleCancelBtn")
        self.SampleCancelBtn.setMaximumSize(QSize(16777215, 16777215))
        self.SampleCancelBtn.setFont(font2)
        self.SampleCancelBtn.setIcon(icon8)

        self.horizontalLayout_17.addWidget(self.SampleCancelBtn)


        self.verticalLayout_38.addLayout(self.horizontalLayout_17)

        self.verticalSpacer_19 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_38.addItem(self.verticalSpacer_19)


        self.verticalLayout_42.addWidget(self.frame_20)

        self.stackedWidget_2.addWidget(self.SampleSizePg)
        self.CoefficientPg = QWidget()
        self.CoefficientPg.setObjectName(u"CoefficientPg")
        self.verticalLayout_21 = QVBoxLayout(self.CoefficientPg)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.widget_7 = QWidget(self.CoefficientPg)
        self.widget_7.setObjectName(u"widget_7")
        self.verticalLayout_41 = QVBoxLayout(self.widget_7)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalSpacer_50 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_41.addItem(self.verticalSpacer_50)

        self.label_30 = QLabel(self.widget_7)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font11)

        self.verticalLayout_41.addWidget(self.label_30)

        self.verticalSpacer_49 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_41.addItem(self.verticalSpacer_49)

        self.ChiRadioButton = QRadioButton(self.widget_7)
        self.ChiRadioButton.setObjectName(u"ChiRadioButton")
        self.ChiRadioButton.setFont(font2)

        self.verticalLayout_41.addWidget(self.ChiRadioButton)

        self.verticalSpacer_48 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_41.addItem(self.verticalSpacer_48)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setSpacing(10)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(3, 3, 3, 3)
        self.PLevelCoeffLabel = QLabel(self.widget_7)
        self.PLevelCoeffLabel.setObjectName(u"PLevelCoeffLabel")
        self.PLevelCoeffLabel.setFont(font)

        self.gridLayout_2.addWidget(self.PLevelCoeffLabel, 0, 0, 1, 1)

        self.PLevelSpinBox = QDoubleSpinBox(self.widget_7)
        self.PLevelSpinBox.setObjectName(u"PLevelSpinBox")
        sizePolicy9 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.PLevelSpinBox.sizePolicy().hasHeightForWidth())
        self.PLevelSpinBox.setSizePolicy(sizePolicy9)
        self.PLevelSpinBox.setMinimumSize(QSize(0, 30))
        self.PLevelSpinBox.setMaximumSize(QSize(80, 25))
        self.PLevelSpinBox.setFont(font4)
        self.PLevelSpinBox.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.PLevelSpinBox.setDecimals(3)
        self.PLevelSpinBox.setMinimum(0.001000000000000)
        self.PLevelSpinBox.setMaximum(1.000000000000000)
        self.PLevelSpinBox.setSingleStep(0.001000000000000)
        self.PLevelSpinBox.setValue(0.950000000000000)

        self.gridLayout_2.addWidget(self.PLevelSpinBox, 0, 1, 1, 1)

        self.NCountCoeffLabel = QLabel(self.widget_7)
        self.NCountCoeffLabel.setObjectName(u"NCountCoeffLabel")
        self.NCountCoeffLabel.setFont(font)

        self.gridLayout_2.addWidget(self.NCountCoeffLabel, 1, 0, 1, 1)

        self.NCountCoeffBox = QSpinBox(self.widget_7)
        self.NCountCoeffBox.setObjectName(u"NCountCoeffBox")
        sizePolicy9.setHeightForWidth(self.NCountCoeffBox.sizePolicy().hasHeightForWidth())
        self.NCountCoeffBox.setSizePolicy(sizePolicy9)
        self.NCountCoeffBox.setMinimumSize(QSize(0, 30))
        self.NCountCoeffBox.setMaximumSize(QSize(80, 25))
        self.NCountCoeffBox.setFont(font4)
        self.NCountCoeffBox.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.NCountCoeffBox.setMaximum(1000)

        self.gridLayout_2.addWidget(self.NCountCoeffBox, 1, 1, 1, 1)

        self.label_18 = QLabel(self.widget_7)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(0, 33))
        self.label_18.setFont(font2)

        self.gridLayout_2.addWidget(self.label_18, 2, 0, 1, 1)

        self.ChiResultLebel = QLabel(self.widget_7)
        self.ChiResultLebel.setObjectName(u"ChiResultLebel")
        self.ChiResultLebel.setFont(font2)

        self.gridLayout_2.addWidget(self.ChiResultLebel, 2, 1, 1, 1)


        self.verticalLayout_41.addLayout(self.gridLayout_2)

        self.verticalSpacer_47 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_41.addItem(self.verticalSpacer_47)

        self.TRadioButton = QRadioButton(self.widget_7)
        self.TRadioButton.setObjectName(u"TRadioButton")
        self.TRadioButton.setFont(font2)

        self.verticalLayout_41.addWidget(self.TRadioButton)

        self.verticalSpacer_46 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_41.addItem(self.verticalSpacer_46)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setSpacing(10)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(3, 3, 3, 3)
        self.PLevelCoeffLabel_3 = QLabel(self.widget_7)
        self.PLevelCoeffLabel_3.setObjectName(u"PLevelCoeffLabel_3")
        self.PLevelCoeffLabel_3.setFont(font)

        self.gridLayout_7.addWidget(self.PLevelCoeffLabel_3, 0, 0, 1, 1)

        self.PLevelSpinBox_3 = QDoubleSpinBox(self.widget_7)
        self.PLevelSpinBox_3.setObjectName(u"PLevelSpinBox_3")
        sizePolicy9.setHeightForWidth(self.PLevelSpinBox_3.sizePolicy().hasHeightForWidth())
        self.PLevelSpinBox_3.setSizePolicy(sizePolicy9)
        self.PLevelSpinBox_3.setMinimumSize(QSize(0, 30))
        self.PLevelSpinBox_3.setMaximumSize(QSize(80, 25))
        self.PLevelSpinBox_3.setFont(font4)
        self.PLevelSpinBox_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.PLevelSpinBox_3.setDecimals(3)
        self.PLevelSpinBox_3.setMinimum(0.001000000000000)
        self.PLevelSpinBox_3.setMaximum(1.000000000000000)
        self.PLevelSpinBox_3.setSingleStep(0.001000000000000)
        self.PLevelSpinBox_3.setValue(0.950000000000000)

        self.gridLayout_7.addWidget(self.PLevelSpinBox_3, 0, 1, 1, 1)

        self.NCountCoeffLabel_2 = QLabel(self.widget_7)
        self.NCountCoeffLabel_2.setObjectName(u"NCountCoeffLabel_2")
        self.NCountCoeffLabel_2.setFont(font)

        self.gridLayout_7.addWidget(self.NCountCoeffLabel_2, 1, 0, 1, 1)

        self.NCountCoeffBox_2 = QSpinBox(self.widget_7)
        self.NCountCoeffBox_2.setObjectName(u"NCountCoeffBox_2")
        sizePolicy9.setHeightForWidth(self.NCountCoeffBox_2.sizePolicy().hasHeightForWidth())
        self.NCountCoeffBox_2.setSizePolicy(sizePolicy9)
        self.NCountCoeffBox_2.setMinimumSize(QSize(0, 30))
        self.NCountCoeffBox_2.setMaximumSize(QSize(80, 25))
        self.NCountCoeffBox_2.setFont(font4)
        self.NCountCoeffBox_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.NCountCoeffBox_2.setMaximum(1000)

        self.gridLayout_7.addWidget(self.NCountCoeffBox_2, 1, 1, 1, 1)

        self.label_24 = QLabel(self.widget_7)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(0, 33))
        self.label_24.setFont(font2)

        self.gridLayout_7.addWidget(self.label_24, 2, 0, 1, 1)

        self.TResultLebel = QLabel(self.widget_7)
        self.TResultLebel.setObjectName(u"TResultLebel")
        self.TResultLebel.setFont(font2)

        self.gridLayout_7.addWidget(self.TResultLebel, 2, 1, 1, 1)


        self.verticalLayout_41.addLayout(self.gridLayout_7)

        self.verticalSpacer_33 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_41.addItem(self.verticalSpacer_33)

        self.ZRadioButton = QRadioButton(self.widget_7)
        self.ZRadioButton.setObjectName(u"ZRadioButton")
        self.ZRadioButton.setFont(font2)

        self.verticalLayout_41.addWidget(self.ZRadioButton)

        self.verticalSpacer_34 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_41.addItem(self.verticalSpacer_34)

        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setSpacing(10)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(3, 3, 3, 3)
        self.PLevelCoeffLabel_4 = QLabel(self.widget_7)
        self.PLevelCoeffLabel_4.setObjectName(u"PLevelCoeffLabel_4")
        self.PLevelCoeffLabel_4.setFont(font)

        self.gridLayout_8.addWidget(self.PLevelCoeffLabel_4, 0, 0, 1, 1)

        self.PLevelSpinBox_4 = QDoubleSpinBox(self.widget_7)
        self.PLevelSpinBox_4.setObjectName(u"PLevelSpinBox_4")
        sizePolicy9.setHeightForWidth(self.PLevelSpinBox_4.sizePolicy().hasHeightForWidth())
        self.PLevelSpinBox_4.setSizePolicy(sizePolicy9)
        self.PLevelSpinBox_4.setMinimumSize(QSize(0, 30))
        self.PLevelSpinBox_4.setMaximumSize(QSize(80, 25))
        self.PLevelSpinBox_4.setFont(font4)
        self.PLevelSpinBox_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.PLevelSpinBox_4.setDecimals(3)
        self.PLevelSpinBox_4.setMinimum(0.001000000000000)
        self.PLevelSpinBox_4.setMaximum(1.000000000000000)
        self.PLevelSpinBox_4.setSingleStep(0.001000000000000)
        self.PLevelSpinBox_4.setValue(0.950000000000000)

        self.gridLayout_8.addWidget(self.PLevelSpinBox_4, 0, 1, 1, 1)

        self.ZResultLebel = QLabel(self.widget_7)
        self.ZResultLebel.setObjectName(u"ZResultLebel")
        self.ZResultLebel.setMaximumSize(QSize(16777215, 30))
        self.ZResultLebel.setFont(font2)

        self.gridLayout_8.addWidget(self.ZResultLebel, 1, 1, 1, 1)

        self.label_25 = QLabel(self.widget_7)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMinimumSize(QSize(0, 33))
        self.label_25.setMaximumSize(QSize(16777215, 30))
        self.label_25.setFont(font2)

        self.gridLayout_8.addWidget(self.label_25, 1, 0, 1, 1)


        self.verticalLayout_41.addLayout(self.gridLayout_8)

        self.verticalSpacer_38 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_41.addItem(self.verticalSpacer_38)

        self.PRadioButton = QRadioButton(self.widget_7)
        self.PRadioButton.setObjectName(u"PRadioButton")
        self.PRadioButton.setFont(font2)

        self.verticalLayout_41.addWidget(self.PRadioButton)

        self.verticalSpacer_37 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_41.addItem(self.verticalSpacer_37)

        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setSpacing(10)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(3, 3, 3, 3)
        self.PLevelCoeffLabel_5 = QLabel(self.widget_7)
        self.PLevelCoeffLabel_5.setObjectName(u"PLevelCoeffLabel_5")
        self.PLevelCoeffLabel_5.setFont(font)

        self.gridLayout_9.addWidget(self.PLevelCoeffLabel_5, 0, 0, 1, 1)

        self.NCountCoeffLabel_3 = QLabel(self.widget_7)
        self.NCountCoeffLabel_3.setObjectName(u"NCountCoeffLabel_3")
        self.NCountCoeffLabel_3.setFont(font)

        self.gridLayout_9.addWidget(self.NCountCoeffLabel_3, 1, 0, 1, 1)

        self.label_26 = QLabel(self.widget_7)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(0, 33))
        self.label_26.setFont(font2)

        self.gridLayout_9.addWidget(self.label_26, 2, 0, 1, 1)

        self.PResultLebel = QLabel(self.widget_7)
        self.PResultLebel.setObjectName(u"PResultLebel")
        self.PResultLebel.setFont(font2)

        self.gridLayout_9.addWidget(self.PResultLebel, 2, 1, 1, 1)

        self.PoissonSpinBox = QSpinBox(self.widget_7)
        self.PoissonSpinBox.setObjectName(u"PoissonSpinBox")
        self.PoissonSpinBox.setMinimumSize(QSize(0, 30))
        self.PoissonSpinBox.setMaximumSize(QSize(80, 30))
        self.PoissonSpinBox.setFont(font4)
        self.PoissonSpinBox.setLayoutDirection(Qt.LeftToRight)
        self.PoissonSpinBox.setAutoFillBackground(False)
        self.PoissonSpinBox.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.PoissonSpinBox.setMaximum(1000)

        self.gridLayout_9.addWidget(self.PoissonSpinBox, 0, 1, 1, 1)

        self.NCountCoeffBox_3 = QSpinBox(self.widget_7)
        self.NCountCoeffBox_3.setObjectName(u"NCountCoeffBox_3")
        sizePolicy9.setHeightForWidth(self.NCountCoeffBox_3.sizePolicy().hasHeightForWidth())
        self.NCountCoeffBox_3.setSizePolicy(sizePolicy9)
        self.NCountCoeffBox_3.setMinimumSize(QSize(0, 30))
        self.NCountCoeffBox_3.setMaximumSize(QSize(80, 25))
        self.NCountCoeffBox_3.setFont(font4)
        self.NCountCoeffBox_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.NCountCoeffBox_3.setMaximum(1000)

        self.gridLayout_9.addWidget(self.NCountCoeffBox_3, 1, 1, 1, 1)


        self.verticalLayout_41.addLayout(self.gridLayout_9)

        self.verticalSpacer_36 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_41.addItem(self.verticalSpacer_36)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.CoeffCalculateBtn = QPushButton(self.widget_7)
        self.CoeffCalculateBtn.setObjectName(u"CoeffCalculateBtn")
        self.CoeffCalculateBtn.setFont(font2)
        self.CoeffCalculateBtn.setIcon(icon9)

        self.horizontalLayout_8.addWidget(self.CoeffCalculateBtn)

        self.CoeffCancelBtn = QPushButton(self.widget_7)
        self.CoeffCancelBtn.setObjectName(u"CoeffCancelBtn")
        self.CoeffCancelBtn.setMinimumSize(QSize(0, 0))
        self.CoeffCancelBtn.setFont(font2)
        self.CoeffCancelBtn.setIcon(icon8)

        self.horizontalLayout_8.addWidget(self.CoeffCancelBtn)


        self.verticalLayout_41.addLayout(self.horizontalLayout_8)

        self.verticalSpacer_45 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_41.addItem(self.verticalSpacer_45)


        self.verticalLayout_21.addWidget(self.widget_7)

        self.stackedWidget_2.addWidget(self.CoefficientPg)

        self.verticalLayout_16.addWidget(self.stackedWidget_2)


        self.horizontalLayout_6.addWidget(self.RightContentMenuContainer)

        self.RightMenuSubContainer = QWidget(self.RightSubMenuSubContainer)
        self.RightMenuSubContainer.setObjectName(u"RightMenuSubContainer")
        self.RightMenuSubContainer.setMinimumSize(QSize(0, 0))
        self.verticalLayout_12 = QVBoxLayout(self.RightMenuSubContainer)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(3, 3, 3, 0)
        self.frame_10 = QFrame(self.RightMenuSubContainer)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.formLayout_3 = QFormLayout(self.frame_10)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setContentsMargins(6, 6, 5, 6)
        self.CloseRightMenuBtn = QPushButton(self.frame_10)
        self.CloseRightMenuBtn.setObjectName(u"CloseRightMenuBtn")
        self.CloseRightMenuBtn.setLayoutDirection(Qt.RightToLeft)
        self.CloseRightMenuBtn.setIcon(icon8)
        self.CloseRightMenuBtn.setIconSize(QSize(18, 18))

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.CloseRightMenuBtn)

        self.label_5 = QLabel(self.frame_10)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)
        self.label_5.setLayoutDirection(Qt.RightToLeft)
        self.label_5.setAutoFillBackground(False)

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_5)


        self.verticalLayout_12.addWidget(self.frame_10, 0, Qt.AlignTop)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_3)

        self.frame_11 = QFrame(self.RightMenuSubContainer)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame_11)
        self.formLayout.setObjectName(u"formLayout")
        self.BaseStatisticsBtn = QPushButton(self.frame_11)
        self.BaseStatisticsBtn.setObjectName(u"BaseStatisticsBtn")
        self.BaseStatisticsBtn.setFont(font2)
        self.BaseStatisticsBtn.setLayoutDirection(Qt.RightToLeft)
        icon17 = QIcon()
        icon17.addFile(u"H:/Easy Statistica/icons/coffee.png", QSize(), QIcon.Normal, QIcon.Off)
        self.BaseStatisticsBtn.setIcon(icon17)
        self.BaseStatisticsBtn.setIconSize(QSize(18, 18))
        self.BaseStatisticsBtn.setCheckable(True)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.BaseStatisticsBtn)

        self.StatCriteriaBtn = QPushButton(self.frame_11)
        self.StatCriteriaBtn.setObjectName(u"StatCriteriaBtn")
        self.StatCriteriaBtn.setFont(font2)
        self.StatCriteriaBtn.setLayoutDirection(Qt.RightToLeft)
        icon18 = QIcon()
        icon18.addFile(u"H:/Easy Statistica/icons/package.png", QSize(), QIcon.Normal, QIcon.Off)
        self.StatCriteriaBtn.setIcon(icon18)
        self.StatCriteriaBtn.setIconSize(QSize(18, 18))
        self.StatCriteriaBtn.setCheckable(True)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.StatCriteriaBtn)

        self.CorrRegrBtn = QPushButton(self.frame_11)
        self.CorrRegrBtn.setObjectName(u"CorrRegrBtn")
        self.CorrRegrBtn.setFont(font2)
        self.CorrRegrBtn.setLayoutDirection(Qt.RightToLeft)
        icon19 = QIcon()
        icon19.addFile(u"H:/Easy Statistica/icons/bar-chart.png", QSize(), QIcon.Normal, QIcon.Off)
        self.CorrRegrBtn.setIcon(icon19)
        self.CorrRegrBtn.setIconSize(QSize(18, 18))
        self.CorrRegrBtn.setCheckable(True)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.CorrRegrBtn)


        self.verticalLayout_12.addWidget(self.frame_11, 0, Qt.AlignTop)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_2)

        self.frame_12 = QFrame(self.RightMenuSubContainer)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.formLayout_2 = QFormLayout(self.frame_12)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.SampleSizeSelectionBtn = QPushButton(self.frame_12)
        self.SampleSizeSelectionBtn.setObjectName(u"SampleSizeSelectionBtn")
        self.SampleSizeSelectionBtn.setFont(font2)
        self.SampleSizeSelectionBtn.setLayoutDirection(Qt.RightToLeft)
        icon20 = QIcon()
        icon20.addFile(u"H:/Easy Statistica/icons/archive.png", QSize(), QIcon.Normal, QIcon.Off)
        self.SampleSizeSelectionBtn.setIcon(icon20)
        self.SampleSizeSelectionBtn.setIconSize(QSize(18, 18))
        self.SampleSizeSelectionBtn.setCheckable(True)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.SampleSizeSelectionBtn)

        self.CoefficientsBtn = QPushButton(self.frame_12)
        self.CoefficientsBtn.setObjectName(u"CoefficientsBtn")
        self.CoefficientsBtn.setFont(font2)
        self.CoefficientsBtn.setLayoutDirection(Qt.RightToLeft)
        icon21 = QIcon()
        icon21.addFile(u"H:/Easy Statistica/icons/book.png", QSize(), QIcon.Normal, QIcon.Off)
        self.CoefficientsBtn.setIcon(icon21)
        self.CoefficientsBtn.setIconSize(QSize(18, 18))
        self.CoefficientsBtn.setCheckable(True)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.CoefficientsBtn)


        self.verticalLayout_12.addWidget(self.frame_12, 0, Qt.AlignBottom)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_4)


        self.horizontalLayout_6.addWidget(self.RightMenuSubContainer)


        self.verticalLayout_15.addWidget(self.RightSubMenuSubContainer, 0, Qt.AlignRight)


        self.horizontalLayout_5.addWidget(self.RightContentContainer)


        self.verticalLayout_11.addWidget(self.MainBodyContent)

        self.DownContainer = QWidget(self.MainBodyContainer)
        self.DownContainer.setObjectName(u"DownContainer")
        sizePolicy3.setHeightForWidth(self.DownContainer.sizePolicy().hasHeightForWidth())
        self.DownContainer.setSizePolicy(sizePolicy3)
        self.DownContainer.setMinimumSize(QSize(20, 15))
        self.horizontalLayout_7 = QHBoxLayout(self.DownContainer)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.DownContainer)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.Copyright = QLabel(self.frame_9)
        self.Copyright.setObjectName(u"Copyright")
        self.Copyright.setGeometry(QRect(30, 0, 211, 15))
        sizePolicy.setHeightForWidth(self.Copyright.sizePolicy().hasHeightForWidth())
        self.Copyright.setSizePolicy(sizePolicy)
        self.Copyright.setMinimumSize(QSize(30, 15))
        self.Copyright.setMaximumSize(QSize(16777215, 16777215))
        font12 = QFont()
        font12.setPointSize(7)
        font12.setBold(True)
        self.Copyright.setFont(font12)

        self.horizontalLayout_7.addWidget(self.frame_9)

        self.SizeGrip = QFrame(self.DownContainer)
        self.SizeGrip.setObjectName(u"SizeGrip")
        self.SizeGrip.setMinimumSize(QSize(15, 15))
        self.SizeGrip.setMaximumSize(QSize(15, 15))
        self.SizeGrip.setFrameShape(QFrame.StyledPanel)
        self.SizeGrip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_7.addWidget(self.SizeGrip)


        self.verticalLayout_11.addWidget(self.DownContainer)


        self.horizontalLayout.addWidget(self.MainBodyContainer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.DataBtn.clicked["bool"].connect(self.CentralMenuSubContainer.showMaximized)
        self.CloseCentralMenuBtn.clicked["bool"].connect(self.CentralMenuSubContainer.close)
        self.ReportsBtn.clicked["bool"].connect(self.CentralMenuSubContainer.showMaximized)
        self.SettingsBtn.clicked["bool"].connect(self.CentralMenuSubContainer.showMaximized)
        self.HelpBtn.clicked["bool"].connect(self.CentralMenuSubContainer.showMaximized)
        self.InfoBtn.clicked["bool"].connect(self.CentralMenuSubContainer.showMaximized)
        self.DataAnalysisBtn.toggled.connect(self.RightMenuSubContainer.setHidden)
        self.CloseRightMenuBtn.clicked["bool"].connect(self.RightMenuSubContainer.close)
        self.CloseRightMenuBtn.clicked["bool"].connect(self.RightContentMenuContainer.close)
        self.MenuBtn_2.clicked["bool"].connect(self.LeftMenuSubContainer.setVisible)
        self.MenuBtn_2.clicked["bool"].connect(self.widget_3.setHidden)
        self.DataBtn_2.clicked["bool"].connect(self.CentralMenuSubContainer.showMaximized)
        self.ReportsBtn_2.clicked["bool"].connect(self.CentralMenuSubContainer.showMaximized)
        self.SettingsBtn_2.clicked["bool"].connect(self.CentralMenuSubContainer.showMaximized)
        self.HelpBtn_2.clicked["bool"].connect(self.CentralMenuSubContainer.showMaximized)
        self.InfoBtn_2.clicked["bool"].connect(self.CentralMenuSubContainer.showMaximized)
        self.DataAnalysisBtn_2.toggled.connect(self.RightMenuSubContainer.setHidden)
        self.DataAnalysisBtn.toggled.connect(self.RightMenuSubContainer.setVisible)
        self.DataAnalysisBtn_2.toggled.connect(self.RightMenuSubContainer.setVisible)
        self.DataAnalysisBtn_2.toggled.connect(self.RightContentMenuContainer.close)
        self.DataAnalysisBtn.toggled.connect(self.RightContentMenuContainer.close)
        self.MenuBtn.clicked["bool"].connect(self.LeftMenuSubContainer.setHidden)
        self.MenuBtn.clicked["bool"].connect(self.widget_3.setVisible)
        self.BaseStatisticsBtn.clicked["bool"].connect(self.RightContentMenuContainer.show)
        self.StatCriteriaBtn.clicked["bool"].connect(self.RightContentMenuContainer.showMaximized)
        self.CorrRegrBtn.clicked["bool"].connect(self.RightContentMenuContainer.show)
        self.SampleSizeSelectionBtn.clicked["bool"].connect(self.RightContentMenuContainer.showMaximized)
        self.CoefficientsBtn.clicked["bool"].connect(self.RightContentMenuContainer.show)
        self.CorrCancelBtn.clicked["bool"].connect(self.RightContentMenuContainer.close)
        self.CoeffCancelBtn.clicked["bool"].connect(self.RightContentMenuContainer.close)
        self.BaseCancelBtn.clicked["bool"].connect(self.RightContentMenuContainer.close)
        self.StatisticalCancelBtn.clicked["bool"].connect(self.RightContentMenuContainer.close)
        self.SampleCancelBtn.clicked["bool"].connect(self.RightContentMenuContainer.close)
        self.BaseCancelBtn.clicked["bool"].connect(self.MainContentContainer.show)
        self.BaseCalculateBtn.clicked["bool"].connect(self.MainContentContainer.show)
        self.BaseCalculateBtn.clicked["bool"].connect(self.RightContentMenuContainer.close)
        self.CloseRightMenuBtn.clicked["bool"].connect(self.MainContentContainer.show)
        self.StatisticalCalculateBtn.clicked["bool"].connect(self.RightContentMenuContainer.close)
        self.CorrCalculateBtn.clicked["bool"].connect(self.RightContentMenuContainer.close)

        self.stackedWidget.setCurrentIndex(0)
        self.MainContentSubContainer.setCurrentIndex(1)
        self.stackedWidget_2.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Easy Statistica", None))
#if QT_CONFIG(tooltip)
        self.MenuBtn_2.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.MenuBtn_2.setText("")
#if QT_CONFIG(tooltip)
        self.DataBtn_2.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.DataBtn_2.setText("")
#if QT_CONFIG(tooltip)
        self.DataAnalysisBtn_2.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.DataAnalysisBtn_2.setText("")
#if QT_CONFIG(tooltip)
        self.ReportsBtn_2.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.ReportsBtn_2.setText("")
#if QT_CONFIG(tooltip)
        self.SettingsBtn_2.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.SettingsBtn_2.setText("")
#if QT_CONFIG(tooltip)
        self.HelpBtn_2.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.HelpBtn_2.setText("")
#if QT_CONFIG(tooltip)
        self.InfoBtn_2.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.InfoBtn_2.setText("")
#if QT_CONFIG(tooltip)
        self.MenuBtn.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.MenuBtn.setText("")
#if QT_CONFIG(tooltip)
        self.DataBtn.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.DataBtn.setText(QCoreApplication.translate("MainWindow", u" Data", None))
#if QT_CONFIG(tooltip)
        self.DataAnalysisBtn.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.DataAnalysisBtn.setText(QCoreApplication.translate("MainWindow", u" Data Analysis", None))
#if QT_CONFIG(tooltip)
        self.ReportsBtn.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.ReportsBtn.setText(QCoreApplication.translate("MainWindow", u" Reports", None))
#if QT_CONFIG(tooltip)
        self.SettingsBtn.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.SettingsBtn.setText(QCoreApplication.translate("MainWindow", u" Settings", None))
#if QT_CONFIG(tooltip)
        self.HelpBtn.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.HelpBtn.setText(QCoreApplication.translate("MainWindow", u" FAQ", None))
#if QT_CONFIG(tooltip)
        self.InfoBtn.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.InfoBtn.setText(QCoreApplication.translate("MainWindow", u"Information", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"More Menu", None))
        self.CloseCentralMenuBtn.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Table Creation:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Number of Columns:", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Number of Rows:", None))
        self.CreateTableBtn.setText(QCoreApplication.translate("MainWindow", u"Create", None))
        self.OpenTableBtn.setText(QCoreApplication.translate("MainWindow", u"Open the Excel file", None))
        self.OpenCsvBtn.setText(QCoreApplication.translate("MainWindow", u"Open the CSV file", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Table for Data:", None))
        self.LetsGoBtn.setText(QCoreApplication.translate("MainWindow", u"Let's start analyzing", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"  Save the data table:", None))
        self.SaveExcelBtn.setText(QCoreApplication.translate("MainWindow", u" Save to Excel file", None))
        self.SaveCsvBtn.setText(QCoreApplication.translate("MainWindow", u" Save to CSV file", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"  Save the result of analysis:", None))
        self.SaveDfPushButton.setText(QCoreApplication.translate("MainWindow", u"Save table to CSV file", None))
        self.SaveDfPushButton_2.setText(QCoreApplication.translate("MainWindow", u"Save table to Excel file", None))
        self.ExportPdfBtn.setText(QCoreApplication.translate("MainWindow", u"Export results to PDF file", None))
        self.SaveJpgPushButton.setText(QCoreApplication.translate("MainWindow", u"Export graphics to JPG file", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"Action for empty cells:", None))
        self.SetDataRadioButton.setText(QCoreApplication.translate("MainWindow", u"Delete rows with empty cells", None))
        self.SetDataRadioButton_2.setText(QCoreApplication.translate("MainWindow", u"Replase empthy cells with value 0 (default)", None))
        self.SetDataRadioButton_3.setText(QCoreApplication.translate("MainWindow", u"Replase empthy cells with average value", None))
        self.SetDataRadioButton_4.setText(QCoreApplication.translate("MainWindow", u"Apply interpolation to empty cells", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0421onfidence level: ", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"  Number of decimal places:", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Results output: ", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"  Number of decimal places:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"FAQ", None))
        self.FAQButton.setText(QCoreApplication.translate("MainWindow", u"Welcome page", None))
        self.FAQButton_2.setText(QCoreApplication.translate("MainWindow", u"Base Statistics", None))
        self.FAQButton_3.setText(QCoreApplication.translate("MainWindow", u"Statistical Criteria", None))
        self.FAQButton_4.setText(QCoreApplication.translate("MainWindow", u"Correlation and Regression", None))
        self.FAQButton_5.setText(QCoreApplication.translate("MainWindow", u"Sample size selection", None))
        self.FAQButton_6.setText(QCoreApplication.translate("MainWindow", u"Coefficients", None))
        self.infoLabel.setText(QCoreApplication.translate("MainWindow", u"Information", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Easy Statistica", None))
        self.MinimizeBtn.setText("")
        self.NormalBtn.setText("")
        self.RestoreBtn.setText("")
        self.CloseBtn.setText("")
        self.firstWelcomeLabel.setText("")
        self.viewWelcomeLabel_1.setText("")
        self.viewWelcomeLabel_2.setText("")
        self.viewWelcomeLabel_3.setText("")
        self.ResultViewLabel.setText("")
        self.ResultViewLabel_1.setText("")
        self.ResultViewLabel_8.setText("")
        self.ResultViewLabel_2.setText("")
        self.ResultViewLabel_3.setText("")
        self.ResultViewLabel_4.setText("")
        self.ResultViewLabel_5.setText("")
        self.ResultViewLabel_6.setText("")
        self.ResultViewLabel_7.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Base Statistics", None))
        self.PLevelCoeffLabel_2.setText(QCoreApplication.translate("MainWindow", u"Confidence interval:", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Normality test:", None))
        self.PearsonCheckBox.setText(QCoreApplication.translate("MainWindow", u"Pearson test", None))
        self.ShapiroCheckBox.setText(QCoreApplication.translate("MainWindow", u"Shapiro\u2013Wilk test", None))
        self.KolmogorovCheckBox.setText(QCoreApplication.translate("MainWindow", u"Kolmogorov\u2013Smirnov test", None))
        self.ZCheckBox.setText(QCoreApplication.translate("MainWindow", u"Z-test", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u" Graphics:", None))
        self.BaseCheckBox.setText(QCoreApplication.translate("MainWindow", u"Histogram", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"Variable(s)", None))
        self.BaseCheckBox_2.setText(QCoreApplication.translate("MainWindow", u"Boxplot", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Variable(s)", None))
        self.BaseCalculateBtn.setText(QCoreApplication.translate("MainWindow", u"Calculate!", None))
        self.BaseCancelBtn.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Statistical criteria", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Parametric criteria:", None))
        self.ttestCheckBox.setText(QCoreApplication.translate("MainWindow", u"Student\u2019s t-test", None))
        self.OneTtestRadioButton.setText(QCoreApplication.translate("MainWindow", u"One-sample t-test", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Expected mean:", None))
        self.TwoTRadioButton.setText(QCoreApplication.translate("MainWindow", u"Two-sample t-test", None))
        self.PairTRadioButton.setText(QCoreApplication.translate("MainWindow", u"Paired t-test", None))
        self.MultiTRadioButton.setText(QCoreApplication.translate("MainWindow", u"Multiple t-test", None))
        self.FisherCheckBox.setText(QCoreApplication.translate("MainWindow", u"Fisher's F-test", None))
        self.AnovaCheckBox.setText(QCoreApplication.translate("MainWindow", u" ANOVA", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Nonparametric criteria:", None))
        self.UtestCheckBox.setText(QCoreApplication.translate("MainWindow", u"Mann-Whitney U-test", None))
        self.WilcoxCheckBox.setText(QCoreApplication.translate("MainWindow", u"Wilcoxon test", None))
        self.KolmCheckBox.setText(QCoreApplication.translate("MainWindow", u"Kolmogorov-Smirnov test", None))
        self.KruWallCheckBox.setText(QCoreApplication.translate("MainWindow", u"Kruskal-Wallis test", None))
        self.FriCheckBox.setText(QCoreApplication.translate("MainWindow", u"Fridman test", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u" Variables:", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Variable", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Variable", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Variable", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Variable", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Variable", None))
        self.StatisticalCalculateBtn.setText(QCoreApplication.translate("MainWindow", u"Calculate!", None))
        self.StatisticalCancelBtn.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Correlation and regression", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Correlation:", None))
        self.PearsonCorrCheckBox.setText(QCoreApplication.translate("MainWindow", u"Pearson correlation", None))
        self.SpearCorrCheckBox.setText(QCoreApplication.translate("MainWindow", u"Spearman rank correlation", None))
        self.KendalCorrCheckBox.setText(QCoreApplication.translate("MainWindow", u"Kendall rank correlation", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Variable", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Variable(s)", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Variable", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Regression:", None))
        self.LinRegCheckBox.setText(QCoreApplication.translate("MainWindow", u"Linear regression", None))
        self.RoCheckBox.setText(QCoreApplication.translate("MainWindow", u"Logistic regression", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Dependent variable", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Independent variable", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Independent variable", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Independent variable", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Independent variable", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Independent variable", None))
        self.CorrCalculateBtn.setText(QCoreApplication.translate("MainWindow", u"Calculate!", None))
        self.CorrCancelBtn.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Sample size selection", None))
        self.SampleRadioButton.setText(QCoreApplication.translate("MainWindow", u"Sample size calculation:", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Confidence level:", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Frequency of occurrence, %:", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Sampling error, %:", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Result:", None))
        self.SampleResult_1.setText("")
        self.ErrorRadioButton.setText(QCoreApplication.translate("MainWindow", u"Sampling error calculation:", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Confidence level:", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Sample size:", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Frequency of occurrence, %:", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Result, %:", None))
        self.SampleResult_2.setText("")
        self.SampleCalculateBtn.setText(QCoreApplication.translate("MainWindow", u"Calculate!", None))
        self.SampleCancelBtn.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Coefficients", None))
        self.ChiRadioButton.setText(QCoreApplication.translate("MainWindow", u"Chi-squared critical value ", None))
        self.PLevelCoeffLabel.setText(QCoreApplication.translate("MainWindow", u"Confidence level:", None))
        self.NCountCoeffLabel.setText(QCoreApplication.translate("MainWindow", u"Degrees of freedom:", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Result:", None))
        self.ChiResultLebel.setText("")
        self.TRadioButton.setText(QCoreApplication.translate("MainWindow", u"Student's (t-test) critical value ", None))
        self.PLevelCoeffLabel_3.setText(QCoreApplication.translate("MainWindow", u"Confidence level:", None))
        self.NCountCoeffLabel_2.setText(QCoreApplication.translate("MainWindow", u"Degrees of freedom:", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Result:", None))
        self.TResultLebel.setText("")
        self.ZRadioButton.setText(QCoreApplication.translate("MainWindow", u"Gaussian (Z-test) critical value", None))
        self.PLevelCoeffLabel_4.setText(QCoreApplication.translate("MainWindow", u"Confidence level:", None))
        self.ZResultLebel.setText("")
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Result:", None))
        self.PRadioButton.setText(QCoreApplication.translate("MainWindow", u"Poisson probability distibution", None))
        self.PLevelCoeffLabel_5.setText(QCoreApplication.translate("MainWindow", u"Mean value:", None))
        self.NCountCoeffLabel_3.setText(QCoreApplication.translate("MainWindow", u"Value:", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Result, %:", None))
        self.PResultLebel.setText("")
        self.CoeffCalculateBtn.setText(QCoreApplication.translate("MainWindow", u"Calculate!", None))
        self.CoeffCancelBtn.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.CloseRightMenuBtn.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Data Analysis", None))
        self.BaseStatisticsBtn.setText(QCoreApplication.translate("MainWindow", u"Base Statistics", None))
        self.StatCriteriaBtn.setText(QCoreApplication.translate("MainWindow", u"Statistical criteria", None))
        self.CorrRegrBtn.setText(QCoreApplication.translate("MainWindow", u"Correlation and regression ", None))
        self.SampleSizeSelectionBtn.setText(QCoreApplication.translate("MainWindow", u"Sample size selection", None))
        self.CoefficientsBtn.setText(QCoreApplication.translate("MainWindow", u"Coefficients", None))
        self.Copyright.setText("")
    # retranslateUi

