#!/usr/bin/env python
import os
import sys

urlpatterns = [
    url(r'^home/', include('home.urls', namespace="home")),
    url(r'^admin/', include(admin.site.urls)),
]