from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView


class Tarefas(ScrollView):
    def __init__(self, tarefas, **kwargs): # keyword arguments
        super().__init__(**kwargs)
        for tarefa in tarefas:
            self.ids.box.add_widget(Tarefa(text=tarefa))
class Tarefa(BoxLayout):
   def __init__(self,text='',**kwargs):
       super().__init__(**kwargs)
       self.ids.label.text = text
class MyApp(App):
    
    def build(self):
       return Tarefas(['Fazer compra','Lavar Carro','Buscar filho','Ir a academia', 'Limpar casa','Almoçar com esposa','Ligar para mãe','fazer caminhada'])
    
  

if __name__=="__main__":
    MyApp().run()