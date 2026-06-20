from django.views.generic import TemplateView
from django.urls import reverse
from .models import Notice

class HomeView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        ctx['depts'] = [
            {'icon': 'bi bi-laptop', 'name': 'Computer Engineering',
             'desc': 'Programming, Web Dev, AI, Databases & Networking.',
             'url': reverse('departments:ce')},
            {'icon': 'bi bi-cpu', 'name': 'Computer Hardware Engineering',
             'desc': 'Hardware Maintenance, Embedded Systems & IoT.',
             'url': reverse('departments:che')},
            {'icon': 'bi bi-motherboard', 'name': 'Electronics Engineering',
             'desc': 'Circuits, PCB Design, Instrumentation & Control.',
             'url': reverse('departments:ee')},
            {'icon': 'bi bi-broadcast', 'name': 'Electronics & Communication',
             'desc': 'Communication Systems, Signal Processing & Wireless.',
             'url': reverse('departments:ece')},
            {'icon': 'bi bi-lightning-charge', 'name': 'Electrical & Electronics',
             'desc': 'Power Systems, Industrial Automation & Renewables.',
             'url': reverse('departments:eee')},
        ]

        ctx['facilities'] = [
            {'icon': 'bi bi-pc-display-horizontal', 'name': 'Smart Computer Labs'},
            {'icon': 'bi bi-motherboard', 'name': 'Electronics Labs'},
            {'icon': 'bi bi-hdd-rack', 'name': 'Hardware Labs'},
            {'icon': 'bi bi-book', 'name': 'Central Library'},
            {'icon': 'bi bi-projector', 'name': 'Seminar Hall'},
            {'icon': 'bi bi-camera-video', 'name': 'Smart Classrooms'},
            {'icon': 'bi bi-person-walking', 'name': 'Sports Facilities'},
            {'icon': 'bi bi-wifi', 'name': 'High-Speed Internet'},
        ]

        ctx['recruiters'] = [
            'TCS', 'Infosys', 'Wipro', 'Cognizant',
            'Tech Mahindra', 'L&T Infotech', 'UST Global', 'IBS Software',
        ]

        ctx['projects'] = [
            {'icon': 'bi bi-robot', 'name': 'Autonomous Campus Drone',
             'desc': 'AI-powered drone for campus surveillance built by ECE & CE students.',
             'dept': 'ECE + CE'},
            {'icon': 'bi bi-sun', 'name': 'Smart Solar Tracker',
             'desc': 'Dual-axis solar tracking system increasing panel efficiency by 40%.',
             'dept': 'EEE'},
            {'icon': 'bi bi-fingerprint', 'name': 'Biometric Smart Vault',
             'desc': 'IoT-based biometric authentication system with cloud logging.',
             'dept': 'CHE'},
        ]

        ctx['events_preview'] = [
            {'title': 'State-Level Hackathon 2026', 'tag': 'Coding', 'date': 'Oct 15-17, 2026',
             'venue': 'Main Auditorium',
             'desc': '48-hour coding marathon focused on AI and Web3 solutions.',
             'img': 'https://images.unsplash.com/photo-1504384308090-c894fdcc538d?auto=format&fit=crop&w=600&q=80'},
            {'title': 'TechFest: Innovate 2026', 'tag': 'Technical Fest', 'date': 'Nov 5, 2026',
             'venue': 'MPTC Campus',
             'desc': 'Annual technical festival with project exhibitions and robotics battles.',
             'img': 'https://images.unsplash.com/photo-1531482615713-2afd69097998?auto=format&fit=crop&w=600&q=80'},
            {'title': 'Robotics Workshop', 'tag': 'Workshop', 'date': 'Aug 22, 2026',
             'venue': 'Electronics Lab 2',
             'desc': 'Hands-on autonomous robot building using Arduino and sensors.',
             'img': 'https://images.unsplash.com/photo-1485827404703-89b55fcc595e?auto=format&fit=crop&w=600&q=80'},
        ]

        return ctx


class AboutView(TemplateView):
    template_name = 'core/about.html'


class ContactView(TemplateView):
    template_name = 'core/contact.html'
