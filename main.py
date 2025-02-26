from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
import webbrowser
import io
from kivymd.toast import toast
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.screenmanager import ScreenManager
from kivymd.uix.dialog import MDDialog
from kivy.clock import Clock
import re as refind
from math import cos as COS, sin as SIN, tan as TAN
import sympy
from sympy import *
x, y, z, t = symbols('x y z t')
k, m, n = symbols('k m n', integer=True)
f, g, h = symbols('f g h', cls=Function)
sympy.init_printing()
try:
    from kivmob import Kivmob
except:
    pass
# from sympy import expand, factor, sqrt, sympify, symbols, exp, sqrt, fraction, diff

#Window.size = (464, 832)
class school(MDApp):
    info_presentation2 = """Développement, factorisation, dérivée, primitive : toutes vos opérations mathématiques en un seul endroit.
Simplifiez les expressions, factorisez les polynômes, calculez les dérivées et les primitives en toute simplicité.
Des outils puissants pour les étudiants, les professionnels et les passionnés de mathématiques.
Une interface conviviale pour des calculs rapides et précis."""
    id_ouf = ["⋅x ", "x**2 ", "w**3", "x**4"]
    #### A revoir avant d'appliquer
    def trouver_string_digit(self, expression_output):
        listring=[]
        lisdigits=[]
        dg_all = refind.findall("[\d]{1,}x", str(expression_output))
        # Affichage avec (digits and x)
        if len(dg_all)>0:
            for dg_n in dg_all:
                listring.append(dg_n)
            for dg_string in dg_all:
                #get only digits(digits without x)
                dg_dig = refind.findall("(\d*)x", dg_string)
                dg_dig=dg_dig[0]
                lisdigits.append(dg_dig)
        return listring, lisdigits
    def historique_enregistrement(self, all_expression):
        with open("historique.py", "a") as histo:
            histo.write(all_expression)
    def affichage_formelle(self, expression1):
        try:
            expression1 = str(expression1)
            expression1 = expression1.replace("**2", "²")
            expression1 = expression1.replace("**(2)", "²")
            expression1 = expression1.replace("**", "^")
            expression1 = expression1.replace("sqrt(", "√(")
            expression1 = expression1.replace("*√(", "√(")
            expression1 = expression1.replace("*x","x")
            expression_output = expression1.replace(")*(",")(")
            screen_manager.get_screen("operation_screen").operation_a_input_par_user.text = expression_output
        except:
            screen_manager.get_screen("operation_screen").operation_a_input_par_user.text = expression1

    def get_input_formel(self, expression1):
        try:
            expression1 = str(expression1)
            expression1 = expression1.replace("²","**2")
            expression1 = expression1.replace("^(", "**(")
            expression1 = expression1.replace("^", "**")
            expression1 = expression1.replace("√(", "sqrt(")
            expression1 = expression1.replace("x", "x")
            listring, lisdigits = self.trouver_string_digit(expression1)
            for i in range(0, len(listring)):
                expression1 = expression1.replace(str(listring[i]), f"{lisdigits[i]}*x")
            expression_output = expression1.replace(")(", ")*(")
        except:
            expression_output=expression1
        return expression_output
    #### Avant d'application des ouf ecritures
    def contater_nous(self, index):
        if (index== 1) or (index == 2):
            webbrowser.open("https://t.me/Thekingdynamo")
    def result_screen(self):
        with open("my_expression.py", "r") as file:
            expression_output=file.read()
        self.affichage_formelle(expression_output)
    def simplifier_les_expressinos(self, expression):
        expression_output = sympify(expression)
        self.affichage_formelle(expression_output)
    def numeric(self, index):
        # print(index)
        with open("my_expression.py", "a") as file:
            file.write(str(index))
        self.result_screen()
    def clean(self):
        with open("my_expression.py", "r") as file:
            expression=file.read()
        expression = expression[:-1]
        with open("my_expression.py", "w") as file:
            file.write(expression)
        self.result_screen()
    def clean_executif_chang(self):
        with open("my_expression.py", "w") as file:
            file.write("")
            file.close()
        screen_manager.get_screen("operation_screen").operation_a_input_par_user.text="Veuillez saisir une expression mathématique"
    def fraction(self):
        with open("my_expression.py", "r") as file:
                expr1=file.read()
        expression_deb=f"fraction({expr1}/"
        with open("my_expression.py", "w") as file:
            file.write(str(expression_deb))
        self.result_screen()
    def execution_operation(self):
        ecran_ope = screen_manager.get_screen("operation_screen").operation_name.title
        file =open("my_expression.py", "r")
        expression1=file.read()
        expression1=self.get_input_formel(expression1)
        if ecran_ope == "Simplifier une expression":
            if len(expression1)<1:
                expression1="0"
            try:
                expression=eval(str(expression1))
                # print(f"{expression1} = {expression}")
                self.affichage_formelle(expression)
                all_expression = f"{expression1} = {expression}\n"
                self.historique_enregistrement(all_expression)
            except Exception as e:
                self.simplifier_les_expressinos(expression1)
        elif ecran_ope == "Dévélopper une expression":
            if len(expression1)<1:
                expression1="0"
            try:
                expression = expand(expression1)
                # print(f"{expression1} = {expression}")
                self.affichage_formelle(expression)
                all_expression = f"{expression1} = {expression}\n"
                self.historique_enregistrement(all_expression)
            except Exception as e:
                self.simplifier_les_expressinos(expression1)
        elif ecran_ope == "Factoriser une expression":
            if len(expression1)<1:
                expression1="0"
            try:
                expression = factor(expression1)
                # print(f"{expression1} = {expression}")
                self.affichage_formelle(expression)
                with open("historique.py", "a") as histo:
                    histo.write(f"{expression1} = {expression}\n")
            except Exception as e:
                self.simplifier_les_expressinos(expression1)
        elif ecran_ope == "Ensemble des solutions":
            if len(expression1)<1:
                expression1="0"
            try:
                expression = solve(eval(expression1))
                # print(f"{expression1} = {expression}")
                self.affichage_formelle(expression)
                with open("historique.py", "a") as histo:
                    histo.write(f"{expression1} = {expression}\n")
            except Exception as e:
                self.simplifier_les_expressinos(expression1)
        elif ecran_ope == "Factoriel":
            if len(expression1)<1:
                expression1="0"
            try:
                expression = factorial(expression1)
                # print(f"{expression1} = {expression}")
                self.affichage_formelle(expression)
                with open("historique.py", "a") as histo:
                    histo.write(f"{expression1} = {expression}\n")
            except Exception as e:
                self.simplifier_les_expressinos(expression1)
        elif ecran_ope == "Dérivée d'une fonction":
            if len(expression1)<1:
                expression1="0"
            try:
                expression1 = expression1.lower()
                expression = diff(expression1)
                # print(f"{expression1} = {expression}")
                self.affichage_formelle(expression)
                with open("historique.py", "a") as histo:
                    histo.write(f"{expression1} = {expression}\n")
            except Exception as e:
                self.simplifier_les_expressinos(expression1)
        elif ecran_ope == "Integrale d'une fonction":
            print()
        elif ecran_ope == "Tracer une courbe":
            print()

    def apropos_use_app(self):
        global dialog
        dialog = None
        with io.open("file_info_app.txt", "r", encoding="UTF-8") as file_simple:
            info_text=file_simple.read()
        close_bt=MDRaisedButton(text="fermé", on_release=self.close_box)
        if not dialog:
            dialog=MDDialog(title= "Info",
                            buttons=[close_bt],
                            text=info_text,
                            pos_hint={"center_x": .5, "center_y": .5},
                            size_hint= (.85, .7),
                            )
        dialog.open()
    def close_box(self, obj):
        dialog.dismiss()
    def non_disponible(self):
        toast("Non disponible dans cette version")
    def on_stop(self):
        try:
            self.ads.hide_banner()
        except:
            pass
        exit()
    def build(self):
        global screen_manager
        #initialise
        try:
            self.ads = Kivmob("ca-app-pub-8803263812567783~9785836190")
            self.ads.new_banner(
                ad_id="ca-app-pub-8803263812567783/8211501276",
                top_pos=False,
                overlap=False
            )
            self.ads.request_banner()
            self.ads.show_banner()
        except:
            pass
        screen_manager= ScreenManager()

        screen_manager.add_widget(Builder.load_file("operations_screen.kv"))
        return screen_manager
    def on_pause(self):
        try:
            self.ads.hide_banner()
        except:
            pass
    def on_resume(self):
        try:
            self.ads.show_banner()
        except:
            pass

    def on_start(self):
        try:
            self.ads.show_banner()
        except:
            pass
    
if __name__ == "__main__":
    with open("my_expression.py", "w") as file:
        file.write("")
        file.close()
    school().run()



