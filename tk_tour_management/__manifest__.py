# -*- coding: utf-8 -*-
# Copyright 2020-Today TechKhedut.
# Part of TechKhedut. See LICENSE file for full copyright and licensing details.
{
    'name': "Advance Tours & Travels Management | Tours & Travels | Hotels Management | Tours | Travels",
    'description': """
        - Advanced Tour Booking
        - Hotel Mangements
        - Tours Packages
        - Tours Location & Places
        - Customised packages
        - Flights & Documents Management
        - Travel Insurances
        - Tour catalog
    """,
    'summary': """
        Advanced Tours, Travels & Hotels Management
    """,
    'version': "1.0",
    'author': 'TechKhedut Inc.',
    'company': 'TechKhedut Inc.',
    'maintainer': 'TechKhedut Inc.',
    'website': "https://www.techkhedut.com",
    'category': 'Tours & Travels',
    'depends': ['contacts', 'account', 'hr', 'crm', 'mail'],
    'data': [
        # security
        'security/ir.model.access.csv',
        # Data
        'data/sequence.xml',
        'data/tour_product_data.xml',
        # wizard views
        'wizard/tour_booking_wizard_view.xml',
        # Views
        'views/assets.xml',
        'views/tour_location_view.xml',
        'views/tour_place_view.xml',
        'views/tour_hotel_view.xml',
        'views/room_type_view.xml',
        'views/hotel_facilities_view.xml',
        'views/tour_package_view.xml',
        'views/package_days_view.xml',
        'views/tour_user_view.xml',
        'views/tour_booking_view.xml',
        'views/package_facilities_view.xml',
        'views/document_list_view.xml',
        # Inherit Views
        'views/tour_inquiry_inherit_view.xml',
        # Report views
        'report/tour_package_report_template.xml',
        'report/tour_booking_report_template.xml',
        # Menus
        'views/menus.xml',
    ],
    'qweb': [
        "static/src/xml/template.xml",
    ],
    'images': [
        'static/description/tour.gif',
    ],
    'license': 'OPL-1',
    'installable': True,
    'application': True,
    'auto_install': False,
    'price': 199,
    'currency': 'USD',
}
