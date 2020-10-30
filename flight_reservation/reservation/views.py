from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.views.generic import(ListView,
                                DetailView,
                                CreateView)
from .forms import TicketForm

from .models import Plane, Flight, Ticket


def about(request):
    return render(request, 'reservation/about.html')

def reserve(request):
    if request.method == 'POST':
        t_form = TicketForm(request.POST)
        if t_form.is_valid():
            t_flight = t_form.cleaned_data.get('flight')
            t_row = t_form.cleaned_data.get('row')
            t_column = t_form.cleaned_data.get('column')
            length = len(Ticket.objects.filter(flight=t_flight).filter(row=t_row).filter(column=t_column))
            # messages.success(request, "plane rows: {}\nplane width: {}".format(t_flight.plane.rows, t_flight.plane.width))
            if length > 0:
                messages.success(request, "Row {} and column {} are already taken".format(t_row, t_column))
                messages.success(request, "Length: {}".format(length))
                return redirect('reservation-home')
            t_form.save()
            messages.success(request, f'Your reservation has been created!')
            return redirect('reservation-home')
    else:
        t_form = TicketForm()
    return render(request, 'reservation/reserve.html', {'t_form': t_form})

class FlightListView(ListView):
    model = Flight
    template_name = 'reservation/home.html'
    context_object_name = 'flights'
    paginate_by = 4

class FlightDetailView(DetailView):
    model = Flight

class TicketCreateView(LoginRequiredMixin, CreateView):
    model = Ticket
    fields = ['flight', 'row', 'column', 'first_name', 'last_name', 'passenger']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
