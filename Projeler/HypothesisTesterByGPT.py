import numpy as np
from scipy.stats import shapiro
import scipy.stats as stats
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QVBoxLayout, QInputDialog

# Data Array'inin icine Verilerinizi Giriniz!
data = np.array([17, 160, 234, 149, 145, 107, 197, 75, 201, 225, 211, 119,
                 157, 145, 127, 244, 163, 114, 145, 65, 112, 185, 202, 146,
                 203, 224, 203, 114, 188, 156, 187, 154, 177, 95, 165, 50, 110,
                 216, 138, 151, 166, 135, 155, 84, 251, 173, 131, 207, 121, 120])

class HipotezTesterApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Arayüz bileşenlerini tanımlama
        self.label = QLabel("Uygulanabilir Testler:\nNormality (1)\nT-Test (2)", self)
        
        self.test_choice_input = QLineEdit(self)
        self.test_choice_input.setPlaceholderText("Test seçimini girin (1/2)")

        self.submit_button = QPushButton("Testi Uygula", self)
        self.submit_button.clicked.connect(self.run_test)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.test_choice_input)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)
        self.setWindowTitle("Hipotez Testi Uygulaması")
        self.show()

    def run_test(self):
        try:
            tercih = int(self.test_choice_input.text())
            if tercih == 1:
                self.shapiro_test()
            elif tercih == 2:
                self.t_test()
            else:
                QMessageBox.warning(self, "Hata", "Lütfen 1 veya 2 değerini giriniz.")
        except ValueError:
            QMessageBox.warning(self, "Hata", "Lütfen geçerli bir sayı giriniz.")

    def shapiro_test(self):
        result = shapiro(data)
        p_value = result.pvalue

        if p_value < 0.05:
            QMessageBox.information(self, "Sonuç", "p-value < 0.05 olduğu için H₀ Hipotezi Reddedilir!")
        else:
            reply = QMessageBox.question(self, "Sonuç",
                                          "p-value >= 0.05 olduğu için H₀ Hipotezi Kabul Edilir!\nT-Testine geçmek istiyor musunuz?",
                                          QMessageBox.Yes | QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.t_test()

    def t_test(self):
        pop_mean, ok = QInputDialog.getDouble(self, "Popülasyon Ortalaması",
                                               "Karşılaştırmak istediğiniz Popülasyon Ortalamasını Giriniz:")
        if ok:
            t_statistic, pvalue = stats.ttest_1samp(data, popmean=pop_mean)

            if pvalue < 0.05:
                QMessageBox.information(self, "Sonuç", "H₀ Hipotezi Reddedilir!\nVeri setiniz normal dağılıma uygun değil!")
            else:
                QMessageBox.information(self, "Sonuç", "H₀ Hipotezi Kabul Edilir!\nVeri setiniz tamamen normal dağılıyor!")

# PyQt uygulamasını başlatma
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ex = HipotezTesterApp()
    sys.exit(app.exec_())
