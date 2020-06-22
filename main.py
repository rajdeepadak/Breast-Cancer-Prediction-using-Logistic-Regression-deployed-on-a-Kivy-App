# Import all libraries ---------------------------------
from kivy.app import App
from kivy.properties import NumericProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from sklearn.linear_model import LogisticRegression
import pandas as pd
# ------------------------------------------------------


# kivy Window Manager class -------
class Windowmanager(ScreenManager):
    pass
# ---------------------------------


# Input Screen (First Window) -------------------------
class Inputscreen(Screen):
    
    Y_pred = NumericProperty(1)
    
    ct = ObjectProperty()
    ucsz = ObjectProperty()
    ucsp = ObjectProperty()
    ma = ObjectProperty()
    secs = ObjectProperty()
    bn = ObjectProperty()
    bc = ObjectProperty()
    nn = ObjectProperty()
    m = ObjectProperty()

    def Predictor(self):
        dataset = pd.read_csv('breast_cancer.csv')
        X = dataset.iloc[:, 1:10]
        Y = dataset.iloc[:, -1]

        classifier = LogisticRegression(random_state=0)
        classifier.fit(X, Y)

             
        x1 = int(self.ct.text)
        x2 = int(self.ucsz.text)
        x3 = int(self.ucsp.text)
        x4 = int(self.ma.text)
        x5 = int(self.secs.text)
        x6 = int(self.bn.text)
        x7 = int(self.bc.text)
        x8 = int(self.nn.text)
        x9 = int(self.m.text)

        if (0<x1<11 and 0<x2<11 and 0<x3<11 and 
            0<x4<11 and 0<x5<11 and 0<x6<11 and 
            0<x7<11 and 0<x8<11 and 0<x9<11):

            x = [x1, x2, x3, x4, x5, x6, x7, x8, x9]       
            response = classifier.predict([x])
            self.Y_pred = int(response[0])
            self.manager.current = 'Output_Screen'
            
        else:
            self.Y_pred = 0
            self.manager.current = 'Output_Screen'                
# -----------------------------------------------------


# Output Screen (Second Window) ---
class Outputscreen(Screen):
    result = NumericProperty(0)
# ---------------------------------


# Root App class -------------
class MainApp(App):
    def build(self):
        return Windowmanager()
# ----------------------------


if __name__ == "__main__":
    MainApp().run()
