# README pour le projet School

## Description

School est une application développée avec Kivy et KivyMD qui permet d'effectuer diverses opérations mathématiques telles que le développement, la factorisation, la dérivée et l'intégration. L'application offre une interface conviviale pour simplifier les expressions, factoriser des polynômes et effectuer des calculs mathématiques complexes.

## Fonctionnalités

- **Opérations mathématiques** : Effectuez des opérations telles que la simplification, le développement, la factorisation, la dérivée et l'intégration.
- **Historique des calculs** : Enregistrez et consultez l'historique de vos expressions mathématiques.
- **Interface utilisateur intuitive** : Utilisation de KivyMD pour une expérience utilisateur agréable.
- **Support pour les expressions symboliques** : Utilisation de SymPy pour manipuler des expressions mathématiques.

## Prérequis

- Python 3.x
- Kivy
- KivyMD
- SymPy
- Kivmob (pour la gestion des publicités)

## Installation

1. Clonez le dépôt :
   ```bash
   git clone https://github.com/HDark02/kivy_Math_general_app
   ```

2. Accédez au répertoire du projet :
   ```bash
   cd kivy_Math_general_app
   ```

3. Installez les dépendances requises :
   ```bash
   pip install "kivy[base]" kivy_examples --pre --extra-index-url https://kivy.org/downloads/simple
   pip install kivy kivymd==1.1.1 sympy kivmob
   ```

## Utilisation

1. Exécutez l'application :
   ```bash
   python main.py
   ```

2. Utilisez l'interface pour entrer des expressions mathématiques et sélectionner l'opération souhaitée.

3. Consultez l'historique des calculs pour voir les résultats précédents.

## Code

Voici un aperçu du code principal de l'application :

```python
from kivymd.app import MDApp
from kivy.lang import Builder
import sympy
from sympy import symbols, Function

class school(MDApp):
    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("operations_screen.kv"))
        return screen_manager

    def execution_operation(self):
        # Code pour exécuter l'opération mathématique
        pass

if __name__ == "__main__":
    school().run()
```

## Aide

Pour toute question ou problème, veuillez consulter le fichier `file_info_app.txt` pour des instructions d'utilisation supplémentaires ou contactez le développeur.

## License

Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.

##Exemple d'utilisation
[Video](https://github.com/HDark02/kivy_Math_general_app/blob/main/bandicam%202025-03-15%2011-10-59-972.mp4)
--- 
## 📬 Contact

Feel free to reach out if you have questions or want to contribute!
---
[Telegram](https://t.me/Thekingdynamo)
[WhatsApp](https://wa.me/+22897606374)
[Facebook](https://www.facebook.com/alexdynamo.dynamo/)
[Instagram](https://www.instagram.com/thekingdynamo/)
[Beacons](https://beacons.page/thekingdynamo)
---
