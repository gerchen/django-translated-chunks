Hi!

Installation:

1. pip install requirements.txt .
2. Add 'chunks' app in settings.py
3. Migrate database.

Usage:

1. Enable chunks templatetags {% load "chunks" %} .
2. Create chunk in admin.
3. Add {% chunk "chunkkey" %} in template source.
