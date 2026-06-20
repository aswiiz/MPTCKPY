from django.views.generic import ListView
from .models import Event

STATIC_EVENTS = [
    {'title': 'State-Level Hackathon 2026', 'tag': 'Coding', 'badge_class': 'bg-danger',
     'date': 'Oct 15-17, 2026', 'venue': 'Main Auditorium',
     'desc': '48-hour coding marathon focused on AI and Web3 solutions.',
     'img': 'https://images.unsplash.com/photo-1504384308090-c894fdcc538d?auto=format&fit=crop&w=600&q=80'},
    {'title': 'TechFest: Innovate 2026', 'tag': 'Featured', 'badge_class': 'bg-success',
     'date': 'Nov 5, 2026', 'venue': 'MPTC Campus',
     'desc': 'Annual technical festival with project exhibitions and robotics battles.',
     'img': 'https://images.unsplash.com/photo-1531482615713-2afd69097998?auto=format&fit=crop&w=600&q=80'},
    {'title': 'Advanced Robotics Workshop', 'tag': 'Workshop', 'badge_class': 'bg-primary',
     'date': 'Aug 22, 2026', 'venue': 'Electronics Lab 2',
     'desc': 'Hands-on autonomous robot building using Arduino and sensor arrays.',
     'img': 'https://images.unsplash.com/photo-1485827404703-89b55fcc595e?auto=format&fit=crop&w=600&q=80'},
    {'title': 'Career Guidance Seminar', 'tag': 'Seminar', 'badge_class': 'bg-warning text-dark',
     'date': 'Sep 10, 2026', 'venue': 'Seminar Hall',
     'desc': 'Expert industry professionals discuss placements, interviews and higher studies.',
     'img': 'https://images.unsplash.com/photo-1522071820081-009f0129c71c?auto=format&fit=crop&w=600&q=80'},
    {'title': 'Electronics Expo 2026', 'tag': 'Expo', 'badge_class': 'bg-info',
     'date': 'Dec 3, 2026', 'venue': 'Main Campus Ground',
     'desc': 'Student-built electronics projects and prototype demonstrations.',
     'img': 'https://images.unsplash.com/photo-1581092160562-40aa08e78837?auto=format&fit=crop&w=600&q=80'},
    {'title': 'AI & ML Workshop', 'tag': 'Workshop', 'badge_class': 'bg-primary',
     'date': 'Jul 18, 2026', 'venue': 'Computer Lab 1',
     'desc': 'Introduction to machine learning models using Python and TensorFlow.',
     'img': 'https://images.unsplash.com/photo-1555949963-aa79dcee981c?auto=format&fit=crop&w=600&q=80'},
    {'title': 'NSS Blood Donation Camp', 'tag': 'NSS', 'badge_class': 'bg-danger',
     'date': 'Aug 5, 2026', 'venue': 'Campus Grounds',
     'desc': 'Annual NSS blood donation drive in collaboration with Karunagappally Taluk Hospital.',
     'img': 'https://images.unsplash.com/photo-1579154204601-01588f351e67?auto=format&fit=crop&w=600&q=80'},
    {'title': 'Industrial Visit – KELTRON', 'tag': 'Industrial Visit', 'badge_class': 'bg-secondary',
     'date': 'Sep 25, 2026', 'venue': 'KELTRON, Thiruvananthapuram',
     'desc': 'Educational visit for Electronics students to KELTRON manufacturing unit.',
     'img': 'https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=600&q=80'},
]

class EventListView(ListView):
    model = Event
    template_name = 'events/event_list.html'
    context_object_name = 'events'
    ordering = ['-event_date']

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['static_events'] = STATIC_EVENTS
        return ctx
