from pathlib import Path

from django.conf import settings


IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp", ".gif"}
UPDATED_SOON = "Content will be updated soon."
IMAGE_UPDATED_SOON = "Image will be updated soon."


DEPARTMENTS = [
    {
        "slug": "computer-engineering",
        "route": "departments:ce",
        "code": "CE",
        "name": "Computer Engineering",
        "icon": "bi bi-laptop",
        "image": "local_images/img_c4ffae8c58.jpg",
        "tagline": "Software, systems, data and connected digital services.",
        "subjects": ["Programming", "Database Management", "Computer Networks", "Web Technology", "Operating Systems", "Software Engineering"],
        "labs": ["Programming Lab", "Network Lab", "Software Development Lab"],
    },
    {
        "slug": "computer-hardware-engineering",
        "route": "departments:che",
        "code": "CHE",
        "name": "Computer Hardware Engineering",
        "icon": "bi bi-cpu",
        "image": "local_images/img_15230d44d1.jpg",
        "tagline": "Computer systems, maintenance, embedded devices and networks.",
        "subjects": ["Computer Architecture", "Hardware Maintenance", "Networking Hardware", "Embedded Systems", "Microprocessors", "IoT Fundamentals"],
        "labs": ["Hardware Lab", "Network Hardware Lab", "Embedded Systems Lab"],
    },
    {
        "slug": "electronics-engineering",
        "route": "departments:ee",
        "code": "EL",
        "name": "Electronics Engineering",
        "icon": "bi bi-motherboard",
        "image": "local_images/img_cc65bf6a70.jpg",
        "tagline": "Circuits, devices, instrumentation and industrial electronics.",
        "subjects": ["Electronic Circuits", "Digital Electronics", "Instrumentation", "PCB Design", "Control Systems", "Power Electronics"],
        "labs": ["Electronic Circuits Lab", "Digital Electronics Lab", "Instrumentation Lab"],
    },
    {
        "slug": "electronics-communication",
        "route": "departments:ece",
        "code": "EC",
        "name": "Electronics & Communication Engineering",
        "icon": "bi bi-broadcast",
        "image": "local_images/img_112a3aa1e0.jpg",
        "tagline": "Communication systems, signal processing and embedded platforms.",
        "subjects": ["Communication Engineering", "Signal Processing", "Microcontrollers", "Wireless Systems", "Digital Electronics", "Antenna Basics"],
        "labs": ["Communication Lab", "Microcontroller Lab", "Signal Processing Lab"],
    },
    {
        "slug": "electrical-electronics",
        "route": "departments:eee",
        "code": "EEE",
        "name": "Electrical & Electronics Engineering",
        "icon": "bi bi-lightning-charge",
        "image": "local_images/img_420b4cf591.jpg",
        "tagline": "Power systems, electrical machines, automation and renewables.",
        "subjects": ["Electrical Machines", "Power Systems", "Industrial Automation", "Electrical Measurements", "Power Electronics", "Renewable Energy"],
        "labs": ["Electrical Machines Lab", "Power Electronics Lab", "Measurements Lab"],
    },
    {
        "slug": "mechanical-engineering",
        "route": "departments:me",
        "code": "ME",
        "name": "Mechanical Engineering",
        "icon": "bi bi-gear-wide-connected",
        "image": "local_images/img_3b9736bbc8.jpg",
        "tagline": "Manufacturing, design, thermal systems and workshop practice.",
        "subjects": ["Engineering Mechanics", "Manufacturing Technology", "Thermal Engineering", "Machine Drawing", "CAD", "Workshop Technology"],
        "labs": ["Workshop", "CAD Lab", "Thermal Lab"],
    },
]


GALLERY_CATEGORIES = [
    "Campus",
    "Labs",
    "Workshops",
    "Library",
    "Sports",
    "Arts",
    "NSS",
    "NCC",
    "Events",
]


def local_media_images(limit=None):
    media_root = Path(settings.MEDIA_ROOT)
    if not media_root.exists():
        return []

    images = []
    for path in sorted(media_root.rglob("*")):
        if path.is_file() and path.suffix.lower() in IMAGE_EXTENSIONS:
            rel = path.relative_to(media_root).as_posix()
            category = infer_category(rel)
            images.append(
                {
                    "url": f"{settings.MEDIA_URL}{rel}",
                    "name": path.stem.replace("_", " ").replace("-", " ").title(),
                    "category": category,
                    "category_slug": category.lower().replace(" ", "-"),
                }
            )
    return images[:limit] if limit else images


def infer_category(relative_path):
    path = relative_path.lower()
    checks = [
        ("lab", "Labs"),
        ("workshop", "Workshops"),
        ("library", "Library"),
        ("sport", "Sports"),
        ("arts", "Arts"),
        ("nss", "NSS"),
        ("ncc", "NCC"),
        ("event", "Events"),
    ]
    for needle, label in checks:
        if needle in path:
            return label
    return "Campus"


def get_department_by_slug(slug):
    return next((dept for dept in DEPARTMENTS if dept["slug"] == slug), None)
