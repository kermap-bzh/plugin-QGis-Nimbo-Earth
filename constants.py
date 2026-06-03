"""
Module containing constants
"""

# URL to access the pricing page
PRICING_URL = 'https://nimbo.earth/pricing'

# URL to access the nimbo maps
MAPS_URL = 'https://maps.nimbo.earth'

# URL to access the about page
ABOUT_URL = 'https://nimbo.earth'

# URL to prepare URL to a get a layer from the MapCache server
SERVICE_URL = 'https://prod-data.nimbo.earth/mapcache/tms/1.0.0'

# URL to get the different layers from the MapCache server
SERVICE_TOKEN_URL = 'https://prod-data.nimbo.earth/mapcache/tms/1.0.0?kermap_token='

# URL to get user features (authorized features)
SERVICE_FEATURE_URL = 'https://prod-admin.nimbo.earth/authorized-feature'

# URL to get user informations
USER_URL = 'https://prod-admin.nimbo.earth'

# Paid plan label to show in the UI
PAID_PLAN_LABEL = '[PAID PLAN ONLY]'

# Nimbo watermark label to show in the UI
NIMBO_WATERMARK_LABEL = '[WATERMARKED]'

# Timeout for requests
TIMEOUT = 30

# Month names dictionary to get the month name from the month number
MONTH_NAMES = {
    1: "January", 2: "February", 3: "March", 4: "April",
    5: "May", 6: "June", 7: "July", 8: "August",
    9: "September", 10: "October", 11: "November", 12: "December"
}