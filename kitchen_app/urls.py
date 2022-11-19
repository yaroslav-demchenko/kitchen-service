from django.urls import path, include

from kitchen_app.views import (
    index,
    DishListView,
    DishDetailView,
    DishCreateView,
    DishUpdateView,
    DishDeleteView,
    DishTypeListView,
    DishTypeDeleteView,
    DishTypeCreateView,
    CooksListView,
    CooksDetailView,
    CookCreateView,
    CookUpdateView,
    CookDeleteView,
    IngredientsListView,
    IngredientsCreateView,
    IngredientsDeleteView,
    toggle_assign_to_dish
)

urlpatterns = [
    path("", index, name="home_page"),
    path("menu/", DishListView.as_view(), name="dish_list"),
    path("menu/<int:pk>/", DishDetailView.as_view(), name="dish_detail"),
    path("menu/create/", DishCreateView.as_view(), name="dish_create"),
    path("menu/<int:pk>/update/", DishUpdateView.as_view(), name="dish_update"),
    path("menu/<int:pk>/delete/", DishDeleteView.as_view(), name="dish_delete"),
    path("menu/<int:pk>/toggle-assign/", toggle_assign_to_dish, name="toggle_dish_assign"),
    path("dish-type/", DishTypeListView.as_view(), name="dish_type_list"),
    path("dish-type/<int:pk>/delete/", DishTypeDeleteView.as_view(), name="dish_type_delete"),
    path("dish-type/create/", DishTypeCreateView.as_view(), name="dish_type_create"),
    path("cooks/", CooksListView.as_view(), name="cook_list"),
    path("cooks/<int:pk>/", CooksDetailView.as_view(), name="cook_detail"),
    path("cooks/create/", CookCreateView.as_view(), name="cook_create"),
    path("cooks/<int:pk>/update/", CookUpdateView.as_view(), name="cook_update"),
    path("cooks/<int:pk>/delete/", CookDeleteView.as_view(), name="cook_delete"),
    path("cold-store/", IngredientsListView.as_view(), name="ingredients_list"),
    path("cold-store/create", IngredientsCreateView.as_view(), name="ingredients_create"),
    path("cold-store/<int:pk>/delete/", IngredientsDeleteView.as_view(), name="ingredients_delete"),

]

app_name = "kitchen_app"
