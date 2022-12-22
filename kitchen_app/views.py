from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from kitchen_app.forms import CookCreationForm, DishSearchForm, DishForm
from kitchen_app.models import (Dish, DishType, Ingredient, Cook)


def index(request):
    num_dishes = Dish.objects.count()
    num_type = DishType.objects.count()
    num_ingredient = Ingredient.objects.count()
    num_cooks = Cook.objects.count()

    context = {
        "num_dishes": num_dishes,
        "num_type": num_type,
        "num_ingredient": num_ingredient,
        "num_cooks": num_cooks
    }

    return render(request, "kitchen_app/index.html", context=context)


class DishListView(LoginRequiredMixin, generic.ListView):
    model = Dish
    template_name = "kitchen_app/dish_list.html"
    context_object_name = "dish_list"
    paginate_by = 5
    queryset = Dish.objects.all().select_related("dish_type")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DishListView, self).get_context_data(**kwargs)

        name = self.request.GET.get("name", "")

        context["search_form"] = DishSearchForm(initial={
            "name": name
        })

        return context

    def get_queryset(self):
        form = DishSearchForm(self.request.GET)

        if form.is_valid():
            return self.queryset.filter(
                name__icontains=form.cleaned_data["name"]
            )

        return self.queryset


class DishDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dish
    template_name = "kitchen_app/dish_detail.html"
    context_object_name = "dish_detail"


class DishCreateView(LoginRequiredMixin, generic.CreateView):
    model = Dish
    template_name = "kitchen_app/dish_form.html"
    form_class = DishForm
    success_url = reverse_lazy("kitchen_app:dish_list")
    context_object_name = "dish_create"


class DishUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Dish
    form_class = DishForm
    success_url = reverse_lazy("kitchen_app:dish_list")


class DishDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Dish
    template_name = "kitchen_app/dish_confirm_delete.html"
    context_object_name = "dish_to_delete"
    success_url = reverse_lazy("kitchen_app:dish_list")


class DishTypeListView(LoginRequiredMixin, generic.ListView):
    model = DishType
    template_name = "kitchen_app/dish_types_list.html"
    context_object_name = "dish_type_list"
    paginate_by = 5


class DishTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = DishType
    fields = "__all__"
    template_name = "kitchen_app/dish_type_create.html"
    success_url = reverse_lazy("kitchen_app:dish_type_list")
    context_object_name = "dish_type_create"


class DishTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = DishType
    template_name = "kitchen_app/dish_types_confirm_delete.html"
    context_object_name = "dish_type_to_delete"
    success_url = reverse_lazy("kitchen_app:dish_type_list")


class CooksListView(LoginRequiredMixin, generic.ListView):
    model = Cook
    template_name = "kitchen_app/cook_list.html"
    context_object_name = "cook_list"
    paginate_by = 5


class CooksDetailView(LoginRequiredMixin, generic.DetailView):
    model = Cook
    template_name = "kitchen_app/cook_detail.html"
    context_object_name = "cook_detail"


class CookCreateView(LoginRequiredMixin, generic.CreateView):
    model = Cook
    form_class = CookCreationForm
    success_url = reverse_lazy("kitchen_app:cook_list")


class CookUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Cook
    fields = 'years_of_experience',
    template_name = "kitchen_app/cook_form.html"
    success_url = reverse_lazy("kitchen_app:cook_list")


class CookDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Cook
    template_name = "kitchen_app/cook_confirm_delete.html"
    context_object_name = "cook_delete"
    success_url = reverse_lazy("kitchen_app:cook_delete")


class IngredientsListView(LoginRequiredMixin, generic.ListView):
    model = Ingredient
    template_name = "kitchen_app/ingredient_list.html"
    context_object_name = "ingredient_list"
    paginate_by = 5


class IngredientsCreateView(LoginRequiredMixin, generic.CreateView):
    model = Ingredient
    fields = "__all__"
    template_name = "kitchen_app/ingredient_create.html"
    context_object_name = "ingredient_create"
    success_url = reverse_lazy("kitchen_app:ingredients_list")


class IngredientsDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Ingredient
    template_name = "kitchen_app/ingredient_confirm_delete.html"
    context_object_name = "ingredient_delete"
    success_url = reverse_lazy("kitchen_app:ingredients_list")


@login_required
def toggle_assign_to_dish(request, pk):
    cook = Cook.objects.get(id=request.user.id)
    if (
        Dish.objects.get(id=pk) in cook.dish.all()
    ):
        cook.dish.remove(pk)
    else:
        cook.dish.add(pk)
    return HttpResponseRedirect(reverse_lazy("kitchen_app:dish_detail", args=[pk]))
