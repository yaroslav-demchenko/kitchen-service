# Kitchen service
Django project for managing cooks and dishes on kitchen

## Check it out!
[Kitchen service deployed to Render](https://kitchen-service-m1mo.onrender.com)
Test account:

* username: guest

* password: Guest1234*

## Built With
* [Python](https://www.python.org/) - The project worked on this
* [Django](https://www.djangoproject.com/) - The project is based on this
* [Bootstrap](https://getbootstrap.com/) - Used to project looks better
## Demo
![Website Interface](demo_img/demo_1.jpg)
![Menu Interface](demo_img/demo_2.jpg)
![Dish detail Interface](demo_img/demo_3.jpg)
![Categories Interface](demo_img/demo_4.jpg)
![User list Interface](demo_img/demo_5.jpg)
![Ingredients Interface](demo_img/demo_6.jpg)
## Installation
Python3 must be already installed!
```shell
git clone https://github.com/yaroslav-demchenko/kitchen-service
cd kitchen-service
python3 -m venv venv
venv\Scripts\activate (on Windows)
source venv/bin/activate (on macOS)
pip install -r requirements.txt
python manage.py migrate #create data base
python manage.py runserver # starts Django server
```

## How to use
- Login to page
- Add some ingredients to Cold store
- Create new Dish Category or choose from existing
- Create new Dish, add ingredients from cold store, choose cook for this dish
- Choose a dish from the menu
- You can join the cooking or remove yourself from the cooking list if you were already on this list
